"""Throwaway evidence-contract experiment; no production mastery policy."""

from copy import deepcopy

ENGINES = ('native', 'STACK-style', 'WeBWorK-style', 'OATutor-style')


def initial(engine='native', variant=1):
    return {
        'engine': engine, 'variant': variant, 'attempts': 0,
        'help': [], 'history_known': True, 'events': [], 'observations': [],
    }


def classify(observation):
    """A proposed evidence filter, not an update to a learner state."""
    if observation['grade']['status'] != 'graded':
        return 'ungraded: no correctness evidence'
    if not observation['context']['history_known']:
        return 'unknown independence: retain, do not infer'
    if observation['context']['help_before'] or observation['attempt'] > 1:
        return 'supported/repeated: retain separately'
    if observation['grade']['score'] not in (0, 1):
        return 'partial: retain; binary mastery mapping undecided'
    return 'independent candidate: correct' if observation['grade']['score'] else 'independent candidate: incorrect'


def fixture_grade(engine, outcome):
    """Invented semantic fixtures, NOT upstream API payloads or real graders."""
    score = {'correct': 1, 'wrong': 0, 'partial': 0.5}.get(outcome)
    detail = {
        'native': {'check': 'root-set', 'result': outcome},
        'STACK-style': {'tree': 'roots', 'raw_score': score,
                        'penalty': 0.1, 'answer_note': 'synthetic-' + outcome},
        'WeBWorK-style': {'score': score, 'session': 'synthetic-placeholder'},
        'OATutor-style': {'step': 'roots', 'isCorrect':
                         True if score == 1 else False if score == 0 else None},
    }[engine]
    return {'status': 'graded' if score is not None else outcome,
            'score': score, 'provenance': engine + '/fixture-v1',
            'source_detail': detail}


def transition(state, action, timestamp):
    state = deepcopy(state)
    if action == 'fresh':
        return initial(state['engine'], state['variant'] + 1)
    if action == 'engine':
        return initial(ENGINES[(ENGINES.index(state['engine']) + 1) % len(ENGINES)])
    if action == 'replay':
        # Transport replay has the same event identity; it is not a new attempt.
        return state
    event = {'id': f"v{state['variant']}-e{len(state['events']) + 1}",
             'action': action, 'at': timestamp}
    state['events'].append(event)
    if action in ('hint', 'feedback', 'solution'):
        state['help'].append(action)
    elif action == 'unknown':
        state['history_known'] = False
    elif action in ('correct', 'wrong', 'partial', 'invalid', 'error'):
        # Invalid syntax and grader failures are recorded, not scored as wrong.
        # This provisional counter counts graded submissions only.
        if action in ('correct', 'wrong', 'partial'):
            state['attempts'] += 1
        observation = {
            'schema': 'proposal-v1', 'event_id': event['id'], 'at': timestamp,
            'learner': 'synthetic-learner',
            'activity': {'id': 'quadratic-roots', 'version': 'authored-v1',
                         'variant': state['variant'], 'part': 'roots',
                         'competencies': ['solve-factorable-quadratic'],
                         'intent': 'independent-probe'},
            'attempt': state['attempts'],
            'context': {'history_known': state['history_known'],
                        'help_before': list(state['help'])},
            'grade': fixture_grade(state['engine'], action),
        }
        observation['interpretation'] = classify(observation)
        state['observations'].append(observation)
    return state

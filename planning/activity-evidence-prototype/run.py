"""Run: python planning/activity-evidence-prototype/run.py

Synthetic results only. Press a key then Enter. No files or network writes.
"""
import json
import sys
from datetime import datetime, timezone

sys.dont_write_bytecode = True
from model import initial, transition

KEYS = {'c': 'correct', 'w': 'wrong', 'p': 'partial', 'i': 'invalid',
        'x': 'error', 'h': 'hint', 'f': 'feedback', 's': 'solution',
        'u': 'unknown', 'n': 'fresh', 'e': 'engine', 'r': 'replay'}


def render(state):
    if sys.stdout.isatty():
        print('\033[2J\033[H', end='')
    print('THROWAWAY ACTIVITY / EVIDENCE PROTOTYPE - synthetic results')
    root = state['variant'] + 1
    print(f'Solve (x - {root})(x - {root + 1}) = 0. Part: roots')
    print(f"Engine: {state['engine']} | variant: {state['variant']} | graded attempts: {state['attempts']}")
    print(f"History known: {state['history_known']} | help shown: {state['help']}")
    print('Event trail: ' + ' > '.join(e['action'] for e in state['events']))
    if state['observations']:
        latest = state['observations'][-1]
        print('Latest observation (full record):')
        # Compact nested objects keep the evidence frame within a normal terminal.
        for key, value in latest.items():
            print(f'  {key}: {json.dumps(value)}')
        print('Earlier evidence: ' + '; '.join(
            o['interpretation'] for o in state['observations'][:-1]))
    else:
        print('No response evidence yet.')
    print('[c] correct [w] wrong [p] partial [i] invalid syntax [x] grader error')
    print('[h] hint [f] feedback [s] solution [u] missing history [r] replay')
    print('[n] fresh variant [e] next engine/reset [j] full state JSON [q] quit')
    print('Results are simulated. No mastery probability is calculated.')


def main():
    state = initial()
    while True:
        render(state)
        try:
            key = input('Action + Enter: ').strip().lower()
        except EOFError:
            break
        if key == 'q':
            break
        if key == 'j':
            print(json.dumps(state, indent=2))
            input('Enter to return: ')
        elif key in KEYS:
            state = transition(state, KEYS[key], datetime.now(timezone.utc).isoformat())


if __name__ == '__main__':
    main()

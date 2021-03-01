#!/usr/bin/env python3

ga = '🍏'
ra = '🍎'

lm = {
    'a': (
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        ),
    'b': (
        '🍎🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍏'
        ),
    'c': (
        '🍏🍎🍎🍎'
        '🍎🍏🍏🍏'
        '🍎🍏🍏🍏'
        '🍎🍏🍏🍏'
        '🍏🍎🍎🍎'
        ),
    'd': (
        '🍎🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍏'
        ),
    'e': (
        '🍎🍎🍎🍎'
        '🍎🍏🍏🍏'
        '🍎🍎🍎🍏'
        '🍎🍏🍏🍏'
        '🍎🍎🍎🍎'
        ),
    'f': (
        '🍎🍎🍎'
        '🍎🍏🍏'
        '🍎🍎🍎'
        '🍎🍏🍏'
        '🍎🍏🍏'
        ),
    'g': (
        '🍏🍎🍎🍎'
        '🍎🍏🍏🍏'
        '🍎🍏🍎🍎'
        '🍎🍏🍏🍎'
        '🍏🍎🍎🍎'
        ),
    'h': (
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        ),
    'i': (
        '🍎'
        '🍎'
        '🍎'
        '🍎'
        '🍎'
        ),
    'j': (
        '🍏🍏🍏🍎'
        '🍏🍏🍏🍎'
        '🍏🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍏🍎🍎🍏'
        ),
    'k': (
        '🍎🍏🍏🍎'
        '🍎🍏🍎🍏'
        '🍎🍎🍏🍏'
        '🍎🍏🍎🍏'
        '🍎🍏🍏🍎'
        ),
    'l': (
        '🍎🍏🍏'
        '🍎🍏🍏'
        '🍎🍏🍏'
        '🍎🍏🍏'
        '🍎🍎🍎'
        ),
    'm': (
        '🍎🍏🍏🍏🍎'
        '🍎🍎🍏🍎🍎'
        '🍎🍏🍎🍏🍎'
        '🍎🍏🍏🍏🍎'
        '🍎🍏🍏🍏🍎'
        ),
    'n': (
        '🍎🍏🍏🍎'
        '🍎🍎🍏🍎'
        '🍎🍏🍎🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        ),
    'o': (
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍏🍎🍎🍏'
        ),
    'p': (
        '🍎🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍏'
        '🍎🍏🍏🍏'
        '🍎🍏🍏🍏'
        ),
    'q': (
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍎🍏'
        '🍏🍎🍏🍎'
        ),
    'r': (
        '🍎🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍏'
        '🍎🍏🍎🍏'
        '🍎🍏🍏🍎'
        ),
    's': (
        '🍏🍎🍎🍎'
        '🍎🍏🍏🍏'
        '🍏🍎🍎🍏'
        '🍏🍏🍏🍎'
        '🍎🍎🍎🍏'
        ),
    't': (
        '🍎🍎🍎🍎🍎'
        '🍏🍏🍎🍏🍏'
        '🍏🍏🍎🍏🍏'
        '🍏🍏🍎🍏🍏'
        '🍏🍏🍎🍏🍏'
        ),
    'u': (
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍏🍎🍎🍏'
        ),
    'v': (
        '🍎🍏🍏🍏🍎'
        '🍎🍏🍏🍏🍎'
        '🍏🍎🍏🍎🍏'
        '🍏🍎🍏🍎🍏'
        '🍏🍏🍎🍏🍏'
        ),
    'w': (
        '🍎🍏🍎🍏🍎'
        '🍎🍏🍎🍏🍎'
        '🍎🍏🍎🍏🍎'
        '🍏🍎🍏🍎🍏'
        '🍏🍎🍏🍎🍏'
        ),
    'x': (
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        ),
    'y': (
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍎🍎🍎'
        '🍏🍏🍏🍎'
        '🍎🍎🍎🍏'
        ),
    'z': (
        '🍎🍎🍎🍎'
        '🍏🍏🍏🍎'
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍏'
        '🍎🍎🍎🍎'
        ),
    '0': (
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍎🍏🍏🍎'
        '🍏🍎🍎🍏'
        ),
    '1': (
        '🍏🍎🍎🍏'
        '🍏🍏🍎🍏'
        '🍏🍏🍎🍏'
        '🍏🍏🍎🍏'
        '🍏🍎🍎🍎'
        ),
    '2': (
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍏🍏🍎🍏'
        '🍏🍎🍏🍏'
        '🍎🍎🍎🍎'
        ),
    '3': (
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍏🍏🍎🍏'
        '🍎🍏🍏🍎'
        '🍏🍎🍎🍏'
        ),
    '.': (
        '🍏'
        '🍏'
        '🍏'
        '🍏'
        '🍎'
        ),
    '!': (
        '🍎'
        '🍎'
        '🍎'
        '🍏'
        '🍎'
        ),
    '?': (
        '🍏🍎🍎🍏'
        '🍎🍏🍏🍎'
        '🍏🍏🍎🍏'
        '🍏🍏🍏🍏'
        '🍏🍏🍎🍏'
        ),
    '-': (
        '🍏🍏🍏'
        '🍏🍏🍏'
        '🍎🍎🍎'
        '🍏🍏🍏'
        '🍏🍏🍏'
        ),
    '"': (
        '🍎🍏🍎'
        '🍎🍏🍎'
        '🍏🍏🍏'
        '🍏🍏🍏'
        '🍏🍏🍏'
        ),
    '\'': (
        '🍎'
        '🍎'
        '🍏'
        '🍏'
        '🍏'
        ),
    '#': (
        '🍏🍎🍏🍎🍏'
        '🍎🍎🍎🍎🍎'
        '🍏🍎🍏🍎🍏'
        '🍎🍎🍎🍎🍎'
        '🍏🍎🍏🍎🍏'
        ),
    '$': (
        '🍏🍎🍎🍎🍎'
        '🍎🍏🍎🍏🍏'
        '🍏🍎🍎🍎🍏'
        '🍏🍏🍎🍏🍎'
        '🍎🍎🍎🍎🍏'
        ),
    ' ': '🍏🍏🍏🍏🍏🍏🍏🍏🍏🍏'
    }
while True:
    msg = input().lower()
    print('\n'.join([ga.join([r[i] for r in [[lm[c][i:i+len(lm[c])//5] for i in range(0, len(lm[c]), len(lm[c])//5)] for c in msg]]) for i in range(5)]))

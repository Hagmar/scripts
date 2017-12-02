import argparse
import requests as rq

SESSION = 'Session cookie'
URL_INPUT = 'http://adventofcode.com/2017/day/{}/input'

PY_M = '''tot = 0

while True:
    line = input().strip()
'''


def main():
    args = parse_args()

    if args.n:
        res = rq.get(URL_INPUT.format(args.day), cookies={'session': SESSION})
        with open('in{}'.format(args.day), 'w') as f:
            f.write(res.text)
    if args.m:
        name = args.name or '{}.py'.format(args.day)
        with open(name, 'w') as f:
            f.write(PY_M)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help='Script filename')
    parser.add_argument('-n', action='store_true', help='New script')
    parser.add_argument('-m', action='store_true', help='Multiline')
    parser.add_argument('day', type=int, help='Day')

    return parser.parse_args()


if __name__ == '__main__':
    main()

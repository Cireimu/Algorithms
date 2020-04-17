#!/usr/bin/python

import sys
import time
plays = ['rock', 'paper', 'scissors']


def rock_paper_scissors(n):
    round_results = []
    if n == 0:
        round_results.append([])
        return round_results
    elif n == 1:
        for play in plays:
            round_results.append([play])
        return round_results
    smaller_permutations = rock_paper_scissors(n-1)

    for play in plays:
        for small_permutations in smaller_permutations:
            round_results.append([play]+small_permutations)
    return round_results


a = time.time()

rock_paper_scissors(10)
b = time.time()
print(f'end: {b-a}')
if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')


def foo(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
    for k in range(n):
        print(k)
    return n

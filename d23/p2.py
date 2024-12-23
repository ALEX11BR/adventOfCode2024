#!/usr/bin/env python3

from collections import defaultdict
from itertools import combinations
from sys import stdin

if __name__ == "__main__":
    links = defaultdict(set)

    for line in stdin:
        elems = line.strip().split("-")

        links[elems[0]].add(elems[1])
        links[elems[1]].add(elems[0])

        links[elems[0]].add(elems[0])
        links[elems[1]].add(elems[1])

    best: set[str] = set()
    for elem in links:
        for l in range(len(links[elem]), len(best) - 1, -1):
            for comb in combinations(links[elem], l):
                if all([links[comb_el].issuperset(set(comb)) for comb_el in comb]):
                    best = set((elem,) + comb)
                    break
            else:
                continue
            break

    ans = ",".join(sorted(best))
    print(ans)

#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin

if __name__ == "__main__":
    links = defaultdict(list)
    t_comps = set()

    for line in stdin:
        elems = line.strip().split("-")

        links[elems[0]].append(elems[1])
        links[elems[1]].append(elems[0])

        if elems[0][0] == "t":
            t_comps.add(elems[0])
        if elems[1][0] == "t":
            t_comps.add(elems[1])

    networks = set()
    for comp in t_comps:
        for comp1 in links[comp]:
            for comp2 in links[comp]:
                if comp1 == comp2:
                    continue

                if comp1 in links[comp2] and comp2 in links[comp1]:
                    networks.add(frozenset([comp, comp1, comp2]))

    ans = len(networks)
    print(ans)

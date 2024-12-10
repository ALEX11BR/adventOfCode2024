#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    ans = 0

    def neighbors(node: tuple[int, int]) -> list[tuple[int, int]]:
        ans = []
        for k in range(4):
            nd = list(node)
            nd[k % 2] += (-1) ** (k // 2)
            if nd[0] >= len(text) or nd[1] >= len(text[0]) or nd[k % 2] < 0:
                continue
            ans.append(tuple(nd))
        return ans

    def dfs(node: tuple[int, int]) -> int:
        ans = 0

        visited = set()
        q = [node]

        while q:
            curr = q.pop()
            if curr in visited:
                continue
            visited.add(curr)

            if int(text[curr[0]][curr[1]]) == 9:
                ans += 1

            for nd in neighbors(curr):
                if nd in visited:
                    continue
                if int(text[nd[0]][nd[1]]) != 1 + int(text[curr[0]][curr[1]]):
                    continue
                q.append(nd)

        return ans

    for i in range(len(text)):
        for j in range(len(text[0])):
            if text[i][j] == "0":
                ans += dfs((i, j))

    print(ans)

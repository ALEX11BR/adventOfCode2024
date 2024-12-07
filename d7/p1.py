#!/usr/bin/env python3

from itertools import product
from sys import stdin

if __name__ == "__main__":
    text = stdin.read().splitlines()

    data = []
    for line in text:
        fields = line.split(": ")
        data.append((int(fields[0]), [int(num) for num in fields[1].split(" ")]))

    ans = 0
    for term, nums in data:
        for ops in product("+*", repeat=(len(nums) - 1)):
            det = nums[0]
            for i in range(len(ops)):
                if ops[i] == "+":
                    det += nums[i + 1]
                else:
                    det *= nums[i + 1]
            if det == term:
                ans += term
                break

    print(ans)

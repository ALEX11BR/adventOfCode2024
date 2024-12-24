#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    values = {}
    expressions: dict[str, list[str]] = {}

    def evaluate(key: str) -> int:
        if key not in values:
            match expressions[key][1]:
                case "AND":
                    values[key] = evaluate(expressions[key][0]) & evaluate(
                        expressions[key][2])
                case "XOR":
                    values[key] = evaluate(expressions[key][0]) ^ evaluate(
                        expressions[key][2])
                case _:
                    values[key] = evaluate(expressions[key][0]) | evaluate(
                        expressions[key][2])
        return values[key]

    read_all_values = False
    for line in stdin:
        line = line.strip()

        if not line:
            read_all_values = True
        elif read_all_values:
            fields = line.split(" ")
            expressions[fields[4]] = fields[:3]
        else:
            fields = line.split(": ")
            values[fields[0]] = int(fields[1])

    ans = 0
    pow2 = 0
    while f"z{pow2:02}" in expressions:
        ans += (1 << pow2) * evaluate(f"z{pow2:02}")
        pow2 += 1

    print(ans)

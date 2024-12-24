#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    values = {}
    expressions: dict[str, list[str]] = {}
    bad_words = set()

    max_digit = 0

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

            max_digit = max(max_digit, int(fields[0][1:]))

    def find_gate(list_comp: list[str]) -> str:
        for gate in expressions:
            if expressions[gate][1] == list_comp[1] and {expressions[gate][0], expressions[gate][2]} == {list_comp[0], list_comp[2]}:
                return gate
        return ""

    def swap_gates(gate1: str, gate2: str):
        aux = expressions.get(gate1, [])
        expressions[gate1] = expressions.get(gate2, [])
        expressions[gate2] = aux

        if not expressions[gate1]:
            del expressions[gate1]
        if not expressions[gate2]:
            del expressions[gate2]

        bad_words.add(gate1)
        bad_words.add(gate2)

    carry_gate = find_gate(["x00", "AND", "y00"])

    for i in range(1, max_digit + 1):
        ok = False
        while not ok:
            ok = True

            gate_z = f"z{i:02}"
            op1, op, op2 = expressions[gate_z]

            xor_gate = find_gate([f"x{i:02}", "XOR", f"y{i:02}"])
            and_gate = find_gate([f"x{i:02}", "AND", f"y{i:02}"])

            if carry_gate in [op1, op2] and xor_gate not in [op1, op2]:
                other_gate = list({op1, op2} - {carry_gate})[0]
                swap_gates(xor_gate, other_gate)
                ok = False
                continue

            if op != "XOR" or {op1, op2} != {xor_gate, carry_gate}:
                correct_gate = find_gate([xor_gate, "XOR", carry_gate])

                swap_gates(correct_gate, gate_z)
                ok = False
                continue

            carry_and_gate = find_gate([carry_gate, "AND", xor_gate])
            carry_gate = find_gate([carry_and_gate, "OR", and_gate])

    ans = ",".join(sorted(bad_words))
    print(ans)

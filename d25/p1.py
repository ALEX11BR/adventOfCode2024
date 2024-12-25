#!/usr/bin/env python3

from sys import stdin

if __name__ == "__main__":
    locks = []
    keys = []
    read_data = []
    lock_height = 0

    for line in stdin:
        line = line.strip()

        if line:
            read_data.append(line)
        else:
            new_elem = [len([line[i] for line in read_data if line[i] == "#"])
                        for i in range(len(read_data[0]))]
            if read_data[0].find(".") == -1:
                locks.append(new_elem)
            else:
                keys.append(new_elem)

            lock_height = len(read_data)
            read_data = []

    new_elem = [len([line[i] for line in read_data if line[i] == "#"])
                for i in range(len(read_data[0]))]
    if read_data[0].find(".") == -1:
        locks.append(new_elem)
    else:
        keys.append(new_elem)

    ans = 0
    for lock in locks:
        for key in keys:
            if all(map(lambda t: t[0] + t[1] <= lock_height, zip(lock, key))):
                ans += 1

    print(ans)

#!/usr/bin/env python3

# NOTE: takes about 2 seconds

if __name__ == "__main__":
    nums = [int(f) for f in input().strip().split(" ")]

    ans = 0
    for _ in range(25):
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums[i] = 1
            elif len(str(nums[i])) % 2 == 0:
                num_str = str(nums[i])
                nums[i] = int(num_str[0:(len(num_str) // 2)])
                nums.insert(i + 1, int(num_str[(len(num_str) // 2):]))
                i += 1
            else:
                nums[i] *= 2024
            i += 1

    ans = len(nums)
    print(ans)

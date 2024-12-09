#!/usr/bin/env python3

if __name__ == "__main__":
    text = [int(c) for c in input()]

    ans = 0
    position = 0
    i_left = 0
    i_right = len(text) - 1

    while i_left <= i_right:
        if i_left % 2 == 0:
            ans += position * (i_left // 2)
            text[i_left] -= 1
            while text[i_left] == 0 and i_left <= i_right:
                i_left += 1
            pass
        else:
            ans += position * (i_right // 2)
            text[i_left] -= 1
            text[i_right] -= 1
            while text[i_left] == 0 and i_left <= i_right:
                i_left += 1
            while text[i_right] == 0 and i_left <= i_right:
                i_right -= 2
            pass
        position += 1

    print(ans)

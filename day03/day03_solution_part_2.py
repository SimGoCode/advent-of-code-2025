# https://adventofcode.com/2025/day/3

from day03_input import INPUT

def solve(input):

    total = 0

    for bank in input.splitlines():
        last_digit_index = -1
        min_remainder = 11

        while min_remainder >= 0:
            max_digit = 0

            for i in range(last_digit_index+1,len(bank)-min_remainder):
                digit = int(bank[i])
                if digit > max_digit:
                    max_digit = digit
                    last_digit_index = i

            total += max_digit * 10 ** min_remainder
            min_remainder -= 1

    return total


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


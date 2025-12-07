# https://adventofcode.com/2025/day/3

from day03_input import INPUT

def solve(input):

    total = 0

    for bank in input.splitlines():
        first_digit = 0
        first_digit_index = 0
        second_digit =0

        for i in range(len(bank)-1):
            digit = int(bank[i])
            if digit > first_digit:
                first_digit = digit
                first_digit_index = i

        for i in range(first_digit_index+1, len(bank)):
            digit = int(bank[i])
            if digit > second_digit:
                second_digit = digit

        total += first_digit * 10 + second_digit

    return total


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


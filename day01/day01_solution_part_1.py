# https://adventofcode.com/2025/day/1

from day01_input import INPUT

def solve(input):
    current_digit = 50
    password = 0

    for instruction in input.splitlines():

        turn_left = instruction.startswith("L")
        instruction = instruction[1:]

        if turn_left:
            current_digit = (current_digit - int(instruction)) % 100
        else:
            current_digit = (current_digit + int(instruction)) % 100

        if current_digit == 0:
            password+=1

    return password


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


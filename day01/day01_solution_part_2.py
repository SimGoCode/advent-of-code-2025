# https://adventofcode.com/2025/day/1

from day01_input import INPUT

def solve(input):
    current_digit = 50
    password = 0

    for instruction in input.splitlines():
        turn_left = instruction.startswith("L")
        step = int(instruction[1:])

        # reducing the step from complete loops
        password += step // 100
        step = step % 100

        if step != 0:

            # If you start on 0, it's impossible to cross 0 again since we reduced the step
            # so we just move the dial
            if current_digit == 0:
                if turn_left:
                    current_digit = (current_digit - step) % 100
                else:
                    current_digit = (current_digit + step) % 100

            else:
                if turn_left:
                    if step >= current_digit:
                        password +=1
                    current_digit = (current_digit - step) % 100

                else:
                    if step >= 100-current_digit:
                        password += 1
                    current_digit = (current_digit + step) % 100
    return password


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


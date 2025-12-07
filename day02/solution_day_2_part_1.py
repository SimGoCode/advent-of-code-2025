# https://adventofcode.com/2025/day/1

from day_02_input import INPUT

def solve(input):

    total = 0

    for ids_range in input.split(","):
        current, end = ids_range.split("-")

        while int(current) <= int(end):
            if len(current)%2 ==0:
                mid = len(current)//2
                first_part = current[:mid]
                second_part = current[mid:]

                if first_part == second_part:
                    total += int(current)

            current = str(int(current)+1)


    return total


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


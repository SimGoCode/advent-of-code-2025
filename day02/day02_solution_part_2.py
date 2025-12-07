# https://adventofcode.com/2025/day/2

from day02_input import INPUT

def solve(input):

    total = 0

    for ids_range in input.split(","):
        current, end = ids_range.split("-")

        while int(current) <= int(end):
            id_size = len(current)

            for pattern_size in range(1,id_size//2 + 1):
                if id_size%pattern_size==0:
                    base = current[:pattern_size]
                    times_repeated = id_size//pattern_size
                    if current == base * times_repeated:
                        total += int(current)
                        break

            current = str(int(current) + 1)

    return total


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


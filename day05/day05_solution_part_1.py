# https://adventofcode.com/2025/day/5

from day05_input import INPUT

def solve(input):

    valid_ids = []
    fresh_ingredients = 0
    reading_ranges = True

    for line in input.splitlines():
        line = line.strip()

        if not line:
            reading_ranges = False
            continue

        if reading_ranges:
            start, end = map(int, line.split("-"))
            valid_ids.append((start, end))

        else:
            ingredient_id = int(line)
            for start, end in valid_ids:
                if start <= ingredient_id <= end:
                    fresh_ingredients += 1
                    break

    return fresh_ingredients



if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


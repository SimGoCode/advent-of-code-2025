# https://adventofcode.com/2025/day/6

from day06_input import INPUT

def solve(input):
    valid_ids = []

    for line in input.splitlines():

        line = line.strip()

        if not line:
            break

        start, end = map(int, line.split("-"))
        valid_ids.append((start, end))

    valid_ids.sort()
    valid_ids_no_duplicates = []

    for start, end in valid_ids:
        if not valid_ids_no_duplicates:
            valid_ids_no_duplicates.append([start, end])
        else:
            last_start, last_end = valid_ids_no_duplicates[-1]

            if start <= last_end + 1:
                valid_ids_no_duplicates[-1][1] = max(last_end, end)
            else:
                valid_ids_no_duplicates.append([start, end])

    fresh_ids = sum(end - start + 1 for start, end in valid_ids_no_duplicates)
    return fresh_ids


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


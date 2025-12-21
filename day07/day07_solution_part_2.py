# https://adventofcode.com/2025/day/7

from day07_input import INPUT

def count_timelines(line_idx, beam_idx, manifold, memo):

    if line_idx == len(manifold):
        return 1

    if (line_idx, beam_idx) in memo:
        return memo[(line_idx, beam_idx)]

    char = manifold[line_idx][beam_idx]

    if char == '^':
        left = count_timelines(line_idx + 1, beam_idx - 1, manifold, memo) if beam_idx > 0 else 0
        right = count_timelines(line_idx + 1, beam_idx + 1, manifold, memo) if beam_idx < len(manifold[0]) - 1 else 0
        result = left + right
    else:
        result = count_timelines(line_idx + 1, beam_idx, manifold, memo)

    memo[(line_idx, beam_idx)] = result
    return result


def solve(input):
    manifold = input.splitlines()
    beam_starting_index = manifold[0].find('S')
    memo = {}
    return count_timelines(1, beam_starting_index, manifold, memo)



if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


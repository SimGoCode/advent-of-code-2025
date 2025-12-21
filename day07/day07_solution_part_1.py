# https://adventofcode.com/2025/day/7

from day07_input import INPUT

def solve(input):
    manifold = []
    split_amount = 0

    for line in input.splitlines():
        manifold.append(line)

    beams_index_set = {manifold[0].find('S')}

    for line in manifold[1:]:
        beams = []
        for index in beams_index_set:
            beams.append(index)

        for beam in beams:
            if line[beam] == '^':
                beams_index_set.discard(beam)
                beams_index_set.add(beam-1)
                beams_index_set.add(beam+1)
                split_amount += 1

    return split_amount



if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


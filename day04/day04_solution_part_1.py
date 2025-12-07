# https://adventofcode.com/2025/day/4

from day04_input import INPUT

def solve(input):
    wall = []

    for lines in input.splitlines():
        row = []
        for char in lines:
            row.append(char)
        wall.append(row)

    rows, columns = len(wall), len(wall[0])
    directions = [(-1,-1), (-1,0),  (-1,1),
                  (0,-1),           (0,1),
                  (1,-1),   (1,0),  (1,1)]

    removable_paper = 0
    for i in range(rows):
        for j in range(columns):
            if wall[i][j] == "@":
                neighboor = 0
                for dx, dy in directions:
                    if i+dx >= 0 and j+dy >= 0:
                        if i+dx < rows and j+dy < columns and wall[i+dx][j+dy] == "@":
                            neighboor += 1
                if neighboor < 4:
                    removable_paper += 1

    return removable_paper


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


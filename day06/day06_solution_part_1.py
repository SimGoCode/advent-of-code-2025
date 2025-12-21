# https://adventofcode.com/2025/day/6

from day06_input import INPUT

def solve(input):

    total = 0
    numbers = []
    operators = []

    for line in input.splitlines():
        if line[0].isdigit():
            numbers.append(line)
        else:
            operators = line


    for i in range(len(operators)):
        if operators[i] != ' ':
            problem_numbers = []
            operator = operators[i]
            problem_end_found = False
            operation_result = 0

            while not problem_end_found and i < len(operators):
                number= ''
                for j in range(len(numbers)):
                    if numbers[j][i].isdigit():
                        number+=(numbers[j][i])

                if number == '':
                    problem_end_found = True
                else:
                    problem_numbers.append(int(number))
                    i+=1

            if operator == '+':
                operation_result = sum(problem_numbers)

            elif operator == '-':
                operation_result = problem_numbers[0] - sum(problem_numbers[1:])

            elif operator == '*':
                operation_result = problem_numbers[0]
                for number in problem_numbers[1:]:
                    operation_result *= number

            elif operator == '/':
                operation_result = problem_numbers[0]
                for number in problem_numbers[1:]:
                    operation_result /= number

            total += operation_result

    return total


if __name__ == "__main__":
    result = solve(INPUT)
    print("Result:", result)


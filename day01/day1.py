# --- Advent of Code 2021 --- 
# --- Day 1: Sonar Sweep ---
#      _____
#     _|____|_
#     ( '<' )
#  >-(   o   )-<
#   (    o    )
#  (     o     )

def read_input(filename):
    input_file = open(filename, 'r')
    input_lst = [int(line.split()[0]) for line in input_file]
    return input_lst

def part1(
    input_lst: list,
) -> int:
    """This function calculate the number of measurements that 
    are larger than the previous measurement.

    Args:
        input_lst (list): The puzzle input data.

    Returns:
        int: The number of times there was an increase.
    """
    increased_count = 0

    for i in range(0, len(input_lst) - 1):
        if input_lst[i] < input_lst[i+1]:
            increased_count = increased_count + 1

    return(increased_count)

def part2(
    input_lst: list,
) -> int:
    """This function calculate the number of measurements that 
    are larger than the previous measurement in a moving window of len 3.

    Args:
        input_lst (list): The puzzle input data.

    Returns:
        int: The number of times there was an increase.
    """
    increased_count = 0

    for i in range(0, len(input_lst) - 3):
        window1 = input_lst[(i):(i)+3]
        window2 = input_lst[(i+1):(i+1)+3]

        if sum(window1) < sum(window2):
            increased_count = increased_count + 1

    return(increased_count)

puzzle_input = read_input('input1.txt')

#Part 1 solution
part1_solution = part1(puzzle_input)
print("Part 1 Solution: %s"%part1_solution)

#Part 2 solution
part2_solution = part2(puzzle_input)
print("Part 2 Solution: %s"%part2_solution)
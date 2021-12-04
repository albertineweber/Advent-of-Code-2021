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

puzzle_input = read_input('input1.txt')

#Part 1 solution
increased_count = part1(puzzle_input)
print("Part 1 Solution: %s"%increased_count)
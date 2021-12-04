# --- Advent of Code 2021 --- 
# --- Day 2: Dive! ---
#       ____
#     _|____|_
#     ( '<' )
#  >-(   o   )-<
#   (    o    )
#  (     o     )

def read_input(filename):
    input_file = open(filename, 'r')
    input_lst = [[(line.split()[0]), int(line.split()[1])] for line in input_file]
    return input_lst

def part1(
    input_lst: list,
) -> int:
    """This function calculates the position of the submarine.

    Args:
        input_lst (list): The puzzle input data.

    Returns:
        int: The product of the horizontal position vs depth.
    """
    position = {'horizontal': 0, 'depth': 0}

    for i in range(0, len(input_lst)):
        direction = input_lst[i][0]
        units = input_lst[i][1]

        if direction == 'forward':
            position['horizontal'] = position['horizontal'] + units

        else:
            if direction == 'down':
                position['depth'] = position['depth'] + units
            else:
                position['depth'] = position['depth'] - units

    return(position['horizontal']*position['depth'])

puzzle_input = read_input('input2.txt')

#Part 1 Solution
part1_solution = part1(puzzle_input)
print("Part 1 Solution: %s"%part1_solution)
# --- Advent of Code 2021 --- 
# --- Day 5: Hydrothermal Venture ---
#       ____
#     _|____|_
#     ( '<' )
#  >-(   o   )-<
#   (    o    )
#  (     o     )

def read_input(
    filename: str,
) -> list:
    """This function reads the input file and returns the data in
    the appropriate format.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: The input data for the puzzle
    """
    input_file = open(filename, 'r')
    input_lst = [[(line.split()[0]).split(','), (line.split()[2]).split(',')] for line in input_file]
    return input_lst

def part1(
    input_lst: list,
) -> int:
    """This function maps the hydrothermal vents and counts the
    number of dangerous areas.

    Args:
        input_lst (list): The puzzle input data.

    Returns:
        int: The number of dangerous areas (with overlapping vents).
    """

    diagram_dict = {}

    for line in input_lst:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            low_x = min(int(line[0][0]), int(line[1][0]))
            high_x = max(int(line[0][0]), int(line[1][0]))
            low_y = min(int(line[0][1]), int(line[1][1]))
            high_y = max(int(line[0][1]), int(line[1][1]))
            for x in range(low_x, high_x+1):
                for y in range(low_y, high_y+1):
                    if x in diagram_dict:
                        if y in diagram_dict[x]:
                            diagram_dict[x][y] = diagram_dict[x][y] + 1
                        else:
                                diagram_dict[x][y] = 1
                    else:
                        diagram_dict[x] = {y: 1}
    
    overlap_count = 0

    for x in diagram_dict:
        for y in diagram_dict[x]:
            if diagram_dict[x][y] >= 2:
                overlap_count = overlap_count + 1

    return(overlap_count)


def part2(
    input_lst: list,
) -> int:
    """This function maps the hydrothermal vents and counts the
    number of dangerous areas, considering diagonals.

    Args:
        input_lst (list): The puzzle input data.

    Returns:
        int: The number of dangerous areas (with overlapping vents).
    """

    diagram_dict = {}

    for line in input_lst:

        vertical_line = (line[0][0] == line[1][0])
        horizontal_line = (line[0][1] == line[1][1])
        diagonal_line_positive = ((line[0][0] == line[0][1]) and (line[1][0] == line[1][1]))
        diagonal_line_negative = ((line[0][0] == line[1][1]) and (line[1][0] == line[0][1]))

        condition = (vertical_line or horizontal_line or diagonal_line_positive or diagonal_line_negative)
        condition = True
        if condition:
            low_x = min(int(line[0][0]), int(line[1][0]))
            high_x = max(int(line[0][0]), int(line[1][0]))
            low_y = min(int(line[0][1]), int(line[1][1]))
            high_y = max(int(line[0][1]), int(line[1][1]))

            if horizontal_line or vertical_line:
                for x in range(low_x, high_x+1):
                    for y in range(low_y, high_y+1):
                        if x in diagram_dict:
                            if y in diagram_dict[x]:
                                diagram_dict[x][y] = diagram_dict[x][y] + 1
                            else:
                                    diagram_dict[x][y] = 1
                        else:
                            diagram_dict[x] = {y: 1}


            elif diagonal_line_positive or diagonal_line_negative:
                for x in range(low_x, high_x+1):
                    if diagonal_line_positive:
                        y = x
                    else:
                        y = -x + int(line[0][0]) + int(line[0][1])
                    if x in diagram_dict:
                        if y in diagram_dict[x]:
                            diagram_dict[x][y] = diagram_dict[x][y] + 1
                        else:
                                diagram_dict[x][y] = 1
                    else:
                        diagram_dict[x] = {y: 1}
            
            else:
                x0 = int(line[0][0])
                xf = int(line[1][0])
                y0 = int(line[0][1])
                yf = int(line[1][1])

                m = int((yf-y0)/(xf-x0))

                for x in range(low_x, high_x+1):
                    y = m*(x - x0) + y0
                    if x in diagram_dict:
                        if y in diagram_dict[x]:
                            diagram_dict[x][y] = diagram_dict[x][y] + 1
                        else:
                                diagram_dict[x][y] = 1
                    else:
                        diagram_dict[x] = {y: 1}
        
    overlap_count = 0

    # for x in range(0,10):
    #     line_list = ''
    #     for y in range(0, 10):
    #         try:
    #             line_list = line_list + str(diagram_dict[x][y])
    #         except KeyError:
    #             line_list = line_list +  '.'
    #     print(line_list)

    for x in diagram_dict:
        for y in diagram_dict[x]:
            if diagram_dict[x][y] >= 2:
                overlap_count = overlap_count + 1

    return(overlap_count)

# puzzle_input = read_input('example5.txt')
puzzle_input = read_input('input5.txt')

#Part 1 Solution
part1_solution = part1(puzzle_input)
print("Part 1 Solution: %s"%part1_solution)

#Part 2 Solution
part2_solution = part2(puzzle_input)
print("Part 2 Solution: %s"%part2_solution)
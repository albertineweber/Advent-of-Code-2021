# --- Advent of Code 2021 --- 
# --- Day 4: Giant Squid ---
#       ____
#     _|____|_
#     ( '<' )
#  >-(   o   )-<
#   (    o    )
#  (     o     )

from typing import Tuple

def read_input(
    filename: str,
) -> Tuple[list, dict]:
    """This function reads the input file and returns the data in
    the appropriate format.

    Args:
        filename (str): The name of the file to read.

    Returns:
        Tuple[list, dict]: The input data for the puzzle.
            drawn_lst (list): The list of drawn numbers.
            board_dict (dict): A dict with the board configuration.
    """

    input_file = open(filename, 'r')
    flag_drawn = 0
    board_count = 0
    board_dict = {}
    for line in input_file:
        if flag_drawn == 0:
            drawn_lst = line.split()[0].split(',')
            flag_drawn = 1
        else:
            if line.split() == []:
                board_count = board_count + 1
                line_count = 0
                board_dict[board_count] = {'rows':{}, 'columns':{}}
            else:
                board_dict[board_count]['rows'][line_count] = line.split()
                line_count = line_count + 1
                size = len(line.split())
    
    for board in board_dict.keys():
        for i in range(0, size):
            column_lst = []
            for j in board_dict[board]['rows'].keys():
                column_lst.append(board_dict[board]['rows'][j][i])
            board_dict[board]['columns'][i] = column_lst

    return drawn_lst, board_dict

def part1(
    input: Tuple,
) -> int:
    """This function obtains the final score for the winning board.

    Args:
        input_lst (Tuple): The puzzle input data.

    Returns:
        int: The final score for the winning board.
    """
    drawn_lst, board_dict = input

    current_drawn_lst = drawn_lst[0:4]
    flag_winner = 0

    for drawn_num in drawn_lst[4:]:
        current_drawn_lst.append(drawn_num)
        if flag_winner == 0:
            for board in board_dict.keys():
                for col in board_dict[board]['columns'].keys():
                    if set(board_dict[board]['columns'][col]).issubset(current_drawn_lst):
                        all_drawn_list = list(current_drawn_lst)
                        winning_num = int(drawn_num)
                        final_board = board
                        flag_winner = 1
                for row in board_dict[board]['rows'].keys():
                    if set(board_dict[board]['rows'][row]).issubset(current_drawn_lst):
                        all_drawn_list = list(current_drawn_lst)
                        winning_num = int(drawn_num)
                        final_board = board
                        flag_winner = 1

    board_sum = 0
    for i in board_dict[final_board]['rows'].keys():
        for num in board_dict[final_board]['rows'][i]:
            if num not in all_drawn_list:
                board_sum = board_sum + int(num)

    return(board_sum*winning_num)


def part2(
    input: Tuple,
) -> int:
    """This function obtains the final score for the last winning board.

    Args:
        input_lst (Tuple): The puzzle input data.

    Returns:
        int: The final score for the last winning board.
    """
    drawn_lst, board_dict = input

    current_drawn_lst = drawn_lst[0:4]

    all_boards = list(board_dict.keys())

    for drawn_num in drawn_lst[4:]:
        current_drawn_lst.append(drawn_num)
        if len(all_boards) > 0:
            for board in all_boards:
                for col in board_dict[board]['columns'].keys():
                    if set(board_dict[board]['columns'][col]).issubset(current_drawn_lst):
                        if board in all_boards:
                            all_boards.remove(board)
                        final_board = board

                
                    for row in board_dict[board]['rows'].keys():
                        if set(board_dict[board]['rows'][row]).issubset(current_drawn_lst):
                            if board in all_boards:
                                all_boards.remove(board)
                            final_board = board
            all_drawn_list = list(current_drawn_lst)
            winning_num = int(drawn_num)

    board_sum = 0
    for i in board_dict[final_board]['rows'].keys():
        for num in board_dict[final_board]['rows'][i]:
            if num not in all_drawn_list:
                board_sum = board_sum + int(num)

    return(board_sum*winning_num)

# puzzle_input = read_input('example4.txt')
puzzle_input = read_input('input4.txt')

#Part 1 Solution
part1_solution = part1(puzzle_input)
print("Part 1 Solution: %s"%part1_solution)

#Part 2 Solution
part2_solution = part2(puzzle_input)
print("Part 2 Solution: %s"%part2_solution)
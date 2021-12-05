# --- Advent of Code 2021 --- 
# --- Day 3: Binary Diagnostic ---
#       ____
#     _|____|_
#     ( '<' )
#  >-(   o   )-<
#   (    o    )
#  (     o     )

def read_input(filename):
    input_file = open(filename, 'r')
    input_lst = [(line.split()[0]) for line in input_file]
    return input_lst

def binary_decoder(
    binary: str,
) -> int:
    """This function converts a binary input to a decimal number.

    Args:
        binary (str): a binary input.

    Returns:
        int: the binary input converted to a decimal number.
    """

    decimal = 0

    for i in range(0, len(binary)):
        position = len(binary) - 1 - i
        decimal = decimal + (2**(i))*int(binary[position])
    
    return(decimal)


def part1(
    input_lst: list,
) -> int:
    """This function obtains the gamma and the epilson rate
    from the diagnostic report.

    Args:
        input_lst (list): The puzzle input data.

    Returns:
        int: The power consumption (product of the gamma v
    the epilson rate).
    """

    size = len(input_lst[0])
    bits = {i: {'0':0, '1':0} for i in range(size)}

    for i in range(0, len(input_lst)):
        for j in range(0, size):
            bit = input_lst[i][j]
            bits[j][bit] = bits[j][bit] + 1

    gamma_rate = ''
    for i in range(0, size):
        if bits[i]['0'] > bits[i]['1']:
            most_common_bit = '0'
        else:
            most_common_bit = '1'

        gamma_rate = gamma_rate + most_common_bit

    epsilon_rate = ''
    for i in range(0, size):
        if gamma_rate[i] == '0':
            least_common_bit = '1'
        else:
            least_common_bit = '0'
        epsilon_rate = epsilon_rate + least_common_bit

    decimal_gamma_rate = binary_decoder(gamma_rate)
    decimal_epsilon_rate = binary_decoder(epsilon_rate)

    return(decimal_gamma_rate*decimal_epsilon_rate)

def bit_criteria_filter(
    pass_criteria_lst: list, 
    rating: str,
) -> str:

    """This function obtains either the oxygen generator rating or
    the CO2 scrubber rating.

    Args:
        pass_criteria_lst (list): The puzzle input data.
        rating (str): The rating to be obtained.

    Returns:
        str: The rating in binary encoding.
    """

    size = len(pass_criteria_lst[0])

    for j in range(0, size):
        filtering_lst = []
        
        bits = {'0':0, '1':0}
    
        for i in range(0, len(pass_criteria_lst)):
            bit = pass_criteria_lst[i][j]
            bits[bit] = bits[bit] + 1
    
        if bits['0'] > bits['1']:
            most_common_bit = '0'
            least_common_bit = '1'
        else:
            most_common_bit = '1'
            least_common_bit = '0'

        if rating == 'oxygen':
            criteria_bit = most_common_bit
        else:
            criteria_bit = least_common_bit

        if len(pass_criteria_lst) > 1:
            for i in range(0, len(pass_criteria_lst)):
                if pass_criteria_lst[i][j] == criteria_bit:
                    filtering_lst.append(pass_criteria_lst[i])

            pass_criteria_lst = list(filtering_lst)

    return(pass_criteria_lst[0])

def part2(
    input_lst: list,
) -> int:
    """This function obtains the oxygen generator and the
    CO2 scrubber rating from the diagnostic report.

    Args:
        input_lst (list): The puzzle input data.

    Returns:
        int: The life support rating (product of the oxygen generator vs the
    CO2 scrubber rating).
    """


    oxygen_generator_rating = bit_criteria_filter(list(input_lst), 'oxygen')
    co2_scrubber_rating = bit_criteria_filter(list(input_lst), 'co2')

    decimal_oxygen_generator_rating = binary_decoder(oxygen_generator_rating)
    decimal_co2_scrubber_rating = binary_decoder(co2_scrubber_rating)

    return(decimal_oxygen_generator_rating*decimal_co2_scrubber_rating)



# puzzle_input = read_input('example3.txt')
puzzle_input = read_input('input3.txt')

#Part 1 Solution
part1_solution = part1(puzzle_input)
print("Part 1 Solution: %s"%part1_solution)

#Part 2 Solution
part2_solution = part2(puzzle_input)
print("Part 2 Solution: %s"%part2_solution)
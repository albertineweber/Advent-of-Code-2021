arq = open('input1.txt', 'r')

input_lst = [int(line.split()[0]) for line in arq]

increased_count = 0

for i in range(0, len(input_lst) - 1):
    if input_lst[i] < input_lst[i+1]:
        increased_count = increased_count + 1

#1s part solution
print(increased_count)
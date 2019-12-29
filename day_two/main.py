import math

DAY_ONE_PART_ONE_INPUT = '../resources/day_two_part_one.txt'

ADD = 1
MULTIPLY = 2
HALT = 99


def file_to_list():
    list = []
    with open(DAY_ONE_PART_ONE_INPUT) as fp:
        line = fp.readline()
        while line:
            string_list = line.split(',')
            list += [int(value) for value in string_list]
            line = fp.readline()
    return list


# knowing math we can test different inputs and simplify the formula, we see that noun increases output by 230400,
# verb increases output by 1 and the base is 1258669
def part_two():
    output = 19690720

    verb = (output - 1258669) % 230400
    noun = math.floor((output - 1258669) / 230400)
    return 100 * noun + verb


def part_one():
    intcode_list = file_to_list()
    intcode_list[1] = 12
    intcode_list[2] = 2

    i = 0
    while intcode_list[i] != HALT:
        command = intcode_list[i]
        if command == ADD:
            intcode_list[intcode_list[i + 3]] = intcode_list[intcode_list[i + 1]] + intcode_list[intcode_list[i + 2]]
        if command == MULTIPLY:
            intcode_list[intcode_list[i + 3]] = intcode_list[intcode_list[i + 1]] * intcode_list[intcode_list[i + 2]]
        i += 4
    return intcode_list[0]


print(F"day two, part one: {part_one()}")
print(F"day two, part two: {part_two()}")

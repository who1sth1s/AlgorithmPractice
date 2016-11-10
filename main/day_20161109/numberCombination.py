BASIC_LIST = [1, 2, 3]
ONE = 0
TWO = 1
THREE = 2


def get_combination(args):
    combination_list = list()
    combination_list = create_combination(args, combination_list)
    filter_combination_list = filter_combination(args, combination_list)
    print(filter_combination_list)


def create_combination(args, combination_list):
    for one_index in range(args, -1, -1):
        for two_index in range(args, -1, -1):
            for three_index in range(args, -1, -1):
                combination = list()
                combination.append(one_index)
                combination.append(two_index)
                combination.append(three_index)
                combination_list.append(combination)

    return combination_list


def filter_combination(args, combination_list):
    filter_combination_list = list()
    for combination in combination_list:
        if (combination[ONE] * BASIC_LIST[ONE]) + (combination[TWO] * BASIC_LIST[TWO]) + (combination[THREE] * BASIC_LIST[THREE]) == args:
            one_combination = [BASIC_LIST[ONE] for i in range(combination[ONE])]
            two_combination = [BASIC_LIST[TWO] for i in range(combination[TWO])]
            three_combination = [BASIC_LIST[THREE] for i in range(combination[THREE])]
            filter_combination_list.append(one_combination + two_combination + three_combination)

    return filter_combination_list


get_combination(4)

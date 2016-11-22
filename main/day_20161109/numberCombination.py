import math


BASIC_LIST = [1, 2, 3]
ONE = 0
TWO = 1
THREE = 2


def get_combination(args):
    combination_list = list()
    combination_list = create_combination(args, combination_list)
    filter_combination_list = filter_combination(args, combination_list)
    combination_count = permutation_combination(filter_combination_list)
    combination_all_case = [combination_case(filter_combination_data) for filter_combination_data in filter_combination_list]
    return combination_all_case


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
            one_combination = [BASIC_LIST[ONE] for index_count in range(combination[ONE])]
            two_combination = [BASIC_LIST[TWO] for index_count in range(combination[TWO])]
            three_combination = [BASIC_LIST[THREE] for index_count in range(combination[THREE])]
            filter_combination_list.append(one_combination + two_combination + three_combination)

    return filter_combination_list


def permutation_combination(filter_combination_list):
    combination_count = 0
    for combination in filter_combination_list:
        combination_count += int(math.factorial(len(combination)) / (math.factorial(combination.count(BASIC_LIST[ONE])) * math.factorial(combination.count(BASIC_LIST[TWO])) * math.factorial(combination.count(BASIC_LIST[THREE]))))

    return combination_count


def combination_case(filter_combination_list):

    if len(filter_combination_list) == 1:
        return [filter_combination_list]
    else:
        result_list = list()
        for number in filter_combination_list:
            copy_combination_data = filter_combination_list.copy()
            copy_combination_data.remove(number)

            for recursive_data in combination_case(copy_combination_data):
                recursive_data.insert(0, number)

                if recursive_data not in result_list:
                    result_list.append(recursive_data)

    return result_list

print(get_combination(5))

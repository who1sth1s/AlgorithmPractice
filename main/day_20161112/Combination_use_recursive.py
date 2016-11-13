COMBINATION_COUNT = 0


def combination_recursive(args):
    if args == 0:
        global COMBINATION_COUNT
        COMBINATION_COUNT += 1
    if args - 1 >= 0:
        combination_recursive(args-1)
    if args - 2 >= 0:
        combination_recursive(args-2)
    if args - 3 >= 0:
        combination_recursive(args-3)

    return COMBINATION_COUNT

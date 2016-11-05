import sys


sys.setrecursionlimit(1500)


def get_fibonacci_number_by_iterate(args_number):
    first_number = 0
    second_number = 1
    finally_number = 0

    if args_number == 1:
        finally_number = first_number

    elif args_number == 2:
        finally_number = second_number

    else:
        for index in range(int(args_number) - 2):
            finally_number = first_number + second_number
            first_number = second_number
            second_number = finally_number

    return finally_number

FINALLY_NUMBER = 0
FIRST_NUMBER = 0
SECOND_NUMBER = 1


def get_fibonacci_number_by_recursive(args_number):
    global FINALLY_NUMBER, FIRST_NUMBER, SECOND_NUMBER

    if args_number > 0:
        args_number -= 1
        if args_number == 0:
            FINALLY_NUMBER = FIRST_NUMBER

        elif args_number == 1:
            FINALLY_NUMBER = SECOND_NUMBER

        elif args_number > 1:
            FINALLY_NUMBER = FIRST_NUMBER + SECOND_NUMBER
            FIRST_NUMBER = SECOND_NUMBER
            SECOND_NUMBER = FINALLY_NUMBER
            get_fibonacci_number_by_recursive(args_number)

    finally_number = FINALLY_NUMBER
    return finally_number

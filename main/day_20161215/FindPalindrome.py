def find_palindrome(input_number):

    repeat_count = 0
    next_number = input_number

    while repeat_count <= 100:

        repeat_count += 1
        next_number = int(next_number) + reverse_number(next_number, int)

        if is_equal_reverse_data(next_number):

            return input_number, repeat_count, next_number

    return str(input_number) + ' is not palindrome'


def is_equal_reverse_data(plain_data):

    return str(plain_data) == reverse_number(plain_data, str)


def reverse_number(number, return_type):

    return return_type(str(number)[::-1])

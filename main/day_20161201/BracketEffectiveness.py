'(), { }, , 〔 〕, [ ], 「 」, (()), 《 》, 〚〛, 〖 〗, 『 』'


def bracket_effectiveness(input_string):

    open_bracket_list = ['(', '{', '〔', '[', '「', '《', '〚', '〖', '『']
    matching_bracket_list = {
        '(': ')',
        '{': '}',
        '〔': '〕',
        '[': ']',
        '「': '」',
        '《': '》',
        '〚': '〛',
        '〖': '〗',
        '『': '』'
    }

    bracket_in_input_string = list()

    for input_char in input_string:

        for open_bracket in open_bracket_list:

            if input_char == open_bracket:

                bracket_in_input_string.append(input_char)
                break

        for matching_bracket in matching_bracket_list.values():

            if input_char == matching_bracket:

                if not bracket_in_input_string:

                    return False

                if matching_bracket_list.get(bracket_in_input_string.pop()) == input_char:
                    break

                return False

    if bracket_in_input_string:

        return False

    return True


print(bracket_effectiveness('((()(({}))'))

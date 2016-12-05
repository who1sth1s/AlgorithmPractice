'(), { }, , 〔 〕, [ ], 「 」, (()), 《 》, 〚〛, 〖 〗, 『 』'


class CustomStack():

    def __init__(self):
        self.stack = list()

    def push(self, parameter):
        self.stack.append(parameter)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return not self.stack


def bracket_effectiveness(input_string):

    matching_bracket_field = {
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

    custom_stack = CustomStack()

    for input_char in input_string:

        if check_open_bracket(input_char, matching_bracket_field):
            custom_stack.push(input_char)

        if check_close_bracket(input_char, matching_bracket_field):

            if custom_stack.is_empty() or matching_bracket_field.get(custom_stack.pop()) != input_char:

                return False

    return not custom_stack.stack


def check_open_bracket(input_char, matching_bracket_field):

    if input_char in matching_bracket_field.keys():

        return True
     
    return False


def check_close_bracket(input_char, matching_bracket_field):
    
    if input_char in matching_bracket_field.values():
        
        return True
    
    return False

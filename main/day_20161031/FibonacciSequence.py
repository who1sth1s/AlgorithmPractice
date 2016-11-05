def get_fibonacci_number_by_iterate(self, args_number):
    if args_number > 2:
        for index in range(2, args_number):
            self.FIBONACCI_LIST.append(self.FIBONACCI_LIST[index-2] + self.FIBONACCI_LIST[index-1])
    return self.FIBONACCI_LIST[args_number-1]


def get_fibonacci_number_by_recursive(self, args_number):
    if args_number > 0:
        args_number -= 1
        if self.ROOTIN_COUNT == 1:
            self.ROOTIN_COUNT += 1
            self.FINALLY_NUMBER = self.FIRST_NUMBER
            self.get_fibonacci_number_by_recursive(args_number)

        elif self.ROOTIN_COUNT == 2:
            self.ROOTIN_COUNT += 1
            self.FINALLY_NUMBER = self.SECOND_NUMBER
            self.get_fibonacci_number_by_recursive(args_number)

        else:
            self.FINALLY_NUMBER = self.FIRST_NUMBER + self.SECOND_NUMBER
            self.FIRST_NUMBER = self.SECOND_NUMBER
            self.SECOND_NUMBER = self.FINALLY_NUMBER
            self.get_fibonacci_number_by_recursive(args_number)
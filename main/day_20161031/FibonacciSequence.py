class FibonacciSequence:
    def __init__(self):
        self.FIRST_NUMBER = 0
        self.SECOND_NUMBER = 1
        self.FIBONACCI_LIST = list()
        self.FIBONACCI_LIST.append(self.FIRST_NUMBER)
        self.FIBONACCI_LIST.append(self.SECOND_NUMBER)
        pass

    def get_fibonacci_number_by_iterate(self, args_number):
        if args_number > 2:
            for index in range(2, args_number):
                self.FIBONACCI_LIST.append(self.FIBONACCI_LIST[index-2] + self.FIBONACCI_LIST[index-1])
        return self.FIBONACCI_LIST[args_number-1]

    def get_fibonacci_number_by_recursive(self, args_number):
        if args_number > 0:
            args_number -= 1
            self.FIBONACCI_LIST.append(self.FIBONACCI_LIST[-2] + self.FIBONACCI_LIST[-1])
            self.get_fibonacci_number_by_recursive(args_number)

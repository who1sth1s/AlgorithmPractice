import time


operandNumFirst = 0
operandNumSeocond = 1
result = 1
count = 1


def getFibonacciNumberByRecursive(number):
    global result, operandNumSeocond, operandNumFirst,count

    if number is 1:
        result = 0

    elif number is 2:
        result = 1

    elif number > 2:
        result = operandNumFirst + operandNumSeocond
        operandNumFirst = operandNumSeocond
        operandNumSeocond = result
        if number is 3:
            pass
        else:
            getFibonacciNumberByRecursive(number-1)
    return result

start = time.time()
a = getFibonacciNumberByRecursive(1000)
print(a)
end = time.time()
print(end-start)
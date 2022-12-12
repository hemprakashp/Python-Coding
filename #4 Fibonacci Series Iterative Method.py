# 4
# Python function to print fibonacci series using iterative method

def fibonacci_iterative(length):
    print('Fibonacci series for the range :', length)
    first, second = 0, 1
    for i in range(0, length):
        if i <= 1:
            result = i
        else:
            result = first + second
            first = second
            second = result
        print(result, end=' ')


fibonacci_iterative(10)

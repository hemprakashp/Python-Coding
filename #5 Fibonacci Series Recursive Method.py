# 5
# Python function to print fibonacci series using recursive method

def fibonacci_recursive(length):
    print('Range of the Fibonacci Series :', length)
    first, second = 0, 1

    def fibonacci(num):
        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibonacci(num - 1) + fibonacci(num - 2)

    for i in range(length):
        print(fibonacci(i), end=' ')


fibonacci_recursive(10)

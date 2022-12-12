# 1
# Python function to reverse a number

def reverse_number(num):
    if str(num).isnumeric():
        print('Before reversing the number is :', num)
        reverse = 0
        while num != 0:
            reverse = (reverse * 10) + (num % 10)
            num = num // 10
        print('After reversing the number is :', reverse)
    else:
        print('Give a valid input')

reverse_number(1234)

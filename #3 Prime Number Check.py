# 3
# Python function to check whether a number is prime or not

def check_prime_number(num):
    for i in range(2, num//2):
        if (num % i) == 0:
            print('The given number is not a prime number')
            break
    else:
        print('The given number is a prime number')


check_prime_number(41)

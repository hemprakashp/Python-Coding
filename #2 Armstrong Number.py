# 2
# Python function to check whether the given number is armstrong or not

# What is Armstrong Number?
# It is a number which is equal to the sum of cube of its digits.
# For eg: 153, 370 etc.
# Let's see it practically by calculating it,
# Suppose I am taking 153 for an example 
# First calculate the cube of its each digits
#   1^3 = (1*1*1) = 1
#   5^3 = (5*5*5) = 125
#   3^3= (3*3*3) = 27
# Now add the cube 
#   1+125+27 = 153
# It means 153 is an Armstrong number.

def armstrong_number_wlists(num):
    empty_list = []
    for i in str(num):
        empty_list.append(int(i) ** 3)
    if sum(empty_list) == num:
        print('The given number is Armstrong number')
    else:
        print('The given number is not Armstrong number')


armstrong_number_wlists(153)
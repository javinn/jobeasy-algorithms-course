# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enter n manually. n > 0

from random import randint


# Method 1
def sum_of_digits_1(number):
    result = 0
    for digits in str(number):
        result += int(digits)
    return result


# Method 2
def sum_of_digits_2(number):
    result = 0
    for ind in range(1, n):
        result += number % 10
        number //= 10
    return result + number


n = int(input('Input a number of digits: '))

my_number = randint(pow(10, n - 1), pow(10, n) - 1)

print(my_number)
print(sum_of_digits_1(my_number))
print(sum_of_digits_2(my_number))

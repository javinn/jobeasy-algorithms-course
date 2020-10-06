# Our code generates a random three-digit number and has to sum up all its digits. For example, if a number is 349,
# the code has to print the number 16, because 3 + 4 + 9 = 16.

from random import randint

n = int(input('Input a number of digits: ')) # 2

# number = randint()

# n = randint(100, 999)
# print(n)
# sum_result = 0
#
# for digit_str in str(n):
#     sum_result += int(digit_str)
#
# print(sum_result)
#
# once = n % 10
# # print(once)
#
# n = n // 10
# # print(n)
#
# tens = n % 10
# # print(tens)
#
# n = n // 10
# # print(n)
#
# result = n + tens + once
#
# print(result)

# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enter n manually. n > 0
number = randint(pow(10, n-1), pow(10, n) - 1)
print(number)
result = 0

# # Option 1
# for digits in str(number):
#     result += int(digits)

# Option 2
for ind in range(1, n):
    result += number % 10
    number //= 10

result += number

print(result)
# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# The task is to display all the numbers from start to n of the Fibonacci sequence φn

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


# 1 2 3 4 5 6 7 ...
# 1 1 2 3 5 8 13 ...


# def fibonacci(n):
#     fibonacci_1 = 1
#     fibonacci_2 = 1
#
#     if n < 0:
#         print('Wrong value')
#     if n == 0:
#         print(0)
#
#
#     if n > 0:
#         print(fibonacci_1)
#     if n > 1:
#         print(fibonacci_2)
#
#
#     index = 0
#     while index < n - 2:
#         fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_1 + fibonacci_2
#         index += 1
#         print(fibonacci_2)


# TODO: HW: Rewrite code, which will return only needed element of Fib sequence
# Homework 2_1
def fibonacci(n):
    if n < 0:
        print('Wrong value')
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    current = 3
    fibonacci_n_1 = 1
    fibonacci_n_2 = 1
    fibonacci_n = 0
    while current <= n:
        fibonacci_n = fibonacci_n_1 + fibonacci_n_2
        fibonacci_n_2 = fibonacci_n_1
        fibonacci_n_1 = fibonacci_n
        current += 1

    return fibonacci_n


print (fibonacci(100))

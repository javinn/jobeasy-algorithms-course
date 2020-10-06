# TODO: Count odd and even digits of the whole number
from random import randint


def count_odds_evens(number):
    evens = 0
    odds = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f"The number of even digits in {number} is {evens}\nThe number of odd digits in {number} is {odds}")


n = 20
count_odds_evens(randint(pow(10, n - 1), pow(10, n) - 1))

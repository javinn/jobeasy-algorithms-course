# Homework 2_2


def zeros_not_for_heros(number):

    if str(number) == "0":
        return number

    while str(number)[-1] == "0":
        number = str(number)[:-1]

    return int(number)



print(zeros_not_for_heros(-1050))

# Homework 2_3

def digital_root (number):
    if number < 1:
        return "Wrong number"
    if number < 10:
        return number

    while number >= 10:
        digi_root = 0

        while number > 0:
            digi_root += number % 10
            number //= 10

        number = digi_root


    return digi_root


print(digital_root(493193))
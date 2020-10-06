# TODO: Find max number from 3 values, entered manually from a keyboard


# Method 1
def max_of_3_numbers_1():
    number_1 = input("Input 1st number: ")
    number_2 = input("Input 2nd number: ")
    number_3 = input("Input 3rd number: ")
    return max(number_1, number_2, number_3)


# Method 2
def max_of_3_numbers_2():
    number_1 = input("Input 1st number: ")
    number_2 = input("Input 2nd number: ")
    number_3 = input("Input 3rd number: ")
    if number_1 > number_2:
        max_number = number_1
    else:
        max_number = number_2
    if number_3 > max_number:
        return number_3
    else:
        return max_number


print(max_of_3_numbers_1())
print(max_of_3_numbers_2())

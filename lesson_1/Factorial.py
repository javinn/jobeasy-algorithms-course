# When User enters a number, its factorial is displayed.
import math

# n = int(input('Input a number '))


# def factorial(number):
#     if number < 0:
#         print('I don\'t like Gamma functions')
#     elif number == 0:
#         return 1
#     else:
#         result = 1
#         for num in range(1, number + 1):
#             result *= num
#         return result


# print(math.factorial(n))

# print(factorial(n))
#
def order(sentence):
    ordered_sentence = ''
    # num_of_words = sentence.count(" ") + 1
    list_of_words = [""] * 6

    position = 1

    for i in sentence:
        word = ''
        while i != ' ':
            word += i
            if 48 < ord(i) < 58:
                position = int(i)
        list_of_words[position-1] = word

    for words in list_of_words:
        ordered_sentence += words

    return ordered_sentence


print(order("Fo1r the2"))
print(ord('9'))
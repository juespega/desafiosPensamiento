"""
Encuentra la lógica en las siguientes operaciones y números
5 + 4 = 19
8 + 2 = 610
10 + 8 = 218
12 + 9 = 321
18 + 2 = 1620
21 + 5 = 1626
"""
def problemTwo(number1, number2):

    while number1 != 0 and number2 != 0:
        print(f"{number1} + {number2} = {number1 - number2}{number1 + number2}")
        number1 = int(input("Enter a number 1: "))
        number2 = int(input("Enter a number 2: "))


num1 = int(input("Enter a number 1: "))
num2 = int(input("Enter a number 2: "))

problemTwo(num1, num2)
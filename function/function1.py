# function/run_function.py

def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(numbe1, number2):
    return numbe1 / number2


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: ")) 

print(f"{number1} + {number2} = {(add(number1, number2))}")
print(f"{number1} - {number2} = {(subtract(number1, number2))}")
print(f"{number1} * {number2} = {(muliply(number1, number2))}")
print(f"{number1} / {number2} = {(divide(number1, number2))}")
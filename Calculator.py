import os
from Calculator_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)

    continue_calculation = True
    choice = ""

    num1 = float(input("Enter the first number : "))

    for symbol in operations:
        print(symbol)

    while continue_calculation:

        operation_symbol = input("Type which operation you want to perform : ")

        num2 = float(input("Enter the next number : "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer} ")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to start a new calculation, press any other key to Exit: ")
        if choice == "n":
            os.system("cls")
            calculator()
        elif choice == 'y':
            num1 = answer
        else:
            print("Exiting...")
            continue_calculation = False


calculator()

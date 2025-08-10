#!/bin/env python3

try:

    # Required utilities for programs.
    from src.baseUtils import clearthescreen
    from src.ioUtils import validinput
    from src.mathUtils import basic_arithmetic

except ImportError as e:

    print("\033[31mFATAL\033[0m Error: some lib not found.")
    print("Error Details: {e}")

    exit() 

def main():

    clearthescreen.clearscreen()
    print("Welcome to the simple calculator.\n")

    a = validinput.valid_input_float("Enter first number: ")
    b = validinput.valid_input_float("Enter second number: ")

    operators = input("\nChoose arithmetic you want (+, -, *, /): ")
    try:
        print(f"\nResult: {basic_arithmetic.arithmetic_operator(a, b, operators)}\n")
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)

    return 0

if __name__ == "__main__":
    main()

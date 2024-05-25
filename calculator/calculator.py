import argparse
from calculator_lib import *


def calculator_argument():
    parser = argparse.ArgumentParser(description="a calculator")
    parser.add_argument("--number1", type=float, help="an integer number1", default="0")
    parser.add_argument("--number2", type=float, help="an integer number2", default="0")
    parser.add_argument("--operand", type=str, help="an oprand")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    try:
        argument = calculator_argument()
        if argument.operand.lower() == 'stop':
             print(f"you stopped the calculator")
        result = calculator_operation(argument.number1,argument.number2, argument.operand)
        print(f"Your result = {float(result)}")
    except KeyboardInterrupt:
        print("\n run again")
        


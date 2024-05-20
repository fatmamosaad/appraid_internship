def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    try:
        if number2 != 0:
            return number1 / number2
    except ZeroDivisionError as error:
        print("Error:", error)


def calculator_operation(number1, number2, operand):
    if operand == "+":
        return addition(number1, number2)
    elif operand == "-":
        return subtraction(number1, number2)
    elif operand == "*":
        return multiply(number1, number2)
    elif operand == "/":
        return divide(number1, number2)
    else:
        print(f"your input is invalid")


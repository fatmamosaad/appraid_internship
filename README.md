# Calculator Script

This script is a simple calculator that performs basic arithmetic operations. It is implemented in Python and uses the argparse library for command line argument parsing.

## Features

The calculator supports the following operations:
- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

## Usage

You can use this script from the command line as follows:

```bash
python calculator.py --number1 [NUMBER1] --number2 [NUMBER2] --operand [OPERAND]

Replace [NUMBER1] and [NUMBER2] with the numbers you want to perform the operation on, and replace [OPERAND] with the operation you want to perform. The operand can be +, -, *, or /.

For example, to add 2 and 3, you would use:

python calculator.py --number1 2 --number2 3 --operand +

If you want to stop the calculator, you can use ‘stop’ as the operand:

python calculator.py --operand stop

Error Handling
The script includes error handling for division by zero and invalid operands. If an error occurs, the script will print an error message and exit.
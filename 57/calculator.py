import argparse
from subprocess import call

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    operation = operation.replace("--", "")
    numbers = [float(number) for number in numbers]
    result = 0
    if operation == "add":
        result = sum(numbers)
    elif operation == "sub":
        for i, number in enumerate(numbers):
            if i == 0:
                result = number
                continue
            result -= number
    elif operation == "mul":
        for i, number in enumerate(numbers):
            if i == 0:
                result = number
                continue
            result *= number
    else:
        for i in range(len(numbers)):
            if i == 0:
                result = numbers[i]
                continue
            result /= numbers[i]

    return round(result, 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser()

    parser.add_argument("--add", type=str, nargs="+", required=False, help="Sums the numbers")
    parser.add_argument("--sub", type=str, nargs="+", required=False, help="Subtracts numbers")
    parser.add_argument("--mul", type=str, nargs="+", required=False, help="Multiplies numbers")
    parser.add_argument("--div", type=str, nargs="+", required=False, help="Divides numbers")

    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    #call_calculator(stdout=True)
    #print(calculator("--div", ['2.2', '7', '1.1']))
    #create_parser()
    print(call_calculator())
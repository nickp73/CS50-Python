def calculate_expression(number1: float, operator: str, number2: float) -> float:

    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "/":
            if number2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return number1 / number2
        case _:
            raise ValueError(f"Invalid operator: '{operator}'")


def main():
    # Prompt the user.
    expression = input("Please input an expression in the form of number operator number: ").strip()

    # Unpack the three expected parts
    parts = expression.split(" ")

    # Check if input is valid.
    if len(parts) != 3:
        print("Invalid input. Please enter a valid arithmetic expression in the form of number operator number.")
        return

    operand1, operator, operand2 = parts

    try:
        number1 = float(operand1)
        number2 = float(operand2)

        result = calculate_expression(number1, operator, number2)

        # Output the result formatted to one decimal place.
        print(f"{result:.1f}")

    except ValueError as e:
        print(f"Error: {e if str(e) else 'Please make sure to enter valid numbers.'}")

    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

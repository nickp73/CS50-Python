arithmetic_expression = input("Enter an arithmetic expression (e.g., 'a + b * c'): ")
# Split the input into a list of tokens
user_input = arithmetic_expression.split()

# Check if the input is valid
if len(user_input) >= 3 and len(user_input) % 2 != 0:
    try:
        total = int(user_input[0])

        for i in range(1, len(user_input), 2):
            operator = user_input[i]
            operand = int(user_input[i + 1])

            if operator == '+':
                total += operand
            elif operator == '-':
                total -= operand
            elif operator == '*':
                total *= operand
            elif operator == '/':
                total /= operand
            elif operator == '%':
                total %= operand
            elif operator == '**':
                total **= operand
            elif operator == '//':
                total //= operand
            else:
                print("Invalid operator:", operator)
                break

        print("Result:", total)
    except ValueError:
        print("Invalid input. Please enter a valid arithmetic expression.")
else:
    print("Invalid input. Please enter a valid arithmetic expression.")


def calculator():
    # Take input from user
    number1 = float(input('Enter first number: '))
    op = input('Enter operator (+,-,*,/,^): ')
    number2 = float(input('Enter second number: '))

    # Define a function to calculate the result
    def calculate(n1, n2, op):
        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            result = n1 / n2
        elif op == '^':
            result = n1 ** n2
        else:
            raise ValueError('Invalid operator')

        return result

    # Calculate and print the result
    result = calculate(number1, number2, op)
    print(number1, op, number2)
    print('=', result)

    # Ask user if they want to calculate again
    calc_again = input('Do you want to calculate again? (y/n): ')
    if calc_again.lower() == 'y':
        calculator()
    elif calc_again.lower() == 'n':
        print('See you later.')
    else:
        calculator()

# Call the calculator function
calculator()
# Simple programm for mathematical operations

print('Можете вводить числа и операторы "+", "-", "*" и "/" последоватльно. Для получения результата введите "=". Начинайте с числа. ')

result = 0

secondOperand = 0

operatorBool = True

firstOperandBool = True

secondOperandBool = True

# the initial loop takes the first number

while firstOperandBool:
    try:
        result = int(input("Введите число: "))

        firstOperandBool = False

        # operand = 0

    except:
        print("Это не число!")

# next loop takes operator for continue or takes '=' for result and exit

while operatorBool:

    operator = input("Введите оператор: ")

    if operator == '+' or operator == '-' or operator == '*' or operator == '/':

        # nested loop takes second operand

        while secondOperandBool:

            try:

                secondOperand = int(input("Введите число: "))

                secondOperandBool = False

            except:

                print("Это не число!")

        # conditional blok for operations with operand

        if operator == '+':

            result = result + secondOperand

            secondOperandBool = True

        elif operator == '-':

            result = result - secondOperand

            secondOperandBool = True

        elif operator == '*':

            result = result * secondOperand

            secondOperandBool = True

        elif operator == '/':

            try:

                result = result / secondOperand

                secondOperandBool = True

            except ZeroDivisionError:

                print(
                    f"На 0 делить нельзя. Попробуйте ещё раз. Предыдущий результат {result}")

                continue

    else:

        if operator == '=':

            print(f"Ваш результат = {result}")

            break

        else:

            print("Это не оператор!")

# main part proceed in second loop

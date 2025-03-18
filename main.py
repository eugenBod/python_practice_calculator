print("Добро пожаловать в простейший калькулятор.")

try:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    message = ("Какая операция вам нужна:\nСложение: +\nВычитание: -\n"
               "Умножение: *\nДеление: /\nВаш выбор (введите знак нужной операции):")
    operation = input(message)
    if operation == "+":
        print("Операция сложения (+)")
        result = first_number + second_number
    elif operation == "-":
        print("Операция вычитания (-)")
        result = first_number - second_number
    elif operation == "*":
        print("Операция умножения (*)")
        result = first_number * second_number
    elif operation == "/":
        try:
            print("Операция деления (/)")
            result = first_number / second_number
        except ZeroDivisionError:
            result = "Деление на ноль невозможно!!!"
    else:
        result = "Операция, которую ввел пользователь, неизвестна."
except ValueError:
    result = "Ошибка ввода. Введите число!!!"
    
print(f"Ответ: {result}")

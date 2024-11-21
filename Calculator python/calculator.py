import math

def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Процент (%)")
    print("6. Возведение в квадрат")
    print("7. Квадратный корень")

    choice = input("Введите номер операции (1-7): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Результат: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Результат: {num1} / {num2} = {num1 / num2}")
            else:
                print("Ошибка: деление на ноль!")
        elif choice == '5':
            print(f"Результат: {num1} % {num2} = {num1 % num2}")

    elif choice == '6':
        num = float(input("Введите число: "))
        print(f"Результат: {num}^2 = {num ** 2}")

    elif choice == '7':
        num = float(input("Введите число: "))
        if num >= 0:
            print(f"Результат: √{num} = {math.sqrt(num)}")
        else:
            print("Ошибка: нельзя найти корень из отрицательного числа!")

    else:
        print("Неверный ввод. Попробуйте снова.")

# Запуск калькулятора
calculator()

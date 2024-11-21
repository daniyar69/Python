import random
import datetime
import string
import base64


def get_password_len():
    while True:
        try:
            password_len = int(input("Введите длину пароля (от 6 до 16): "))
            if 6 <= password_len <= 16:
                return password_len
            else:
                print("Введите длину пароля в пределах от 6 до 16!")
        except ValueError:
            print("Ошибка: введите числовое значение.")


def is_special_symbol():
    while True:
        choice = input("Хотите добавить спец. символы? Да/Нет: ").strip().lower()
        if choice in ["да", "yes"]:
            return True
        elif choice in ["нет", "no"]:
            return False
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")


def generate_password(pass_len, include_special_symbols):
    chars = string.ascii_letters + string.digits
    if include_special_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(pass_len))
    print(f"\nСгенерированный пароль: {password}\n")
    return password


def encode_password(password):
    encoded_bytes = base64.b64encode(password.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decode_password(encoded_password):
    decoded_bytes = base64.b64decode(encoded_password.encode("utf-8"))
    return decoded_bytes.decode("utf-8")


def save_password(password):
    platform = input("Для какой платформы создать запись? ").strip()
    encoded_password = encode_password(password)
    date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("passwords.txt", "a", encoding="utf-8") as file:
            file.write(f"{platform} - {encoded_password} - {date_now}\n")
        print("\nПароль успешно сохранён в 'passwords.txt'!\n")
    except Exception as e:
        print(f"Ошибка при сохранении пароля: {e}")


# Функция для просмотра паролей
def view_passwords():
    try:
        with open("passwords.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("База данных паролей пуста.")
                return

            print("\nСписок сохраненных паролей:")
            platforms = {}
            for i, line in enumerate(lines, start=1):
                platform, encoded_password, date = line.strip().split(" - ")
                platforms[i] = (platform, encoded_password, date)
                print(f"{i}. {platform} (дата: {date})")

            while True:
                choice = input("\nВведите номер записи, чтобы показать пароль, или '0' для выхода: ").strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 0:
                        print("Выход из просмотра паролей.")
                        return
                    elif choice in platforms:
                        platform, encoded_password, date = platforms[choice]
                        decoded_password = decode_password(encoded_password)
                        print(f"\nПлатформа: {platform}\nПароль: {decoded_password}\nДата создания: {date}\n")
                    else:
                        print("Неверный выбор. Попробуйте снова.")
                else:
                    print("Введите число.")
    except FileNotFoundError:
        print("Файл 'passwords.txt' не найден. Пароли ещё не сохранены.")


def main():
    print("Добро пожаловать в Password Generator!\n")
    while True:
        print("Выберите действие:")
        print("1. Создать новый пароль")
        print("2. Просмотреть сохраненные пароли")
        print("0. Выход")
        choice = input("\nВведите номер действия: ").strip()

        if choice == "1":
            password_len = get_password_len()
            include_special_symbols = is_special_symbol()
            generated_password = generate_password(password_len, include_special_symbols)
            save_password(generated_password)
        elif choice == "2":
            view_passwords()
        elif choice == "0":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()


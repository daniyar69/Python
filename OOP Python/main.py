# Базовый класс "Сотрудник"
class Employee:
    def __init__(self, name, position, base_salary):
        self.name = name
        self.position = position
        self.base_salary = base_salary

    def calculate_total_salary(self):
        """Расчёт итоговой зарплаты (по умолчанию только базовая)."""
        return self.base_salary

    def display_info(self):
        """Выводит информацию о сотруднике."""
        print(f"Имя: {self.name}")
        print(f"Должность: {self.position}")
        print(f"Итоговая зарплата: {self.calculate_total_salary()} руб.\n")


# Класс "Менеджер"
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, "Менеджер", base_salary)
        self.bonus = bonus

    def calculate_total_salary(self):
        """Итоговая зарплата: базовая + бонус."""
        return self.base_salary + self.bonus


# Класс "Разработчик"
class Developer(Employee):
    def __init__(self, name, base_salary, project_bonus):
        super().__init__(name, "Разработчик", base_salary)
        self.project_bonus = project_bonus

    def calculate_total_salary(self):
        """Итоговая зарплата: базовая + премия за проекты."""
        return self.base_salary + self.project_bonus


# Класс для управления сотрудниками
class EmployeeManager:
    def __init__(self):
        self.employees = []  # Список для хранения сотрудников

    def add_employee(self, employee):
        """Добавляет сотрудника в список."""
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} добавлен!\n")

    def list_employees(self):
        """Выводит список всех сотрудников."""
        if not self.employees:
            print("Список сотрудников пуст.\n")
            return
        print("Список сотрудников:")
        for i, employee in enumerate(self.employees, start=1):
            print(f"{i}. {employee.name} - {employee.position}")
        print()

    def show_employee_details(self, index):
        """Показывает информацию о конкретном сотруднике."""
        try:
            employee = self.employees[index]
            print("\nДетали сотрудника:")
            employee.display_info()
        except IndexError:
            print("Ошибка: сотрудник с таким номером не найден.\n")


# Главная функция для работы с программой
def main():
    manager = EmployeeManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить менеджера")
        print("2. Добавить разработчика")
        print("3. Показать список сотрудников")
        print("4. Показать детали сотрудника")
        print("0. Выйти")
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            name = input("Введите имя менеджера: ").strip()
            base_salary = int(input("Введите базовую зарплату менеджера: "))
            bonus = int(input("Введите бонус менеджера: "))
            manager.add_employee(Manager(name, base_salary, bonus))

        elif choice == "2":
            name = input("Введите имя разработчика: ").strip()
            base_salary = int(input("Введите базовую зарплату разработчика: "))
            project_bonus = int(input("Введите премию за проекты: "))
            manager.add_employee(Developer(name, base_salary, project_bonus))

        elif choice == "3":
            manager.list_employees()

        elif choice == "4":
            manager.list_employees()
            if manager.employees:
                index = int(input("Введите номер сотрудника: ")) - 1
                manager.show_employee_details(index)

        elif choice == "0":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Ошибка: неверный выбор. Попробуйте снова.\n")


# Запуск программы
if __name__ == "__main__":
    main()




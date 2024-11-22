from abc import ABC, abstractmethod


# Базовый класс "Животное"
class Animal(ABC):
    def __init__(self, name, species, age, is_endangered=False):
        self.name = name
        self.species = species
        self.age = age
        self.is_endangered = is_endangered

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self, food):
        print(f"{self.name} ест {food}.")

    def sleep(self):
        print(f"{self.name} спит.")

    def info(self):
        status = "под угрозой" if self.is_endangered else "не под угрозой"
        return f"{self.name} ({self.species}), возраст: {self.age}, статус: {status}"


# Подклассы для конкретных животных
class Lion(Animal):
    def __init__(self, name, age, is_endangered=False):
        super().__init__(name, "Лев", age, is_endangered)

    def make_sound(self):
        print("Рррр!")

    def hunt(self):
        print(f"{self.name} охотится.")


class Elephant(Animal):
    def __init__(self, name, age, is_endangered=False):
        super().__init__(name, "Слон", age, is_endangered)

    def make_sound(self):
        print("Трууу!")

    def spray_water(self):
        print(f"{self.name} разбрызгивает воду.")


class Penguin(Animal):
    def __init__(self, name, age, is_endangered=False):
        super().__init__(name, "Пингвин", age, is_endangered)

    def make_sound(self):
        print("Кря!")

    def swim(self):
        print(f"{self.name} плавает.")


# Класс "Вольер"
class Exhibit:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.animal_list = []

    def add_animal(self, animal):
        self.animal_list.append(animal)
        print(f"{animal.name} добавлен в вольер '{self.name}'.")

    def remove_animal(self, animal):
        if animal in self.animal_list:
            self.animal_list.remove(animal)
            print(f"{animal.name} удален из вольера '{self.name}'.")
        else:
            print(f"{animal.name} не найден в вольере '{self.name}'.")

    def show_all_animals(self):
        if not self.animal_list:
            print(f"В вольере '{self.name}' нет животных.")
        else:
            print(f"Животные в вольере '{self.name}':")
            for animal in self.animal_list:
                print(f"- {animal.info()}")


# Базовый класс "Сотрудник"
class Staff(ABC):
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age

    @abstractmethod
    def work(self):
        pass

    def report(self):
        print(f"{self.name} готовит отчет.")


# Подкласс "Смотритель"
class Zookeeper(Staff):
    def __init__(self, name, age):
        super().__init__(name, "Смотритель", age)

    def work(self):
        print(f"{self.name} кормит животных.")

    def feed_animal(self, animal, food):
        print(f"{self.name} кормит {animal.name} ({animal.species}) {food}.")
        animal.eat(food)


# Подкласс "Ветеринар"
class Vet(Staff):
    def __init__(self, name, age):
        super().__init__(name, "Ветеринар", age)

    def work(self):
        print(f"{self.name} проверяет здоровье животных.")

    def check_health(self, animal):
        print(f"{self.name} проверяет здоровье {animal.name} ({animal.species}).")
        print(f"Здоровье {animal.name} в порядке!")


# Класс "Зоопарк"
class Zoo:
    def __init__(self):
        self.exhibits = []
        self.staff_list = []

    def add_exhibit(self, exhibit):
        self.exhibits.append(exhibit)
        print(f"Вольер '{exhibit.name}' добавлен в зоопарк.")

    def add_staff(self, staff):
        self.staff_list.append(staff)
        print(f"Сотрудник {staff.name} добавлен в зоопарк.")

    def show_all_exhibits(self):
        if not self.exhibits:
            print("В зоопарке пока нет вольеров.")
        else:
            for exhibit in self.exhibits:
                exhibit.show_all_animals()

    def daily_operations(self):
        print("Ежедневные операции зоопарка:")
        for staff in self.staff_list:
            staff.work()


# Интерфейс меню
def menu():
    zoo = Zoo()

    while True:
        print("\nДобро пожаловать в Зоопарк!")
        print("1. Добавить вольер")
        print("2. Добавить сотрудника")
        print("3. Добавить животное в вольер")
        print("4. Показать все вольеры и животных")
        print("5. Провести ежедневные операции")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название вольера: ")
            location = input("Введите местоположение вольера: ")
            exhibit = Exhibit(name, location)
            zoo.add_exhibit(exhibit)

        elif choice == "2":
            name = input("Введите имя сотрудника: ")
            position = input("Введите должность (Смотритель/Ветеринар): ")
            age = int(input("Введите возраст сотрудника: "))
            if position.lower() == "смотритель":
                zoo.add_staff(Zookeeper(name, age))
            elif position.lower() == "ветеринар":
                zoo.add_staff(Vet(name, age))
            else:
                print("Неверная должность.")

        elif choice == "3":
            if not zoo.exhibits:
                print("Сначала добавьте вольер.")
                continue
            animal_type = input("Введите тип животного (Лев/Слон/Пингвин): ")
            name = input("Введите имя животного: ")
            age = int(input("Введите возраст животного: "))
            is_endangered = input("Животное под угрозой исчезновения? (Да/Нет): ").lower() == "да"

            if animal_type.lower() == "лев":
                animal = Lion(name, age, is_endangered)
            elif animal_type.lower() == "слон":
                animal = Elephant(name, age, is_endangered)
            elif animal_type.lower() == "пингвин":
                animal = Penguin(name, age, is_endangered)
            else:
                print("Неверный тип животного.")
                continue

            print("Доступные вольеры:")
            for i, exhibit in enumerate(zoo.exhibits):
                print(f"{i + 1}. {exhibit.name} ({exhibit.location})")
            exhibit_choice = int(input("Выберите вольер (номер): ")) - 1

            if 0 <= exhibit_choice < len(zoo.exhibits):
                zoo.exhibits[exhibit_choice].add_animal(animal)
            else:
                print("Неверный выбор.")

        elif choice == "4":
            zoo.show_all_exhibits()

        elif choice == "5":
            zoo.daily_operations()

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор.")


# Запуск программы
if __name__ == "__main__":
    menu()
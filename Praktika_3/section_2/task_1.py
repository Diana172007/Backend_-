class Employee:
    """Базовый класс сотрудника: имя, фамилия, возраст и оклад."""

    def __init__(self, name, last_name, age, base_salary):
        """Создаёт сотрудника.

        Args:
            name (str): Имя сотрудника.
            last_name (str): Фамилия сотрудника.
            age (int): Возраст.
            base_salary (float): Базовый оклад.
        """
        self.name = name
        self.last_name = last_name
        self.age = age
        self.salary = base_salary

    def salary_calculation(self):
        """Возвращает строку с базовой зарплатой сотрудника.

        Returns:
            str: Описание зарплаты.
        """
        return f"Зарплата сотрудника {self.salary}"


class Manager(Employee):
    """Менеджер: сотрудник с надбавкой."""

    def __init__(self, name, last_name, age, base_salary, allowance):
        """Создаёт менеджера.

        Args:
            name (str): Имя.
            last_name (str): Фамилия.
            age (int): Возраст.
            base_salary (float): Базовый оклад.
            allowance (float): Надбавка.
        """
        super().__init__(name, last_name, age, base_salary)
        self.allowance = allowance

    def salary_calculation(self):
        """Возвращает строку с зарплатой менеджера (оклад + надбавка).

        Returns:
            str: Описание зарплаты.
        """
        return f"Зарплата менеджера {self.salary + self.allowance}"


class Developer(Employee):
    """Разработчик: сотрудник с надбавкой и премией."""

    def __init__(self, name, last_name, age, base_salary, allowance, premia):
        """Создаёт разработчика.

        Args:
            name (str): Имя.
            last_name (str): Фамилия.
            age (int): Возраст.
            base_salary (float): Базовый оклад.
            allowance (float): Надбавка.
            premia (float): Премия.
        """
        super().__init__(name, last_name, age, base_salary)
        self.allowance = allowance
        self.premia = premia

    def salary_calculation(self):
        """Возвращает строку с зарплатой разработчика (оклад + надбавка + премия).

        Returns:
            str: Описание зарплаты.
        """
        return f"Зарплата разработчика {self.salary + self.allowance + self.premia}"


m = Manager("Аня", "Смирнова", 30, 80000, 20000)
d = Developer("Иван", "Петров", 25, 70000, 10000, 15000)

print(m.salary_calculation(), m.name)
print(d.salary_calculation())

class Employee:
    def __init__(self, name, last_name, age, base_salary):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.salary = base_salary

    def salary_calculation(self):
        return f"Зарплата сотрудника {self.salary}"


class Manager(Employee):
    def __init__(self, name, last_name, age, base_salary, allowance):
        super().__init__(name, last_name, age, base_salary)
        self.allowance = allowance

    def salary_calculation(self):
        return f"Зарплата менеджера {self.salary + self.allowance}"


class Developer(Employee):
    def __init__(self, name, last_name, age, base_salary, allowance, premia):
        super().__init__(name, last_name, age, base_salary)
        self.allowance = allowance
        self.premia = premia

    def salary_calculation(self):
        return f"Зарплата разработчика {self.salary + self.allowance + self.premia}"


m = Manager("Аня", "Смирнова", 30, 80000, 20000)
d = Developer("Иван", "Петров", 25, 70000, 10000, 15000)

print(m.salary_calculation())
print(d.salary_calculation())

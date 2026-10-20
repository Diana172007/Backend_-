class Vehicle:
    """Базовый класс транспортного средства: название, скорость, вместимость."""

    def __init__(self, name, speed, capacity):
        """Создаёт транспортное средство.

        Args:
            name (str): Название.
            speed (int): Максимальная скорость (км/ч).
            capacity (int): Вместимость (количество мест).
        """
        self.name = name
        self.speed = speed
        self.capacity = capacity

    def info(self):
        """Возвращает общее описание транспортного средства.

        Returns:
            str: Описание с названием, скоростью и вместимостью.
        """
        return f"{self.name} разгоняется до скорости {self.speed} и вмещает {self.capacity}"


class Car(Vehicle):
    """Легковой автомобиль с количеством дверей."""

    def __init__(self, name, speed, capacity, count_door):
        """Создаёт легковой автомобиль.

        Args:
            name (str): Название.
            speed (int): Максимальная скорость (км/ч).
            capacity (int): Вместимость.
            count_door (int): Количество дверей.
        """
        super().__init__(name, speed, capacity)
        self.count_door = count_door

    def info(self):
        """Возвращает описание автомобиля.

        Returns:
            str: Описание с названием, вместимостью, дверями и скоростью.
        """
        return f"Легковая машина {self.name}, {self.capacity} мест, {self.count_door} двери, скорость {self.speed} км/ч."


class Bicycle(Vehicle):
    """Велосипед с количеством скоростей."""

    def __init__(self, name, speed, capacity, gears):
        """Создаёт велосипед.

        Args:
            name (str): Название.
            speed (int): Максимальная скорость (км/ч).
            capacity (int): Вместимость.
            gears (int): Количество скоростей.
        """
        super().__init__(name, speed, capacity)
        self.gears = gears

    def info(self):
        """Возвращает описание велосипеда.

        Returns:
            str: Описание с названием, вместимостью, скоростями и скоростью.
        """
        return f"Велосипед {self.name}, {self.capacity} мест, {self.gears} скорость, скорость {self.speed} км/ч."


class Airplane(Vehicle):
    """Самолёт с размахом крыльев."""

    def __init__(self, name, speed, capacity, wingspan):
        """Создаёт самолёт.

        Args:
            name (str): Название.
            speed (int): Максимальная скорость (км/ч).
            capacity (int): Вместимость.
            wingspan (float): Размах крыльев (м).
        """
        super().__init__(name, speed, capacity)
        self.wingspan = wingspan

    def info(self):
        """Возвращает описание самолёта.

        Returns:
            str: Описание с названием, вместимостью, размахом крыльев и скоростью.
        """
        return f"Самолёт {self.name}, {self.capacity} мест, размах крыльев {self.wingspan} м, скорость {self.speed} км/ч."


vehicles = [
    Car("Toyota Camry", 220, 5, 4),
    Bicycle("Stels", 25, 1, 21),
    Airplane("Boeing 737", 850, 189, 35.8),
]

for v in vehicles:
    print(v.info())

class Vehicle:
    def __init__(self, name, speed, capacity):
        self.name = name
        self.speed = speed
        self.capacity = capacity

    def info(self):
        return f"{self.name} разгоняется до скорости {self.speed} и вмещает {self.capacity}"


class Car(Vehicle):
    def __init__(self, name, speed, capacity, count_door):
        super().__init__(name, speed, capacity)
        self.count_door = count_door

    def info(self):
        return f"Легковая машина {self.name}, {self.capacity} мест, {self.count_door} двери, скорость {self.speed} км/ч."


class Bicycle(Vehicle):
    def __init__(self, name, speed, capacity, gears):
        super().__init__(name, speed, capacity)
        self.gears = gears

    def info(self):
        return f"Велосипед {self.name}, {self.capacity} мест, {self.gears} скорость, скорость {self.speed} км/ч."


class Airplane(Vehicle):
    def __init__(self, name, speed, capacity, wingspan):
        super().__init__(name, speed, capacity)
        self.wingspan = wingspan

    def info(self):
        return f"Самолёт {self.name}, {self.capacity} мест, размах крыльев {self.wingspan} м, скорость {self.speed} км/ч."


vehicles = [
    Car("Toyota Camry", 220, 5, 4),
    Bicycle("Stels", 25, 1, 21),
    Airplane("Boeing 737", 850, 189, 35.8),
]

for v in vehicles:
    print(v.info())

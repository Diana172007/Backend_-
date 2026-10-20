class SpaceShip:
    """Космический корабль: топливо, корпус, скорость."""

    def __init__(self, fuel, hull, speed):
        """Создаёт корабль с заданными параметрами.

        Args:
            fuel (int): Запас топлива.
            hull (int): Прочность корпуса.
            speed (int): Текущая скорость.
        """
        self.fuel = fuel
        self.hull = hull
        self.speed = speed

    def move(self):
        """Тратит топливо и изнашивает корпус при движении."""
        if self.fuel > 0:
            self.fuel -= 10
            self.hull -= 5
        else:
            print("Нет топлива!")


class CrewMember:
    """Член экипажа: здоровье, навык, роль."""

    def __init__(self, health, skills, role):
        """Создаёт члена экипажа.

        Args:
            health (int): Здоровье.
            skills (int): Навык.
            role (str): Роль в команде.
        """
        self.health = health
        self.skills = skills
        self.role = role

    def work(self):
        """Работает: теряет здоровье, но растёт в навыке."""
        self.health -= 5
        self.skills += 1


class Mission:
    """Миссия: цель, ресурсы и события."""

    def __init__(self, goal, resources: dict):
        """Создаёт миссию.

        Args:
            goal (str): Цель миссии.
            resources (dict): Ресурсы.
        """
        self.goal = goal
        self.resources = resources

    def accident(self, ship: SpaceShip):
        """Авария: корабль повреждается, тратит топливо.

        Args:
            ship (SpaceShip): Корабль, с которым произошла авария.
        """
        print("Авария! Корабль повреждён.")
        ship.fuel -= 5
        ship.hull -= 5

    def asteroid_encounter(self, ship: SpaceShip):
        """Встреча с астероидом: повреждения и остановка.

        Args:
            ship (SpaceShip): Корабль, встретивший астероид.
        """
        print("Встреча с астероидом!")
        ship.fuel -= 10
        ship.hull -= 10
        ship.speed = 0


ship = SpaceShip(fuel=100, hull=100, speed=50)
pilot = CrewMember(health=100, skills=10, role="пилот")
mission = Mission(goal="экспедиция", resources={"еда": 50})

ship.move()
pilot.work()
mission.accident(ship)
mission.asteroid_encounter(ship)

from abc import ABC, abstractmethod
from datetime import date


class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Книгу {self.title} написал {self.author} в {self.year}"

    def print_info(self):
        print(self.info())

    @property
    def age(self):
        return date.today().year - self.year

    @age.setter
    def age(self, value):
        self.year = date.today().year - value

    @classmethod
    def from_string(cls, text):
        title, author, year = text.split(";")
        return cls(title, author, int(year))

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title == other.title
            and self.author == other.author
            and self.year == other.year
        )

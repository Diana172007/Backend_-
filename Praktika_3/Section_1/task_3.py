from datetime import date


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Книгу {self.title}  написал {self.author} в {self.year}"

    @property
    def age(self):
        return date.today().year - self.year

    @age.setter
    def age(self, a):
        self.year = date.today().year - value

    @classmethod
    def from_string(cls, text):
        title, author, year = text.split(";")
        return cls(title, author, int(year))

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.author == other.author
            and self.year == other.year
        )

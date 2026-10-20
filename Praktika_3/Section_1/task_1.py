class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Книгу {self.title}  написал {self.author} в {self.year} году"


example = Book("Капитанская дочка", "А.С.Пушкин", 1836)
print(example.info())

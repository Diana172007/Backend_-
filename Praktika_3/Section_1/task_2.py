class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
    def info(self):
        return f'Книгу {self.title}  написал {self.author} в {self.year}'
class Ebook(Book):
    def __init__(self,title,author,year,format):
        super().__init__(title,author,year)
        self.format=format
    def info(self):
        return  f'Книгу {self.title}  написал {self.author} в {self.year} году жанра {self.format}'
example = Ebook('Капитанская дочка', 'А.С.Пушкин', 1836,'Роман')
print(example.info())


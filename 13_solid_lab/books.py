class Book:
    MIN_PAGES = 20

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        if value < Book.MIN_PAGES:
            raise ValueError("The book must be more than 20 pages!")
        self.__pages = value

    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"


class Library:
    def __init__(self, books: list[Book] | None = None):
        self.books = books if books is not None else []

    def find_book(self, title: str) -> Book | None:
        return next((book for book in self.books if book.title == title), None)


book1 = Book("Dama pika", "Пушкин", 52)
book2 = Book("Вълчи капан I", "Христо Калев", 200)
book3 = Book("Лебедовата песен на майора ", "Христо Калев", 230)
book4 = Book("Нерон вълкът", "Христо Калев", 180)
book5 = Book("Сънят на уморения лъв", "Христо Калев", 170)

b = Library([book1, book2, book3, book4, book5])

print(b.find_book('Вълчи капан I'))

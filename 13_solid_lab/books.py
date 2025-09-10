class Book:
    def __init__(self, title, author, page):
        self.title = title
        self.author = author
        self.page = page

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, value):
        if value < 20:
            raise ValueError('The book must be more than 20 pages!')
        self.__page = value

    def __repr__(self):

        return f"Title: {self.title}, Author: {self.author}, Page: {self.page}."

class Library:

    def __init__(self, book: list[Book]):
        self.book = book

    def book_search_by_title(self, name):

        search = next((x for x in self.book if x.title == name), None)
        if search:
            return f"The book {name} has been found"


    def add_book(self, name_book: Book):

        if not isinstance(name_book, Book):
            raise TypeError('Not is isinstance!')

        if name_book not in self.book:
            self.book.append(name_book)
            return f"I added {name_book} to the library."

        return "The book is already in the library!"

book1 = Book("Dama pika", "Пушкин", 52)
book2 = Book("Вълчи капан I", "Христо Калев", 200)
book3 = Book("Лебедовата песен на майора ", "Христо Калев", 230)
book4 = Book("Нерон вълкът", "Христо Калев", 180)
book5 = Book("Сънят на уморения лъв", "Христо Калев", 170)

b = Library([book1, book2, book3, book4, book5])
print(b.add_book(book4))
print(b.book_search_by_title('Вълчи капан I'))

from typing import List, Dict

from project.user import User


class Library:

    def __init__(self):

        self. user_records: List[User] = []
        self. books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[str: Dict[str: int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):

        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for data in self.rented_books.values():
            if book_name in data:
                return (f'The book "{book_name}" is already rented'
                    f' and will be available in'
                    f' {data[book_name]} days!')

    def return_book(self, author:str, book_name:str, user: User):
        library = self.rented_books[user.username]
        if book_name in library:
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
            self.books_available[author].append(book_name)

        return f"{user.username} doesn't have this book in his/her records!"
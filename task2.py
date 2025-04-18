import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"({self.title} by {self.author} published ({self.year}))"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        log.info("Book was added: %s", book)

    def remove_book(self, title: str):
        original_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < original_count:
            log.info("Book removed: %s", title)
        else:
            log.warning("No book found with title: %s", title)

    def show_books(self):
        if self.books:
            log.info("Library collection:")
            for book in self.books:
                log.info(book)
        else:
            log.info("No books in the library. Please add some.")


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        try:
            year = int(year)
        except ValueError:
            log.error("Invalid year format. Please enter a number.")
            return
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                log.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

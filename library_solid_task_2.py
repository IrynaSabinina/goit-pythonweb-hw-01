from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Принцип SRP - окремий клас Book для зберігання інформації про книгу
class Book:
    def __init__(self, title: str, author: str, year: str) -> None:
        self.title: str = title
        self.author: str = author
        self.year: str = year

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# Принцип ISP - створюємо інтерфейс для бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass


# Принцип OCP - можна розширювати клас Library, не змінюючи його код
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        self.books = [book for book in self.books if book.title != title]
        logger.info(f"Book removed: {title}")

    def show_books(self) -> None:
        if not self.books:
            logger.info("No books in the library.")
        else:
            for book in self.books:
                logger.info(book)


# Принцип DIP - LibraryManager залежить від абстракції LibraryInterface
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


# Основна функція для роботи з бібліотекою
def main() -> None:
    library: Library = Library()
    manager: LibraryManager = LibraryManager(library)

    while True:
        command: str = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title: str = input("Enter book title: ").strip()
                author: str = input("Enter book author: ").strip()
                year: str = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title: str = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()

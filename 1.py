# Клас автора
class Author:
    def __init__(self, name):
        self.name = name

# Клас книги
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Клас бібліотеки
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу '{book.title}' додано.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книгу '{title}' видалено.")
                return
        print("Книгу не знайдено.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Знайдено книгу '{book.title}' автора {book.author.name}.")
                return
        print("Книгу не знайдено.")

# === Інтерактивна частина ===
lib = Library()

while True:
    print("\n1 - Додати книгу\n2 - Видалити книгу\n3 - Знайти книгу\n4 - Вихід")
    choice = input("Оберіть дію: ")

    if choice == "1":
        title = input("Введіть назву книги: ")
        author_name = input("Введіть ім’я автора: ")
        author = Author(author_name)
        book = Book(title, author)
        lib.add_book(book)
    elif choice == "2":
        title = input("Введіть назву книги для видалення: ")
        lib.remove_book(title)
    elif choice == "3":
        title = input("Введіть назву книги для пошуку: ")
        lib.find_book(title)
    elif choice == "4":
        print("Завершення роботи.")
        break
    else:
        print("Невірний вибір.")

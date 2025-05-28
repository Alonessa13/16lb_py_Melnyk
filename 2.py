# Клас книги з історією
class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False
        self.borrowed_by = None
        self.due_date = None

# Клас бібліотеки з видачею
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title, reader, due):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = reader
                book.due_date = due
                print(f"Книга '{title}' видана {reader}, до {due}.")
                return
        print("Книгу не знайдено або вже видано.")

    def return_book(self, title, reader, current_date):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                if book.borrowed_by != reader:
                    print("Ім’я не збігається з тим, хто взяв книгу.")
                    return
                if current_date > book.due_date:
                    print(f"Книга '{title}' повернута із запізненням.")
                else:
                    print(f"Книга '{title}' повернута вчасно.")
                book.is_borrowed = False
                book.borrowed_by = None
                book.due_date = None
                return
        print("Книга не була видана або не знайдена.")

# === Інтерактивна частина ===
lib = Library()

while True:
    print("\n1 - Додати книгу\n2 - Видати книгу\n3 - Повернути книгу\n4 - Вихід")
    choice = input("Оберіть дію: ")

    if choice == "1":
        title = input("Назва книги: ")
        lib.add_book(Book(title))
    elif choice == "2":
        title = input("Назва книги для видачі: ")
        reader = input("Ім’я читача: ")
        due = input("Крайній термін повернення (рррр-мм-дд): ")
        lib.borrow_book(title, reader, due)
    elif choice == "3":
        title = input("Назва книги для повернення: ")
        reader = input("Ваше ім’я: ")
        current = input("Сьогоднішня дата (рррр-мм-дд): ")
        lib.return_book(title, reader, current)
    elif choice == "4":
        print("Завершення роботи.")
        break
    else:
        print("Невірний вибір.")

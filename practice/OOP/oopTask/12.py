class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_issued = False
        Book.total_books += 1

    def issue_book(self):
        if self.__is_issued:
            print("Book is already issued.")
        else:
            self.__is_issued = True
            print("Book issued successfully.")

    def return_book(self):
        if not self.__is_issued:
            print("Book was not issued.")
        else:
            self.__is_issued = False
            print("Book returned successfully.")

    def is_issued(self):
        return self.__is_issued

    def show_info(self):
        status = "Issued" if self.__is_issued else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)

    def __str__(self):
        return f"{self.title} by {self.author}"


class Person:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")


class Member(Person):
    def __init__(self, name, member_id):
        super().__init__(name)
        self.member_id = member_id

    def show_info(self):
        print(f"Member Name: {self.name}")
        print(f"Member ID: {self.member_id}")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def add_member(self, member):
        self.members.append(member)
        print("Member added successfully.")

    def show_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n===== BOOKS =====")
        for book in self.books:
            book.show_info()

    def issue_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.issue_book()
                return

        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return

        print("Book not found.")

    @classmethod
    def show_total_books(cls):
        print(f"Total Books Added: {Book.total_books}")

    @staticmethod
    def library_rules():
        print("\n===== LIBRARY RULES =====")
        print("1. Return books within 15 days.")
        print("2. Keep books clean and safe.")
        print("3. Do not damage library property.")


# ---------------- MAIN PROGRAM ---------------- #

library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Add Member")
    print("6. Show Total Books")
    print("7. Show Library Rules")
    print("8. Polymorphism Demo")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(title, author)
        library.add_book(book)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        title = input("Enter Book Title to Issue: ")
        library.issue_book(title)

    elif choice == "4":
        title = input("Enter Book Title to Return: ")
        library.return_book(title)

    elif choice == "5":
        name = input("Enter Member Name: ")
        member_id = input("Enter Member ID: ")

        member = Member(name, member_id)
        library.add_member(member)

    elif choice == "6":
        Library.show_total_books()

    elif choice == "7":
        Library.library_rules()

    elif choice == "8":
        if not library.books or not library.members:
            print("Add at least one book and one member first.")
        else:
            print("\n===== POLYMORPHISM DEMO =====")

            items = [
                library.books[0],
                library.members[0]
            ]

            for item in items:
                item.show_info()

    elif choice == "9":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice. Try again.")
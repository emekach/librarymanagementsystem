library = {}

def add_book(title, author):
    book_id = len(library) + 1
    library[book_id] = {"title": title, "author": author, "available": True}
    print(f"Book '{title}' by {author} has been added with ID: {book_id}")

def list_books():
    print("List of books in the library:")
    for book_id, book in library.items():
        status = "Available" if book['available'] else "Borrowed"
        print(f"{book_id}. {book['title']} by {book['author']} - {status}")

def borrow_book(book_id, user_name):
    book = library.get(book_id)
    if not book:
        print("Invalid book ID.")
        return

    if book['available']:
        book['available'] = False
        print(f"Book '{book['title']}' has been borrowed by {user_name}")
    else:
        print("Book not available for borrowing.")

def return_book(book_id):
    book = library.get(book_id)
    if not book:
        print("Invalid book ID.")
        return

    if not book['available']:
        book['available'] = True
        print(f"Book '{book['title']}' returned.")
    else:
        print("The book is not borrowed.")

def main():
    while True:
        print("\nWelcome to the University of Benin Library System Menu:")
        print("1. Add a book")
        print("2. List all books")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            add_book(title, author)
        elif choice == "2":
            list_books()
        elif choice == "3":
            book_id = int(input("Enter the book ID to borrow: "))
            user_name = input("Enter your name: ")
            borrow_book(book_id, user_name)
        elif choice == "4":
            book_id = int(input("Enter the book ID to return: "))
            return_book(book_id)
        elif choice == "5":
            print("Goodbye!, Thank You for visiting our library")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

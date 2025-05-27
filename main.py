from models import Book
from db import Session


def add_book():
    print("\n Add a New Book")
    title = input("Enter the book title: ").strip()
    author = input("Enter the author name: ").strip()
    genre = input("Enter the genre: ").strip()

    if not title or not author or not genre:
        print("All fields are required.")
        return

    session = Session()
    new_book = Book(title=title, author=author, genre=genre)
    session.add(new_book)
    session.commit()
    print(f" Book '{title}' added successfully!")


def view_books():
    print("\n All Books:")
    session = Session()
    books = session.query(Book).all()

    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"{book.id}. {book.title} by {book.author} [{book.genre}]")
            
def delete_book():
    print("\n Delete a Book")
    session = Session()
    books = session.query(Book).all()

    if not books:
        print(" No books available to delete.")
        return

    for book in books:
        print(f"{book.id}. {book.title} by {book.author} [{book.genre}]")

    try:
        book_id = int(input("Enter the ID of the book to delete: ").strip())
        book_to_delete = session.query(Book).get(book_id)

        if not book_to_delete:
            print(" Book not found.")
            return

        confirm = input(f"Are you sure you want to delete '{book_to_delete.title}'? (y/n): ").lower()
        if confirm == "y":
            session.delete(book_to_delete)
            session.commit()
            print(f" Book '{book_to_delete.title}' deleted.")
        else:
            print("ℹ Delete cancelled.")

    except ValueError:
        print("Invalid input. Please enter a number.")



def main_menu():
    while True:
        print("\n==== Book Review CLI ====")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Delete a book")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
            
if __name__ == "__main__":
    main_menu()


from models import Book
from db import Session
from models import Book, Reader, Review



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
        print("No books available to delete.")
        session.close()
        return

    for book in books:
        print(f"{book.id}. {book.title} by {book.author} [{book.genre}]")

    try:
        book_id = int(input("Enter the ID of the book to delete: ").strip())
        book_to_delete = session.query(Book).get(book_id)

        if not book_to_delete:
            print("Book not found.")
            return

        confirm = input(f"Are you sure you want to delete '{book_to_delete.title}'? (y/n): ").lower()
        if confirm == "y":
            session.delete(book_to_delete)
            session.commit()
            print(f"Book '{book_to_delete.title}' deleted.")
        else:
            print("ℹ Delete cancelled.")

    except ValueError:
        print("Invalid input. Please enter a number.")
        session.close()



def add_review():
    print("\n Add a Review")
    session = Session()

    books = session.query(Book).all()
    if not books:
        print("No books available. Please add a book first.")
        session.close()
        return

    for book in books:
        print(f"{book.id}. {book.title} by {book.author}")

    try:
        book_id = int(input("Enter the ID of the book you want to review: ").strip())
        book = session.query(Book).get(book_id)

        if not book:
            print("Book not found.")
            session.close()
            return

        reader_name = input("Enter your name: ").strip()
        if not reader_name:
            print("Reader name is required.")
            session.close()
            return

        # Get or create reader
        reader = session.query(Reader).filter_by(name=reader_name).first()
        if not reader:
            reader = Reader(name=reader_name)
            session.add(reader)
            session.commit()

        rating = int(input("Enter a rating (1-5): ").strip())
        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5.")
            session.close()
            return

        comment = input("Enter your comment: ").strip()
        review = Review(rating=rating, comment=comment, book=book, reader=reader)

        session.add(review)
        session.commit()
        print(f"Review added for '{book.title}' by {reader.name}!")

    except ValueError:
        print("Invalid input. Please enter numbers where expected.")

    session.close()


def view_reviews():
    print("\n View Reviews for a Book")
    session = Session()

    books = session.query(Book).all()
    if not books:
        print("No books available.")
        session.close()
        return

    for book in books:
        print(f"{book.id}. {book.title} by {book.author}")

    try:
        book_id = int(input("Enter the ID of the book: ").strip())
        book = session.query(Book).get(book_id)

        if not book:
            print("Book not found.")
            session.close()
            return

        if not book.reviews:
            print("No reviews for this book yet.")
        else:
            print(f"\n Reviews for '{book.title}':")
            for review in book.reviews:
                print(f"- {review.reader.name} rated {review.rating}/5")
                print(f"  Comment: {review.comment}\n")

    except ValueError:
        print("Invalid input. Please enter a number.")
    
    session.close()
    

def view_reviews():
    print("\n View Reviews for a Book")
    session = Session()

    books = session.query(Book).all()
    if not books:
        print("No books available.")
        session.close()
        return

    for book in books:
        print(f"{book.id}. {book.title} by {book.author}")

    try:
        book_id = int(input("Enter the ID of the book to view reviews: ").strip())
        book = session.query(Book).get(book_id)

        if not book:
            print("Book not found.")
            session.close()
            return

        print(f"\n Reviews for '{book.title}':")
        if not book.reviews:
            print("No reviews yet.")
        else:
            for review in book.reviews:
                print(f"{review.rating}/5 by {review.reader.name}")
                print(f"{review.comment}\n")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    session.close()

def main_menu():
    while True:
        print("\n==== Book Review CLI ====")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Delete a book")
        print("4. Add a review")
        print("5. View reviews for a book")
        print("6. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            add_review()
        elif choice == "5":
            view_reviews()  
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main_menu()


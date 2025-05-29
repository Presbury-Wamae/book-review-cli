from models import Book
from db import Session
from sqlalchemy import func
from models import Book, Reader, Review


def register_reader():
    print("Register a New Reader")
    session = Session()

    name = input("Enter your name: ").strip()

    if not name:
        print("Name is required.")
        session.close()
        return

    existing_reader = session.query(Reader).filter_by(name=name).first()
    if existing_reader:
        print(f"Reader '{name}' is already registered.")
    else:
        new_reader = Reader(name=name)
        session.add(new_reader)
        session.commit()
        print(f"Reader '{name}' registered successfully!")

    session.close()


def view_reader_reviews():
    print("View Reviews by a Reader")
    session = Session()

    name = input("Enter the reader's name: ").strip()
    if not name:
        print("Reader name is required.")
        session.close()
        return

    reader = session.query(Reader).filter_by(name=name).first()
    if not reader:
        print(f"Reader '{name}' not found.")
        session.close()
        return

    reviews = reader.reviews
    if not reviews:
        print(f"Reader '{name}' has not written any reviews yet.")
    else:
        print(f"Reviews by '{name}':")
        for review in reviews:
            print(f"- '{review.book.title}' rated {review.rating}/5")
            print(f"  Comment: {review.comment}\n")

    session.close()





def add_book():
    print("Add a New Book")
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
    print(f"Book '{title}' added successfully!")


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
    print("Delete a Book")
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
            print("Delete cancelled.")

    except ValueError:
        print("Invalid input. Please enter a number.")
        session.close()



def add_review():
    print("Add a Review")
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
    print("View Reviews for a Book")
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
            print(f"Reviews for '{book.title}':")
            for review in book.reviews:
                print(f"- {review.reader.name} rated {review.rating}/5")
                print(f"  Comment: {review.comment}\n")

    except ValueError:
        print("Invalid input. Please enter a number.")
    
    session.close()
    

def book_insights():
    print("Book Insights")
    session = Session()

    books = session.query(Book).all()
    if not books:
        print("No books found.")
        session.close()
        return

    for book in books:
        review_count = session.query(func.count(Review.id)).filter(Review.book_id == book.id).scalar()
        average_rating = session.query(func.avg(Review.rating)).filter(Review.book_id == book.id).scalar()

        print(f"{book.title} by {book.author}")
        print(f"   - Total Reviews: {review_count}")
        if average_rating:
            print(f"   - Average Rating: {round(average_rating, 2)}/5")
        else:
            print("   - Average Rating: N/A (no reviews)")
        print()

    session.close()


def main_menu():
    while True:
        print("\n==== Book Review CLI ====")
        print("1. Register a reader")
        print("2. View reader's reviews")
        print("3. Add a new book")
        print("4. View all books")
        print("5. Delete a book")
        print("6. Add a review")
        print("7. View reviews for a book")
        print("8. Book insights")
        print("9. Exit")
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            register_reader()
        elif choice == "2":
            view_reader_reviews()
        elif choice == "3":
            add_book()
        elif choice == "4":
            view_books()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            add_review()
        elif choice == "7":
            view_reviews()  
        elif choice == "8":
            book_insights()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
            
if __name__ == "__main__":
    main_menu()


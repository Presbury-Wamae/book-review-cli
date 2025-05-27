# Book Review CLI
 Book Review CLI
A Command-Line Interface (CLI) application built with Python and SQLAlchemy for managing books and their reviews. Users can add books, write reviews, view reviews, and delete books — all from the terminal!





 Features
📖 Add new books to your reading list

📜 View all books

🗑️ Delete books

📝 Write reviews for books

🔍 View all reviews for a selected book

🛠️ Technologies Used
Python 3

SQLAlchemy (ORM)

SQLite (Database)

Alembic (for database migrations)




📦 Installation
Clone the repository

bash
Copy
Edit
git clone <your-repo-url>
cd book-review-cli
Create a virtual environment & activate it

bash
Copy
Edit
python3 -m venv virtual
source virtual/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up the database

bash
Copy
Edit
alembic upgrade head
▶️ Usage
Start the application with:

bash
Copy
Edit
python main.py




Follow the on-screen instructions to:

Add a book

View the book list

Delete a book

Add a review

View all reviews for a book




🧪 Example
pgsql
Copy
Edit
==== Book Review CLI ====
1. Add a new book
2. View all books
3. Delete a book
4. Add a review
5. View reviews for a book
6. Exit



🧠 Learning Objectives
This project reinforces:

Object-Oriented Programming (OOP)

One-to-Many relationships using SQLAlchemy

Using Alembic for managing database migrations

Building user-friendly CLI tools in Python




📁 Project Structure
css
Copy
Edit
book-review-cli/
├── alembic/
├── models.py
├── main.py
├── db.py
├── README.md
├── requirements.txt



🙌 Acknowledgments
Built as part of the Phase 3 Python/SQL ORM Project at Moringa School.
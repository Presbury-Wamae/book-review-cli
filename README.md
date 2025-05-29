
BOOK REVIEW CLI
Your personal command-line book tracker and review system


OVERVIEW
The Book Review CLI is a command-line application that allows users to:

Add and manage books

Write and view reviews for books

Register readers and track their activity

Get insights like total reviews and average rating per book

Built using Python and SQLAlchemy, this tool is ideal for bootcamp projects, personal tracking, or CLI-based apps.


🛠 FEATURES
Add, view, and delete books

Add reviews to books

View all reviews for a selected book

Register readers

View all reviews by a specific reader

View book insights: number of reviews and average rating



PROJECT STRUCTURE
bash
Copy
Edit
book-review-cli/
├── alembic/                  # Alembic migration scripts
├── db.py                     # SQLAlchemy session and engine setup
├── main.py                   # CLI entry point and logic
├── models.py                 # SQLAlchemy models (Book, Reader, Review)
├── README.md                 # You're here!
SETUP INSTRUCTIONS
Clone the repo

bash
Copy
Edit
git clone <your-repo-url>
cd book-review-cli
Create and activate a virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run Alembic migrations

bash
Copy
Edit
alembic upgrade head
Run the app

bash
Copy
Edit
python main.py


USAGE GUIDE
Once the app is running, you’ll see a menu like:

markdown
Copy
Edit
==== Book Review CLI ====
1. Add a new book
2. View all books
3. Delete a book
4. Add a review
5. View reviews for a book
6. Register a reader
7. View reader's reviews
8. Book insights
9. Exit
Follow the prompts to interact with the database.



TECHNOLOGIES USED
Python 3

SQLAlchemy ORM

SQLite (default DB)

Alembic (migrations)



INSIGHTS FEATURE
This feature provides:

Number of reviews per book

Average rating per book

Perfect for understanding how books are performing among readers.



FUTURE IMPROVEMENTS
Add CLI-based search for books

Filter reviews by rating

Export data to CSV or JSON

Add login system for readers



AUTHOR
Project built by Presbury Wamae
A student at Moringa School, passionate about web dev and game design
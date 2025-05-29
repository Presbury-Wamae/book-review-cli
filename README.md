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

book-review-cli/  

├── alembic/ 					# Alembic migration scripts  

├── db.py 					# SQLAlchemy session and engine setup  

├── main.py 					# CLI entry point and logic 

├── models.py 				# SQLAlchemy models (Book, Reader, Review) 

 ├── README.md 				# You're here!  

 

SETUP INSTRUCTIONS  

Clone the repo 

 git clone  

cd book-review-cli  

 

Create and activate a virtual environment 

python3  -m  venv  virtual 

source venv/bin/activate  

 

Install dependencies 

pip install -r requirements.txt  

 

Run Alembic migrations 

 alembic upgrade head  

 

Run the app 

 python main.py 

 

 

 

 

 

 

 

USAGE GUIDE  

Once the app is running, you’ll see a menu like: 

markdown Copy Edit ==== Book Review CLI ==== 

Add a new book 

View all books 

Delete a book 

Add a review 

View reviews for a book 

Register a reader 

View reader's reviews 

Book insights 

Exit Follow the prompts to interact with the database. 

 

TECHNOLOGIES USED  

Python 3 

SQLAlchemy ORM 

SQLite (default DB) 

Alembic (migrations) 

 

INSIGHTS FEATURE  

This feature provides: 

Adding a new book 

Viewing all books  

Deleting a specific book 

Registering a new reader  

Viewing all reviews a reader has made  

Adding a review to a book 

Viewing reviews for a book   

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

 
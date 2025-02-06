# Dream-Journal-CLI
a simple yet unique command-line application that helps users track and analyze their dreams over time. Users can log dreams, categorize them by theme (e.g., adventure, nightmare, lucid), and reflect on recurring patterns. The system provides an easy way to revisit past dreams and look for insights into sleep habits or subconscious thoughts.

Features

Add new dreams with a title, description, and category.

View all logged dreams.

Search for a dream by title.

Filter dreams by category.

Delete a dream from the journal.

User-friendly CLI interface with input validation and error handling.

Installation

Prerequisites

Ensure you have Python 3 installed on your system.

Setup Instructions

Clone the repository:

git clone <repo-url>
cd dream-journal-cli

Install dependencies using Pipenv:

pipenv install

Activate the virtual environment:

pipenv shell

Set up the database:

python lib/db/seed.py

Usage

Run the CLI application with:

python lib/cli.py

Available Commands

Add a Dream - Enter a title, description, and select a category.

View All Dreams - List all logged dreams.

View Dreams by Category - Choose a category to filter dreams.

Find a Dream by Title - Search for a dream using keywords.

Delete a Dream - Remove a dream from the journal.

Exit - Close the application.

Database Structure

The application includes two main models:

Dream: Stores dream title, description, category, and timestamp.

Category: Defines different dream categories (e.g., Lucid, Nightmare, Fantasy).

Future Enhancements

Edit dreams after creation.

Export dreams to a text file.

Implement user authentication for personalized journals.

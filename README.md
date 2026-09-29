# Library Management System

A command-line library management system built in Python, using OOP to
model books, members, and borrowing/returning with JSON file persistence.

## Features
- Add books and members
- Check book availability by ISBN
- View all books
- Borrow and return books (tracks who has what)
- Data persists between sessions via JSON

## Tech Stack
- Python 3 (standard library only — no external dependencies)

## How to Run
​```bash
python library.py
​```
Follow the on-screen menu to add books, add members, borrow, or return.

## Project Structure
- Book — represents a single book (title, author, ISBN, availability)
- Member — represents a library member and their currently issued books
- Library — manages the collections and core operations (add/find/borrow/return/save/load)

## What I Learned
- Structuring a multi-class program with OOP (composition between Library, Book, Member)
- Persisting program state to disk with JSON
- Basic CLI application design with a menu-driven loop

## Planned Improvements
- Track issue/return dates properly
- Ability to remove books/members and view a member's borrowed books
- Save incrementally instead of only on exit

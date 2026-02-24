# SQLite Poems 🖋

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?style=flat&logo=sqlite)[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]

## 📖 About the Project

This repository is being developed for future integration with the website of the poet Oleg Shlygin.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)] It serves as a lightweight backend utility to process, store, and manage a collection of poems using Python and an SQLite database.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)] 

The project aims to simplify the way poetry is stored and retrieved, transitioning it from a standard raw text format into a structured relational database for easier web query and display.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]

## 🗂 Project Structure

- `main.py` — The primary Python script.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)] It contains the logic for reading the text, processing the data, and interacting with the SQLite database.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]
- `Poems.txt` — The source text file containing the raw collection of poems.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]
- `pdatabase1.db` — The SQLite database where the parsed poems and their metadata are structured and stored.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]
- `README.md` — This documentation file.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]

## 🚀 Getting Started

### Prerequisites

To run this project, you will need Python 3.x installed on your machine.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)] SQLite3 is included by default in Python's standard library, so no external database software is required.[[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]

### Installation & Setup

1. Clone the repository:
      git clone https://github.com/AresRense/sqlite-poems.git
   [[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]

2. Navigate into the directory:
      cd sqlite-poems
   [[1](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FAresRense%2Fsqlite-poems)]

3. Run the script:
   Execute the main Python script to run the database operations:
   ```bash
   python main.py

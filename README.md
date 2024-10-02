# Data Engineering Challenge

A project demonstrating data engineering tasks using SQLite and Python, including database creation, data population, and querying. Managed with Poetry and includes unit tests for verification.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)

## Prerequisites
- Python 3.8 or higher
- [Poetry](https://python-poetry.org/docs/#installation)
  
## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/MilonTheDataGuy/data-engineering-challenge.git
    cd data-engineering-challenge
    ```  
  
2. **Install dependencies:** 
    ```sh  
    poetry install
    ```
  
## Usage
  
1. **Run the main script:**
    ```sh
    poetry run python src/main.py
    poetry run python src/execute_sql.py
    
    ```
    This command will create and populate the SQLite database with ratings data and create the necessary tables.
  
## Running Tests
  
1. **Run all tests:**
    ```sh
    poetry run python -m unittest discover -s tests
    ```
  
    This command will discover and run all test files in the `tests` directory.
  
2. **Run a specific test file:**
    ```sh
    poetry run python -m unittest tests.unittest_cases
    ```
  
    This command will run the `tests/unittest_cases.py` file specifically.
  
## Project Structure
data-engineering-challenge/
├── README.md
├── pyproject.toml
├── poetry.lock
├── data/
│ ├── ratings.db
├── src/
│ ├── init.py
│ ├── main.py
│ ├── execute_sql.py
│ ├── sql/
│ │ ├── create_aggregates_table.sql
│ │ ├── create_ratings_table.sql
│ │ ├── top_products.sql
├── tests/
│ ├── init.py
│ ├── unittest_cases.py

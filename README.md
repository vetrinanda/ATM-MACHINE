# ATM Machine API

## Overview

ATM Machine is a modern banking system implemented in Python, providing a RESTful API for core banking operations. Built with FastAPI and SQLAlchemy, this project allows users to create accounts, manage balances, and perform secure transactions through HTTP endpoints. Account data is stored in a relational database, ensuring data integrity and scalability.

## Features

- Create new bank accounts with unique account numbers and PINs
- Deposit and withdraw funds securely
- Check account balances
- Change ATM PIN
- Robust input validation and error handling
- Persistent storage using SQLAlchemy ORM

## Technology Stack

- Python 3.10+
- FastAPI (API framework)
- SQLAlchemy (ORM/database management)
- Pydantic (data validation)
- dotenv (environment variable management)

## Getting Started

1. **Clone the repository:**
	```bash
	git clone <repository-url>
	cd ATM-MACHINE
	```

2. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```

3. **Set up environment variables:**
	- Create a `.env` file with your database connection string and other settings as needed.

4. **Run the application:**
	```bash
	uvicorn app.main:app --reload
	```

5. **Access the API documentation:**
	- Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser for interactive API docs (Swagger UI).

## Project Structure

- `app/` - Main application package
  - `main.py` - FastAPI app and endpoints
  - `models.py` - SQLAlchemy models
  - `database.py` - Database configuration
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## License

This project is licensed under the MIT License.

# ATM Management System

## Project Overview

ATM Management System is a console-based banking application developed using Python and MySQL.

The project simulates basic ATM operations such as user authentication, checking balance, depositing money, withdrawing money, transferring money, viewing transaction history, and viewing customer profile details.

---

## Technologies Used

- Python 3.11
- MySQL
- MySQL Connector/Python

---

## Features

### 1. User Authentication
- Login using account number and PIN
- Account validation using MySQL database

### 2. Account Operations
- Check account balance
- Deposit money
- Withdraw money
- Transfer money between accounts

### 3. Transaction Management
- Stores all transactions in database
- View transaction history

### 4. Customer Profile
- View customer details
- Display account information

---

## Database Design

The project uses three main tables:

### Customers Table

Stores customer information:

- Customer ID
- Full Name
- Mobile Number
- Email
- Address

### Accounts Table

Stores account details:

- Account Number
- Customer ID
- PIN
- Balance
- Account Type
- Account Status

### Transactions Table

Stores banking transactions:

- Transaction ID
- Account Number
- Transaction Type
- Amount
- Description
- Transaction Time

---

## Project Structure
ATM_Management_System

│
├── main.py
│
├── database
│ ├── db_connection.py
│ └── schema.sql
│
├── services
│ ├── auth_service.py
│ ├── account_service.py
│ └── atm_service.py
│
├── models
│ └── account.py
│
├── requirements.txt
└── README.md


---

## Installation

Install required packages:
pip install -r requirements.txt


---

## Database Configuration

1. Create MySQL database.
2. Execute SQL queries from `schema.sql`.
3. Update MySQL username and password in:
database/db_connection.py



---

## Running the Project

Run the application:
python main.py


---

## Future Enhancements

- GUI based interface
- Change PIN functionality
- Mini statement generation
- Admin dashboard
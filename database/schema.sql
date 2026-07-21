CREATE DATABASE atm_management_system;
USE atm_management_system;
CREATE TABLE customers
(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,

    full_name VARCHAR(100) NOT NULL,

    mobile VARCHAR(10) NOT NULL UNIQUE,

    email VARCHAR(100) UNIQUE,

    address VARCHAR(200),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE accounts
(
    account_no BIGINT PRIMARY KEY,

    customer_id INT NOT NULL,

    pin CHAR(4) NOT NULL,

    balance DECIMAL(12,2) NOT NULL DEFAULT 0.00,

    account_type ENUM('Savings','Current') DEFAULT 'Savings',

    status ENUM('Active','Blocked') DEFAULT 'Active',

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);
CREATE TABLE transactions
(
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,

    account_no BIGINT NOT NULL,

    transaction_type ENUM
    (
        'Deposit',
        'Withdraw',
        'Transfer'
    ) NOT NULL,

    amount DECIMAL(12,2) NOT NULL,

    description VARCHAR(255),

    transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(account_no)
    REFERENCES accounts(account_no)
);
'''SHOW TABLES;
DESC customers;

DESC accounts;

DESC transactions;
'''
INSERT INTO customers (full_name, mobile, email, address)
VALUES
('Vaishali Gaikwad', '9876543210', 'vaishali@gmail.com', 'Pune'),
('Rahul Sharma', '9876543211', 'rahul@gmail.com', 'Mumbai'),
('Priya Patil', '9876543212', 'priya@gmail.com', 'Nashik');

SELECT * FROM customers;


INSERT INTO accounts
(account_no, customer_id, pin, balance, account_type, status)
VALUES
(10010001, 1, '1234', 50000.00, 'Savings', 'Active'),
(10010002, 2, '4321', 25000.00, 'Savings', 'Active'),
(10010003, 3, '1111', 75000.00, 'Current', 'Active');

SELECT * FROM accounts;



INSERT INTO transactions
(account_no, transaction_type, amount, description)
VALUES
(10010001, 'Deposit', 50000, 'Opening Balance'),

(10010002, 'Deposit', 25000, 'Opening Balance'),

(10010003, 'Deposit', 75000, 'Opening Balance');

SELECT * FROM transactions;


#verify
'''SELECT
c.customer_id,
c.full_name,
a.account_no,
a.balance
FROM customers c
JOIN accounts a
ON c.customer_id = a.customer_id;'''

from database.db_connection import get_connection


class AccountService:

    def __init__(self):
        self.connection = get_connection()

    def deposit(self, account_no):

        try:

            amount = float(input("Enter amount to deposit: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            cursor = self.connection.cursor()

            # Update balance
            update_query = """
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_no = %s
            """

            cursor.execute(update_query, (amount, account_no))

            # Save transaction
            transaction_query = """
            INSERT INTO transactions
            (account_no, transaction_type, amount, description)
            VALUES
            (%s, 'Deposit', %s, %s)
            """

            cursor.execute(
                transaction_query,
                (account_no, amount, "Cash Deposit")
            )

            self.connection.commit()

            # Get updated balance
            cursor.execute(
                "SELECT balance FROM accounts WHERE account_no=%s",
                (account_no,)
            )

            balance = cursor.fetchone()[0]

            print("\nDeposit Successful!")
            print(f"Updated Balance: ₹{balance:.2f}")

            cursor.close()

        except ValueError:
            print("Please enter a valid numeric amount.")

        except Exception as e:
            self.connection.rollback()
            print(f"\nDatabase Error: {e}")
    
    
    def withdraw(self, account_no):
        """
        Withdraw money from account
        and record the transaction.
        """

        try:

            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= 0:
                print("Amount must be greater than 0.")
                return

            cursor = self.connection.cursor()

            # Check current balance
            balance_query = """
            SELECT balance
            FROM accounts
            WHERE account_no = %s
            """

            cursor.execute(balance_query, (account_no,))

            result = cursor.fetchone()

            current_balance = float(result[0])


            # Check sufficient balance
            if amount > current_balance:
                print("\nInsufficient Balance!")
                print(f"Available Balance: ₹{current_balance:.2f}")
                cursor.close()
                return


            # Update balance
            update_query = """
            UPDATE accounts
            SET balance = balance - %s
            WHERE account_no = %s
            """

            cursor.execute(
                update_query,
                (amount, account_no)
            )


            # Insert transaction
            transaction_query = """
            INSERT INTO transactions
            (account_no, transaction_type, amount, description)
            VALUES
            (%s, 'Withdraw', %s, %s)
            """

            cursor.execute(
                transaction_query,
                (account_no, amount, "Cash Withdrawal")
            )


            self.connection.commit()


            # Get updated balance
            cursor.execute(
                "SELECT balance FROM accounts WHERE account_no=%s",
                (account_no,)
            )

            balance = cursor.fetchone()[0]


            print("\nWithdrawal Successful!")
            print(f"Withdrawn Amount: ₹{amount:.2f}")
            print(f"Remaining Balance: ₹{balance:.2f}")


            cursor.close()


        except ValueError:
            print("Please enter a valid numeric amount.")


        except Exception as e:
            self.connection.rollback()
            print(f"Database Error: {e}")
    
    def transfer(self, sender_account_no):

        """
        Transfer money from one account to another.
        """

        try:

            receiver_account_no = input("Enter receiver account number: ").strip()

            amount = float(input("Enter amount to transfer: ₹"))


            if amount <= 0:
                print("Amount must be greater than 0.")
                return


            cursor = self.connection.cursor()


            # Check receiver account exists
            receiver_query = """
            SELECT account_no
            FROM accounts
            WHERE account_no = %s
            """

            cursor.execute(
                receiver_query,
                (receiver_account_no,)
            )

            receiver = cursor.fetchone()


            if receiver is None:
                print("Receiver account does not exist.")
                cursor.close()
                return



            # Check sender balance
            balance_query = """
            SELECT balance
            FROM accounts
            WHERE account_no = %s
            """

            cursor.execute(
                balance_query,
                (sender_account_no,)
            )

            sender_balance = float(cursor.fetchone()[0])


            if amount > sender_balance:
                print("\nInsufficient Balance!")
                print(f"Available Balance: ₹{sender_balance:.2f}")
                cursor.close()
                return



            # Deduct money from sender
            debit_query = """
            UPDATE accounts
            SET balance = balance - %s
            WHERE account_no = %s
            """

            cursor.execute(
                debit_query,
                (amount, sender_account_no)
            )



            # Add money to receiver
            credit_query = """
            UPDATE accounts
            SET balance = balance + %s
            WHERE account_no = %s
            """

            cursor.execute(
                credit_query,
                (amount, receiver_account_no)
            )



            # Sender transaction
            sender_transaction = """
            INSERT INTO transactions
            (account_no, transaction_type, amount, description)
            VALUES
            (%s, 'Transfer', %s, %s)
            """

            cursor.execute(
                sender_transaction,
                (
                    sender_account_no,
                    amount,
                    f"Transferred to {receiver_account_no}"
                )
            )



            # Receiver transaction
            receiver_transaction = """
            INSERT INTO transactions
            (account_no, transaction_type, amount, description)
            VALUES
            (%s, 'Transfer', %s, %s)
            """

            cursor.execute(
                receiver_transaction,
                (
                    receiver_account_no,
                    amount,
                    f"Received from {sender_account_no}"
                )
            )



            self.connection.commit()


            print("\nTransfer Successful!")
            print(f"Amount Transferred: ₹{amount:.2f}")
            print(f"To Account: {receiver_account_no}")



            cursor.close()



        except ValueError:
            print("Please enter a valid numeric amount.")


        except Exception as e:
            self.connection.rollback()
            print(f"Database Error: {e}")

    def transaction_history(self, account_no):

        try:

            cursor = self.connection.cursor(dictionary=True)


            query = """
            SELECT
                transaction_id,
                transaction_type,
                amount,
                description,
                transaction_time
            FROM transactions
            WHERE account_no = %s
            ORDER BY transaction_time DESC
            """


            cursor.execute(query, (account_no,))


            transactions = cursor.fetchall()


            if not transactions:
                print("\nNo transactions found.")
                return


            print("\n========== TRANSACTION HISTORY ==========")


            for t in transactions:

                print("--------------------------------")
                print("Transaction ID :", t["transaction_id"])
                print("Type            :", t["transaction_type"])
                print("Amount          : ₹", t["amount"])
                print("Description     :", t["description"])
                print("Date            :", t["transaction_time"])


            cursor.close()


        except Exception as e:

            print("Database Error:", e)

    def view_profile(self, account_no):

        try:

            cursor = self.connection.cursor(dictionary=True)


            query = """
            SELECT
                c.full_name,
                c.mobile,
                c.email,
                c.address,
                a.account_no,
                a.account_type,
                a.status
            FROM customers c
            JOIN accounts a
            ON c.customer_id = a.customer_id
            WHERE a.account_no = %s
            """


            cursor.execute(query, (account_no,))


            profile = cursor.fetchone()


            if profile:

                print("\n========== PROFILE ==========")

                print("Name          :", profile["full_name"])
                print("Mobile        :", profile["mobile"])
                print("Email         :", profile["email"])
                print("Address       :", profile["address"])
                print("Account No    :", profile["account_no"])
                print("Account Type  :", profile["account_type"])
                print("Status        :", profile["status"])


            cursor.close()


        except Exception as e:

            print("Database Error:", e)
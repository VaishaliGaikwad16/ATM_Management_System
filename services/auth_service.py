from database.db_connection import get_connection


class AuthService:

    def __init__(self):
        self.connection = get_connection()

    def login(self):

        attempts = 3

        while attempts > 0:

            account_no = input("Enter Account Number : ").strip()
            pin = input("Enter PIN : ").strip()

            cursor = self.connection.cursor(dictionary=True)

            query = """
            SELECT
                a.account_no,
                a.balance,
                a.account_type,
                a.status,
                c.customer_id,
                c.full_name,
                c.mobile,
                c.email,
                c.address
            FROM accounts a
            JOIN customers c
            ON a.customer_id = c.customer_id
            WHERE a.account_no = %s
            AND a.pin = %s
            AND a.status = 'Active'
            """

            cursor.execute(query, (account_no, pin))

            account = cursor.fetchone()

            if account:
                return account

            attempts -= 1

            print("\nInvalid Account Number or PIN.")
            print(f"Attempts Left : {attempts}")

        return None

    def get_account_details(self, account_no):

        cursor = self.connection.cursor(dictionary=True)

        query = """
        SELECT
            a.account_no,
            a.balance,
            a.account_type,
            a.status,
            c.customer_id,
            c.full_name,
            c.mobile,
            c.email,
            c.address
        FROM accounts a
        JOIN customers c
        ON a.customer_id = c.customer_id
        WHERE a.account_no = %s
        """

        cursor.execute(query, (account_no,))

        return cursor.fetchone()
from services.auth_service import AuthService
from services.account_service import AccountService


class ATM:

    def __init__(self):
        self.auth_service = AuthService()
        self.account_service = AccountService()

    def start(self):

        print("=" * 50)
        print("      ATM MANAGEMENT SYSTEM")
        print("=" * 50)

        account = self.auth_service.login()

        if account:

            print("\nLogin Successful!")

            print("=" * 50)
            print(f"Welcome, {account['full_name']}")
            print("=" * 50)

            self.dashboard(account)

        else:
            print("\nLogin Failed.")

    def dashboard(self, account):

        while True:

            print("\n========== ATM MENU ==========")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Transaction History")
            print("6. View Profile")
            print("7. Logout")

            choice = input("\nEnter your choice : ")

            if choice == "1":
                print(f"\nCurrent Balance : ₹{account['balance']:.2f}")

            elif choice == "2":
                self.account_service.deposit(account["account_no"])

                # Refresh balance after deposit
                account = self.auth_service.get_account_details(account["account_no"])

            elif choice == "3":
                self.account_service.withdraw(account["account_no"])

                # Refresh balance after withdrawal
                account = self.auth_service.get_account_details(account["account_no"])

            elif choice == "4":

                self.account_service.transfer(
                    account["account_no"]
                )

                account = self.auth_service.get_account_details(
                    account["account_no"]
                )
           
            elif choice == "5":

                self.account_service.transaction_history(
                    account["account_no"]
                )

            elif choice == "6":

                self.account_service.view_profile(
                    account["account_no"]
                )
            elif choice == "7":
                print("\nThank you for using our ATM.")
                break

            else:
                print("\nFeature will be implemented in the next modules.")
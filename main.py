from client import Client
from bank import Bank

bank = Bank()
print("Welcome to {}!".format(bank.name))
running = True

while running:
    print()
    print("Choose an option:"
          "1. Open a new account."
          "2. Open an existing account."
          "3. Exit.")
    choice = int(input("1, 2, or 3: "))
    if choice == 1:
        print("\nOpen New Account - Fill Below Details")
        client = Client(input("Name: "), int(input("Deposit Amount: $ ")))
        bank.update_db(client)
        print("\nAccount Created Successfully! Your Account Number is: ", client.account['account_number'])
    elif choice == 2:
        print("\nOpen Existing Account. Please Enter Credentials Below.")
        name = input("Name: ")
        account_number = int(input("Account Number: "))
        current_client = bank.authentication(name, account_number)
        if current_client:
            print("\nWelcome {} !".format(current_client.account['name']))
            account_open = True
            while account_open:
                print("""\nChoose An Option:"
                      "1. Withdraw"
                      "2. Deposit"
                      "3. Balance"
                      "4. Exit\n""")
                account_choice = int(input("1, 2, 3 or 4: "))
                if account_choice == 1:
                    current_client.withdraw(int(input("\nWithdraw Amount: $ ")))
                elif account_choice == 2:
                    current_client.deposit(int(input("\nDeposit Amount: $ ")))
                elif account_choice == 3:
                    print()
                    current_client.balance()
                else:
                    print("\nThank You for Visiting!")
                    current_client = ''
                    account_open = False
        else:
            print("\nAuthentication Failed ! No Account Found.")
            continue
    else:
        print("\nGoodbye !!!")
        running = False


#show balance, withdraw, deposit
def check_balance():
    print(f"your current balance is {balance}")


def deposit(amount):
    global balance
    if amount > 0:
        balance  += amount
    else:
        print("You cannot deposit negative or zero amount")

def withdraw(amount):
    global balance
    if amount <=0:
        print("You cannot withdraw negative or zero amount")
    elif amount > balance:
        print("You cannot withdraw , insufficient balance")
    else:
        balance -= amount



balance= 0.0



print("WELCOME TO ABC BANK!!")
while True:
    print("1. check your balance")
    print("2. deposit your amoubt")
    print("3. withdraw an amount")
    print("4. exit")
    choice = int(input("Enter your choice(1-4): "))
    if choice == 1:
        check_balance()
    elif choice == 2:
        amt = float(input("Enter the amount to deposit: "))
        deposit(amt)

    elif choice == 3:
        amt = float(input("Enter the amount to withdraw: "))
        withdraw(amt)
    elif choice == 4:
        break
    else:
        print("Invalid choice!! RE-TRY")
    print("thankyou for banking with us!!")


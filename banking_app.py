name = input("What is your name? ")
balance = int(input("Enter your current balance: "))

deposit = int(input("Deposit amount: "))
balance += deposit

withdraw = int(input("Withdrawal amount: "))
balance -= withdraw

print(("Hello " + name + " YOUR NEW BALANCE IS " + str(balance)).title())

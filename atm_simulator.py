Balance= 1000
deposit_limit = 10000

def withdraw(withdraw_amount):
    if withdraw_amount < 0:
        print("Withdraw amount should be greater than zero")
        return Balance
    elif withdraw_amount > Balance:
        print("insufficient in account")
        return Balance
    else:
        newBalance= Balance-withdraw_amount
        return newBalance
    
def deposit(deposit_amount):
    if deposit_amount<0:
        print ("invalid deposit amount")
    elif deposit_amount>deposit_limit:
        print("deposit limit reached, max limit is - ", deposit_limit)
    else:
        deposit=Balance+deposit_amount
        return deposit
        
    
print("ATM")
print("""
1. Balance
2. withdraw
3. DEPOSIT
4. QUIT
""")


option=int(input("enter option:"))


if option==1:
    print("Balance is 1000")

    
if option==2:
    print("Balance is 1000")
    withdraw_amount=float(input("enter withdraw anount"))
    print (withdraw(withdraw_amount))

    
if option==3:
    print("Balance is 1000",Balance)
    deposit_amount=float(input("enter deposit amount"))
    print(deposit(deposit_amount))
    
if option==4:
    exit()



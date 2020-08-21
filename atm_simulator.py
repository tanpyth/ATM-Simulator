print("hello python learning")
print ("Hi Tanvi!")

Balance= 1000
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
    withdraw=float(input("enter withdraw anount"))
    if withdraw>0:
        newbalance=(Balance-withdraw)
        print(newbalance)
    elif withdraw>Balance:
        print("no funds in account")
    else:
        print("none withdraw made")

    
if option==3:
    print("Balance is 1000",Balance)
    DEPOSIT=float(input("enter DEPOSIT amount"))
    if DEPOSIT>0:
        currentbalance=(Balance+DEPOSIT)
        print(currentbalance)
    else:
        print("none deposit made")
if option==4:
    exit()


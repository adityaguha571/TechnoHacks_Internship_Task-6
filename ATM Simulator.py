print("Welcome")
p = int(input("Please enter your pin number: "))
m = 100000

while True:
    if p != 0:
        print("1-Check Balance")
        print("2-Deposit")
        print("3-Withdraw")
        print("4-Exit")

        choice = int(input("Please choose a method: "))

        if choice == 1:
            print("Your Account Balance is: ", m)

        elif choice == 2:
            d = int(input("Enter the amount to be deposited: "))
            if d > 0:
                print(d, "is successfully deposited")
                m += d
                print("The Available Balance is: ", m)
            else:
                print("The Amount is not Deposited")

        elif choice == 3:
            w = int(input("Enter the Amount to be withdrawn: "))
            if w <= m:
                print(w, "is withdrawn successfully")
                m -= w
                print("The Available Balance is: ", m)
            else:
                print("Insufficient balance. The amount is not Withdrawn")

        elif choice == 4:
            print("Thank you for using our service. Goodbye!")
            break

        else:
            print("Wrong choice")
    else:
        print("Invalid pin number. Exiting...")
        break

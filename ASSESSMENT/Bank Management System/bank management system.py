"""                                          Core Python Assessment Test  Bank Management System           """



li = []

class myclass:
 
    def add_customer(self):
        d = {}

        c = input("Enter Your Name ===> :")
        a = int(input("Enter Account No ===> :"))
        b = int(input("Enter Your Balance ===> :"))

        

        d["Account No"] = a
        d["Name"] = c
        d["Balance"] = b

        li.append(d)

        print("Customer Add Successfully !!")

        
    def view_customer(self):
        if not li:
            print("\n Customer Name Not match to Records !!")
            return
        try:
            n = input("Enter the name to search :")
        except:
            print("\nInvalid Input Name !!")

        for i , entry in enumerate(li,1):
            if entry["Name"] == n:
                print("\nCustomer Found !!")
                print(f"{i}. Name : {entry["Name"]}, Account No : {entry["Account No"]}, Balance : ₹{entry["Balance"]}")


        
    def search_customer(self):
        if not li:
            print("\nAccount No not Match to Record ")
            return
        try:
            a = int(input("Enter Account No to Search :"))
        except:
            print("\n Invalid Input please Enter the Account No !!")
            return

        for d in li:
            if d["Account No"] == a:
                print(f"Account Found : Name : {d["Name"]}, Account No : {d["Account No"]}, Balance : ₹{d["Balance"]}")
            # else:
            #     print("Account No not Match to Record !!")



    def view_all(self):
            print("All Account Details !!")
            for i ,entry in enumerate(li,1):
                print(f"{i}. Name : {entry["Name"]}, Account No : {entry["Account No"]}, Balance : ₹{entry["Balance"]}")



    def total_amount(self):
            if not li:
                print("\nNo Customer Data Available !!")
                return

            total = sum(entry["Balance"] for entry in li)
            print(f"\n Total Balance in Bank : ₹{total}")


    def find_customer_by_account(self, account_no):
        for entry in li:
            if entry["Account No"] == account_no:
                return entry
        return None

    def withdraw_amount(self):
        try:
            account_no = int(input("Enter Your Account No: "))
        except ValueError:
            print("Invalid Account Number!")
            return

        customer = self.find_customer_by_account(account_no)
        if customer is None:
            print("Account No not found!")
            return

        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount!")
            return

        if amount <= 0:
            print("Amount should be greater than zero.")
            return

        if customer["Balance"] >= amount:
            customer["Balance"] -= amount
            print(f"Withdrawal Successful! New Balance: ₹{customer['Balance']}")
        else:
            print("Insufficient Balance!")

    def deposit_amount(self):
        try:
            account_no = int(input("Enter Your Account No: "))
        except ValueError:
            print("Invalid Account Number!")
            return

        customer = self.find_customer_by_account(account_no)
        if customer is None:
            print("Account No not found!")
            return

        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid amount!")
            return

        if amount <= 0:
            print("Amount should be greater than zero.")
            return

        customer["Balance"] += amount
        print(f"Deposit Successful! New Balance: ₹{customer['Balance']}")

    def view_balance(self):
        try:
            account_no = int(input("Enter Your Account No: "))
        except ValueError:
            print("Invalid Account Number!")
            return

        customer = self.find_customer_by_account(account_no)
        if customer is None:
            print("Account No not found!")
            return

        print(f"Current Balance: ₹{customer['Balance']}")
        

obj = myclass()


while True:
    menu = """
    =========== Select Your Role =========

    1) Banker
    2) Customer

    3) Exit
    """

    print(menu)
    
    try:
        choice = int(input("Enter Your Role ===> :"))
    except ValueError:
        print("Invalid Input Please select a number !!")
        continue

    if choice == 1:
        while True:

            menu2 = """
            ======== Operations Menu =========
        
            1) Add Customer
            2) View Customer
            3) Search Customer
            4) View All Customer
            5) Total Amounts in Bank
            6) Back To Main Menu
            """

            print(menu2)
            try:
                choice2 = int(input("Enter Your Choice :"))
            except ValueError:
                print("Invalid Input please select a number !! ")
                continue

            if choice2 == 1:
                obj.add_customer()
            elif choice2 == 2:
                obj.view_customer()
            elif choice2 == 3:
                 obj.search_customer()
            elif choice2 == 4:
                 obj.view_all()
            elif choice2 == 5:
                obj.total_amount()
            elif choice2 == 6:
                break
            else:
                print("\n Invalid Choice !!")

    elif choice == 2:
         while True:
            menu_customer = """
            ======= Customer Menu =======

            1) Withdraw Amount
            2) Deposit Amount
            3) View Balance
            4) Back To Main Menu
            """
            print(menu_customer)
            try:
                cust_choice = int(input("Enter Your Choice : "))
            except ValueError:
                print("Invalid Input please select a number !! ")
                continue

            if cust_choice == 1:
                obj.withdraw_amount()
            elif cust_choice == 2:
                obj.deposit_amount()
            elif cust_choice == 3:
                obj.view_balance()
            elif cust_choice == 4:
                break
            else:
                print("Invalid Choice !!")
        
    elif choice == 3:
        print("Thank You !!")
        break
    else:
        print("Invalid Choice !!")


                 



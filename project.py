from datetime import *
from tabulate import *

class BankAccount:
    def __init__(self):
        self.bank_name = ""
        self.ifsc_code = ""
        self.account_number = 0
        self.name = ""
        self.age= 0
        self.gender = "" 
        self.dob  = ""
        self.address = ""
        self.city = ""
        self.toa = ""
        self.balance = 0
        self.pan = ""
        self.adha = 0
        self.statement=[]
        self.credit_statement=[]
        self.debit_statement=[]

    def create_account(self):
        ###########BANK NAME##################
        bank_list=['HDFC','SBI','ICICI','AXIS']
        flag=0
        while(True):
            temp=input("Enter Bank Name['HDFC','SBI','ICICI','AXIS']: ").upper()
            for i in bank_list:
                if temp==i:
                    self.bank_name=temp
                    flag=1
                    if(self.bank_name=='HDFC'):
                        self.ifsc_code='HDFC0001'
                    elif(self.bank_name=='SBI'):
                        self.ifsc_code='SBI0002'
                    elif(self.bank_name=='ICICI'):
                        self.ifsc_code='ICICI0003'
                    else:
                        self.ifsc_code='AXIS0004'
                    break
            if flag==1:
                break
            else:
                print("Invalid bank name entered: ")

        
        ##############ACCOUNT NUMBER###############
        self.account_number=int(input("Enter Account Number: "))
        
        ############NAME###########################
        self.name = input("Enter Name: ").upper()
        
        ###################GENDER##################
        while(True):
            temp=input("Enter Employee gender(M/F): ").upper()
            if temp=='M' or temp=='F':
                self.gender=temp
                break
            else:
                print("Invalid Gender entered: ")

        #################DOB/AGE#####################
        temp = input("Enter DOB(DD-MM-YYYY): ")
        self.dob = datetime.strptime(temp,"%d-%m-%Y")
        temp1 = datetime.today()
        self.age = temp1.year-self.dob.year-((temp1.month,temp1.day)<(self.dob.month,self.dob.day))

        
        self.address = input("Enter Address: ").title()
        self.city = input("Enter City: ").title()

        ##############TYPE OF ACCOUNT################
        while(True):
            temp=input("Enter Type of Account(S/C/J): ").upper()
            if temp=="S" or temp=="C" or temp=="J":
                self.toa=temp
                break
            else:
                print("Invalid toa entered: ")

        ##########BALANCE###################
        while(True):
            self.balance=int(input("Enter Balance: "))
            if self.balance<0:
                print("Invalid amount entered: ")
            else:
                print("Balance updated. ")
                self.statement.append(self.balance)
                self.credit_statement.append(self.balance)
                self.debit_statement.append("0")
                break
        
        ##############PAN######################

        while(True):
            temp=input("Enter Pan(first 5 alpha, next 4 digits, last alpha): ").upper()
            flag=0
            if len(temp)==10:
                for i in range(10):
                    if(i<5):
                        if(not(temp[i].isalpha())):
                            flag=1
                    elif(i>=5 and i<9):
                        if(not(temp[i].isdigit())):
                            flag=1
                    else:
                        if(not(temp[i].isalpha())):
                            flag=1
                if flag==1:
                    print("Invalid Pan Entered ")
                else:
                    self.pan = temp
                    print(self.pan," is entered")
                    break
            else:
                print("Invalid Pan entered ")
        
        ######ADHAAR###############
        while(True):
            temp=input("Enter Adhaar(12 digits required): ")
            if len(temp)==12:
                if(temp.isdigit()):
                    self.adha=temp
                    break
            else:
                print("Invalid adhaar entered: ")
        print("Account Created Succesfully. ")

    
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited in your account.")
        print("New Balance is: ",self.balance)
        self.statement.append(self.balance)
        self.credit_statement.append(amount)
        self.debit_statement.append("0")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn from your account.")
            print("New Balance is: ",self.balance)
            self.statement.append(self.balance)
            self.debit_statement.append(amount)
            self.credit_statement.append("0")
            
    def funds_trans(self, trans):
        if trans > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= trans
            print(f"{trans} has been transferred from your account.")
            print("New Balance is: ",self.balance)
            self.statement.append(self.balance)
            self.debit_statement.append(trans)
            self.credit_statement.append("0")
            
    def check_balance(self):
        print(f"Current balance is {self.balance}.")
    
    def print_customer_details(self):
        print("")
        print("Bank Name: ", self.bank_name)
        print("Ifsc Code: ", self.ifsc_code)
        print("Account Number: ", self.account_number)
        print("Account Holder Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)
        print("DOB: ", self.dob) 
        print("Address: ", self.address)
        print("City: ", self.city)
        print("Type of Account: ", self.toa)
        print("Balance: ", self.balance)
        print("Pan Card: ", self.pan)
        print("Adhaar: ", self.adha)

ch=1
cust=[]
while(ch!=0):
    print(" ")
    print("Press 1 to create your account: ")
    print("Press 2 to delete your account: ")
    print("Press 3 to update account details: ")
    print("Press 4 to deposit: ")
    print("Press 5 for withdraw: ")
    print("Press 6 to Transfer funds: ")
    print("Press 7 for Searching details of account: ")
    print("Press 8 for Balance Enquiry: ")
    print("Press 9 to display: ")
    print("Press 10 to see passbook: ")
    print("Press 0 to exit: ")
    ch=int(input("Enter your choice: "))
    
    if ch==1:
        temp=BankAccount()
        temp.create_account()
        cust.append(temp);

    elif ch==2:
        temp=int(input("Enter account number to be deleted: "));
        for i in cust:
            if i.account_number==temp:
                cust.remove(i);
    elif ch==3:
        print("Enter A to upadte account holder name: ")
        print("Enter B to update address of account holder: ")
        print("Enter C to update DOB of account holder: ")
        choice=input("Enter your choice in caps: ")
        if choice=='A':
            temp=int(input("Enter account number: "));
            for i in cust:
                if i.account_number==temp:
                    i.name=input("Enter new name: ")
                    print("Succesfully Updated New Name. ")
                    break
        elif choice=='B':
            temp=int(input("Enter account number: "));
            for i in cust:
                if i.account_number==temp:
                    i.address=input("Enter new address: ")
                    print("Succesfully Updated New Address. ")
                    break
        elif choice=='C':
            temp=int(input("Enter account number: "));
            for i in cust:
                if i.account_number==temp:
                    temp5 = input("Enter new DOB(DD-MM-YYYY): ")
                    i.dob = datetime.strptime(temp5,"%d-%m-%Y")
                    temp1 = datetime.today()
                    i.age = temp1.year-i.dob.year-((temp1.month,temp1.day)<(i.dob.month,i.dob.day))
                    print("Succesfully Updated New DOB. ")
                    break
        else:
            print("Invalid Choice ");
            

    elif ch==4:
        temp=int(input("Enter account number: "));
        for i in cust:
            if i.account_number==temp:
                i.deposit(int(input("Enter Amount to be deposited: ")))

    elif ch==5:
        temp=int(input("Enter account number: "));
        for i in cust:
            if i.account_number==temp:
                i.withdraw(int(input("Enter Amount to be withdrawn: ")))

    elif ch==6:
        temp=int(input("Enter account number: "));
        for i in cust:
            if i.account_number==temp:
                i.funds_trans(int(input("Enter Amount to be transferred: ")))

    elif ch==7:
        print("Enter A to Search by account number ")
        print("Enter B to Search by name ")
        print("Enter C to Search by Type of Account ")
        choice=input("Enter your choice in caps: ")
        if choice=='A':
            temp=int(input("Enter account number: "));
            for i in cust:
                if i.account_number==temp:
                    print(BankAccount.print_customer_details(i))
                    break
        elif choice=='B':
            temp=input("Enter account holder name: ");
            for i in cust:
                if i.name==temp:
                    print(BankAccount.print_customer_details(i))
                    break

        elif choice=='C':
            temp=input("Enter Type of Account(S/C): ")
            for i in cust:
                if i.toa==temp:
                    print(BankAccount.print_customer_details(i))
                    print("")
        else:
            print("Invalid Choice ");
            

    elif ch==8:
        temp=int(input("Enter account number: "));
        for i in cust:
            if i.account_number==temp:
                i.check_balance();
    elif ch==9:
        for i in cust:
            print(BankAccount.print_customer_details(i))
            print("")

    elif ch==10:
        temp=int(input("Enter account number: "));
        for i in cust:
            if i.account_number==temp:
                data=list(zip(i.debit_statement,i.credit_statement,i.statement))
                headers=["Debit","Credit","Balance"]
                print(tabulate(data,headers,tablefmt="grid"))
        

    elif ch==0:
        print("Thank You")
        break

    else:
        print("Invalid Choice ")

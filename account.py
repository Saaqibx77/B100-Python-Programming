from account import Account
import csv

while True:
    print('''What you want to do
            1.Create Account
            2.withdraw
            3.deposit
            4.Check balance
            5. Exit''')
    ch=int(input("Enter choice"))
    if ch==1:
        name=input("Enter name")
        acno=int(input("Enter account number:"))
        bal=int(input("Enter amount to  open account"))
        typ=input("Enter type of Account (general/bussiness)")
        A=Account(name,typ,acno,bal)
        print("Account Created..")
        F=open("account.csv","a",newline='')
        wobj=csv.writer(F)
        wobj.writerow([A.cname,A.typeac,A.accountno,A.bankbal])
        F.close()

    elif ch==2:
        import os
        print("Withdrawl process started")
        acno=int(input("Enter account number "))
        amt=int(input("Enter Amount"))
        F=open("account.csv","r")
        F2=open("temp.csv","w",newline='')

        robj=csv.reader(F)
        wobj=csv.writer(F2)

        for rec in robj:
            if int(rec[2])==acno:
                print("Account found")
                print(rec)
                if amt>int(rec[3]):
                    print("Amount can not be withrawn...")
                else:
                    rec[3]=int(rec[3])-amt
                    print("Transaction successful")
            wobj.writerow(rec)
        F2.close()
        F.close()
        os.remove("account.csv")
        os.rename("temp.csv","account.csv")
    elif ch==3:
        
        import os
        print("Deposit process started")
        acno=int(input("Enter account number "))
        amt=int(input("Enter Amount"))
        F=open("account.csv","r")
        F2=open("temp.csv","w",newline='')

        robj=csv.reader(F)
        wobj=csv.writer(F2)

        for rec in robj:
            if int(rec[2])==acno:
                print("Account found")
                print(rec)
                rec[3]=int(rec[3])+amt
                print("Transaction successful")
            wobj.writerow(rec)
        F2.close()
        F.close()
        os.remove("account.csv")
        os.rename("temp.csv","account.csv")

    elif ch==4:
        accno=int(input("Enter Account number to check balance"))
        found=False
        F=open("account.csv","r")

        robj=csv.reader(F)

        for rec in robj:
            if int(rec[2])==accno:
                print("Account found")
                print(rec)
                break
        else:
            print("record not found")
        F.close()
    elif ch==5:
        print("Exiting..")
        break
                
    

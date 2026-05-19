class Account:
    def __init__(self,cname,typeac,accountno,bankbal):
        self.cname=cname
        self.typeac=typeac
        self.accountno=accountno
        self.bankbal=bankbal

    def deposit(self,amt):
        
            self.bankbal+=amt
            print("Amount Deposited..")
            print("Updated Balance :",self.bankbal)
        
            

    def withdraw(self,amt):
        if amount>self.bankbal:
            print("Not Sufficient balance available current balance :",self.bankbal)
        else:
            self.bankbal=self.bankbal-amt
            print("Amount Withdrawn")
            print("Updated Balance :",self.bankbal)

    def display(self):
        print("Account Number :",self.accountno)
        print("Name :",self.cname)
        print("Current Balance :",self.bankbal)
        print("Type of Account :",self.typeac)
        
        

    def to_string(self):
        return self.accountno+" "+self.cname+" "+self.bankbal+" "+self.typeac

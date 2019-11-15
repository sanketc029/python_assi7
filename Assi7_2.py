
class BankAcc:
    ROI=10.5

    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
        BankAcc.ROI


    def Display(self):

        print("Name of cust ",self.name)
        print("Amount of cust ",self.amount)

    def Deposit(self,deposit):
        self.amount=self.amount+deposit
        return self.amount

    def Withdraw(self,wthdr):
        self.amount=self.amount-wthdr
        return self.amount
    def CalInterest(self):
        intr=BankAcc.ROI/100
        total=self.amount*intr
        print(total)
        self.amount=self.amount + total
        return self.amount

def main():

    name=input("Enter the name ")
    amount=int(input("Enter the amount "))
    obj1=BankAcc(name,amount)
    obj1.Display()
    deposit=int(input("Enter the amt for deposit"))
    print("afert deposit ",obj1.Deposit(deposit))

    wthdr=int(input("Enter the amt for withdraw "))
    print("afert withdraw ",obj1.Withdraw(wthdr))

    print("After add 10.5% ROI in amount : ", obj1.CalInterest())

if __name__=="__main__":
    main()
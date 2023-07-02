class BankAccount:
    def __init__(self,account_number,ifsc_code,account_holder,balance=0):
        self.account=account_number
        self.ifsc=ifsc_code
        self.account_holder=account_holder
        self.balance=balance


    def deposite(self,deposite):

        self.balance+=deposite
        print(f"Amount deposit in your account is :{deposite} , available balance is :{self.balance} ")
    def withdrawl(self,withdrawl):
        if withdrawl<=self.balance:

            self.balance-=withdrawl
            print(f'amount debit from your account is : {withdrawl} , available balance is :{self.balance} ')
        else:
            print("suficient balance low")
    def fundtransfer(self,fundtransfer):
        if fundtransfer<=self.balance:

            self.balance-=fundtransfer
            print(f'fund transfer from your account is : {fundtransfer} , available balance is :{self.balance} ')
        else:
            print("suficient balance low for fund transfer")
    def message(self,message):
        print("your amount will be deducted form your account ")
vivek=BankAccount(1224545,"sbin33d","rahul",0)
vivek.deposite(110)
vivek.withdrawl(50)
vivek.fundtransfer(30)
vivek.deposite(500)
vivek.fundtransfer(500)
vivek.deposite(1000)
vivek.withdrawl(120)
vivek.deposite(10500)
vivek.withdrawl(50)
vivek.deposite(2000)
vivek.withdrawl(10000)
vivek.deposite(1050000)

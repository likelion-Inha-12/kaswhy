from 실습2 import account

class savingsAccount(account):
    def __init__(self, name, balance, interests):
        super().__init__(name, balance)
        self.interests = interests

    def deposit(self, money):
        if(money <= 0):
            print("금액은 양수여야 합니다.")
            return
        
        self.balance += money
        print("%d원이 입금되었습니다." %money)
        new_interests = (self.balance / 100) * self.interests
        self.balance += new_interests
        print("%s님의 계좌에 %.1f원의 이자가 추가되었습니다." %(self.name, new_interests))
        return


    def withdraw(self, money):
        new_balance = self.balance - money

        if(new_balance < 0 or money <= 0):
            print("출금 금액이 잔액을 초과하거나 잘못 입력되었습니다.")
            return
        
        self.balance = new_balance
        print("%d원이 출금되었습니다." %money)
        return


    def checkBalance(self):
        print("%s님의 계좌 잔액은 %.1f원입니다.\n이자율: %.1f%%" %(self.name, self.balance, self.interests))
        return

        
account1 = savingsAccount('soyeon', 1000, 5)
account1.checkBalance()
account1.deposit(500)
account1.withdraw(100)
account1.checkBalance()
class account():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        if(money <= 0):
            print("금액은 양수여야 합니다.")
            return
        
        self.balance += money
        print("%d원이 입금되었습니다." %money)
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
        print("%s님의 계좌 잔액은 %d원입니다." %(self.name, self.balance))
        return
    
# # 정상 작동 예시
# print("---------------------------예제 1------------------------------")
# account1 = account('soyeon', 1000)
# account1.checkBalance()
# account1.deposit(500)
# account1.withdraw(200)
# account1.checkBalance()

# # 출금 불가 예시
# print("---------------------------예제 2------------------------------")
# account2 = account('soyeon', 1000)
# account2.checkBalance()
# account2.deposit(500)
# account2.withdraw(2000)
# account2.checkBalance()


# # 입금 불가 예시 & 출금 불가 예시
# print("---------------------------예제 3------------------------------")
# account3 = account('soyeon', 1000)
# account3.checkBalance()
# account3.deposit(-500)
# account3.withdraw(2000)
# account3.checkBalance()

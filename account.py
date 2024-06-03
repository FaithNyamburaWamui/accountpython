class Account:
    def __init__(self,number,pin,balance):
        self.number=number
        self.__pin=pin
        self.balance=balance
        self.transactions=[]

    def check_pin(self,pin):
         if pin==self.__pin:
           return self.balance
         else:
            return "Wrong password"
        
    def deposit(self,amount):
       self.amount=amount
       if amount > 0:
          self.balance+=amount
          print(f"You deposited {amount} and your new balance is {self.balance}")
       else:
          print(f"The balance is {self.balance}")
    
    def with_draw(self,value):
       self.value=value
       if value<=self.balance:
          self.balance-=value
          print(f"Your have withdrawn {value} and your new balance is {self.balance}")
       else:
          print("You have insufficient funds")

    def account_details(self):
        print(f"Your pin is {self.__pin} and new balance is {self.balance}")

    def is_transaction(self):
       print(f"Your had withdrawn {self.value} and deposited {self.amount}. Your new balance is {self.balance}")

    def change_account_owner(self,name):
       self.name=name
       print(f"Your account name is {self.name} and your pinis {self.__pin}")
        

    def set_overdraft_limit(self, overdraft_limit):
        self.overdraft_limit = overdraft_limit
        print(f"Overdraft limit set to {self.overdraft_limit}")

    def calculate_interest(self, annual_interest_rate):
        monthly_interest_rate = annual_interest_rate / 12 / 100
        interest_amount = self.balance * monthly_interest_rate
        self.balance += interest_amount
        print(f"Interest applied is ${interest_amount}")
        
    def freeze_account(self):
        self.is_frozen = True
        print("Account frozen.")

    def unfreeze_account(self):
        self.is_frozen = False
        print("Account unfrozen.")

    def add_transaction(self, transaction_type, amount):
        self.transactions.append({"type": transaction_type, "amount": amount})

    def set_minimum(self):
       self.__balance=200
       print(f"The minimum balnce is {self.balance}")
    

    def transfer_funds(self, target_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount
            self.add_transaction("Transfer Out", -amount)
            target_account.add_transaction("Transfer In", amount)
            print(f"${amount} transferred to {target_account}.")
        else:
            print("Insufficient balance for transfer.")

    def close_account(self):
        self.balance = 0
        self.transactions = []
        print("Account closed.")


          
          


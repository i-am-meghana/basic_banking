from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.get_balance()
Sara.get_balance()

Sara.deposit(500)
#Dave.deposit(20000)

Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)
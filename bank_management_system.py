class Bank:
	def __init__(self):
		self.users = {}
		self.loan_enabled = True
		self.is_bankrupt = False
		self.total_balance = 0
		self.total_loan_amount = 0

class User:
	def __init__(self, bank, name, email, address, ac_type):
		self.bank = bank
		self.name = name
		self.email = email
		self.address = address
		self.ac_type = ac_type
		self.balance = 0
		self.loan_count = 0
		self.transaction_history = []
		self.ac_no = len(bank.users) + 1
		bank.users[self.ac_no] = self


	def deposit(self, amount, is_transfer = False):
		if amount >= 0:
			self.balance += amount
			self.bank.total_balance += amount
			self.transaction_history.append(f"- Deposit: ${amount}")
			if not is_transfer:
				print(f"\n--> Deposited {amount}, current balance: ${self.balance}")
		else:
			print("\n--> Invalid deposit amount")

	def withdraw(self, amount):
		if amount < 1:
			print("\n--> Invalid withdrawal amount")
		elif amount > self.balance:
			print(f"\n--> Insufficient balance, you only have ${self.balance} in you account")
		elif self.bank.is_bankrupt:
			print("\n--> Sorry, Bank is bankrupt!")
		else:
			self.balance -= amount
			self.bank.total_balance -= amount
			self.transaction_history.append(f"- Withdraw: ${amount}")
			print(f"\n--> Withdrawn ${amount}, current balance: ${self.balance}")

	def check_available_balance(self):
		print(f"\n--> Your balance: ${self.balance}")

	def check_transaction_history(self):
		print(*self.transaction_history, sep="\n")

	def request_loan(self, amount):
		if amount < 1:
			print("\n--> Invalid loan amount")
		elif self.loan_count >= 2:
			print("\n--> Sorry, you have already taken 2 loans.")
		elif not self.bank.loan_enabled:
			print("\n--> Sorry, loans are not available now.")
		else :
			self.balance += amount
			self.loan_count += 1
			self.bank.total_loan_amount += amount
			self.transaction_history.append(f"- Loan Deposit: ${amount}")
			print(f"\n--> Loan Deposited {amount}, current balance: ${self.balance}")

	def transfer_money(self, amount, to_account):
		if amount < 1:
			print("\n--> Invalid transfer amount amount")
		elif amount > self.balance:
			print(f"\n--> Insufficient balance, you only have ${self.balance} in you account")
		elif to_account not in self.bank.users:
			print("\n--> Invalid account number.")
		else:
			self.balance -= amount
			self.transaction_history.append(f"- Transfer: ${amount}")
			self.bank.users[to_account].deposit(amount, True)
			print(f"\n--> Transfarred ${amount}, current balance: ${self.balance}")

	def __repr__(self) -> str:
		return f"Account Number: {self.ac_no} | Name: {self.name} | Email: {self.email} | Address: {self.address} | Account Type: {self.ac_type} | Balance: ${self.balance}\n"


class Admin:
	def __init__(self, bank):
		self.bank = bank

	def create_account(self, name, email, address, ac_type):
		user = User(self.bank, name, email, address, ac_type)
		print(f"\n--> New user created, account number: {user.ac_no}")
		return user

	def delete_user(self, ac_no):
		if ac_no in self.bank.users:
			user = self.bank.users[ac_no]
			user.withdraw(user.balance)
			del self.bank.users[ac_no]
			print("\n--> User's balance withdrawn and account deleted")
		else:
			print("\n--> Invalid account number")

	def print_user_list(self):
		print(self.bank.users)

	def check_total_balance(self):
		print(f"\n--> Total available balance: ${self.bank.total_balance}")

	def check_total_loan_amount(self):
		print(f"\n--> Total loan amount: ${self.bank.total_loan_amount}")

	def disable_loan(self):
		self.bank.loan_enabled = False
		print("\n--> Loan Disabled.")

	def enable_loan(self):
		self.bank.loan_enabled = True
		print("\n--> Loan Enabled.")

	def declare_bankrupt(self):
		self.bank.is_bankrupt = True
		print("\n--> Bankrupt declared!")
from bank_management_system import Bank, User, Admin

def initial_options():
	print("\n1. Create New Account")
	print("2. User Login")
	print("3. Admin Login")
	print("0. Exit")

def user_options():
	print("\n1. Check Balance")
	print("2. Deposit Money")
	print("3. Withdraw Money")
	print("4. Transfer Money")
	print("5. Apply for Loan")
	print("6. Review Transcation History")
	print("0. Exit")

def admin_options():
	print("\n1. Create account")
	print("2. Delete account")
	print("3. List all accounts")
	print("4. Check Total Balance")
	print("5. Check Total Loan Amount")
	print("6. Enable Loan")
	print("7. Disable Loan")
	print("8. Declare Bankrup")
	print("0. Exit")




bank = Bank()
initial_options()
option = input("Please select an option: ")

while option != "0":
	if option == "1":
		name = input("Enter your name: ")
		email = input("Enter your email: ")
		address = input("Enter your address: ")
		ac_type = input("Enter your account type (Savings or Current): ")
		user = User(bank, name, email, address, ac_type)
		print(f"\nYour account has been created and you can login now. Account No: {user.ac_no}")

		initial_options()
		option = input("Please select an option: ")

	if option == "2":
		ac_no = int(input("Enter your Account No: "))
		if ac_no not in bank.users:
			print("\nInvalid account number.");
		else:
			user = bank.users[ac_no];
			print(f"\nWelcome, {user.name}! You're now logged in.");
			
			user_options()
			user_choice = input("Please select an option: ")

			while user_choice != "0":

				if user_choice == "1":
					user.check_available_balance()
				elif user_choice == "2":
					amount = int(input("Enter deposit amount: "))
					user.deposit(amount)
				elif user_choice == "3":
					amount = int(input("Enter withdraw amount: "))
					user.withdraw(amount)
				elif user_choice == "4":
					amount = int(input("Enter transfer amount: "))
					to_ac = int(input("Enter recipient account number: "))
					user.transfer_money(amount, to_ac)
				elif user_choice == "5":
					amount = int(input("Enter loan amount: "))
					user.request_loan(amount)
				elif user_choice == "6":
					user.check_transaction_history()

				user_options()
				user_choice = input("Please select an option: ")
	
	if option == "3":
		admin = Admin(bank)

		admin_options()
		admin_choice = input("Please select an option: ")

		while admin_choice != "0":

			if admin_choice == "1":
				name = input("Enter user name: ")
				email = input("Enter user email: ")
				address = input("Enter user address: ")
				ac_type = input("Enter user account type (Savings or Current): ")
				user = admin.create_account(name, email, address, ac_type)
				print(f"\nNew account has been created. Account No: {user.ac_no}")
			elif admin_choice == "2":
				ac_no = int(input("Enter account number: "))
				admin.delete_user(ac_no)
			elif admin_choice == "3":
				admin.print_user_list()
			elif admin_choice == "4":
				admin.check_total_balance()
			elif admin_choice == "5":
				admin.check_total_loan_amount()
			elif admin_choice == "6":
				admin.enable_loan()
			elif admin_choice == "7":
				admin.disable_loan()
			elif admin_choice == "8":
				admin.declare_bankrupt()

			admin_options()
			admin_choice = input("Please select an option: ")
	initial_options()
	option = input("Please select an option: ")


# Bank Chatbot Code

## Imports
import json
import re

## Class Definitions

class Account:
    def __init__(self, name, account_type):
        self.name = name
        self.account_type = account_type
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False


class StudentAccount(Account):
    def __init__(self, name, student_id):
        super().__init__(name, 'Student')
        self.student_id = student_id

    def verify_student(self):
        # Implement verification logic for student
        pass

class SeniorAccount(Account):
    def __init__(self, name, age):
        super().__init__(name, 'Senior')
        self.age = age

    def verify_senior(self):
        # Implement verification logic for senior
        pass

class BusinessAccount(Account):
    def __init__(self, name, business_id):
        super().__init__(name, 'Business')
        self.business_id = business_id

    def verify_business(self):
        # Implement verification logic for business
        pass


## Functions

def create_account(name, account_type, verification_info):
    if account_type == 'Student':
        return StudentAccount(name, verification_info)
    elif account_type == 'Senior':
        return SeniorAccount(name, verification_info)
    elif account_type == 'Business':
        return BusinessAccount(name, verification_info)
    else:
        raise ValueError('Invalid account type')


def main_loop():
    print("Welcome to the Bank Chatbot!")
    while True:
        command = input("What would you like to do? (create, deposit, withdraw, exit): ").lower()
        if command == 'create':
            name = input("Enter account holder name: ")
            acc_type = input("Enter account type (Student/Senior/Business): ").capitalize()
            verification = input("Enter verification info (ID/Age/Business ID): ")
            account = create_account(name, acc_type, verification)
            print(f'Account created for {account.name} with balance {account.balance}')
        elif command == 'deposit':
            amount = float(input("Enter deposit amount: "))
            if account.deposit(amount):
                print(f'Deposit successful! New balance: {account.balance}')
            else:
                print('Deposit failed.')
        elif command == 'withdraw':
            amount = float(input("Enter withdrawal amount: "))
            if account.withdraw(amount):
                print(f'Withdrawal successful! New balance: {account.balance}')
            else:
                print('Withdrawal failed.')
        elif command == 'exit':
            print('Thank you for using the Bank Chatbot. Goodbye!')
            break
        else:
            print('Invalid command')


if __name__ == '__main__':
    main_loop()
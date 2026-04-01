# Chatbot intro
def introduction():
    print('---------------------------------')
    print('  _____   _____   _____')
    print(' /     \ |     | /     \\')
    print(' |  !  | |  0  | |  !  |')
    print(' \     / |     | \     /')
    print('  -----  |     |  -----')
    print(' /     \ |     | /     \\')
    print(' \     / |     | \     /')
    print('  -----   -----   -----')
    print('---------------------------------')
    print("Welcome to the Elite 101 Bank, where your financial well-being is our top priority. We offer a wide range of products and services, including checking accounts, savings accounts, credit cards, and loans, all designed to help you achieve your financial goals. We are here to assist you with any questions or concerns you may have about our services, providing personalized guidance and support every step of the way.")
    print('---------------------------------')


# Chatbot functions
def register():
    print('---------------------------------')
    print("It seems like you didn't have an account created. Let's gather some information to get started.")
    print('---------------------------------')
    name = input("What is your full name? ")
    email = input("What is your email address? ")
    phone = input("What is your phone number? ")
    address = input("What is your full address? ")
    city = input("What city do you live in? ")
    state = input("What state do you live in? ")
    zip_code = input("What is your zip code? ")
    date_of_birth = input("What is your date of birth (MM/DD/YYYY)? ")
    db = open(r"database.txt", "a")
    print('---------------------------')
    print("Your information has been collected. Now please register")
    username = input("Username: ")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    if password == confirm_password:
        db.write(username + "," + password + "\n")
        db.close()
        print('---------------------------')
        print("Account created")
    else:
        print("Passwords do not match. Please try again.")


def login():
    print('---------------------------')
    print("Welcome to the chatbot")
    print("Please login")
    username = input("Username: ")
    password = input("Password: ")
    with open(r"database.txt", "r") as db:
        for line in db:
            user, passw = line.strip().split(",")
            if username == user and password == passw:
                print('---------------------------')
                print('Welcome to Elite 101 Bank! How can I help you today?')
                print('---------------------------')
                return True
    print("Wrong username or password")
    return False


# Menu
def display_menu():
    print('Menu:')
    print('1. Open a Checking Account')
    print('2. Open a Savings Account')
    print('3. Apply for a Credit Card')
    print('4. Exit conversation')
    print('---------------------------------')


def user_selection():
    while True:
        user_choice = input("Enter a number between 1-4: ")
        if user_choice == '1':
            open_checking_account()
        elif user_choice == '2':
            open_savings_account()
        elif user_choice == '3':
            apply_for_credit_card()
        elif user_choice == '4':
            print("Thank you for using the program")
            break
        else:
            print("\nSorry, not a valid choice.")


def open_checking_account():
    print('---------------------------------')
    print('You have chosen to open a checking account. Please choose the type of account you would like to open:')
    print('1. Basic Checking Account')
    print('2. Premier Checking Account')
    print('3. Student Checking Account')
    print('4. Senior Checking Account')
    print('5. Business Checking Account')
    print('---------------------------------')
    
    while True:
        user_choice = input("Enter a number between 1-5: ")
        
        if user_choice == '1':
            print('---------------------------------')
            print('🏦 BASIC CHECKING ACCOUNT')
            print('---------------------------------')
            print('Perfect for everyday banking needs.')
            print('')
            print('FEATURES:')
            print('  • Monthly Maintenance Fee: $12.99')
            print('  • Minimum Balance Required: $500')
            print('  • Debit Card: Yes (Free)')
            print('  • Online & Mobile Banking: Yes')
            print('  • ATM Network: 50,000+ ATMs nationwide')
            print('  • Check Writing: Unlimited')
            print('  • Overdraft Protection: Available')
            print('  • Interest Rate: 0.01% APY')
            print('')
            print('IDEAL FOR: Budget-conscious individuals wanting basic banking services')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? (yes/no): ')
            if confirm == 'yes':
                application()
                break
            else:
                print("Let's return to the menu")
                break
                
        elif user_choice == '2':
            print('---------------------------------')
            print('⭐ PREMIER CHECKING ACCOUNT')
            print('---------------------------------')
            print('Premium banking experience with exclusive benefits.')
            print('')
            print('FEATURES:')
            print('  • Monthly Maintenance Fee: FREE (no minimum balance)')
            print('  • Minimum Balance Required: $0')
            print('  • Debit Card: Premium card (Free)')
            print('  • Online & Mobile Banking: Yes (Advanced)')
            print('  • ATM Network: 50,000+ ATMs + partner banks')
            print('  • Check Writing: Unlimited')
            print('  • Overdraft Protection: Included')
            print('  • Interest Rate: 0.05% APY')
            print('  • Monthly Rewards: Cash back on debit purchases')
            print('  • Priority Customer Service: 24/7 Dedicated Line')
            print('  • Travel Benefits: Rental car insurance, travel discounts')
            print('')
            print('IDEAL FOR: Active bankers wanting premium features and rewards')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? (yes/no): ')
            if confirm == 'yes':
                application()
                break
            else:
                print("Let's return to the menu")
                break
                
        elif user_choice == '3':
            print('---------------------------------')
            print('🎓 STUDENT CHECKING ACCOUNT')
            print('---------------------------------')
            print('Designed specifically for college students and young adults.')
            print('')
            print('FEATURES:')
            print('  • Monthly Maintenance Fee: FREE')
            print('  • Minimum Balance Required: $0')
            print('  • Age Requirement: 17-24 years old')
            print('  • Debit Card: Free student ID card')
            print('  • Online & Mobile Banking: Yes (Student-friendly)')
            print('  • ATM Network: 40,000+ ATMs nationwide')
            print('  • Check Writing: Limited (10 checks/month)')
            print('  • Overdraft Protection: Available (optional)')
            print('  • Interest Rate: 0.02% APY')
            print('  • Student Discounts: 10-15% off various merchants')
            print('  • Budgeting Tools: Built-in spending tracker')
            print('')
            print('REQUIREMENTS:')
            print('  • Valid student ID or proof of enrollment')
            print('  • Social Security Number')
            print('')
            print('IDEAL FOR: College students managing their first checking account')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? (yes/no): ')
            if confirm == 'yes':
                student_checking_process()
                break
            else:
                print("Let's return to the menu")
                break
                
        elif user_choice == '4':
            print('---------------------------------')
            print('👴 SENIOR CHECKING ACCOUNT')
            print('---------------------------------')
            print('Specially designed for customers 55 and older.')
            print('')
            print('FEATURES:')
            print('  • Monthly Maintenance Fee: FREE')
            print('  • Minimum Balance Required: $100')
            print('  • Age Requirement: 55+ years old')
            print('  • Debit Card: Specially designed card')
            print('  • Online & Mobile Banking: Yes (Simplified Interface)')
            print('  • ATM Network: 50,000+ ATMs nationwide')
            print('  • Check Writing: Unlimited')
            print('  • Overdraft Protection: Yes')
            print('  • Interest Rate: 0.03% APY')
            print('  • Paper Statements: Free (monthly)')
            print('  • Phone Support: 24/7 Dedicated Senior Line')
            print('  • Financial Advisor: Free quarterly consultations')
            print('  • Reduced Fees: 50% off all service fees')
            print('')
            print('SPECIAL BENEFITS:')
            print('  • Large print statements available')
            print('  • Easier online banking interface')
            print('  • Direct deposit setup assistance')
            print('')
            print('IDEAL FOR: Seniors wanting ease of use and personalized service')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? (yes/no): ')
            if confirm == 'yes':
                senior_checking_process()
                break
            else:
                print("Let's return to the menu")
                break
                
        elif user_choice == '5':
            print('---------------------------------')
            print('💼 BUSINESS CHECKING ACCOUNT')
            print('---------------------------------')
            print('Comprehensive solution for business owners and entrepreneurs.')
            print('')
            print('FEATURES:')
            print('  • Monthly Maintenance Fee: $19.99')
            print('  • Minimum Balance Required: $2,500')
            print('  • Business Debit Card: 5 free cards')
            print('  • Additional Cards: $5 each')
            print('  • Check Writing: Unlimited')
            print('  • Online & Mobile Banking: Yes (Business Dashboard)')
            print('  • Wire Transfers: Up to 10 free per month')
            print('  • ACH Transfers: Unlimited')
            print('  • Interest Rate: 0.01% APY')
            print('  • Credit Line: Up to $25,000 available')
            print('  • Payroll Processing: Integrated payroll system')
            print('  • Invoice Management: Built-in invoicing tools')
            print('')
            print('BUSINESS REQUIREMENTS:')
            print('  • Business License or EIN')
            print('  • Business Tax ID')
            print('  • Owner identification and SSN')
            print('  • Business address verification')
            print('')
            print('ADDITIONAL BENEFITS:')
            print('  • Business credit card available')
            print('  • Merchant services')
            print('  • Accounting software integration')
            print('  • Dedicated business accountant')
            print('')
            print('IDEAL FOR: Business owners needing comprehensive payment solutions')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? (yes/no): ')
            if confirm == 'yes':
                business_checking_process()
                break
            else:
                print("Let's return to the menu")
                break
        else:
            print("\nSorry, not a valid choice.")


def student_checking_process():
    """Special process for student checking accounts"""
    print('---------------------------------')
    print('📋 STUDENT ACCOUNT APPLICATION')
    print('---------------------------------')
    school_name = input("Which school do you attend? ")
    graduation_year = input("Expected graduation year? ")
    major = input("What is your major? ")
    print('\nCollecting your information...')
    application()


def senior_checking_process():
    """Special process for senior checking accounts"""
    print('---------------------------------')
    print('📋 SENIOR ACCOUNT APPLICATION')
    print('---------------------------------')
    age = input("Are you 55 or older? (yes/no): ")
    if age.lower() != 'yes':
        print("❌ You must be 55 or older to open a Senior Checking Account.")
        return
    retirement_status = input("Are you retired? (yes/no): ")
    print('\nVerifying your information...')
    application()


def business_checking_process():
    """Special process for business checking accounts"""
    print('---------------------------------')
    print('📋 BUSINESS ACCOUNT APPLICATION')
    print('---------------------------------')
    business_name = input("Business Name: ")
    business_type = input("Type of Business (e.g., LLC, Corporation, Sole Proprietor): ")
    ein = input("EIN (Employer Identification Number): ")
    years_in_business = input("How many years has your business been operating? ")
    employees = input("Number of employees: ")
    print('\nVerifying business information...')
    application()


def open_savings_account():
    print('---------------------------------')
    print('You have chosen to open savings accounts. You can deposit money into your savings account at anytime and earn interest on your balance. To open a savings account, you have to pick one of the 3 different types of account below.')
    print('---------------------------------')
    print('1. Traditional Savings Account')
    print('2. Money Market Account')
    print('3. CD (Certificate of Deposit)')
    print('---------------------------------')
    while True:
        savings_account = input("Enter a number between 1-3: ")
        if savings_account == '1':
            print('---------------------------------')
            print('💰 TRADITIONAL SAVINGS ACCOUNT')
            print('---------------------------------')
            print('You have chosen to open a traditional savings account')
            print('A traditional savings account is a type of savings account that allows you to deposit money at a fixed interest rate.')
            print('This type of account is ideal for individuals who want to save money for a specific purpose or for a short period of time.')
            print('')
            print('FEATURES:')
            print('  • Interest Rate: 0.02% APY')
            print('  • Minimum Balance: $25')
            print('  • Monthly Fee: FREE')
            print('  • Withdrawal Limit: 6 per month (Federal limit)')
            print('  • Direct Deposit: Yes')
            print('  • Online Access: Yes')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? ')
            if confirm == 'yes':
                application()
                break
            else:
                print("Let's return to the menu")
                break
        elif savings_account == '2':
            print('---------------------------------')
            print('📈 MONEY MARKET ACCOUNT')
            print('---------------------------------')
            print('You have chosen to open a money market account.')
            print('A money market account is a type of savings account that allows you to deposit money at a higher interest rate than a traditional savings account.')
            print('This type of account is ideal for individuals who want to save money for a long-term purpose and is great for those funds that you would like to invest in the future and provides the highest interest rates compared to traditional savings accounts.')
            print('')
            print('FEATURES:')
            print('  • Interest Rate: 0.05% APY (Tiered rates)')
            print('  • Minimum Balance: $2,500')
            print('  • Monthly Fee: $10 (waived if balance > $10,000)')
            print('  • Check Writing: Limited (3 checks per month)')
            print('  • Withdrawal Limit: 6 per month (Federal limit)')
            print('  • Debit Card Access: Yes')
            print('  • Online Access: Yes')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? ')
            if confirm == 'yes':
                application()
                break
            else:
                print("Let's return to the menu")
                break
        elif savings_account == '3':
            print('---------------------------------')
            print('📅 CD (CERTIFICATE OF DEPOSIT)')
            print('---------------------------------')
            print('You have chosen to open a CD (Certificate of Deposit).')
            print('A CD (Certificate of Deposit) is a type of savings account that allows you to deposit money at a much higher interest rate than a traditional savings account.')
            print('This type of account is good for those funds that you would never touch for a long period of time and provides the highest interest rates compared to traditional savings accounts.')
            print('Also, you will not be able to take out the money from your CD account at anytime. You must wait for the money to mature or finish growing in a specific time before you can withdraw it.')
            print('')
            print('FEATURES:')
            print('  • Interest Rates (varies by term):')
            print('    - 3-Month CD: 0.30% APY')
            print('    - 6-Month CD: 0.40% APY')
            print('    - 1-Year CD: 0.50% APY')
            print('    - 3-Year CD: 0.75% APY')
            print('    - 5-Year CD: 1.00% APY')
            print('  • Minimum Balance: $500')
            print('  • Monthly Fee: FREE')
            print('  • Early Withdrawal Penalty: 3-6 months interest')
            print('  • Automatic Renewal: Yes (Optional)')
            print('---------------------------------')
            confirm = input('Are you sure you want to open this account? ')
            if confirm == 'yes':
                application()
                break
            else:
                print("Let's return to the menu")
                break
        else:
            print("\nSorry, not a valid choice.")


def apply_for_credit_card():
    print('---------------------------------')
    print('You have chosen to apply for a credit card.')
    print('In order to apply for a credit card, please provide some more information to complete your application.')
    print('---------------------------------')
    types_of_credit_cards = input("What type of credit card would you like to apply for? ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    ssn = input("SSN: ")
    address = input("Address: ")
    phone = input("Phone Number: ")
    email_input = input("Do you have any email? y or n ")
    income = input("Annual Income: ")
    
    if email_input == 'y':
        email = input("Email: ")
    else:
        email = 'N/A'
    
    if income.isnumeric():
        income = int(income)
    else:
        print('Please enter a valid number')
        income = int(input())
    
    retake = input(f"Is the following information correct? {first_name} {last_name} {ssn} {address} ")
    if retake.lower() == 'yes':
        print('Thank you for your application. We will review your information and get back to you shortly.')
    else:
        print('Please retake the application')
        apply_for_credit_card()
    print('---------------------------------')


def application():
    print('---------------------------------')
    print("Let's get started with your new Savings/Checking Account! Please select how you'd like to apply:")
    print("1. Apply Online")
    print("2. Apply In Person")
    choice = input("Enter your choice: ")
    if choice == "1":
        online_application()
    elif choice == "2":
        print("You have chosen to apply in person. In order to create a bank account you'll have to visit your nearest branch to complete the application process.")
        exit_programs()
    else:
        print("Invalid choice. Please select 1 or 2.")
    print('---------------------------------')


def online_application():
    print("You have chosen to apply online. To apply you'll need to provide the following information: ")
    print("1. Re-submit Your Identification")
    print("2. Provide Contact Details")
    print("3. Select a Single or Joint Account")
    print("4. Accept the Terms and Conditions")
    print("5. Submit Your Application")
    print("6. Fund Your New Account")
    print("---------------------------------")
    print("Please provide the following information to complete your application for steps 1 and 2:")
    print("---------------------------------")
    
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    ssn = input("SSN: ")
    address = input("Address: ")
    phone = input("Phone Number: ")
    email_input = input("Do you have any email? y or n ")
    income = input("Annual Income: ")
    
    if email_input == 'y':
        email = input("Email: ")
    else:
        email = 'N/A'
    
    if income.isnumeric():
        income = int(income)
    else:
        print('Please enter a valid number')
        income = int(input())
    
    retake = input(f"Is the following information correct? {first_name} {last_name} {ssn} {address} {phone} {email} {income} ")
    if retake.lower() == 'yes':
        different_accounts()
    else:
        print('Please retake the application')
        online_application()


def different_accounts():
    print('---------------------------------')
    print('Thank you for your information and we should continue to the next step.')
    print('What type of account would you like to open?')
    print('1. Single Account: This account is for one individual only.')
    print('2. Joint Account: This account is for two or more individuals.')
    print('---------------------------------')
    
    while True:
        user_choice = input("Enter a number between 1-2: ")
        if user_choice == '1':
            print('---------------------------------')
            print('You have chosen to open a single checking account. Please enter your name and date of birth to complete the process.')
            print('---------------------------------')
            name = input("Name: ")
            dob = input("Date of Birth: ")
            print('---------------------------------')
            print('Thank you for opening a single checking account with Elite 101 Bank. Your account will be ready for use soon.')
            print('---------------------------------')
            print('Now take a look at the Bank\'s Terms and rules to know what you can do with your account.')
            print('---------------------------------')
            bank_terms_and_conditions()
            break
        elif user_choice == '2':
            print('---------------------------------')
            print('You have chosen to open a joint checking account. Please enter the names and dates of birth for both account holders to complete the process.')
            print('---------------------------------')
            name1 = input("Name of first account holder: ")
            dob1 = input("Date of Birth of first account holder: ")
            name2 = input("Name of second account holder: ")
            dob2 = input("Date of Birth of second account holder: ")
            print('---------------------------------')
            print('Thank you for opening a joint checking account with Elite 101 Bank. Your account will be ready for use soon.')
            print('---------------------------------')
            print('Now take a look at the Bank\'s Terms and rules to know what you can do with your account.')
            print('---------------------------------')
            bank_terms_and_conditions()
            break
        else:
            print("\nSorry, not a valid choice.")


def bank_terms_and_conditions():
    print('---------------------------------')
    print('Elite 101 Bank Terms and Conditions')
    print('---------------------------------')
    print('1. Elite 101 Bank is a bank that provides a variety of banking services, including checking accounts, savings accounts, and credit cards.')
    print('2. Elite 101 Bank is committed to providing a safe and secure banking experience for all of its customers.')
    print('3. Elite 101 Bank is not responsible for any losses or damages that may occur as a result of using its services.')
    print('4. Elite 101 Bank reserves the right to modify or cancel any of its services at any time.')
    print('5. Elite 101 Bank is not responsible for any unauthorized transactions that may occur on your account.')
    print('6. Elite 101 Bank is not responsible for any lost or stolen passwords.')
    print('7. Elite 101 Bank is not responsible for any damages that may occur to your device as a result of using its services.')
    print('---------------------------------')
    
    agreement = input("Do you agree to the terms and conditions? y or n ")
    if agreement.lower() == 'y':
        print('--------------------------------------')
        print('Thank you for your agreement. Now we will continue to the next step.')
        print('How much money would you like to deposit into your account?')
        print('--------------------------------------')
        print('Our bank has a minimum balance of 500 dollars.')
        min_balance = float(input("Enter the minimum balance required for this account: "))
        if min_balance >= 500:
            print('---------------------------------')
            print('Thank you for opening a Savings/Checking Account with Elite 101 Bank. Your account will be ready for use after 5 business days.')
            print('---------------------------------')
            exit()
        else:
            print('Your balance is below the minimum required. Please try again.')
            bank_terms_and_conditions()
    else:
        print('Please retake the application')
        bank_terms_and_conditions()


def exit_programs():
    print('---------------------------------')
    exit_choice = input('Would you like to continue using Elite 101 Bank? y or n ')
    if exit_choice.lower() == 'y':
        print('Thank you for using Elite 101 Bank. Let us continue to the next step.')
    else:
        print('Thank you for using Elite 101 Bank. Have a great day!')


# Main program
def main():
    introduction()
    while True:
        print("Let's get started by making an account in Elite 101 Bank:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            register()
            display_menu()
            user_selection()
        elif choice == "2":
            if login():
                display_menu()
                user_selection()
            else:
                print("Exiting program")
                break
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


main()

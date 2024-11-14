
# Chatbot intro
def introduction():
  print('---------------------------------');
  print('  _____   _____   _____');
  print(' /     \ |     | /     \ ');
  print(' |  !  | |  0  | |  !  |');
  print(' \     / |     | \     /');
  print('  -----  |     |  -----');
  print(' /     \ |     | /     \ ')
  print(' \     / |     | \     / ');
  print('  -----   -----   ----- ');
  print('---------------------------------');
  print("Welcome to the Elite 101 Bank, where your financial well-being is our top priority. We offer a wide range of products and services, including checking accounts, savings accounts, credit cards, and loans, all designed to help you achieve your financial goals.!0! arehere to assist you with any questions or concerns youmay have about our services, providing personalized guidance and support every step of the way.")
  print('---------------------------------');


# Chatbot functions
def resigter():
  print('---------------------------------')
  print("It seem like that you didn't have a account created lets gather some information to get started.")
  print('---------------------------------')
  name = input("What is your full name? ")
  email = input("What is your email address? ")
  phone = input("What is your phone number? ")
  address = input("What is your full address? ")
  city = input("What city do you live in? ")
  state = input("What state do you live in? ")
  zip_code = input("What is your zip code? ")
  date_of_birth = input("What is your date of birth (MM/DD/YYYY)? ")
  db= open(r"database.txt","a")
  print('---------------------------')
  print("You information is collect. Now please register")
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
        print('Welcome to Elite 101 Bank! How can I help you today?');
        print('---------------------------')
        return True
  print("Wrong username or password")
  return False 

# Menu 
def display_menu():
  print('Menu:');
  print('1. Open a Checking Account'); 
  print('2. Open a Savings Account');
  print('3. Apply for a Credit Card');
  print('4. Exit conversation');
  print('---------------------------------');


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
  print('---------------------------------');
  print('You have chosen to open a checking account. Please choose the type of account you would like to open:')
  print('1. Basic Checking Account');
  print('2. Premier Checking Account');
  print('3. Student Checking Account');
  print('4. Senior Checking Account');
  print('5. Businesses Checking Account')
  print('---------------------------------');
  while True:
    user_choice = input("Enter a number between 1-5: ")
    if user_choice == '1':
      print('---------------------------------');
      print('You have chosen to open a basic checking account. This account offers a variety of features, including a debit card, online and mobile banking, and a free checking account with a minimum balance required to keep it free.')
      print('---------------------------------')
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    elif user_choice == '2':
      print('---------------------------------');
      print('You have chosen to open a premier checking account. This account offers a variety of features, including a debit card, online and mobile banking, and a free checking account with no minimum balance required. You will have a higher annual percentage yield.')
      print('---------------------------------')
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    elif user_choice == '3':
      print('---------------------------------');
      print('You have chosen to open a student checking account.');
      print('A student checking account is a type of checking account that is designed for students. It typically offers lower fees and a higher interest rate than a traditional checking account.');
      print('This type of account is ideal for students who are looking for a low-cost way to manage their money.');
      print('---------------------------------');
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    elif user_choice == '4':
      print('---------------------------------');
      print('You have chosen to open a Senior Checking Account. This type of account is designed specifically for seniors and offers special features and benefits, such as reduced fees and access to personalized financial advice.') 
      print('---------------------------------')
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    elif user_choice == '5':
      print('---------------------------------');
      print('You have chosen to open a Business Checking Account.')
      print('A Business Checking Account is a type of checking account designed for businesses. This account is designed for business owners and entrepreneurs for everyday business transactions, such as paying bills, managing payroll, and making deposits.');
      print('---------------------------------')
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    else:
      print("\nSorry, not a valid choice.")

  
def open_savings_account():
  print('---------------------------------');
  print('You have chosen to open savings accounts. You can deposit money into your savings account at anytime and earn interest on your balance.  To open a savings account, you have to pick on the 3 different types of account below.')
  print('---------------------------------')
  print('1. Traditional Savings Account')
  print('2. Money marketing account')
  print('3. CD (Certificate of Deposit)')
  print('---------------------------------')
  while True:
    savings_account = input("Enter a number between 1-3: ")
    if savings_account == '1':
      print('---------------------------------');
      print('You have chosen to open a traditional savings account')
      print('A traditional savings account is a type of savings account that allows you to deposit money at a fixed interest rate.') 
      print('This type of account is ideal for individuals who want to save money for a specific purpose or for a short period of time.')
      print('---------------------------------')
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    elif savings_account == '2':
      print('---------------------------------');
      print('You have chosen to open a money marketing account.')
      print('A money marketing account is a type of savings account that allows you to deposit money at a higher interest rate than a traditional savings account.')
      print(' This type of account is ideal for individuals who want to save money for a long-term purpose and its great for those moneys that you would like to invest in the future and provides the highest interest rates than traditional savings accounts.') 
      print('---------------------------------')
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    elif savings_account == '3': 
      print('---------------------------------');
      print('You have chosen to open a CD (Certificate of Deposit).')
      print('A CD (Certificate of Deposit) is the type of savings account that allows you to deposit money at a the most higher interest rate than a traditional savings account.')
      print(' This type of account is good for those moneys that you would never touch for a long period of time and provides the highest interest rates than traditional savings accounts.')
      print('Also, you not be able to take out the money from your CD account at anytime. You must wait for the money to mature or finish growing in a specific time before you can withdraw it.') 
      print('---------------------------------')
      comfirm=input('Are you sure you want to open this account?')
      if comfirm == 'yes':
        application()
      else:
        print("let return to the menu" )
        return user_selection() 
    else:
      print("\nSorry, not a valid choice." )
      return 


def apply_for_credit_card():
  print('---------------------------------');
  print('You have chosen to apply for a credit card.')   
  print('In order to apply for an credit please provide some more information to complete your application.')
  print('---------------------------------'); 
  types_of_credit_cards = input("What type of credit card would you like to apply for? ")
  first_name = input("First Name: ")
  last_name = input("Last Name: ")
  ssn = input("SSN: ")
  address = input("Address: ")
  phone = input("Phone Number: ")
  email = input("Do you have any email? y or n ")
  income = input("Annual Income: ")
  if email == 'y':
    email = input("Email: ")
  else:
    email = 'N/A'    
  if income.isnumeric():
    income=int(income)
  else:
    print('Please enter a valid number')
    income = input()
    income=int(income)
  retake = input(f"Is the following information correct? {first_name} {last_name} {ssn} {address}")
  if retake.lower() == 'yes':
    print('Thank you for your application. We will review your information and get back to you shortly.')
  else:
    print('Please retake the application') 
    apply_for_credit_card()
  print('---------------------------------');

def application():
  print('---------------------------------');
  print("Let's get started with your new Savings/Checking Account! Please select how you'd like to apply:");
  print("1. Apply Online");
  print("2. Apply In Person");
  choice = input("Enter your choice: ");
  if choice == "1":
    online_application()
  elif choice == "2":
    print("You have chosen to apply in person.  In order to create a bank account you'll have to visit your nearest branch to complete the application process."); 
    exit_programs()
  else:
    print("Invalid choice. Please select 1 or 2.");
  print('---------------------------------');

def online_application():
  print("You have chosen to apply online. To apply you'll needed to provide the following information: ");
  print("1. Re-sumbit Your Identification");
  print("2. Provide Contact Details");
  print("3. Select a Single or Joint Account");
  print("4. Accept the Terms and Conditions");
  print("5. Submit Your Application");
  print("6. Fund Your New Account"); 
  print("---------------------------------");
  print("Please provide the following information to complete your application or for step 1 and 2:");
  print("---------------------------------");
  first_name = input("First Name: "); 
  last_name = input("Last Name: ");
  ssn = input("SSN: ");
  address = input("Address: ");
  phone = input("Phone Number: ");
  email = input("Do you have any email? y or n ");
  if email == 'y':
    email = input("Email: ");
  else:
    email = 'N/A';
  income = input("Annual Income: ");
  if income.isnumeric():
    income=int(income)
  else:
    print('Please enter a valid number')
    income = input()
    income=int(income)
  retake = input(f"Is the following information correct? {first_name} {last_name} {ssn} {address} {phone} {email} {income}") 
  if retake.lower() == 'yes':
    different_accounts()
  else:
    print('Please retake the application') 
    bank_terms_and_conditions()
 
  
def bank_terms_and_conditions():
  print('---------------------------------');
  print('Elite 101 Bank Terms and Conditions');
  print('---------------------------------');
  print('1. Elite 101 Bank is a bank that provides a variety of banking services, including checking accounts, savings accounts, and credit cards.')
  print('2. Elite 101 Bank is committed to providing a safe and secure banking experience for all of its customers.')
  print('3. Elite 101 Bank is not responsible for any losses or damages that may occur as a result of using its services.')
  print('4. Elite 101 Bank reserves the right to modify or cancel any of its services at any time.') 
  print('5. Elite 101 Bank is not responsible for any unauthorized transactions that may occur on your account.')
  print('6. Elite 101 Bank is not responsible for any lost or stolen passwords.')
  print('7. Elite 101 Bank is not responsible for any damages that may occur to your device as a result of using its services.')
  print('8. Elite 101 Bank is not responsible for any damages that may occur to your device as a result of using its services.')
  print('---------------------------------');
  agreement = input(f"Do you agree to the terms and conditions? y or n ")
  if agreement.lower() == 'y':
    print('--------------------------------------')
    print('Thank you for your agreement. Now we will continue to the next step.')
    print('How much money would you like to deposit into your account?')
    print('--------------------------------------')
    print('Our bank have a minimum balance under 500 dollars.')
    min_balance = float(input("Enter the minimum balance required for this account: "))
    if min_balance >= 500:
        print('---------------------------------');
        print('Thank you for opening a Savings/Checking Account with Elite 101 Bank. Your account will be ready for use after 5 business days.')
        print('---------------------------------');
        exit()
  else:
    print('Please retake the application') 
    bank_terms_and_conditions()
    
    
def different_accounts():  
  print('---------------------------------');
  print('Thank you for your information and we should continued to the next step.')
  print('What type of account would you like to open?')
  print('1. Single Account: This account is for one individual only.')
  print('2. Joint Account: This account is for two or more individuals.')
  print('---------------------------------');
  while True:
    user_choice = input("Enter a number between 1-2: ")
    if user_choice == '1':
      print('---------------------------------');
      print('You have chosen to open a single checking account. Please enter your name and date of birth to complete the process.')
      print('---------------------------------');
      name = input("Name: ")
      dob = input("Date of Birth: ")
      print('---------------------------------');
      print('Thank you for opening a single checking account with Elite 101 Bank. Your account will be ready for use soon.')
      print('---------------------------------');
      print('Now take a look at the Banks Term and rules to know what you can do with your account.')
      print('---------------------------------');
      bank_terms_and_conditions()
      break
    elif user_choice == '2':
      print('---------------------------------');
      print('You have chosen to open a joint checking account. Please enter the names and dates of birth for both account holders to complete the process.')
      print('---------------------------------');
      name1 = input("Name of first account holder: ")
      dob1 = input("Date of Birth of first account holder: ")
      name2 = input("Name of second account holder: ")
      dob2 = input("Date of Birth of second account holder: ")
      print('---------------------------------');
      print('Thank you for opening a joint checking account with Elite 101 Bank. Your account will be ready for use soon.')
      print('---------------------------------');
      print('Now take a look at the Banks Term and rules to know what you can do with your account.')
      print('---------------------------------');
      bank_terms_and_conditions()
      break

def exit_programs():
  print('---------------------------------');
  exit = input('Would wants to coniue using Elite 101 Bank? y or n ')
  if exit.lower() == 'y':
    print('Thank you for using Elite 101 Bank. Lets us continue to the next step.')
  else:
    print('Thank you for using Elite 101 Bank. Have a great day!')


    
  

# Main program
def main():
  introduction()
  while True:
   print("Let's get started by making a account in the !0!:")
   print("1. Register")
   print("2. Login")
   print("3. Exit")
   choice = input("Enter your choice: ")
   if choice == "1":
     resigter()
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


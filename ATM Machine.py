import pyttsx3
import random

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

class Account:
    person = {}  # Stores name -> account info
    info = {}    # Stores account -> {phone number: pin, balance: value}

    def __init__(self, balance=0):
        self.balance = balance
    
    def create_acc(self):
        speak("Please enter your name:")
        name = input("Name: ")
        speak("Enter the Phone Number for your Account:")
        phone_num = int(input("Phone Number: "))

        # Generate a 15-digit account number
        account = random.randint(1, 9)
        for _ in range(14):
            account = account * 10 + random.randint(0, 9)

        # Generate a 4-digit PIN
        pin = random.randint(1, 9)
        for _ in range(3):
            pin = pin * 10 + random.randint(0, 9)

        # Initialize account details
        self.info[account] = {"phone": phone_num, "pin": pin, "balance": 0}
        self.person[name] = account
        
        speak("Your Account has been created successfully.")
        print(f"----------Account Details----------\nName :{name}\nPhone Number :{phone_num}\nAccount Number :{account}\n-----------------------------------")


    def deposit(self):
        account = int(input("Enter your account number: "))
        if account in self.info:
            speak("Enter the Amount you need to deposit")
            try:
                amount = int(input("₹: "))
                self.info[account]["balance"] += amount
                speak(f"₹{amount} has been successfully deposited. ")
                print(f"₹{amount} has been successfully deposited. ")
            except ValueError:
                speak("Invalid amount. Please enter a valid number.")
                print("Invalid amount. Please enter a valid number.")
        else:
            print("Account not found. Create a Bank Account.")
            speak("Account not found.Create a Bank Account.")
    
    def withdraw(self):
        account = int(input("Enter your account number: "))
        if account in self.info:
            speak("Enter the Amount you need to withdraw")
            try:
                amount = int(input("₹: "))
                if amount > self.info[account]["balance"]:
                    speak("Insufficient funds.")
                    print("Insufficient funds.")
                else:
                    self.info[account]["balance"] -= amount
                    speak(f"Your Transaction has been processed ")
                    speak("Transcation Successfull")
                    speak(f"₹{amount} has been successfully withdrawn. ")
                    print(f"₹{amount} has been successfully withdrawn. ")
                    ch=input("Want to Check Your Balance ?(type yes or no ): ")
                    if ch.lower()=='yes':
                        speak("Your Remaining balance is ₹" + str(self.info[account]['balance']))
                        print("Your Remaining balance is ₹" + str(self.info[account]['balance']))
                    else:
                        pass
            except ValueError:
                speak("Invalid amount. Please enter a valid number.")
                print("Invalid amount. Please enter a valid number.")
        else:
            print("Account not found.")
            speak("Account not found.")
    
    def check_balance(self):
        account = int(input("Enter your account number: "))
        if account in self.info:
            balance = self.info[account]["balance"]
            speak(f"Your current balance is: ₹{balance}")
            print(f"Your current balance is: ₹{balance}")
        else:
            speak("Account not found.")
            print("Account not found.")
    
    def change_pin(self):
        account = int(input("Enter your account number: "))
        phone_num = int(input("Enter the Phone number linked with the Account: "))
        
        if account in self.info and self.info[account]["phone"] == phone_num:
            new_pin = int(input("Enter the New ATM PIN: "))
            self.info[account]["pin"] = new_pin
            speak("Your PIN has been changed successfully.")
            print("Your PIN has been changed successfully.")
        else:
            speak("Account number or phone number is incorrect.")
            print("Account number or phone number is incorrect.")
        

# Main Menu Loop
speak("Welcome to Harshad Mehta Banks")
print("----------Welcome to Harshad Mehta Banks------------")
while True:    
    ac = Account()
    print("1. Create Account \n2. Deposit Money \n3. Withdraw Money \n4. Check Balance \n5. Change PIN \n6. Exit")
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        ac.create_acc()
    elif choice == 2:
        ac.deposit()
    elif choice == 3:
        ac.withdraw()
    elif choice == 4:
        ac.check_balance()
    elif choice == 5:
        ac.change_pin()
    elif choice == 6:
        speak("Thank You For Using Harshad Mehta Bank Visit Again")
        print("Thanks for Using the Bank")
        break
    else:
        print("Invalid Choice")
        speak("Invalid Choice")



# This is a basic console-based banking system in Python that allows users to create accounts, deposit and withdraw money, check their balance, and change their ATM PIN. The system uses the `pyttsx3` library to provide text-to-speech feedback. Account information, including account number, phone number, PIN, and balance, is stored in dictionaries. The system ensures secure handling of transactions by validating account details. Users can interact with the system through a simple menu interface.
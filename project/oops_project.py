# Bank Management System using OOP (classes, classmethods, staticmethods)
# Data is persisted in JSON file (data.json)

import json
import random
import string
from pathlib import Path 

class Bank:
    # Class variables (shared by all objects of this class)
    database = r"D:\Developer Rohit\Python_journy\project\data.json"  # use raw string for backslashes
    data = []  # list to hold all account records in memory

    # Load existing data from JSON file at class load time
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                content = fs.read()
                if content.strip():  # avoid empty file issues
                    data = json.loads(content)
        else:
            print("No such file exist")  # will be created on first update
    except Exception as error:
        print(error)

    """
    BEST PRACTICE NOTES:
    • Class Method (@classmethod): Knows about its class, receives 'cls'. 
      Use when you need to access/modify class variables (e.g., generate account using class context).
    • Static Method (@staticmethod): Does not know about class or instance. 
      Behaves like a normal function placed inside the class for logical grouping.
    """

    @staticmethod
    def __update():
        """Persist Bank.data to JSON file (private helper method)."""
        try:
            with open(Bank.database, 'w') as fs:
                fs.write(json.dumps(Bank.data))
        except Exception as e:
            print("Error while updating database:", e)

    @classmethod
    def __accountgenerater(cls):
        """Generate a random 8-digit account number (private helper)."""
        # alpha=random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits, k=8)
        # spchar=random.choices("!@#$^&*",k=1)
        # id=alpha+num+spchar
        id = num
        random.shuffle(id)
        return "".join(id)


    def createaccount(self):
        """Create a new bank account after basic validation."""
        info = {
            "name": input("Enter Your Name: "),
            "age": int(input("Enter Your age: ")),
            "email": input("Enter Your Email: "),
            "pin": int(input("Enter You 4 digit Pin: ")),
            "accountNumber": Bank.__accountgenerater(),
            "balance": 0
        }
        # Validation: age must be 18+ and PIN must be exactly 4 digits
        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("Account can not be created")
        else:
            print("Account created Successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please Note your Account number")
            Bank.data.append(info)  # add to in-memory list
            Bank.__update()         # persist to JSON file

    def deposit(self, amount):
        """Deposit money into an account after verifying account number + PIN."""
        accountnum = input("Enter Account Number:")
        pin = int(input("Enter Pin: "))
        flag = False
        for i in Bank.data:
            if i["accountNumber"] == accountnum and i["pin"] == pin:
                i["balance"] += amount
                flag = True
                break
        if flag == False:
            print("Invalid user Details")
        else:
            Bank.__update()
            print("Amount deposit SuccessFully")

    def withdraw(self, amount):
        """Withdraw money if account is valid and has sufficient balance."""
        accountnum = input("Enter Account Number:")
        pin = int(input("Enter Pin: "))
        flag = False
        for i in Bank.data:
            if i["accountNumber"] == accountnum and i["pin"] == pin:
                if i["balance"] > amount:  # note: uses > not >=
                    i["balance"] -= amount
                    flag = True
                    break
                else:
                    print("Insufficient balance")
                    return
        if flag == False:
            print("Invalid user Details")
        else:
            Bank.__update()
            print("Amount withDraw SuccessFully")
    def userInfo(self):
        """Show account details for a valid account number + PIN."""
        accountnum = input("Enter Account Number:")
        pin = int(input("Enter Pin: "))
        flag = False
        for i in Bank.data:
            if i["accountNumber"] == accountnum and i["pin"] == pin:
                print("==========  ACCOUNT DETAILS ============")
                print(f"Name           : {i['name']}")
                print(f"Age            : {i['age']}")
                print(f"Email          : {i['email']}")
                print(f"Account Number : {i['accountNumber']}")
                print(f"Account Balance: {i['balance']}")
                print("=========================================")
                flag = True
                break
        if flag == False:
            print("Invalid user Details")
        else:
            # read-only operation -> no need to call __update()
            print("Fetched user details SuccessFully")

    def deleteUser(self):
        """Delete an account permanently after verifying credentials."""
        accountnum = input("Enter Account Number:")
        pin = int(input("Enter Pin: "))
        flag = False
        for i in Bank.data:
            if i["accountNumber"] == accountnum and i["pin"] == pin:
                Bank.data.remove(i)
                flag = True
                break
        if flag == False:
            print("Invalid user Details")
        else:
            Bank.__update()
            print(" user deleted SuccessFully")

    def updateInfo(self):
        """Update name or email of an existing account."""
        accountnum = input("Enter Account Number:")
        pin = int(input("Enter Pin: "))
        flag = False
        for i in Bank.data:
            if i["accountNumber"] == accountnum and i["pin"] == pin:
                print("==========  ACCOUNT DETAILS ============")
                print(f"Name           : {i['name']}")
                print(f"Age            : {i['age']}")
                print(f"Email          : {i['email']}")
                print(f"Account Number : {i['accountNumber']}")
                print(f"Account Balance: {i['balance']}")
                print("=========================================")
                print("Press 1 for Update Name")
                print("Press 2 for update Email")
                check = int(input("Tell your response: "))

                if check == 1:
                    name = input("Enter new Name: ")
                    i["name"] = name
                if check == 2:
                    email = input("Enter new Email: ")
                    i["email"] = email

                flag = True
                break
        if flag == False:
            print("Invalid user Details")
        else:
            Bank.__update()
            print("updated user details SuccessFully")

        


# ------------------------------------------------------------
# Program entry point / menu
# BEST PRACTICES (suggested improvements, logic unchanged):
#   1. Validate inputs (e.g. amount > 0, handle ValueError from int()).
#   2. Store PIN as a string so leading zeros (e.g. 0123) are preserved.
#   3. Use if/elif instead of many separate if's for the menu.
#   4. Wrap the menu in a while loop so the user can do multiple operations.
#   5. Prefer `if __name__ == "__main__":` to guard the entry point.
# ------------------------------------------------------------
user = Bank()

print("Press 1 for creating the account")
print("Press 2 for money deposit in the account")
print("Press 3 for money withdraw from the account")
print("Press 4 for account details")
print("Press 5 for update account details")
print("Press 6 for delete account")

check = int(input("Tell your response: "))

if check == 1:
    user.createaccount()
if check == 2:
    amount = int(input("Enter The Amount: "))
    user.deposit(amount)
if check == 3:
    amount = int(input("Enter The Amount: "))
    user.withdraw(amount)
if check == 4:
    user.userInfo()
if check == 5:
    user.updateInfo()
if check == 6:
    user.deleteUser()
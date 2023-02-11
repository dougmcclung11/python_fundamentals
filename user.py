

def login(database, username, password):

    if username in database:
        if database[username] == password:
            print(f"Welcome, {username}\n")
            return username
        else:
            print(f"Incorrect password for {username}")
            return ""
    else:
        print("User not found. Please Register")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    if username not in database:
        print("Username has been registered!")


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = (f"{username} donated {donation_amt}")
    print("Thank you for your donation!")
    return donation_string

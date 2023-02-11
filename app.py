from donations_pkg import homepage, user

database = {"admin": "password123"}
donations = []
authorized_user = ""


homepage.show_homepage()
if authorized_user == "":
    print("You must be logged in to donate.")

if authorized_user != "":
    print(f"Logged in as: {authorized_user}")


while True:
    option_select = input("Choose an option: ")
    if option_select == "1":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        authorized_user = user.login(database, username, password)

    if option_select == "2":
        username = input("Please create a username: ")
        password = input("Please create a password: ")

        authorized_user = user.register(database, username)
    if authorized_user != "":
        database[username] = password

    if option_select == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = user.donate(authorized_user)
            donations.append(donation_string)

    if option_select == "4":
        homepage.show_donations(donations)

    if option_select == "5":
        print("Leaving DonateMe... Goodbye!")
        break

def show_homepage():
    print("         === DonateMe Homepage ===       ")
    print("--------------------------------------------")
    print("| 1.      Login      | 2.     Register     |")
    print("--------------------------------------------")
    print("| 3.     Donate      | 4.   Show Donations |")
    print("--------------------------------------------")
    print("|                5. Exit                   |")
    print("--------------------------------------------")


def show_donations(donations):
    print("\n    --- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for x in donations:
            print(donations)

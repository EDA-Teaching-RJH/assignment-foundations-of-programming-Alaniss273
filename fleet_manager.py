def init_database():
    n = ["Kirk", "Spock", "Picard", "Janeway", "Sisko"]
    r = ["Captain", "Commander", "Captain", "Captain", "Captain"]
    d = ["Command", "SCience", "Command", "Command", "Command"]
    id = ["SC 937-0176 CEC", "S 179-276 SP", "SP 937-215", "SJ 854-336", "SS 682-190"]

    return n, r, d, id

def display_menu():
    un = input("What is your full name?")
    print("1. add_member")
    print("2. remove_member")
    print("3. update_rank")
    print("4. display_roster")
    print("5. search_crew")
    print("6. filter_by_division")
    print("7. calculate_payroll")
    print("8. count_officers")

    
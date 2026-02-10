def init_database():
    n = ["Kirk", "Spock", "Picard", "Janeway", "Sisko"]
    r = ["Captain", "Commander", "Captain", "Captain", "Captain"]
    d = ["Command", "SCience", "Command", "Command", "Command"]
    id = ["SC 937-0176 CEC", "S 179-276 SP", "SP 937-215", "SJ 854-336", "SS 682-190"]

    return n, r, d, id

n, r, d, id = init_database()

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

    opt = input("Select option: ")

def add_member():
    nid = input("What is the ID?")
    if nid in id:
        print("ID is not unique.")
        return

    nr = input("What is the new rank?")
    if nr not in r:
        print("Rank is not valid.")
        return

    n.append(input("What is their name?"))
    r.append(nr)
    d.append("What is their division?")
    id.append(nid)

def remove_member():
    wid = input("What is the ID?")
    if wid not in id:
        print("ID cannot be found.")
        return
    index = id.index(wid)

    n.pop(index)
    r.pop(index)
    d.pop(index)
    id.pop(index)
    print("Member has been removed.")

def update_rank():
    wid = input("What is the ID?")
    if wid not in id:
        print("ID cannot be found.")
        return
    
    nr = input("What is the new rank?")

    for i in range(len(n)):
        if id[i] == wid:
            r[i] == nr
            print("Rank is successfully updated.")
            return
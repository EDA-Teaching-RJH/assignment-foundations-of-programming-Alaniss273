def init_database():
    n = ["Kirk", "Spock", "Picard", "Janeway", "Sisko"]
    r = ["Captain", "Commander", "Captain", "Captain", "Captain"]
    d = ["Command", "Science", "Command", "Command", "Command"]
    ids = ["SC 937-0176 CEC", "S 179-276 SP", "SP 937-215", "SJ 854-336", "SS 682-190"]

    return n, r, d, ids

n, r, d, ids = init_database()

def display_menu():   
    print("\nOptions Menu:")
    print("1. Add member")
    print("2. Remove member")
    print("3. Update rank")
    print("4. Display roster")
    print("5. Search crew")
    print("6. Filter by division")
    print("7. Calculate payroll")
    print("8. Count officers")
    print("9. Exit")
    
    opt = input("Select option: ")
    return opt

def add_member(n, r, d, ids):
        
    nid = input("What is the new ID?")
    if nid in ids:
        print("ID is not unique.")
        return

    nr = input("What is the new rank?")
    if nr not in r:
        print("Rank is not valid.")
        return

    n.append(input("What is their name?"))
    r.append(nr)
    d.append(input("What is their division?"))
    ids.append(nid)

    print("Member added successfully.")
        
def remove_member(n, r, d, ids):
        wid = input("What is the ID?")
        if wid not in ids:
            print("ID cannot be found.")
            return
        
        index = ids.index(wid)
        n.pop(index)
        r.pop(index)
        d.pop(index)
        ids.pop(index)

        print("Member has been removed.")

def update_rank(n, r, ids):
        wid = input("What is the ID?")
        if wid not in ids:
            print("ID cannot be found.")
            return
    
        nr = input("What is the new rank?")
        print("Rank is successfully updated.")
        return

def display_roster(n, r, d, ids):
     for i in range(len(n)):
        print(n[i] + " - " + r[i] + " - " + d[i] + " - " + ids[i])

def search_crew(n, r, d, ids):
     sc = input("What do you want to look up?")
     for i in range(len(n)):
        if sc in n[i]:
            print(n[i], r[i], d[i], ids[i])

def filter_by_division(n, d):
    fbd = input("What division are you looking for?")

    found = False
    for i in range(len(d)):
        if d[i] == fbd:
            print(n[i])
            found = True

    if not found:
        print("No one was found in that division.")

def calculate_payroll(r):
    pay = 0
    for pr in r:
        if pr == "Captain":
            pay += 200
        elif pr == "Commander": 
             pay += 300
        else:
            pay += 100
    return pay 

def count_officers(r):
    target = input("Are you looking for 'Captain' or 'Commander'?")

    count = 0
    for cr in r:
        if cr == target:
            count += 1
    return count 

def main():
    n, r, d, ids = init_database()

    un = input("What is your full name?")
    print("\nWelcome Fleet Manager! - " + un)

    while True:
        opt = display_menu()

        if opt == "1":
            add_member(n, r, d, ids)
        
        elif opt == "2":
            remove_member(n, r, d, ids)

        elif opt == "3":
            update_rank(n, r, ids)

        elif opt == "4":
            display_roster(n, r, d, ids)

        elif opt == "5":
            search_crew(n, r, d, ids)

        elif opt == "6":
            filter_by_division(n, d)

        elif opt == "7":
            total = calculate_payroll(r)
            print("Total payroll is:", total)

        elif opt == "8":
            total = count_officers(r)
            print("Number of officers is:", total)
        
        elif opt == "9":
            print("Goodbye! - " + un)
            print("...")
            print("Shut down successful")
            break

        else: 
            print("Invalid option.")

main()
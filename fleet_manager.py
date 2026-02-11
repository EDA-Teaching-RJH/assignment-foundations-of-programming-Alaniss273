def init_database():
    n = ["Kirk", "Spock", "Picard", "Janeway", "Sisko"]
    r = ["Captain", "Commander", "Captain", "Captain", "Captain"]
    d = ["Command", "SCience", "Command", "Command", "Command"]
    ids = ["SC 937-0176 CEC", "S 179-276 SP", "SP 937-215", "SJ 854-336", "SS 682-190"]

    return n, r, d, ids

print("Welcome Fleet Manager!")
un = input("What is your full name?")

print("\nOptions Menu:")
print("1. Add member")
print("2. Remove member")
print("3. Update rank")
print("4. Display roster")
print("5. Search crew")
print("6. Filter by division")
print("7. Calculate payroll")
print("8. Count officers")
    
opt = input("Select option: ")

def add_member():
        
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
        
def remove_member():
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

def update_rank():
        wid = input("What is the ID?")
        if wid not in ids:
            print("ID cannot be found.")
            return
    
        nr = input("What is the new rank?")
        print("Rank is successfully updated.")
        return

def display_roster():
     for i in range(len(n)):
          print(n[i] + " - " + r[i] + " - " + d[i] + " - " + ids[i])

def search_crew():
     sc = input("What do you want to look up?")
     for i in range(len(n)):
          if sc in n[i]:
               print(n[i], r[i], d[i], ids[i])

def filter_by_divisions():
     

def calculate_payroll():
    pay = 0
    for r in r:
        if r == "Captain":
            pay += 200
        else: 
             pay += 300
    return pay 

def count_officers():
    count = 0
    for r in r:
        if r == "Captain" or r == "Commander":
            count = count + 1
    return count 

def main():
    n, r, d, ids = init_database()

    while True:
        opt = display_menu()

        if choice == "1":
             add_member()
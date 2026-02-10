def init_database():
    n = ["Kirk", "Spock", "Picard", "Janeway", "Sisko"]
    r = ["Captain", "Commander", "Captain", "Captain", "Captain"]
    d = ["Command", "SCience", "Command", "Command", "Command"]
    ids = ["SC 937-0176 CEC", "S 179-276 SP", "SP 937-215", "SJ 854-336", "SS 682-190"]

    return n, r, d, ids

n, r, d, ids = init_database()

def main():
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
main()

ranklist = ["Captain", "Lt. Commander", "Commander", "Lieutenant", "Ensign", "Lt junior grade", "Rear Admiral", "Vice Admiral", "Admiral", "Fleet Admiral"]
divlist = ["Command", "Science", "Operations", "Medical", "Engineering", "Security", "Communications", "Navigation", "Tactical"]
def main():
    names, ranks, divs, ids = init_database()
    while True:
        option = display_menu()
        if option == 1:
         add_member(names, ranks, divs, ids)
        elif option == 2:
            remove_member(names, ranks, divs, ids)
        elif option == 3:
            update_rank(names, ranks, ids)
        elif option == 4:
            display_roster (names, ranks, divs, ids)
        elif option == 5:
            search_crew(names, ranks, divs, ids)
        elif option == 6:
            filter_by_division(names, divs)
        elif option == 7:
            calculate_payroll(ranks)
        elif option == 8:
            count_officers(ranks)

def init_database():
    names = ["James T.Kirk", "Leonard McCoy", "Spock", "Montgomery Scott", "Hikaru Sulu", "Nyota Uhura", "Pavel Chekov"]
    ranks = ["Captain", "Lt. Commander", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant", "Ensign" ]
    divs = ["Command", "Science", "Science", "Operations", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "Unknown", "S 179-276 SP", "SE 197-54 T", "Unknown", "Unknown", "656-5827 B"]
    return names, ranks, divs, ids
def display_menu():
    Username = input("please enter your username here: ")
    print(f"Hello {Username}, please pick an option below")
    option = int(input("1 -Add Member\n2 -remove member\n3 -update rank\n4 -display roster\n5 -search crew\n6 -filter by division\n7 -calculate payroll\n8 -Count officers\n9 -Accessthe Database\n"))
    print(option)
    return option
def add_member(names, ranks, divs, ids):
    print("You have selected add member")
    name_new = input("What is the name of the new memeber? ")
    rank_new = input("What is the rank of the new member?  ")
    div_new = input("What is the division of the new member? ")
    id_new = input("what is the ID of the new member? ")
    if id_new in (ids):
        print("This ID is already in use. Please enter a uniue ID.")
        add_member(names, ranks, divs, ids)
    else:
        names.append(name_new)
        ranks.append(rank_new)
        divs.append(div_new)
        ids.append(id_new)
        print(f"{name_new} has been added to the crew roster.")
def remove_member(names, ranks, divs, ids):
    print("you have selected remove member")
    name_to_remove = input("what is the name of the member you want to remove? ")
    name_to_remove = name_to_remove.title()
    if name_to_remove in names:
        index = names.index(name_to_remove)
        names.pop(index)
        ranks.pop(index)
        divs.pop(index)
        ids.pop(index)
        print(f"{name_to_remove} has been removed from the crew roster.")
    else:
        print(f"{name_to_remove} cannot be found in the crew roster")
def update_rank(names, ranks, ids):
    print("you have selected update rank")
    name_to_update = input("what is the name of the member you want to update? ")
    name_to_update = name_to_update.title()
    if name_to_update in names:
        index = names.index(name_to_update)
        new_rank = input("what is the new rank of the member? ")
        ranks[index] = new_rank
        print(f"{name_to_update} has been updated to {new_rank}")
    else:
        print(f"{name_to_update} cannot be found in the crew roster")
    if new_rank not in ranklist:
        print("This is not a valid rank. please enter a valid rank.")
        update_rank(names, ranks, ids)
def display_roster(names, ranks, divs, ids):
    print("Crew Roster:")
    for i in range(len(names)):
        print(f"name: {names[i]} rank: {ranks[i]} division: {divs[i]} ID: {ids[i]}")
    return
def search_crew(names, ranks, divs, ids):
    print("you have selected to search the crew roster")
    search = input("what is the name of the crew member you want to search for? ")
    search = search.title()
    if search in names:
        index = names.index(search)
        print(f"name: {names[index]} rank: {ranks[index]} division: {divs[index]} ID: {ids[index]}")
    else:
        print(f"{search} cannot be found in the crew roster")
def filter_by_division(names, divs):
    print("you have selected to filter by division")
    divfilter = input("whatd division do you want to filter by? ")
    divfilter = divfilter.title()
    if divfilter in divlist:
        print(f"crew members in the {divfilter} division:")
        for i in range(len(names)):
            if divs[i] == divfilter:
                print(f"name: {names[i]} Divs: {divs[i]}")
    else:
        print(f"{divfilter} is not a valid division. please enter a valid division.")
def calculate_payroll(ranks):
    print("You have selected to calculate payroll")
    tpay = 0
    for i in range(len(ranks)):
        if ranks[i] == "Ensign":
            tpay += 1000
        elif ranks[i] == "Lt junior grade":
            tpay += 2000
        elif ranks[i] == "Lieutenant":
            tpay += 3000
        elif ranks[i] == "Commander":
            tpay += 4000
        elif ranks[i] == "Captain":
            tpay += 5000
        elif ranks[i] == "Lt. Commander":
            tpay += 6000
        elif ranks[i] == "Commander":
            tpay += 7000
        elif ranks[i] == "Rear Admiral":
            tpay += 8000
        elif ranks[i] == "Vice Admiral":
            tpay += 9000
        elif ranks[i] == "Admiral":
            tpay += 10000
        elif ranks[i] == "Fleet Admiral":
            tpay += 11000
        print(f"The total payroll for the crew is: {tpay}")
    
    
def count_officers(ranks):
    print("You have selected to count officers")
    officercount = 0
    for i in range(len(ranks)):
        if ranks[i] in ranklist:
         officercount += 1
        print(f"The total number of officers is {officercount}")
main()


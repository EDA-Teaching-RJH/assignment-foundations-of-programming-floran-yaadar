def init_database(name, rank, divs, ids):
    name = ["James T.Kirk", "Leonard McCoy", "Spock", "Montgomery Scott", "Hikaru Sulu", "Nyota Uhura", "Pavel Chekov"]
    rank = ["Captain", "Lt. Commander", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant", "Ensign" ]
    divs = ["Command", "Science", "Science", "Operations", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "Unknown", "S 179-276 SP", "SE 197-54 T", "Unknown", "Unknown", "656-5827 B"]
    return name, rank, divs, ids
def display_menu():
    Username = input("please enter your username here: ")
    print(f"Hello {Username}, please pick an option below")
    option = int(input("1 -Add Member\n2 -remove member\n3 -update rank\n4 -display roster\n5 -search crew\n6 -filter by division\n7 -calculate payroll\n8 -Count officers\n9 -Accessthe Database"))
    print(option)
    while True:
        if option == 1:
            add_member(name, rank, divs, ids)
        elif option ==2:
            remove_member(name, rank, divs, ids)
        elif option ==3: 
            update_rank(name, rank, divs, ids)
        elif option ==4:
            display_roster()
        elif option ==5:
            search_crew()
        elif option ==6:
            filter_by_division()
        elif option ==7:
            calculate_payroll()
        elif option ==8:   
             count_officers()
        elif option ==9:
             init_database()
def add_member(name, rank, divs, ids):
    name, rank, divs, ids = init_database()
    new_name = input("Enter the name of the new member: ")
    new_rank = input("Enter the rank of the new member: ")
    new_div = input("Enter the division of the new member: ")
    new_id = input("Enter the ID of the new member: ")
    name.append(new_name)
    rank.append(new_rank)
    divs.append(new_div)
    ids.append(new_id)
    print(f"{new_name} has been added to the crew roster.")
def remove_member(name, rank, divs, ids):
    name_to_remove = input("Enter the name of the member to remove: ")
    if name_to_remove in name:
        index = name.index(name_to_remove)
        name.pop(index)
        rank.pop(index)
        divs.pop(index)
        ids.pop(index)
        print(f"{name_to_remove} has been removed from the crew roster.")
    else:
        print(f"{name_to_remove} not found in the crew roster.")
def update_rank(name, rank, divs, ids):
    name_to_update = input("Enter the name of the member to update: ")
    if name_to_update in name:
        index = name.index(name_to_update)
        new_rank = input("Enter the new rank: ")
        rank[index] = new_rank
        print(f"{name_to_update}'s rank has been updated to {new_rank}.")
    else:
        print(f"{name_to_update} not found in the crew roster.")
def display_roster(name, rank, divs, ids):
    print("Crew Roster:")
    for i in range(len(name)):
        print(f"Name: {name[i]}, Rank: {rank[i]}, Division: {divs[i]}, ID: {ids[i]}")
def search_crew(name, rank, divs, ids):       
    search_name = input("Enter the name of the crew member to search for: ")
    if search_name in name:
        index = name.index(search_name)
        print(f"Name: {name[index]}, Rank: {rank[index]}, Division: {divs[index]}, ID: {ids[index]}")
    else:
        print(f"{search_name} not found in the crew roster.")
def filter_by_division(name, divs):
    division_to_filter = input("Enter the division to filter by: ")
    print(f"Crew members in the {division_to_filter} division:")
    for i in range(len(name)):
        if divs[i] == division_to_filter:
            print(f"Name: {name[i]}, Rank: {rank[i]}, ID: {ids[i]}")
def calculate_payroll(rank):
    rank_pay = {
        "Captain": 100000,
        "Lt. Commander": 75000,
        "Commander": 60000,
        "Lieutenant": 50000,
        "Ensign": 40000
    }
    total_payroll = 0
    for rank in rank:
        total_payroll += rank_pay.get(rank, 0)
    print(f"Total payroll for the crew: ${total_payroll}")
def count_officers(ranks):
    officer_count = 0
    for rank in ranks:
        if rank in ["Captain", "Lt. Commander", "Commander"]:
            officer_count += 1
    print(f"Total number of officers in the crew: {officer_count}")

display_menu();

def main():
    name, rank, divs, ids = init_database()
    display_menu()
main()
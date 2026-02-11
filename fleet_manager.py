def init_database():
    name = ["James T.Kirk", "Leonard McCoy", "Spock", "Montgomery Scott", "Hikaru Sulu", "Nyota Uhura", "Pavel Chekov"]
    rank = ["Captain", "Lt. Commander", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant", "Ensign" ]
    divs = ["Command", "Science", "Science", "Operations", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "Unknown", "S 179-276 SP", "SE 197-54 T", "Unknown", "Unknown", "656-5827 B"]
def display_menu():
    Username = input("please enter your username here: ")
    print(f"Hello {Username}, please pick an option below")
    option = int(input("1 -Add Member\n2 -remove member\n3 -update rank\n4 -display roster\n5 -search crew\n6 -filter by division\n7 -calculate payroll\n8 -Count officers\n9 -Accessthe Database"))
    print(option)
    while true:
        if option == 1:
            add_member()
        elif option ==2:
            remove_member()
        elif option ==3: 
            update_rank()
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


display_menu();

def main():
    init_databse()
    display_menu()
    add_memeber(names, ranks, divs, ids)
    remove_members(names, ranks, divs, ids)
    update_rank(names, ranks, ids)
    display_roster(names, ranks, divs, ids)
    search_crew(names, ranks, divs, ids)
    filter_by_division(names, divs)
    calculate_payroll(ranks)
    count_officers(ranks)

def main():
    name, rank, divs, ids = init_database()
    display_menu()
def init_database():
    names = ["James T.Kirk", "Leonard McCoy", "Spock", "Montgomery Scott", "Hikaru Sulu", "Nyota Uhura", "Pavel Chekov"]
    ranks = ["Captain", "Lt. Commander", "Commander", "Lt. Commander", "Lieutenant", "Lieutenant", "Ensign" ]
    divs = ["Command", "Science", "Science", "Operations", "Command", "Operations", "Command"]
    ids = ["SC 937-0176 CEC", "Unknown", "S 179-276 SP", "SE 197-54 T", "Unknown", "Unknown", "656-5827 B"]
    return names, ranks, divs, ids
def display_menu():
    Username = input("please enter your username here: ")
    print(f"Hello {Username}, please pick an option below")
    option = int(input("1 -Add Member\n2 -remove member\n3 -update rank\n4 -display roster\n5 -search crew\n6 -filter by division\n7 -calculate payroll\n8 -Count officers\n9 -Accessthe Database"))
    print(option)
    return option
main()


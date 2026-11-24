#
# User interface section
#


from functions import add_station, move_title, sort_by_category, preview_broad
def print_list(stations):
    for i in stations:
        print(i)
def print_menu():
    print("1.Add segment")
    print("2.Move a segment to the end")
    print("3. List segments by category")
    print("4. Preview broadcast")
    print("0. Exit")
def start():
    stations= [
        {"title":"Headlines","category": "News" , "duration": 3},
        {"title":"Interview" , "category": "Talk" ,"duration": 6},
        {"title":"Forecast", "category": "News","duration": 2},
        {"title":"Traffic" ,"category": "News","duration": 3}
    ]
    while True:
        print_menu()
        choice = int(input("What do you want to do? "))
        if choice == 1:
            title = input("The title is: ")
            categ = input("The category is: ")
            minu = int(input("The duration is: "))
            try:
                add_station(stations, title, categ, minu)
                print_list(stations)
            except ValueError as e :
                print(f"Error: {e}")
        elif choice ==2:
            title=input("The title you want to move is: ")
            try:
                new_list=move_title(stations, title)
                print_list(new_list)
            except ValueError as e :
                print(f"Error: {e}")
        elif choice ==3:
            category= input("What category do you want: ")
            try:
                sorted_list=sort_by_category(stations, category)
                print_list(sorted_list)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice==4:
            time_selected=int(input("Broadcast: "))
            new_list=[]
            current_time=0
            new_list=preview_broad(stations, new_list, time_selected, current_time)
            if new_list==False:
                print("error")
            else:
                print_list(new_list)
        elif choice == 0:
            break



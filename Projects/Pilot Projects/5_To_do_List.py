from datetime import date
import os

print("*" * 60)
print("|", "To-DO List".center(56), "|")
print("-" * 60)
print("|", "Select Option".center(56), "|")
print("|", "1. Add new list".center(56), "|")
print("|", "2. View old list".center(56), "|")
print("|", "3. Add in existing list".center(56), "|")
print("|", "4. Exit".center(56), "|")
print("*" * 60)
u_option = int(input("=> "))
user_list = []
if u_option == 1:
    print("Enter your name?")
    name = input("=> ").upper()
    n = int(input("Enter number of list you want to post: "))

    for i in range(1, n + 1):
        u_list = input(f"{i}. ")
        user_list.append(u_list)
    u_date = date.today()

    while True:
        while True:
            print("*"*80)
            print("|",f"{name} To-Do List".center(76),"|")
            print("|",f'Created at:{u_date}'.rjust(76),"|")
            print("|","-"*76,"|")
            for a in (user_list):
                print("|",user_list.index(a)+1,f' {a}'.ljust(74),"|")
            print("*"*80)
            print("Do you want to add more?[Yes/No] ")
            l_edit = input().upper()
            if l_edit == 'YES':
                n = int(input("Enter number of list you wanna add: "))
                for i in range(1, n + 1):
                    u_list = input(f"{i}. ")
                    user_list.append(u_list)
                print("*" * 80)
                print("|", f"{name} To-Do List".center(76), "|")
                print("|", f'Created at:{u_date}'.rjust(76), "|")
                print("|", "-" * 76, "|")
                for a in (user_list):
                    print("|", user_list.index(a) + 1, f' {a}'.ljust(74), "|")
                print("*" * 80)
            else:
                break

        print("Do you wanna save it and exit? [Yes/No]")
        u_save = input().upper()
        if u_save == "YES":
            with open(f'{name}.txt', 'w+') as f:
                f.write(f'{user_list.__str__()}')
                f.seek(10)  # go to the start of the file
                print(f.read())

            print(f"***Your file {name}.txt is successfully saved in directory***")

        else:
            exit()

if u_option == 2:
    print("Enter the file name you want to view")
    name = input("=> ").upper()
    try:
        with open(f'{name}.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Sorry there is no file named {name}.txt ")


if u_option == 3:
    print("Enter your name?")
    name = input("=> ").upper()
    if os.path.isfile(os.path.join(f'./{name}.txt')) == True:
       print("Enter no. of list you wanna add: ")
       n = int(input("=> "))
       for i in range(1, n + 1):
           u_list = input(f"{i}. ")
           user_list.append(u_list)
       with open(f"{name}.txt",'a') as file:
           file.write(user_list.__str__())
       print("Your To do list are added successfully")

    else:
        print(f"sorry there is no file named {name}.txt")
if u_option == 4:
    exit()

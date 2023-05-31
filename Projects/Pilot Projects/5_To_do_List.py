from datetime import datetime
print("*"*60)
print("|","To-DO List".center(56),"|")
print("*"*60)
print("Enter your name?")
name = input("=> ").upper()
print("Enter completion year: ")
c_date_year = int(input("Year"))
print("Enter completion month: ")
c_date_month = int(input("Month"))
print("Enter completion day(date): ")
c_date_day = int(input("Date"))
print("Enter completion Hour")
c_hour = int(input("Hour: "))
print("Enter completion Minute")
c_minute = int(input("Minute: "))
c_date = datetime(c_date_year,c_date_month,c_date_day,c_hour,c_minute)
print(c_date)

print(name)
user_list = []
n = int(input("Enter number of list you wanna post: "))
for i in range(1 ,n+1):
    u_list = input(f"{i}. ")
    user_list.append(u_list)


print("*"*80)
print("|","Your To-Do List".center(76),"|")
print("|","-"*76,"|")
for a in (user_list):
    print("|",user_list.index(a)+1,f' {a}'.ljust(74),"|")
print("*"*80)

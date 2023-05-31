import math
from datetime import date
print("*"*60)
print("||","<---Welcome to Birthdate Calculator--->".center(54),"||")
print("*"*60)
u_year = int(input("Enter your birth year::[YYYY] "))
while True:
    u_month = int(input("Enter your birth month::[MM] "))
    if u_month <=12:
        u_day = int(input("Enter your birth day(date)::[DD] "))
        if u_day <= 32:
            b_date = date(u_year, u_month, u_day)
            print("*" * 60)
            print("|", f'Your birthdate is :: {b_date}'.center(56), "|")
            print("*" * 60)




        # b_date = date(u_year, u_month, u_day)
        # print("*"*60)
        # print("|",f'Your birthdate is :: {b_date}'.center(56),"|")
        # print("*"*60)

            def birthday_calculator():
                age = date.today() - b_date
                age = (age / 365).days
                print("|"," ".center(56),"|")
                print( "|",f'Your Age is:{age}'.center(56),"|")
                print("|", " ".center(56), "|")

                now_month = date.today().month
                now_day = date.today().day
                if u_month >= now_month:
                    now = ((u_month*30.32 -now_month*30.117 )-(now_day))+u_day
                # rem_month = u_month - now

                    print("|",f'remaining days for birthday:{math.ceil(now)}'.center(56),"|")
                    print("|", " ".center(56), "|")
                    print("*" * 60)
                else:
                    now = (((u_month+now_month)*30.42)+(now_day+u_day))
                    print("|", f'remaining days for birthday:{math.floor(now)}'.center(56), "|")
                    print("|", " ".center(56), "|")
                    print("*" * 60)

            def Horroscope():
                astro_sign = ' '
                if u_month == 12:
                    astro_sign = 'Sagittarius' if (u_day < 22) else 'capricorn'

                elif u_month == 1:
                    astro_sign = 'Capricorn' if (u_day < 20) else 'aquarius'

                elif u_month == 2:
                    astro_sign = 'Aquarius' if (u_day < 19) else 'pisces'

                elif u_month == 3:
                    astro_sign = 'Pisces' if (u_day < 21) else 'aries'

                elif u_month == 4:
                    astro_sign = 'Aries' if (u_day < 20) else 'taurus'
                elif u_month == 5:
                    astro_sign = 'Taurus' if (u_day < 21) else 'gemini'
                elif u_month == 6:
                    astro_sign = 'Gemini' if (u_day < 21) else 'cancer'
                elif u_month == 7:
                    astro_sign = 'Cancer' if (u_day < 23) else 'leo'

                elif u_month == 8:
                    astro_sign = 'Leo' if (u_day < 23) else 'virgo'
                elif u_month == 9:
                    astro_sign = 'Virgo' if (u_day < 23) else 'libra'
                elif u_month == 10:
                    astro_sign = 'Libra' if (u_day < 23) else 'scorpio'
                elif u_month == 11:
                    astro_sign = 'scorpio' if (u_day < 22) else 'sagittarius'
                print("|", " ".center(56), "|")
                print("|",f"Your Astrological sign is : {astro_sign}".center(56),"|")
                print("|", " ".center(56), "|")
                print("*" * 60)


            b = birthday_calculator()
            h = Horroscope()
            exit()
        else:
            print("*" * 60)
            print('|',"XXX Enter Valid Date XXX".center(56),'|')
            print("*" * 60)
    # print()
    else:
        print("*" * 60)
        print('|',"XXX Enter Valid Month XXX".center(56),'|')
        print("*" * 60)
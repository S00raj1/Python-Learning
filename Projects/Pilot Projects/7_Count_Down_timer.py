import time
hour = int(input("Enter hour"))
while hour > 0:
    minute =int(input("Enter minute"))
    while minute > 0:
        seconds = 60
        while seconds > 0:

            time.sleep(1)
            current_time = f"Time Elapsed : {hour:0>2} : {minute:0>2} : {seconds:0>2}"
            print('\r',current_time, end='')

            # if hour == 00:
            #     if minute == 00:
            #         if seconds == 00:
            #             print("",end="")

            seconds -= 1

        minute -= 1

        hour -= 1
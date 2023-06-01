import random

print("*" * 60)
print("|", "Random Password Generator".center(56), "|")
print("-" * 60)

n = int(input("Enter number of character you want for password: "))
while True:
    rview = []

    if 5 < n < 15:
        while True:

            options = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%&*+"
            print("The AI generated random password is: ", "".join(random.choices(options, k=n)))
            print("Do you want next password?[Yes/No] ")
            reply = input("=> ").upper()
            if reply == "NO":
                break

        print("Do you like our random password generator? [Yes/No}")
        review = input("=> ").upper()
        if review == "YES":
            print("Thank you for liking us")
            print("Do you wanna suggest some changes?[Yes/No]")
            rvw = input("=> ").upper()
            if rvw == "YES":
                rvws = input("Feedback: ")
                rview.append(rvws)
                with open("review.txt", 'a') as file:
                    file.write(rview)
                print("Thank you for ur feedback")
                exit()
            exit()
        else:
            print("Do you wanna suggest some changes?[Yes/No]")
            rvw = input("=> ").upper()
            if rvw == "YES":
                rvws = input("Feedback: ")
                rview.append(rvws)
                with open("review.txt", 'a') as file:
                    file.write(rview)
                print("Thank you for ur feedback")
                exit()
            exit()

    elif n < 5:
        print("Please provide length greater then 5")
        n=int(input())

    elif n > 15:
        print("Please provide length smaller then 15")
        n = int(input())


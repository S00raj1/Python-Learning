import random
name = input("Enter your name: ")
while True:
    print("*" * 60)
    print("|", "---[Guess Number]---".center(56), "|")
    print("|", "Welcome to Number guessing game".center(56), "|")
    print("|", "-" * 56, "|")
    print("|", "".center(56), "|")
    print("|", "#Disclaimer#".center(56), "|")
    print("|", "This game is not for gambling purpose.".center(56), "|")
    print("|", "This game is developed for fun.".center(56), "|")
    print("*" * 60)
    won = 0
    lose = 0
    chance = 10
    for i in range(1,11):

        print("Guess number between 1 to 5")
        User_input = int(input("Number "))
        if User_input == random.randrange(1,6):
            won += 1
            chance -= 1
            print("*" * 60)
            print("|",f"Won: {won}".ljust(22),f'Chance: {chance}'.center(6),f"Lose: {lose}".rjust(23),"|")
            print("*" * 60)
        else:
            lose += 1
            chance -= 1
            print("*" * 60)
            print("|",f"Won: {won}".ljust(22),f'Chance: {chance}'.center(6),f"Lose: {lose}".rjust(23),"|")
            print("*" * 60)

    if won == 6:
        print(f"{name} won the game with {(won /10)*100}% accuracy.. ")
    else:
        print(f"{name} lose the game with {(lose / 10)*100}% inaccuracy .. ")

    user_choice = input(f'{name} do you want to play more?[Yes][No]')
    if user_choice.upper() == "NO":
        exit()

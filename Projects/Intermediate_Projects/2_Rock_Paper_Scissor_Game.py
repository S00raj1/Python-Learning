import random
import time

win = 0
loss = 0
draw = 0
game = 0

u_choice = ""
while True:
    print("*" * 60)
    print('|', "Rock Paper Scissor Game".center(56), "|")
    print("*" * 60)
    print('|', '1. Rock     👊'.center(55), "|")
    print('|', '2. Paper    🤚'.center(55), "|")
    print('|', '3. Scissors ✌️'.center(56), "|")
    print("*" * 60)
    options = "Rock", "Paper", "Scissors"
    c_choice = random.choice(options)
    c_choice = c_choice.upper()
    user_input = int(input("Enter your choice:  "))

    while True:

        if user_input == 1:
            u_choice = "Rock".upper()

            print(f'Computer choice is {c_choice} and your choice is {u_choice}')
            if u_choice == c_choice:
                print("Game Draw")
                draw += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10),f"draw: {draw}".center(40),f"loss: {loss}".rjust(10))
                break
            elif c_choice == "PAPER":
                print("You Loss")
                loss += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break
            else:
                print("You won")
                win += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break

        elif user_input == 2:
            u_choice == "Paper".upper()

            print(f'Computer choice is {c_choice} and your choice is {u_choice}')

            if u_choice == c_choice:
                print("Game Draw")
                draw += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break
            elif c_choice == "Scissors":
                print("You Loss")
                loss += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break
            else:
                print("You won")
                win += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break

        elif user_input == 3:
            u_choice = "Scissors".upper()
            print(f'Computer choice is {c_choice} and your choice is {u_choice}')

            if u_choice == c_choice:
                print("Game Draw")
                draw += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break
            elif c_choice == "ROCK":
                print("You Loss")
                loss += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break
            else:
                print("You won")
                win += 1
                game += 1
                print(f'Total played: {game}')
                print(f'win: {win}'.ljust(10), f"draw: {draw}".center(40), f"loss: {loss}".rjust(10))
                break
    if not (input("Do you wanna play again? [y/n] ")).lower() == 'y':
        break

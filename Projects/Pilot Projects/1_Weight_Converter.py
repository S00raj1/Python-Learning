name = input("Enter your name: ")
name = name.upper()
while True:
    print('+' * 60)
    print('|', 'Welcome To Weight Converter'.center(56), '|')
    print('+', '-' * 56, '+')
    print('|', 'Choose the option'.center(56), '|')
    print('+', '-' * 56, '+')
    print('|', '1. Kg to Pounds'.center(56), '|')
    print('|', '2. Pounds to Kg '.center(56), '|')
    print('|', '3. Kg to Gram  '.center(56), '|')
    print('|', '4. Gram to Kg  '.center(56), '|')
    print('|', '5. Kg to Quintal'.center(56), '|')
    print('|', '6. Quintal to Kg'.center(56), '|')
    print('+' * 60)
    count = 0
    User = int(input("Enter Your Weight: "))
    choice = int(input("Choose the conversion type:"))
    while choice >= 6:
        count += 1
        for i in range(count,6):

            print('+' * 60)
            print('|','Invalid choice, Please choose between 1-6'.center(56),'|')
            print('|',f"Chance left: {6-count}".center(56),'|')
            print('+' * 60)
            break
        choice = int(input("Choose the correct conversion type:"))
        if count==5:
            print('+' * 60)
            print("|","".center(56),'|')
            print("|","".center(56),'|')
            print("|","".center(56),'|')
            print('|',f"You are annoying me {name}\U0001FAE1\U0001FAE1\U0001FAE1\U0001FAE1, GOODBYE".center(53),'|')
            print("|","".center(56),'|')
            print("|","".center(56),'|')
            print("|","".center(56),'|')
            print('+' * 60)
            break
    if count==5:
        break
    else:

        def weight_converter(weight):

            if choice == 1:

                return (weight / 2.20462)

            elif choice == 2:
                return weight * 2.20462
            elif choice == 3:
                return weight * 1000
            elif choice == 4:
                return weight / 1000

            elif choice == 5:
                return weight / 100
            elif choice == 6:
                return weight * 100


        # else:
        #     # print('You chose out of range\nPlease choose')
        #     return choice

        converted = weight_converter(User)
        print('+' * 60)
        print('|', f'You chose option {choice} '.center(56), '|')
        print('|', f'Your converted weight is {converted}'.center(56), '|')
        print('+' * 60)
        value = (input("Do you wanna convert more? [Yes/No]"))
        if value.upper() == 'NO':
            break

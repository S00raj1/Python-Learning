print('=' * 15 + '[ Palindrome Finder ]' + '=' * 15)


def game():
    while True:
        word = input('Enter a word: ')
        rev = word[::-1]
        if rev == word:
            print('+' + '-' * 50 + '+')
            print('|' + f' The word {word} is a palindrome'.center(50) + '|')
            print('+' + '-' * 50 + '+')
        else:
            print('+' + '-' * 50 + '+')
            print('|' + f' The word {word} is not a palindrome'.center(50) + '|')
            print('+' + '-' * 50 + '+')

        response = input("Do you want to check again? [yes/no]")
        response = response.lower()
        if response == 'no':
            break



game()
print('=' * 19 + '[ exiting now ]' + '=' * 18)
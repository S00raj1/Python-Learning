from translate import Translator

print("*" * 90)
print("|", "Welcome to Word Translator".center(86), "|")
print("*" * 90)
while True:

    sentence = input("Enter a sentence to translate:: ")
    print("*"*90)
    print("|","Choose Language Translation Type".center(86),"|")
    print("*"*90)
    print("|","".center(86),"|")
    print("|","1. English To Nepali".center(86),"|")
    print("|","2. English To Hindi".center(86),"|")
    print("|"," 3. English To Chinese".center(86),"|")
    print("|","4. English To French".center(86),"|")
    print("|","5. English To Korean".center(86),"|")
    print("|"," 6. English To Spanish".center(86),"|")
    print("|","".center(86),"|")
    print("*"*90)
    option = int(input("Enter the option: "))

    match option:
        case 1:
            try:
                translator = Translator(to_lang="Nepali")
                translation = translator.translate(sentence)
                print("*" * 90)
                print("|",f"English: {sentence}".center(86),"|")
                print("|",f"Nepali: {translation}".center(86),"|")
                print("|", "".center(86), "|")
                print("*" * 90)
            except:
                print("*" * 90)
                print("|", "Sorry cannot translate it".center(86), "|")
                print("*" * 90)
        case 2:
            try:
                translator = Translator(to_lang="Hindi")
                translation = translator.translate(sentence)
                print("*" * 90)
                print("|", f"English: {sentence}".center(86), "|")
                print("|", f"Hindi: {translation}".center(86), "|")
                print("|", "".center(86), "|")
                print("*" * 90)
            except:
                print("*" * 90)
                print("|", "Sorry cannot translate it".center(86), "|")
                print("*" * 90)

        case 3:
            try:
                translator = Translator(to_lang="Chinese")
                translation = translator.translate(sentence)
                print("*" * 90)
                print("|", f"English: {sentence}".center(86), "|")
                print("|", f"Chinese: {translation}".center(86), "|")
                print("|","".center(86),"|")
                print("*"*90)
            except:
                print("*" * 90)
                print("|", "Sorry cannot translate it".center(86), "|")
                print("*" * 90)


        case 4:
            try:
                translator = Translator(to_lang="French")
                translation = translator.translate(sentence)
                print("*" * 90)
                print("|", f"English: {sentence}".center(86), "|")
                print("|", f"French: {translation}".center(86), "|")
                print("|","".center(86),"|")
                print("*"*90)
            except:
                print("*" * 90)
                print("|", "Sorry cannot translate it".center(86), "|")
                print("*" * 90)

        case 5:
            try:
                translator = Translator(to_lang="Korean")
                translation = translator.translate(sentence)
                print("*" * 90)
                print("|", f"English: {sentence}".center(86), "|")
                print("|", f"Korean: {translation}".center(86), "|")
                print("|","".center(86),"|")
                print("*"*90)
            except:
                print("*" * 90)
                print("|", "Sorry cannot translate it".center(86), "|")
                print("*" * 90)
        case 6:
            try:
                translator = Translator(to_lang="Spanish")
                translation = translator.translate(sentence)
                print("*" * 90)
                print("|", f"English: {sentence}".center(86), "|")
                print("|", f"Spanish: {translation}".center(86), "|")
                print("|","".center(86),"|")
                print("*"*90)
            except:
                print("*" * 90)
                print("|", "Sorry cannot translate it".center(86), "|")
                print("*" * 90)

        case _:
            print("*" * 90)
            print("|","Invalid Option".center(86),"|")
            print("|","".center(86),"|")
            print("*"*90)
            break

    check = input("Do you want to translate more?[Yes/No]  ")
    if check.upper() == "NO":
        exit()

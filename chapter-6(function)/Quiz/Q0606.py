words = input("Enter words seperated by -:")
def sort_words():
    items = words.split('-')
    items = sorted(items)
    print('-'.join(items))
sort_words()

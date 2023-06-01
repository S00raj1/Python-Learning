import itertools

#
animals = ['Bill', 'Billard', 'Bear', 'Cat', 'Lion', 'Tiger', 'Dog', 'Donkey', 'Carrot', 'Dada', 'Bird']
animals = sorted(animals, key=lambda x: x[1])

# animals = ['Dada', 'Cat', 'Carrot', 'Bear', 'Bill', 'Billard', 'Lion', 'Tiger', 'Bird'    'Dog', 'Donkey', ]

print(animals)
values = itertools.groupby(animals, lambda x: x[1])
grouped = {k: list(v) for k, v in values}
print(grouped)

#
#
# books = ['Science','Social','Math','English','Nepali','Computer','Health','Optional Math','Account']
# books = sorted(books)
# print(books)
# values = itertools.groupby(books,lambda x:x[0])
# grouped = {x:tuple(v) for x,v in values}
# print(grouped)
# grouped = itertools.groupby(books, lambda  y:y[1])
# display = {y:list(v) for y,v in grouped}
# print(display)


#
# location = ('Biratnagar','Sitagunj','Sunsari','Morang','Amardaha','Kathmandu','Kalopul','Thapagaun')
# location = sorted(location)
# geo = itertools.groupby(location,lambda a:a[0])
# cag = {a:list(v) for a,v in geo}
# print(cag)
#

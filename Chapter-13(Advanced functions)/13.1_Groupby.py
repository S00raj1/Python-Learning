import itertools
animals = ['Bear','Cat','Lion','Tiger','Dog','Donkey','Carrot','Dada','Bill']
animals = sorted(animals)
print(animals)
values = itertools.groupby(animals,lambda x:x[0])
grouped = {k:list(v) for k,v in values}
print(grouped)
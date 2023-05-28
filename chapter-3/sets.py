numbers = {1,2,3.4,10,11}
animals = { 'cat','dog','tiger'}
random_lists = {1,'John ', 'Moon',True,45.6}


numb = {1,1,2,3,4,5,6,7,8,1,2,}
# dublicate items get discarded
print(numb)


# adding single item to existing set
numb.add(20)
print (numb)


# adding multiple items to existing set
# for adding multiple items we use update instead of add
numb.update([25,30,40,50])
print(numb)



# Removing items from sets
even = { 2,4,6,8,10,12}
even.discard(12)
print(even)


random  =  {'a','b','c','d','e','f'}
random.discard('a')
print(random)


# for printing length of set
print(len(random))


# for union of two sets
odd = { 1,3,5,7,9,11}
prime = {2,3,5,7,11,13}
x = odd | prime
print(x)
print(odd.intersection(prime))


# for intersection of two sets
a = {1,2,3,4,5,6,7,8,9}
b = {2,3,5,4,8,10,11,12}
x = a & b
print (x)
print(a.union(b))
# for difference between two sets
print(a-b)
print(a.difference(b))

# for symmetric difference between two sets
print(a.symmetric_difference(b))
print(a^b)



# for accessing items in sets
# We can not access individual item of the set, however we can iterate through all items of a set using for loop.
prime = {2,3,5,7,11,13,17}
for i in prime:
    print(i)




x = [1,1,2,3,4,5,7,8,9,9,1,0,10,1,1,0,10]
x = list(set(x))
print(x)
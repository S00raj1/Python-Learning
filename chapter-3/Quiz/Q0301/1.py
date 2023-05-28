my_list = []
my_list.append(5)
my_list.append(9)
print(my_list)

number = input('input a number')
# number = int(number)
my_list.append(int(number))
print(my_list)

more_items = [1,5,9]
more_items.extend(my_list)
print(more_items)


print('the length of more items is : '+str(len((more_items))))

more_items.pop(1)
print(more_items)
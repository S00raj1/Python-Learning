wild = ['tiger','lion','deer','bear','zebra']
wild.sort()
print(wild)
wild.reverse()
print(wild)
wildd = ['leopard','elephant','rhino']
wild.extend(wildd)
print(wild)
i = wild.index('leopard')

print(i)
wild.pop(i)
print(wild)
# print(wild.index('leopard'))
wild.insert(2,'leopard')
print(wild)
wild.remove('rhino')
print(wild)
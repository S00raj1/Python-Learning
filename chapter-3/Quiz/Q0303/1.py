multi = [
    [12,52,37],
    [46,51,16],
    [17,82,39]
]

x = multi [1][1]

print(x)

x = multi[-1][-2]
print(x)

print(len(multi))

multi.append([40,61,10])
print (multi)


for i in multi:
    for j in i:
        print(j)
    print(len(i))

multi.clear()
print(multi)
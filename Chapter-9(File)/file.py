with open('text.txt','w') as f:
    f.write('Hello world!!\n')
    f.write("Sathi k xa khabar timro")
    f.write('Eahh hello k xa khabar timro')

with open("details.txt","w") as file:
    file.write("Hello world")


with open('text.txt', 'a') as fc:
    fc.write('\nEahh hello ')

with open('text.txt','r') as fcb:
    for i in fcb:
        print(i)
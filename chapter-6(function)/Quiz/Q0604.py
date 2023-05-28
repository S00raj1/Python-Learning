number = int(input('enter a number for multiplication'))
def mul_table(number,limit:int=10):
    for i in range(1, limit+1):
        print(f'|'+' ' +(str(f'{number}')+ '  '+'X'+'  '+ str(i)+' ').center(10)+'|' + '   '+ str(number*i).center(10) + '|')
mul_table(number)
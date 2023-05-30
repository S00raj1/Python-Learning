def is_even(num):
    return  num %2 == 0
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = filter(is_even,(list_1))
print(list(list_2))

def odd(num):
    return num % 2 !=0
even_1 = (4,5,6,4,7,8,9,10,12,11,13,14,15,16)
even_2 = filter(odd,even_1)
print(list(even_2))


def check(num):
    if num < 0:
        return num
a = [10,-11,12,-14,15,-16,-13]
a1 = filter(check,a)
print(list(a1))
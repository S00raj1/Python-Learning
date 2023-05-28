'''
Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee according to the customer's requirements.

The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user. Please use the function make_coffee() to prepare a coffee and serve it.

Followings are the ingredients for coffee:

    Sugar: no. of spoons int
    Beans: no. of spoons int
    Milk: volume in ml. int

The total volume of coffee should be 250ml. The maximum volume of milk can be only up to 150ml. The volume Greater than the limit should give the error saying not acceptable.

Finally print the line describing the coffee you prepared along with milk and water composition.
'''

sugar = int(input('no. of spoons for sugar'))
beans = int(input('no. of spoons for beans'))
milk = int(input('volume of milk in ml'))
water = 250-milk-sugar-beans
cofi = sugar+beans+water
def make_coffee(sugar,beans,milk,water):
    coffee = 250

    if milk <= 150:
        if coffee == (milk + cofi):
            print('Your coffee is ready to serve')
        else:
            print("sorry your coffee is more then total coffee")
    else:
        print('Sorry milk greater then 150ml is not acceptable')


make_coffee(sugar,beans,milk,water)



print('Welcome to Pizza Delivery')
pizzaSize = input('What size of pizza do you want to buy? S, M, or L? ')
pepperoni = input('Do you want to buy pepperoni Pizza?  Y or N? ')
xtraCheese = input('Do you want to add extra cheese?   Y or N? ')
bill = 0

if  pizzaSize == 'S' or pizzaSize == 's':
    bill += 15
    if pepperoni == 'Y' or  pepperoni == 'y':
        bill += 5
        if xtraCheese == 'Y' or  xtraCheese == 'y':
            bill += 2
            print(f'You ordered pizza with size S,  pepperoni and extra cheese. Your bill is ${bill}')
        else:
            print(f'You ordered pizza with size S,  pepperoni. Your bill is ${bill}')
    elif  pepperoni == 'N' or  pepperoni == 'n':
        if  xtraCheese == 'Y' or  xtraCheese == 'y':
            bill += 2
            print(f'You ordered Pizza with size S and extra cheese.   Your bill is ${bill}')
        else:
            print(f'You  ordered Pizza with size S. Your bill is ${bill}')
    else:
        print(f'You  ordered Pizza with size S. Your bill is ${bill}')
elif pizzaSize == 'M'  or pizzaSize == 'm':
    bill += 20
    if pepperoni == 'Y' or  pepperoni == 'y':
        bill += 5
        if xtraCheese == 'Y' or  xtraCheese == 'y':
            bill += 2
            print(f'You ordered pizza with size M,  pepperoni and extra cheese. Your bill is ${bill}')
        else:
            print(f'You ordered pizza with size M,  pepperoni. Your bill is ${bill}')
    elif  pepperoni == 'N' or  pepperoni == 'n':
        if  xtraCheese == 'Y' or  xtraCheese == 'y':
            bill += 2
            print(f'You ordered Pizza with size M and extra cheese.   Your bill is ${bill}')
        else:
            print(f'You  ordered Pizza with size M. Your bill is ${bill}')
    else:
        print(f'You  ordered Pizza with size M. Your bill is ${bill}')
elif pizzaSize == 'L' or  pizzaSize == 'l':
    bill += 25
    if pepperoni == 'Y' or  pepperoni == 'y':
        bill += 5
        if xtraCheese == 'Y' or  xtraCheese == 'y':
            bill += 2
            print(f'You ordered pizza with size L,  pepperoni and extra cheese. Your bill is ${bill}')
        else:
            print(f'You ordered pizza with size L,  pepperoni. Your bill is ${bill}')
    elif  pepperoni == 'N' or  pepperoni == 'n':
        if  xtraCheese == 'Y' or  xtraCheese == 'y':
            bill += 2
            print(f'You ordered Pizza with size L and extra cheese.   Your bill is ${bill}')
        else:
            print(f'You  ordered Pizza with size L. Your bill is ${bill}')
    else:
        print(f'You  ordered Pizza with size L. Your bill is ${bill}')
else:
    print('Invalid Pizza Order')
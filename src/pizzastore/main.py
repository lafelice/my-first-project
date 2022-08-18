import random
pizzas = [
    (1, 'Mexicana', 15, 'Base + jalapeno + meet + cheeser'),
    (2, 'Kebabpizza', 12, 'kebab + feta + turkish pepper + cheese'),
    (3, 'Vegeteriana', 11, 'mushrooms + paprika + olive + tomato + onion'),
    (4, 'Frutti Di Mare', 15, 'Tuna + shrimps + mussel'),
    (5, 'Quatro stagioni', 12, 'Tuna + mushrooms + shrimps + turkey strips'),
    (6, 'Margherita', 10, 'cheese + tomato'),
    (7, 'Hawaii', 11, 'turkey + ananas + cheese'),
    (8, 'Quatro formaggi', 12, 'Emmental + feta + chedar + mozzarella'),
    (9, 'Romeo', 12, 'salami + anans + shrimps + cheese'),
    (10, 'Special', 13, 'kebab + chicken + salami + olive + feta + paprika')
]
while True:
    print('Hello! 0 - Exit, 1 - pizzas')
    c = input('Your choice: ')
    match c:
        case '0':
            print('See you later.')
            break
        case '1':
            for pizzas_item in pizzas:
                print(*pizzas_item)

        case '2':
            receipt = random.randint(1, 5)
            print(f"Random amount items in receipt")
            for pizzas_item in random.sample(pizzas, receipt):
                pizzas_amount = random.randint(1, 3)
                print(f"{pizzas_item[1]} {pizzas_item[3]} * {pizzas_amount}")

        case '3':
            price = int(input ('Enter price:'))
            newlist = [i for i in pizzas if i[2] < price]
            for pizzas_price in newlist:
                print(*pizzas_price)


        case _:
            print('Wrong choice! Try again')

print('Bye!')
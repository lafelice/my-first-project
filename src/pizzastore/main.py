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

            print(*pizzas[0])
            print(*pizzas[1])
            print(*pizzas[2])
            print(*pizzas[3])
            print(*pizzas[4])
            print(*pizzas[5])
            print(*pizzas[6])
            print(*pizzas[7])
            print(*pizzas[8])
            print(*pizzas[9])
        case _:
            print('Wrong choice! Try again')

print('Bye!')
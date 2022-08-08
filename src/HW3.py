import cmath
print("a*x^2 + b*x + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 -4*a*c
x1 = (-b + D ** 0.5) / (2 * a)
x2 = (-b - D ** 0.5) / (2 * a)

if D > 0:
    print('x1 = ', x1, 'x2 = ', x2)
elif D < 0:
    print('The solution are complex numbers {0} and {1}'.format(x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print('x = ', x)
else:
    print('No roots')

number = 123
reverse = 0
reminder = number%10
reverse = (reverse*10) + reminder
number = number//10
reminder = number%10
reverse = reverse*10 + reminder
number = number//10
reminder = number%10
reverse = reverse*10 + reminder
number = number//10

print("The reverse number is:{} ".format(reverse))
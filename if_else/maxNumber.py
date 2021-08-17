#Вывести большее число
a=int(input('Первое число волшебника '))
b=int(input('Второе число волшебника '))
c=int(input('Второе число волшебника '))

if a >= b and a >= c:
    print(a, "наибольшее")
elif b >= a and b >= c:
    print(b, "наибольшее")
elif c >= a and c >= b:
    print(c, "наибольшее")

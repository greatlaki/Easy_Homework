a=int(input("Введите сторону треугольника:"))
b=int(input("Введите сторону треугольника:"))
c=int(input("Введите сторону треугольника:"))

if (c+b) > a and (a+c) > b and (a+b) > c:
    if a == b or a == c or b == c:
        print('Треугольник - равнобедренный')
    elif a == b == c:
        print('Треуголник - равносторонний')
    else:
        print("Треуголник - разносторонний")
else:
    print('Triangle doesnt exists')
    


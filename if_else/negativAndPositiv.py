positiv=0
negativ=0
x = int(input("Введите первое число :"))
y = int(input("Введите второе число :"))
z = int(input("Введите третье число :"))

if (x < 0):
    negativ += 1
elif (x > 0):
    positiv += 1
    
if (y < 0):
    negativ += 1
elif(y > 0):
    positiv += 1
    
if (z < 0):
    negativ += 1
elif(z > 0):
    positiv += 1

if(positiv == 0 and negativ == 0):
    print("Все числа нули не отрицательные и не положительные")
else:
    print(negativ,'отрицательных чисел волшебника')
    print(positiv,'положительных чисел волшебника')
    nZero = 3 - (positiv + negativ)
    print(nZero," - нулей")

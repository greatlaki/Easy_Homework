#Правильное окончание
a=int(input('Количство волшебников '))
if a == 1:
    print(a, end=' волшебник')
elif a > 1 and a < 6:
    print(a, end=' волшебника')
elif a > 7:
    print(a, end=' волшебников')
    

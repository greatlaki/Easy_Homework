c = int(input("Введите число: "))
x = c;
if c > 0:
    c += 1
elif c < 0:
    c += 2
elif c == 0:
    c = 10
else:
    print('nothing will work')

print(c)

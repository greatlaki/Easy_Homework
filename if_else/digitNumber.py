a=int(input())
if a < 10 and a > 0:
    print('Singl, positive number')
elif a > -10 and a < 0:
    print('Singl, negative number')
elif a >= 10 and a < 100:
    print('Double, positive number')
elif a <= -10 and a > -100:
    print('Double, negative number')
else:
    print('Digit is big')
        

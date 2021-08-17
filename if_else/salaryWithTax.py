s = int(input("Какая у тебя зэпэ "))
n = 0
if s > 0 and s <= 500:
    n = 0
elif s > 500 and s <= 1000:
    n = 5
elif s > 1000 and s <= 2500:
    n = 15
elif s > 2500 and s <= 1000000:
    n = 25
else:
    n = 40

sAfter = s * ((100-n)/100)
print(s, ' - зарплата до вычета налогов, а после = ',sAfter,"$", sep='')


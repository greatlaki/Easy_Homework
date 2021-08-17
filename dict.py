##dict_1 = {'Andrei': 13,
##          'Vadim': 23,
##          'Anna': 20}
##
##for key, value in dict_1.items():
##    print(f"Ключ: {key} , значение: {value}")

# ---------------Task 1---------------

a = ['first', 1, 2, 3, 'second', 10, 20, 'third', 15, 56 ,70, 'fourth', -50]
'''
for i in range(len(a)):
    print(i)

first_key = a[0]
first_value = a[1:4]

second_key = a[4]
second_value = a[5:7]

third_key = a[7]
third_value = a[8:11]

fourth_key = a[11]
fourth_value = a[12]

d = {first_key: first_value,
     second_key: second_value,
     third_key: third_value,
     fourth_key: fourth_value}

for key, value in d.items():
    print(f"Ключ: {key} , значение: {value}")
'''
#--------------------------------------------------

##my_dict = {}
##current_str = None
##
##for e in a:
##    if(type(e) == str):
##        my_dict[e] = []
##        current_str = e
##    else:
##        my_dict[current_str].append(e)
##        
##for key, value in my_dict.items():
##    print(f"Ключ: {key} , значение: {value}")


# ---------------Task 2---------------

my_text = 'Как дела? Я слышал, ты бежишь от самого себя (но куда?)Как дела? (У, у) Я слышал, ты бежишь от самого себя (но куда?)'

'''
words = my_text.split()
d2 = {}
word = []
redo = []
for i in words:
    if i == i:
        redo += i
    else:
        redo = 1
print(word)
print(redo)
'''
#--------------------------------------------------

##my_dict2 = {}
##for word in my_text.split():
##    if word in my_dict2:
##        my_dict2[word] = my_dict2[word] + 1
##    else:
##        my_dict2[word] = 1
##
##for key, value in my_dict2.items():
##    print(f"Ключ: {key} , значение: {value}")

my_dict3 = {}
for word in my_text.split():
    my_dict3[word] = my_dict3.get(word, 0) + 1 # 0 передается, если ключа не существует

for key, value in my_dict3.items():
    print(f"Ключ: {key} , значение: {value}")
    





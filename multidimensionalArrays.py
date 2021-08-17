# Определяем ф-ю, которая будет выводить список в виде матрицы
def print_matrix(list_2d): 
                        
    for i in range(len(list_2d)):
       for j in range(len(list_2d[i])):
            print(list_2d[i][j], end = ' ')
       print()
#-------------------------------------------------
# ________________Task 1 _____________________       
def create_2d_arr(m, n):
# Создать матрицу, m - кол-во строк, n - столбцы 
    d2_arr = [] # Двумерный список,нешний массив

    for i in range(m): #Интерируемся по кол-ву СТРОК в массиве
        internal_arr = [] #Внутренний, вложенный массив
        
        for j in range(n): #Интерируемся по кол-ву СТОЛБЦОВ в массиве
            internal_arr.append(0) # Помещаем нули, n - раз

        d2_arr.append(internal_arr)
        
    return  d2_arr

list_2d_create = create_2d_arr(3, 3)

print_matrix(list_2d_create)

# ________________Task 2 _____________________
'''     
input:  output:

1 2 3   3 2 1
4 5 6   6 5 4
7 8 9   9 8 7
'''
# Нужно отзеркалить таблицу
def swap(arr, i, j): # j = len(arr) - 1 -i
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def mirror_2d_arr(arr_2d):
    for arr in arr_2d:
        for i in range(len(arr) // 2): # Вложенные массив с четной длиной меняются все местами
            swap(arr, i, len(arr) - 1 -i)

print_matrix(arr_2d)
    


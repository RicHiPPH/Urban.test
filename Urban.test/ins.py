from module_4.sortfunc import *


data_1 = list(map(int,input("Введите числа через пробел ").split()))  # 1 2 3 4 5
data_2 = list(map(int,input("Введите числа через пробел ").split()))
data_3 = list(map(int,input("Введите числа через пробел ").split()))

bubble_sort(data_1)
selection_sort(data_2)
insertion_sort(data_3)

print("Пузырьковая сортировка: " ,data_1)
print("Сотрировка выбором: ",data_2)
print("Сортировка вставкой: " , data_3)


#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#for i in a:
#    if i < 10:
#        print(i)


#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#c = []
#for i in a:
#    for j in b:
#        if i == j:
#            c.append(i)
#print(c)
#result = list(filter(lambda elem: elem in b, a))
#print(result)

#Импортируем нужный модуль и объявляем словарь:
#
#import operator
#d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#
#Сортируем в порядке возрастания:
#
#result = dict(sorted(d.items(), key=operator.itemgetter(1)))
#
#И в порядке убывания:
#
#result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

#Допустим, вот наши словари:
#dict_a = {1:10, 2:20}
#dict_b = {3:30, 4:40}
#dict_c = {5:50, 6:60}
#d = {}
#Объединить их можно вот так:
#for i in (dict_a,dict_b,dict_c):
#    d.update(i)
#print(d)
#А можно с помощью «звёздочного» синтаксиса:




#result = {**dict_a, **dict_b, **dict_c}
#print(result)
#n = int(input())
#def rash_():
#    global n
#    print(n,n * 2)
#rash_()

#n = input()
#n1 = int(n)
#n2 = int(n * 2)
#print(n1+n2)

#a = 46
#d = "String"
#d *= 5
#print(a,d)

#a = int(input("Введите число с 4 цифрами"))
#n1= round(a // 1000 % 10)
#n2=round(a // 100 % 10)
#n3=round(a // 10 % 10)
#n4=round(a % 10)
#print(n1, ",", n2, ",", n3, ",", n4)




def print_params(a = 1, b = "str",c = True):
    print(a,b,c)
print_params()
print_params(12,"Hello",False)
print_params(b=25)
print_params(c=[1,2,3])

values_list = [5,"or",True]
values_dict = {"a": 1, "b": "in", "c": True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "if"]
print_params(*values_list_2,42)

#def print_params(*args):
#    print(*args)
#print_params(1,2,3.5)
#print_params()   #Без аргументов
#
#
#def print_params(b = 25,c = [1,2,3]):
#    print(b,c)
#print_params()
#print_params()
#
#
#def print_params(a,b,c):
#    print(a,b,c)
#values_list = [1,"or",True]
#values_dict = {"a": 1, "b": "in", "c": True}
#print_params(*values_list)     #Спокойно выведет значение при использовнии *args
#print_params(**values_dict)    #Выведет ошибку при использовании *args
#
#values_list_2 = [54.32, "if"]
#print_params(*values_list_2,42)
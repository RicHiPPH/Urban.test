
#def print_params(a = 1, b = "str",c = True):
#    print(a,b,c)
#print_params()


#def print_params(*args):
#    print()
#print_params()


#def print_params(*args):
#    print()
#print_params(b=25)
#print_params(c=[1,2,3])       !!Error!!


def print_params(a,b,c):
    print(a,b,c)
values_list = [1,"or",True]
values_dict = {"a": 1, "b": "in", "c": True}
print_params(*values_list)     #Спокойно выведет значение при использовнии *args
print_params(**values_dict)    #Выведет ошибку при использовании *args

values_list_2 = [54.32, "if"]
print_params(*values_list_2,42)
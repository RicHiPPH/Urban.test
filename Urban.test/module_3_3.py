
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


immutable_var = 1, 2, 3, "sring", True
print( immutable_var)
#immutable_var [0] = 20 # объекты в данном случае не изменяемы, так как это кортеж, чтобы изменить объкты нужно создать список и обращаться к нему
mutable_list = ([1, 2, 3,"a","White"], 0)
print(mutable_list)
mutable_list[0][1] = 55
mutable_list[0][4] = "Black"
print(mutable_list)
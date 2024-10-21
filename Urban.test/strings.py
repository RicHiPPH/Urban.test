my_dist = {"Vladimir": 2001 , "Ekaterina": 2002}
print(my_dist)
print(my_dist.get("Vladimir"))
print(my_dist.get("Anton"))
my_dist.update({"Sasha": 2004 , "Max": 2003})
print(my_dist)
a = my_dist.pop("Max")
print(a)
print(my_dist)
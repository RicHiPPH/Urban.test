from pprint import pprint


#name = "sample.txt"
#file = open(name, "r") #r,w,a read, write, append
#pprint(file.read())
#file.close()

name = "sample2.txt"
file = open(name, "a") #r,w,a read, write, append
file.write("\nHello world2")
file.close()
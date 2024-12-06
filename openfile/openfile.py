from pprint import pprint
import io

name = "sample2.txt"
file = open(name, "r", encoding="utf-8") #r,w,a read, write, append
print(file.writable())
print(file.readable())
print(file.seekable())
print(file.closed)
pprint(file.tell())
pprint(file.read())
pprint(file.tell())
file.close()

#name = "sample2.txt"
#file = open(name, "a") #r,w,a read, write, append
#file.write("\nHello world2")
#file.close()
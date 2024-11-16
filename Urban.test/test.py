class Example:

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)
    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)

ex = Example('data', second=25, third=3.14)

















#class Cat:
#    def say(self):
#        print("May")
#
#    def eat(self):
#        print("Mnya")
#
#cat1 = Cat()
#cat2 = Cat()
#
#cat1.say()
#cat2.eat()




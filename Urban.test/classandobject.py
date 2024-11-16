class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f"Привет меня зовут {self.name}, мне {self.age}")

    def birthday(self):
        self.age += 1
        print(f"У меня день рождения, мне теперь {self.age}")


den = Human("Den",12)
max = Human("Max",22)
max.birthday()



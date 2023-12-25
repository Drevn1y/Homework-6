class Animal:
    def __init__(self, age):
        self.age = age

class Dog(Animal):
    def __init__(self, age, dog):
        super().__init__(age)
        self.dog = dog

    def make_sound(self):
        print(self.dog)

class Cat(Animal):
    def __init__(self, age, cat):
        super().__init__(age)
        self.cat = cat

    def make_sound(self):
        print(self.cat)

class Cow(Animal):
    def __init__(self, age, cow):
        super().__init__(age)
        self.cow = cow

    def make_sound(self):
        print(self.cow)

#интерфейс
while True:
    print('==============')
    print('Звуки!')
    print('1. Dog\n2. Cat\n3. Cow')
    choose = int(input('Выберите что вы хотите услышать: '))

    # логика
    if choose == 1:
        print('Выбрано: Dog')
        dog = Dog(dog='Гав-гав', age=1)
        dog.make_sound()

    elif choose == 2:
        print('Выбрано Cat')
        cat = Cat(cat='Мяю-мяю', age=2)
        cat.make_sound()

    elif choose == 3:
        print('Выбрано Cow')
        cow = Cow(cow='Му-му', age=3)
        cow.make_sound()
    else:
        print('Ошибка, Введите число от 1 до 3!')
## Наследование

Объясните, что такое наследование и как оно работает в Python

### Решение

По определению наследование — это механизм, при котором объект выступает основой для другого объекта, сохраняя все свои
свойства.

То есть если класс B наследуется от класса A, все характеристики класса A будут доступны и в классе B.
Класс A будет «базовым классом» (base class), а класс B — «производным классом» (derived class).

Это удобно, когда есть несколько классов с общей функциональностью.

Базовый синтаксис:

class Base: pass

class Derived(Base): pass

Более проработанный пример:

class Animal:
    def __init__(self):
        print("and I'm alive!")

    def eat(self, food):
        print("ñom ñom ñom", food)

class Human(Animal):
    def __init__(self, name):
        print('My name is ', name)
        super().__init__()

    def write_poem(self):
        print('Foo bar bar foo foo bar!')

class Dog(Animal):
    def __init__(self, name):
        print('My name is', name)
        super().__init__()

    def bark(self):
        print('woof woof')


michael = Human('Michael')
michael.eat('Spam')
michael.write_poem()

bruno = Dog('Bruno')
bruno.eat('bone')
bruno.bark()

>>> My name is  Michael
>>> and I'm alive!
>>> ñom ñom ñom Spam
>>> Foo bar bar foo foo bar!
>>> My name is Bruno
>>> and I'm alive!
>>> ñom ñom ñom bone
>>> woof woof

Вызов super() вызывает метод базового класса, то есть, вызывая super().__init__(), мы вызвали __init__ класса Animal.

В Python есть более продвинутая возможность — метаклассы (MetaClasses), которые позволяют программисту напрямую управлять созданием классов.

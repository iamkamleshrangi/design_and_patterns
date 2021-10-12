from abc import ABCMeta, abstractmethod

class IProduct(metaclass=ABCMeta):
    ''' Class interface Product '''
    @staticmethod
    @abstractmethod
    def create_object():
        "An abstract interface method"

class ConcreteProductA(IProduct):
    def __init__(self):
        self.name = 'ConcreteProductA'

    def create_object(self):
        return self

class ConcreteProductB(IProduct):
    def __init__(self):
        self.name = 'ConcreteProductB'

    def create_object(self):
        return self

class ConcreteProductC(IProduct):
    def __init__(self):
        self.name = 'ConcreteProductC'

    def create_object(self):
        return self

class Creator:
    @staticmethod
    def create_object(some_property):
        'A static method to get a concrete product'
        if some_property == 'a':
            return ConcreteProductA()
        elif some_property == 'b':
            return ConcreteProductB()
        elif some_property == 'c':
            return ConcreteProductC()
        return None

PRODUCT = Creator().create_object('a')
print(PRODUCT.name)

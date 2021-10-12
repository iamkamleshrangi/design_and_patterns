from abc import ABCMeta, abstractmethod

class IChair:
    ''' Chair interface '''
    @staticmethod
    @abstractmethod
    def get_dimensions(dimension):
        ''' get dimension static, abstract method '''

class SmallChair(IChair):
    def __init__(self):
        self._height = 50
        self._width = 50
        self._depth = 50

    def get_dimensions(self):
        return {'height':self._height,
                'width':self._width,
                'depth':self._depth}

class MediumChair(IChair):
    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return {'height':self._height,
                'width': self._width,
                'depth':self._depth}

class BigChair(IChair):
    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        return {'height':self._height,
                'width':self._width,
                'depth':self._depth}

class ChairFactory:
    @staticmethod
    def get_chair(chair_type):
        if 'small' in chair_type:
            return SmallChair()
        elif 'medium' in chair_type:
            return MediumChair()
        elif 'big' in chair_type:
            return BigChair()

CHAIR = ChairFactory.get_chair('medium')
print(CHAIR.get_dimensions())

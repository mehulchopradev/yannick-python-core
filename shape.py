from abc import abstractmethod, ABC
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

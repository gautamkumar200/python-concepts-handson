from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def getAreaa(self):
        pass

class Child(Shape):
    pass

if __name__ == "__main__":
  #shape = Child()
  print(5/2)
  print(5//2)

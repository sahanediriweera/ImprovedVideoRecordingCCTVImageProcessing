from abc import ABC, abstractmethod

class Difference(ABC):
    @abstractmethod
    def difference(self,frame):
        pass
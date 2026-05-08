from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def __str__(self):
        pass

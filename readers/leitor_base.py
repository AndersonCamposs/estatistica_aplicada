from abc import ABC, abstractmethod

class LeitorBase(ABC):

    @abstractmethod
    def lerArquivo(self) -> list:
        pass
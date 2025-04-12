class Rol:
    def __init__(self, dados: list[float]):
        self._dados = dados

    @property
    def dados(self) -> list[float]: 
        return self._dados
    
    @dados.setter
    def dados(self, dados: list[float]) -> None:
        self._dados = dados
        
    def getMaiorElemento(self) -> float:
        return self._dados[-1]
    
    def getMenorElemento(self) -> float:
        return self._dados[0]
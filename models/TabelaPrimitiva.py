class TabelaPrimitiva:
    def __init__(self, dados: list[float]):
        self._dados: list = dados

    @property
    def dados(self) -> list[float]:
        return self._dados
    
    @dados.setter
    def dados(self, dados: list[float]) -> None:
        self._dados = dados
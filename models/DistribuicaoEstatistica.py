from math import log2, ceil
from models.Rol import Rol

class DistribuicaoEstatistica:
    def __init__(self, dados: list[float]):
        self._rol: Rol = Rol(sorted(dados))
        self._n = len(self._rol.dados)
        self._k = self._calcularNumeroClasses()
        self._h = self._calcularAmplitudeTotal()
        self._hi = self._calcularAmplitudeClasse()

    def _calcularNumeroClasses(self) -> float:
        return ceil(1 + log2(self._n))
    
    def _calcularAmplitudeTotal(self) -> float:
        return self._rol.getMaiorElemento() - self._rol.getMenorElemento()
    
    def _calcularAmplitudeClasse(self) -> float:
        return ceil(self._h/self._k)
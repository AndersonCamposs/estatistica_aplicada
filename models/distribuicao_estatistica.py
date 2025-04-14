from math import log2, ceil
from prettytable import PrettyTable
from models.rol import Rol

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
    
    def exibirDistribuicaoEmTabela(self): 
        table = PrettyTable()
        table.field_names = ["n", "k", "h", "hi", "Lmin", "Lmax"]
        table.add_row([self._n, self._k, self._h, self._hi, min(self._rol.dados), max(self._rol.dados)], divider=True)

        print(table)
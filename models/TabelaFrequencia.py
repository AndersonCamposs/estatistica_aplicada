from models.FrequenciaClasse import FrequenciaClasse

class TabelaFrequencia:
    def __init__(self):
        self.classes: list[FrequenciaClasse] = []

    def obterSomatorioFrequencias(self) -> int:
        soma = 0
        for classe in self.classes:
            soma += classe.frequencia

        return soma
    
    def obterSomatorioFrequenciasRelativas(self):
        soma = 0
        for classe in self.classes:
            soma += classe.frequenciaRelativa

        return soma
    
    def obterLimitesInferiores(self) -> list[float]:
        return [i.limiteInferior for i in self.classes]
    
    def obterLimitesSuperiores(self) -> list[float]:
        return [i.limiteSuperior for i in self.classes]
    
    def obterFrequencias(self) -> list[int]:
        return [i.frequencia for i in self.classes]
    
    def obterPontosMedios(self):
        return [i.pontoMedio for i in self.classes]
    
        
from models.frequencia_classe import FrequenciaClasse
from prettytable import PrettyTable

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
    
    def exibirTabelaFormatada(self):
        table = PrettyTable()
        table.add_column("i", [classe.numClasse for classe in self.classes])
        table.add_column("int.", [classe.getLimites() for classe in self.classes])
        table.add_column("fi", [classe.frequencia for classe in self.classes])
        table.add_column("xi", [classe.pontoMedio for classe in self.classes])
        table.add_column("fi/n", [classe.frequenciaRelativa for classe in self.classes])
        table.add_column("Fi", [classe.frequenciaAcumulada for classe in self.classes])
        table.add_row(["////", "////", f"Σ = {self.obterSomatorioFrequencias()}", "////", f"Σ = {self.obterSomatorioFrequenciasRelativas()}", "////"], divider=True)

        print(table)
    
        
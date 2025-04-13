class FrequenciaClasse:
    def __init__(self, numClasse, limiteInferior, limiteSuperior):
        self.numClasse = numClasse
        self.dados: list[float] = []
        self.limiteInferior: float = limiteInferior
        self.limiteSuperior: float = limiteSuperior
        self.frequencia: int = 0
        self.pontoMedio: float = 0
        self.frequenciaRelativa: float = 0.0
        self.frequenciaAcumulada: int = 0

    def getLimites(self) -> str:
        return f"[{self.limiteInferior} - {self.limiteSuperior})"
    
    def setFrequencia(self):
        self.frequencia = len(self.dados)

    def setPontoMedio(self):
        self.pontoMedio = (self.limiteSuperior + self.limiteInferior) / 2
    
    def setFrequenciaRelativa(self, n):
        self.frequenciaRelativa = self.frequencia / n
    
    def setFrequenciaAcumulada(self, frequenciaAcumulada):
        self.frequenciaAcumulada = frequenciaAcumulada

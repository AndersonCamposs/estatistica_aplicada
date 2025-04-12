from models.TabelaPrimitiva import TabelaPrimitiva
from models.DistribuicaoEstatistica import DistribuicaoEstatistica
from models.TabelaFrequencia import TabelaFrequencia
from models.FrequenciaClasse import FrequenciaClasse

class ProcessadorEstatistico:
    def __init__(self, valores: list[float]) -> None:
        self._tabelaPrimitiva: TabelaPrimitiva = TabelaPrimitiva(valores)
        self._distribuicaoEstatistica: DistribuicaoEstatistica = DistribuicaoEstatistica(self._tabelaPrimitiva.dados)
    
    def obterTabelaFrequencia(self) -> TabelaFrequencia:
        copyRol = self._distribuicaoEstatistica._rol.dados.copy()
        count = 1
        tabelaFrequencia = TabelaFrequencia()
        #limite inferior da primeira classe
        limiteInferior = copyRol[0]

        while(count <= self._distribuicaoEstatistica._k):
            frequenciaClasse = FrequenciaClasse(count, limiteInferior=limiteInferior, limiteSuperior=limiteInferior + self._distribuicaoEstatistica._hi)
            # o limite inferior da próxima classe será o limite superior da atual
            limiteInferior = frequenciaClasse.limiteSuperior
            tabelaFrequencia.classes.append(frequenciaClasse)
            count += 1

        for i in range(len(tabelaFrequencia.classes)):
            classeAtual = tabelaFrequencia.classes[i]
            for j in range(len(copyRol)):
                if copyRol[0] >= classeAtual.limiteInferior and copyRol[0] < classeAtual.limiteSuperior:
                    classeAtual.dados.append(copyRol.pop(0))
                else:
                    break
            
            classeAtual.setFrequencia()
            classeAtual.setPontoMedio()
            classeAtual.setFrequenciaRelativa(self._distribuicaoEstatistica._n)
            if (classeAtual.numClasse == 1):
                classeAtual.setFrequenciaAcumulada(classeAtual.frequencia)
            else:
                classeAtual.setFrequenciaAcumulada(tabelaFrequencia.classes[i-1].frequenciaAcumulada)

        return tabelaFrequencia

from pandas import Series
from prettytable import PrettyTable
from models.tabela_primitiva import TabelaPrimitiva
from models.distribuicao_estatistica import DistribuicaoEstatistica
from models.tabela_frequencia import TabelaFrequencia
from models.frequencia_classe import FrequenciaClasse

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
                if (copyRol[0] >= classeAtual.limiteInferior and copyRol[0] < classeAtual.limiteSuperior):
                    classeAtual.dados.append(copyRol.pop(0))
                else:
                    break
            
            classeAtual.setFrequencia()
            classeAtual.setPontoMedio()
            classeAtual.setFrequenciaRelativa(self._distribuicaoEstatistica._n)
            if (classeAtual.numClasse == 1):
                classeAtual.setFrequenciaAcumulada(classeAtual.frequencia)
            else:
                classeAtual.setFrequenciaAcumulada(tabelaFrequencia.classes[i-1].frequenciaAcumulada + classeAtual.frequencia)

        return tabelaFrequencia

    def obter_medidas_de_tendencia_central(self, tabela_frequencia: TabelaFrequencia) -> list[float]:
        sr = Series(self._distribuicaoEstatistica._rol.dados)
        moda = sr.mode()
        media_ponderada = self._calcular_media_ponderada(tabela_frequencia)
        mediana = self._calcular_mediana(tabela_frequencia)
        
        table = PrettyTable()
        table.field_names = ["MODA", "MÉDIA PONDERADA", "MEDIANA"]
        table.add_row([moda.tolist(), media_ponderada, mediana])
        print(table)
    
    def _calcular_mediana(self, tabela_frequencia: TabelaFrequencia):
        freq_acumulada_alvo = (tabela_frequencia.obterSomatorioFrequencias() / 2)
        i = None
        i_anterior = None

        for j in range(len(tabela_frequencia.classes)):
            if(tabela_frequencia.classes[j].frequenciaAcumulada > freq_acumulada_alvo):
                i = tabela_frequencia.classes[j]
                i_anterior = tabela_frequencia.classes[j - 1]
                break
       
        
        mediana: float = round(((i.limiteSuperior - i.limiteInferior) * (tabela_frequencia.obterSomatorioFrequencias() - i_anterior.frequenciaAcumulada) + (i.frequencia * i.limiteInferior)) / i.frequencia, 2)
        return mediana
    
    def _calcular_media_ponderada(self, tabela_frequencia: TabelaFrequencia):
        lista_de_freqs = [i for i in tabela_frequencia.obterFrequencias()]
        lista_pontos_medios = [i for i in tabela_frequencia.obterPontosMedios()]
        numerador = 0
        denominador = 0
        for fi, xi in zip(lista_de_freqs, lista_pontos_medios):
            numerador += (fi * xi)
            denominador += fi
        
        media_ponderada = numerador/denominador

        return media_ponderada
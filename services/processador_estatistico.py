from pandas import Series
from math import sqrt
from models.tabela_primitiva import TabelaPrimitiva
from models.distribuicao_estatistica import DistribuicaoEstatistica
from models.tabela_frequencia import TabelaFrequencia
from models.frequencia_classe import FrequenciaClasse

class ProcessadorEstatistico:
    def __init__(self, valores: list[float]) -> None:
        self._tabelaPrimitiva: TabelaPrimitiva = TabelaPrimitiva(valores)
        self._distribuicao_estatistica: DistribuicaoEstatistica = DistribuicaoEstatistica(self._tabelaPrimitiva.dados)
        self._tabela_frequencia: TabelaFrequencia = self.obterTabelaFrequencia()
        self._obter_medidas_de_tendencia_central()
        self._obter_medidas_dispersao()
    
    def obterTabelaFrequencia(self) -> TabelaFrequencia:
        copyRol = self._distribuicao_estatistica._rol.dados.copy()
        count = 1
        tabelaFrequencia = TabelaFrequencia()
        #limite inferior da primeira classe
        limiteInferior = copyRol[0]

        while(count <= self._distribuicao_estatistica._k):
            frequenciaClasse = FrequenciaClasse(count, 
            limiteInferior=limiteInferior, limiteSuperior=limiteInferior + self._distribuicao_estatistica._hi)
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
            classeAtual.setFrequenciaRelativa(self._distribuicao_estatistica._n)
            if (classeAtual.numClasse == 1):
                classeAtual.setFrequenciaAcumulada(classeAtual.frequencia)
            else:
                classeAtual.setFrequenciaAcumulada(
                    tabelaFrequencia.classes[i-1].frequenciaAcumulada + classeAtual.frequencia)

        return tabelaFrequencia

    def _obter_medidas_de_tendencia_central(self) -> None:
        sr = Series(self._distribuicao_estatistica._rol.dados)
        moda = sr.mode()
        media_ponderada = self._calcular_media_ponderada()
        mediana = self._calcular_mediana()
        
        self._distribuicao_estatistica._moda = moda.tolist()
        self._distribuicao_estatistica._media_ponderada = media_ponderada
        self._distribuicao_estatistica._mediana = mediana
    
    def _calcular_mediana(self):
        freq_acumulada_alvo = (self._tabela_frequencia.obterSomatorioFrequencias() / 2)
        i = None
        i_anterior = None

        for j in range(len(self._tabela_frequencia.classes)):
            if(self._tabela_frequencia.classes[j].frequenciaAcumulada > freq_acumulada_alvo):
                i = self._tabela_frequencia.classes[j]
                i_anterior = self._tabela_frequencia.classes[j - 1]
                break
       
        
        mediana: float = ((i.limiteSuperior - i.limiteInferior) * ((self._tabela_frequencia.obterSomatorioFrequencias()/2) - i_anterior.frequenciaAcumulada) + (i.frequencia * i.limiteInferior)) / i.frequencia
        return mediana
    
    def _calcular_media_ponderada(self):
        lista_de_freqs = [i for i in self._tabela_frequencia.obterFrequencias()]
        lista_pontos_medios = [i for i in self._tabela_frequencia.obterPontosMedios()]
        numerador = 0
        denominador = 0
        for fi, xi in zip(lista_de_freqs, lista_pontos_medios):
            numerador += (fi * xi)
            denominador += fi
            
        print(denominador)
        
        media_ponderada = numerador/denominador

        return media_ponderada

    def _obter_medidas_dispersao(self) -> None:
        desvio_medio = self._calcular_desvio_medio()
        variancia = self._calcular_variancia()
        desvio_padrao = self._calcular_desvio_padrao(variancia)

        self._distribuicao_estatistica._desvio_medio = desvio_medio
        self._distribuicao_estatistica._variancia = variancia
        self._distribuicao_estatistica._desvio_padrao = desvio_padrao


    def _calcular_desvio_medio(self):
        somatorio = 0
        for i in self._tabela_frequencia.classes:
            somatorio += i.frequencia * abs(i.pontoMedio - self._distribuicao_estatistica._media_ponderada)

        return somatorio / self._distribuicao_estatistica._n
    
    def _calcular_variancia(self):
        somatorio = 0
        for i in self._tabela_frequencia.classes:
            somatorio += i.frequencia * pow(i.pontoMedio - self._distribuicao_estatistica._media_ponderada, 2)

        return somatorio / self._distribuicao_estatistica._n
    
    def _calcular_desvio_padrao(self, variancia):
        return sqrt(variancia)
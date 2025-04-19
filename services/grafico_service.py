import matplotlib.pyplot as plt
from models.tabela_frequencia import TabelaFrequencia
class GraficoService:
    def __init__(self) -> None:
        pass

    def plotHistograma(self, tabelaFrequencia: TabelaFrequencia, hi: float, k: float):
        limitesInferiores: list[float] = tabelaFrequencia.obterLimitesInferiores() 
        limitesSuperiores: list[float] = tabelaFrequencia.obterLimitesSuperiores()
        frequencias: list[int] = tabelaFrequencia.obterFrequencias()
        amplitudes: list[float] = [hi for i in range(k)]
        posicoes = limitesInferiores.copy()

        plt.bar(posicoes, frequencias, width=amplitudes, align='edge', edgecolor='black', color='lightgreen')
        
        x_label = [limitesInferiores[0]] + limitesSuperiores
        plt.xticks(x_label, labels=[str(i) for i in x_label])

        y_label = [i for i in range(0, max(frequencias) + 10, 25)]
        plt.yticks(y_label, [str(i) for i in y_label])

        plt.title("Histograma de frequência")
        plt.xlabel("Notas de matemática")
        plt.ylabel("Frequências")

        for i in range(len(frequencias)):
            centro = limitesInferiores[i] + amplitudes[i] / 2
            plt.text(centro, frequencias[i] + 2, str(frequencias[i]), ha='center')


        plt.show()

    def plotPoligono(self, tabelaFrequencia: TabelaFrequencia, hi: float):
        pontosMedios: list[float] = tabelaFrequencia.obterPontosMedios()
        frequencias: list[int] = tabelaFrequencia.obterFrequencias()

        pontosMedios = [pontosMedios[0] - hi] + pontosMedios + [pontosMedios[-1] + hi]
        frequencias = [0] + frequencias + [0]

        plt.plot(pontosMedios, frequencias, marker='o', linestyle='-', color='blue')
        plt.fill_between(pontosMedios, frequencias, color='blue', alpha=0.1)
        plt.xticks(ticks=pontosMedios, labels=[str(i) for i in pontosMedios])
        
        plt.ylim(0)
        plt.axhline(y=0, color='black', linewidth=1.0)
        plt.yticks(range(0, max(frequencias) + 30, 25)) 

        plt.title("Polígono de frequência")
        plt.xlabel("Notas de matemática")
        plt.ylabel("Frequências")

        plt.grid(True, linestyle='--', alpha=0.7)

        for x, y in zip(pontosMedios, frequencias):
            plt.text(x - 2, y + 4, str(y), ha='left', fontsize=10, color='black')

        plt.show()

    def plot_grafico_freq_acum(self, tabelaFrequencia: TabelaFrequencia, n: int):
        limitesSuperiores = [tabelaFrequencia.obterLimitesInferiores()[0]] + tabelaFrequencia.obterLimitesSuperiores()
        freqsAcumuladas = [0] + [i.frequenciaAcumulada for i in tabelaFrequencia.classes]

        plt.plot(limitesSuperiores, freqsAcumuladas, marker='o', linestyle='-', color='blue')

        plt.xticks(limitesSuperiores, labels=[str(i) for i in limitesSuperiores])

        plt.ylim(0)
        plt.axhline(y=0, color='black', linewidth=1.0)
        plt.yticks(range(0, n + 30, 100)) 

        for xi, yi in zip(limitesSuperiores, freqsAcumuladas):
            plt.plot([xi, xi], [0, yi], 'r--', linewidth=1)

        for x, y in zip(limitesSuperiores, freqsAcumuladas):
            plt.text(x + 2, y + 5, str(y), ha='left', fontsize=10, color='black')

        plt.title("Gráfico de frequência acumulada")
        plt.xlabel("Notas de matemática")
        plt.ylabel("Frequências acumuladas")

        plt.show()

        



        


        
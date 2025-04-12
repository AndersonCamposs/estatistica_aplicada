import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path
from services.ProcessadorEstatistico import ProcessadorEstatistico

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

df = pd.read_csv(Path(__file__).resolve().parent / "data" / "data.csv")
processadorEstatistico = ProcessadorEstatistico(df["Nota de matemática 0 - 100"].to_list())


tabelaFrequencia = processadorEstatistico.obterTabelaFrequencia()

'''lim_inf = tabelaFrequencia.obterLimitesInferiores()
lim_sup = tabelaFrequencia.obterLimitesSuperiores()
frequencias = tabelaFrequencia.obterFrequencias()

# Calculando a largura de cada classe
larguras = [sup - inf for sup, inf in zip(lim_sup, lim_inf)]

# Posição da base das barras (limite inferior)
posicoes = lim_inf


# Criando o histograma manual
plt.bar(posicoes, frequencias, width=larguras, align='edge', edgecolor='black', color='lightgreen')

x_label = [lim_inf[0]] + lim_sup

plt.xticks(ticks=x_label, labels=[str(i) for i in x_label])

# Eixos e título
plt.title('Histograma de Frequência')
plt.xlabel('Notas de matemática 0-100')
plt.ylabel('Frequência')

# Adicionando os intervalos como rótulos no meio das barras (opcional)
for i in range(len(frequencias)):
    centro = lim_inf[i] + larguras[i] / 2
    plt.text(centro, frequencias[i] + 2, str(frequencias[i]), ha='center')

plt.show()'''


# Pontos médios das classes
pontos_medios = tabelaFrequencia.obterPontosMedios()

# Frequências
frequencias = tabelaFrequencia.obterFrequencias()

# Opcional: adicionar ponto inicial e final com frequência 0 para "fechar" o polígono
pontos_medios = [pontos_medios[0] - processadorEstatistico._distribuicaoEstatistica._hi] + pontos_medios + [pontos_medios[-1] + processadorEstatistico._distribuicaoEstatistica._hi]
frequencias = [0] + frequencias + [0]

print("pontos médios: ", pontos_medios)
print("frequências: ", frequencias)

# Construindo o gráfico do polígono de frequência
plt.plot(pontos_medios, frequencias, marker='o', linestyle='-', color='blue')
plt.xticks(ticks=pontos_medios, labels=[str(i) for i in pontos_medios])
plt.ylim(0)
plt.axhline(y=0, color='black', linewidth=1.0)
plt.yticks(range(0, max(frequencias) + 30, 25))

# Personalização
plt.title('Polígono de Frequência')
plt.xlabel('Ponto Médio das Classes')
plt.ylabel('Frequência')

plt.grid(True, linestyle='--', alpha=0.7)

for x, y in zip(pontos_medios, frequencias):
    plt.text(x - 2, y + 2, str(y), ha='left', fontsize=10, color='black')

plt.show()
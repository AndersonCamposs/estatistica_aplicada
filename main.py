import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
from pathlib import Path
from services.ProcessadorEstatistico import ProcessadorEstatistico

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

df = pd.read_csv(Path(__file__).resolve().parent / "data" / "data.csv")
processadorEstatistico = ProcessadorEstatistico(df["Nota de matemática 0 - 100"].to_list())


tabelaFrequencia = processadorEstatistico.obterTabelaFrequencia()

lim_inf = tabelaFrequencia.obterLimitesInferiores()
lim_sup = tabelaFrequencia.obterLimitesSuperiores()
frequencias = tabelaFrequencia.obterFrequencias()

# Calculando a largura de cada classe
larguras = [sup - inf for sup, inf in zip(lim_sup, lim_inf)]

# Posição da base das barras (limite inferior)
posicoes = lim_inf

# Criando o histograma manual
plt.bar(posicoes, frequencias, width=larguras, align='edge', edgecolor='black', color='lightgreen')

# Eixos e título
plt.title('Histograma de Frequência')
plt.xlabel('Intervalos de Classe')
plt.ylabel('Frequência')

# Adicionando os intervalos como rótulos no meio das barras (opcional)
for i in range(len(frequencias)):
    centro = lim_inf[i] + larguras[i] / 2
    plt.text(centro, frequencias[i] + 0.5, str(frequencias[i]), ha='center')

plt.show()

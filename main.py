import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path
from services.ProcessadorEstatistico import ProcessadorEstatistico
from services.GraficoService import GraficoService
from utils.MensagemUtils import MensagemUtils

sys.path.append(os.path.abspath(os.path.dirname(__file__)))



class Main:
    def __init__(self):
        df = pd.read_csv(Path(__file__).resolve().parent / "data" / "data.csv")
        self.processadorEstatistico = ProcessadorEstatistico(df["Nota de matemática 0 - 100"].to_list())
        self.tabelaFrequencia = self.processadorEstatistico.obterTabelaFrequencia()
        self.graficoService = GraficoService(self.processadorEstatistico)

    def run(self):
        while(True):
            MensagemUtils().exibirOpcoes()
            opt = input("Selecione sua opção: ")
            if (opt == '0'):
                break
            elif(opt == '1'):
                self.graficoService.plotHistograma(self.tabelaFrequencia, self.processadorEstatistico._distribuicaoEstatistica._hi, self.processadorEstatistico._distribuicaoEstatistica._k)
            elif(opt == '2'):
                self.graficoService.plotPoligono(self.tabelaFrequencia, self.processadorEstatistico._distribuicaoEstatistica._hi)
            elif(opt == '3'):
                self.tabelaFrequencia.exibirTabelaFormatada()
                input("PRESSIONE ENTER PARA CONTINUAR...")
            else:
                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE.")
            
            os.system("cls")
        
        #self.graficoService.plotHistograma(self.tabelaFrequencia, self.processadorEstatistico._distribuicaoEstatistica._hi, self.processadorEstatistico._distribuicaoEstatistica._k)
        #self.graficoService.plotPoligono(self.tabelaFrequencia, self.processadorEstatistico._distribuicaoEstatistica._hi)


def main():
    app = Main()
    app.run()

if __name__ == "__main__":
    main()

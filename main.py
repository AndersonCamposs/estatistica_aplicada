import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path
from services.processador_estatistico import ProcessadorEstatistico
from services.grafico_service import GraficoService
from utils.mensagem_utils import MensagemUtils
from readers.leitor_csv import LeitorCSV
from readers.leitor_excel import LeitorExcel

sys.path.append(os.path.abspath(os.path.dirname(__file__)))



class Main:
    def __init__(self):
        self.processadorEstatistico = ProcessadorEstatistico(LeitorCSV(str(Path(__file__).resolve().parent / "data" / "data.csv"), "Nota de matemática 0 - 100").lerArquivo())
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

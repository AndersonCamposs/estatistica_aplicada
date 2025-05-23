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
        self.graficoService = GraficoService()

    def run(self):
        while(True):
            MensagemUtils().exibirOpcoes()
            opt = input("Selecione sua opção: ")
            if (opt == '0'):
                break
            elif(opt == '1'):
                self.graficoService.plotHistograma(self.processadorEstatistico._tabela_frequencia, self.processadorEstatistico._distribuicao_estatistica._hi, self.processadorEstatistico._distribuicao_estatistica._k)
            elif(opt == '2'):
                self.graficoService.plotPoligono(self.processadorEstatistico._tabela_frequencia, self.processadorEstatistico._distribuicao_estatistica._hi)
            elif(opt == '3'):
                self.graficoService.plot_grafico_freq_acum(self.processadorEstatistico._tabela_frequencia, self.processadorEstatistico._distribuicao_estatistica._n)
            elif(opt == '4'):
                self.processadorEstatistico._tabela_frequencia.exibirTabelaFormatada()
            elif(opt == '5'):
                print(self.processadorEstatistico._tabelaPrimitiva.dados)
                self.processadorEstatistico._tabelaPrimitiva.exibirTabelaFormatada()
            elif(opt == '6'):
                print(self.processadorEstatistico._distribuicao_estatistica._rol.dados)
            elif(opt == '7'):
                self.processadorEstatistico._distribuicao_estatistica.exibirDistribuicaoEmTabela()
            elif(opt == '8'):
                self.processadorEstatistico._distribuicao_estatistica.exibir_medidas_tendencia_central()
            elif(opt == '9'):
                self.processadorEstatistico._distribuicao_estatistica.exibir_medidas_dispersao()
            else:
                print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE.")
            
            input("PRESSIONE ENTER PARA CONTINUAR...")
            os.system("cls")
        
        #self.graficoService.plotHistograma(self.tabelaFrequencia, self.processadorEstatistico._distribuicao_estatistica._hi, self.processadorEstatistico._distribuicao_estatistica._k)
        #self.graficoService.plotPoligono(self.tabelaFrequencia, self.processadorEstatistico._distribuicao_estatistica._hi)


def main():
    app = Main()
    app.run()

if __name__ == "__main__":
    main()

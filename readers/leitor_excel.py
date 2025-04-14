import pandas as pd
from readers.leitor_base import LeitorBase

class LeitorExcel(LeitorBase):
    def __init__(self, caminho_arquivo, coluna_dos_dados):
        super().__init__()
        self._caminho_arquivo = caminho_arquivo
        self._coluna_dos_dados = coluna_dos_dados

    def lerArquivo(self) -> list[float]:
        df = pd.read_excel(self._caminho_arquivo)
        return df[self._coluna_dos_dados].dropna().tolist()
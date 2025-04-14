from prettytable import PrettyTable

class MensagemUtils:
    def __init__(self):
        pass

    def exibirOpcoes(self):
        table = PrettyTable()
        table.align = 'l'
        table.field_names = ["CÓD.", "OPÇÃO"]
        table.add_row([0, "SAIR"], divider=True)
        table.add_row([1, "HISTOGRAMA DE FREQUÊNCIA"], divider=True)
        table.add_row([2, "POLÍGONO DE FREQUÊNCIA"], divider=True)
        table.add_row([3, "GRÁFICO DE FREQUÊNCIA ACUMULADA"], divider=True)
        table.add_row([4, "TABELA DE FREQUÊNCIA"], divider=True)
        table.add_row([5, "TABELA PRIMITIVA"], divider=True)
        table.add_row([6, "ROL"], divider=True)
        table.add_row([7, "EXIBIR DISTRIBUIÇÃO ESTATÍSTICA(n, k, h, hi, Lmin, Lmax)"], divider=True)
        print(table)
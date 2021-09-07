
class Data:

    def __init__(self, dia, mes, ano):
        self.dia = str(dia)
        self.mes = str(mes)
        self.ano = str(ano)

    def formata_data(self):
        print(self.dia + "/" + self.mes + "/" + self.ano)
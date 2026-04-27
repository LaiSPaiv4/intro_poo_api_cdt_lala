print("\nDesafio 4: Status de Bateria (Lógica + Erros)\n")

class Celular:

    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo

    def verificar_status(self):

        try:
            entrada = input(f"bateria do {self.modelo}:")
            nivel = float(entrada)
            if nivel < 0 or nivel > 100:
                print("Valor inválido! Digite de 0 a 100.")
            elif nivel < 15:
                print(f"bateria em {nivel}%! Carregue já.")
            elif nivel > 85:
                print(f"Bateria em {nivel}%. Carga excelente!")
            else:
                print(f"Bateria em {nivel}%. Status normal.")
        except ValueError:
            print("Erro: Digite apenas números!")


cel = Celular("Samsung", "S25")
cel.verificar_status()

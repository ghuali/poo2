class Transporte:
    def __init__(self,ruedas:int,asientos:int) -> None:
        self.ruedas = ruedas
        self.asientos = asientos

    def desplazar(x:str,y:str) -> None:
        print("Estas en",x,"y vas a",y)
    def information(self):
        print(self.ruedas,self.asientos)
class Guagua(Transporte):
    pass


if __name__ == "__main__":
    Intercity = Guagua
    LanzaroteBus = Guagua

    Intercity.ruedas = 8
    Intercity.asientos = 50
    Intercity.desplazar("Arrecife","Orzola")
    Intercity.information(Intercity)

    LanzaroteBus.ruedas = 6
    LanzaroteBus.asientos = 30
    LanzaroteBus.desplazar("Arrecife","Tías")
    LanzaroteBus.information(LanzaroteBus)
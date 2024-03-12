class Vehiculos:
    def __init__(self,ruedas:int,color:str):
        self.ruedas = ruedas
        self.color = color

    def info(self):
        print(self.ruedas,self.color)
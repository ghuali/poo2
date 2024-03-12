from Automovil import Automoviles
from Bicicleta import Bicicletas
from Camion import Camiones
from Motocicleta import Motocicletas

if __name__ == "__main__":
    coche = Automoviles(4,"rojo")
    HiperCamion = Camiones(8,"Amarillo")
    bici = Bicicletas(2,"verde")
    moto = Motocicletas(3,"Azul")

    coche.info()
    HiperCamion.info()
    bici.info()
    moto.info()
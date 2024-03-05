### Parámetro posicional
def tipicaFuncion(unpar:int,dospar:int) ->None:
    pass

tipicaFunción(3, 6)
#unpar = 3
#dospar = 6


### Parámetro con valor por defecto
def tipicaFuncion(unpar:int, dospar = 6:int) ->None:
    pass

tipicaFuncion(3)
#unpar = 3
#dospar = 6


### Parámetro arbitrario
def tipicaFuncion(unpar:int, dospar:str, content:int)->str:
    pass

tipicaFuncion(3, 6, 6, 6,content=3)

### Parámetro nominal
def tipicaFuncion(unpar:in,dospar:int) ->None
    pass

tipicalFuncion(dopspar = 6, unpar=3)

unpar = 3
dospar = 6


### Ejercicio 3 
def myDiv(id:str, *clas:str, content:str)->
    resultado=' ''
    resultado += '< div id=20 + id + '"'
    if len(clas) != 0:
        resultado += 'class = "'

        fore e in clas:
            resultado += e + ','

        resultado += '\b"'

    resultado += '>0 + content + '</div>' 
    resultado return

def main():
    print(myDiv("midiv","but_h1","row","clear",content="Lorem ipsum"))


### Ejercicio 5

def myScrip(*src:src)->Str:
Funcion que tuene como entrada un numero indeterminado de cadena de caracteres y como salida una cadena de caracteres. Probablemente transforma las entradas y la salida
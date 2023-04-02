espac = 0
longitudCaracteres = 0
lineaFinal = ""

def troncoInicio(espacio):
    a = 1
    lineaIzq = ""
    lineaDer = ""

    for i  in range(6):
        for i in range(espacio):
            lineaIzq += " "

        for i in range(a):
            lineaDer += str(i)
            lineaIzq += str(i) 
    
        print(lineaIzq + lineaDer)

        global longitudCaracteres

        longitudCaracteres = len(lineaDer)

        lineaIzq = ''
        lineaDer = ''
        espacio -= 1
        a += 1

    global espac

    espac = espacio


def tronco():
    linea = ""

    for i in range(longitudCaracteres*2):
        linea += str(i)

    for i in range(espac):
        linea = " " + linea

    aux = linea

    for i in range(6):
        if i == 1:
            linea = linea.replace("45678","     ")
    
        if i == 2:
            linea = linea.replace("3456789","       ")

        if i == 3:
            linea = linea.replace("3456789","       ")

        if i == 4:
            linea = linea.replace("45678","     ")

        print(linea)
        linea = aux

        global lineaFinal
        lineaFinal = aux

def troncoFinal():
    lineaIzq = ""
    lineaDer = ""

    global espac
    global longitudCaracteres

    for i  in range(4):
        for i in range(espac + 1):
            lineaIzq += " "

        for i in range(longitudCaracteres):
            lineaDer += str(i)
            lineaIzq += str(i) 
    
        print(lineaIzq + lineaDer)

        lineaIzq = ''
        lineaDer = ''
        espac += 1
        longitudCaracteres -= 1

def base():
    global lineaFinal
    for i in range (3):
        lineaFinal = lineaFinal.replace("01", " ")
        lineaFinal = lineaFinal.replace("234567891 1", "")
        lineaFinal = lineaFinal.removesuffix("11")
        print(lineaFinal + "012345678910")

    cantLetras = 4
    letras = ""
    letrasAux = ""
    espacios = 17

    for i in range(4):
        for i in range(espacios):
            letras+= " "

        for i in range(cantLetras):
            letras+= str(i)
            letrasAux += str(i)

        print(letras + letrasAux)
        letras = ""
        letrasAux = ""
        cantLetras -= 1
        espacios += 1

troncoInicio(20)
tronco()
troncoFinal()
base()

for i in range(3):
    print()
    print("   !!!!!!! AL INFINITO Y MAS ALLA !!!!!!")
    print()
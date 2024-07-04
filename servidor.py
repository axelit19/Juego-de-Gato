import socket,random

Usuario="192.168.100.7" #Importante favor de cambiar este usuario por su direccion ip o localhost
Puerto=1234 #Este puerto puede ser cambiando, por favor cambiar tambien en el cliente.py para correr asi el programa

Gato_a=[["_","_","_"], #Definimos una matriz de 3x3 inicializandola con espacios vacios
        ["_","_","_"],
        ["_","_","_"]]
#Metodo que imprime una matriz
#No recibe parametros
def imprimematriz(): 
    print("La matriz es la siguiente")
    for i in range (len(Gato_a)):
        for j in range(len(Gato_a[i])):
            print("\t",Gato_a[i][j],end=" ")
        print()

#Metodo que convierte la matriz en una cadena para poder pasarla por el metodo sendell del socket 
#Para que pueda ser imprimida por el cliente        
def obtenermatrizSocket():
    resultado=""
    for i in range(len(Gato_a)):
        for j in range(len(Gato_a[i])):
            resultado += f"\t{Gato_a[i][j]}"
        resultado += "\n"
    return resultado.encode()

#Metodo que selecciona una posicion aleatoria en el tablero de Gato, dicha posicion es la de la maquina
#Recibe como parametros la matriz, e un simbolo
def gatoposicionMaquina(Gato_a,simbolo):
    while True:
        imprimematriz()
        x1=random.randint(0,2)
        y1=random.randint(0,2)
        if x1 not in range(3) or y1 not in range(3):
            print("Coordenas fuera del rango")
            continue
        if Gato_a[x1][y1] =="_":
            Gato_a[x1][y1]=simbolo
            break
        else:
            print("Existe un simbolo ya aqui")
            continue
    
#Metodo que verifica si hay un ganador verticalmente
#Recibe como parametro un simbolo, una j que se iniciliza en cero y una variable en false para regresar true
#si se encontro la palabra en vertical
def verificaVertical(simbolo, j,variable):
    variable=False
    for i in range (3):
        if Gato_a[i][j]==simbolo and Gato_a[i][j+1]==simbolo and Gato_a[i][j+2]==simbolo:
            variable=True
    return variable

#Metodo que verifica si hay un ganador horizontalmente
#Recibe como parametro un simbolo, una j que se iniciliza en cero y una variable en false para regresar true
#si se encontro la palabra en horizontal
def verificaHorizontal(simbolo,i,variable):
    variable=False
    for j in range(3):
        if Gato_a[i][j]==simbolo and Gato_a[i+1][j]==simbolo and Gato_a[i+2][j]==simbolo:
            variable=True
    return variable

#Metodo que verifica si hay un ganador en diagonal verifica las dos unicas diagonales que puede haber
#Recibe como parametro un simbolo que es el se buscara           
def verificaDiagonal(simbolo):
    i=0
    j=0
    variableuno=False
    variabledos=False
    if Gato_a[i][j]==simbolo and Gato_a[i+1][j+1]==simbolo and Gato_a[i+2][j+2]==simbolo:
        variableuno=True

    j2=2
    if Gato_a[i][j2]==simbolo and Gato_a[i+1][j2-1]==simbolo and Gato_a[i+2][j2-2]==simbolo:
        variabledos=True

    return variableuno or variabledos
#Metodo que posiciona la entrad del cliente en el tablero de Gato
#Recibe como parametro el tablero de Gato, la posicion x y y, si esta fuera del rango pide otro vez la posicion  
def gatoposicion(Gato_a,simbolo,x1,y1):
        imprimematriz()
        if x1 not in range(3) or y1 not in range(3):
            print("Coordenas fuera del rango, por favor ingresa otra opcion")
            return False
        if Gato_a[x1][y1] =="_":
            Gato_a[x1][y1]=simbolo
            return True
        else:
            print("Existe un simbolo ya aqui")
            print("Ingresa otra opcion por favor")
            return False
            #
#Aqui implementamos nuestro servidor, creamos nuestro socket e implementamos la partida de juego
#Establecemos un ciclo mientras se mantenga la conexion para establecer el juego, primero colocando los metodos de la maquina
#Rompemos el ciclo cuando gana la maquina o el usuario, implementamos un while True, para validar correctamente los datos ingresados por
#el usuario        
with socket.socket() as conexion:
    conexion.bind((Usuario,Puerto))
    conexion.listen()
    cliente, puerto=conexion.accept()
    with cliente:
        print(f"Esta conectado el cliente: {puerto}")
        while True:
            gatoposicionMaquina(Gato_a,"Y")
            para1=verificaVertical("Y",0,False)
            para2=verificaDiagonal("Y")
            para3=verificaHorizontal("Y",0,False)
            if(para1 or para2 or para3):
                print("Lo siento perdiste")
                break
            while True:
                matrizsocket=obtenermatrizSocket()
                cliente.send(b"Dame las coordenas de tu punto deseado\n")
                cliente.sendall(matrizsocket)
                informacion=cliente.recv(1024)
                try:
                    x,y= map(int,informacion.decode().split(','))
                    continua=gatoposicion(Gato_a,"X",x,y)
                    if(continua):
                        break
                    else:
                        continue
                except Exception as e:
                    print("Ocurrio un excepcion")
                    print(e)
                    continue    
            para3=verificaVertical("X",0,False)
            para4=verificaDiagonal("X")
            para5=verificaHorizontal("X",0,False)
            if(para3 or para4 or para5):
                print("Felicidades Ganaste :) ")
                break





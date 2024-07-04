import socket

Host="192.168.100.7" #Por favor cambiar esta direccion con el usuario de servidor
Puerto=1234 #De igual forma cambiar el puerto al del servidor
#Metodo que pregunta la posicion x que se pondra en el tablero de juego, utiliza una excepcion, e regresa la variable x
def preguntausariox():
    while True:
        try:
            print("Ingresa la posicion x de donde deseas poner la letra")
            x=int(input()) 
            if x<0 or x>2:
                print("Ingresa un parametro valido")
            else:
                return x
        except ValueError:
            print("Ingresa una entrada valida de 0 a 2")
#Metodo que pregunta la posicion y que se pondra en el tablero de juego, utiliza una excepcion y ciclo para validar la posicion del usuario
def preguntausarioy():
    while True:
        try:
            print("Ingresa la posicion x de donde deseas poner la letra")
            y=int(input()) 
            if y<0 or y>2:
                print("Ingresa un parametro valido")
            else:
                return y
        except ValueError:
            print("Ingresa una entrada valida de 0 a 2")

#Aqui se implenta el socket de usuario, se establece la conexion e mientras esta se true, se pregunta la posicion en le tablero e se imprime el tablero
with socket.socket() as usuario:
    usuario.connect((Host,Puerto))
    while True:
        x=preguntausariox()
        y=preguntausarioy()
        mensaje=f"{x},{y}".encode()
        usuario.sendall(mensaje)
        print("\n")
        informacion=usuario.recv(1024)
        matriz=informacion.decode()
        print(matriz)
        print(f"Received{informacion!r}")


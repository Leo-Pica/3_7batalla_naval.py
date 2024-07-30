#Se nos pide crear un juego donde en una matriz de 5 x 5 se coloquen 3 números 1 que representen barcos y se 
#ubiquen al azar.Los demás esapcios serán ocupados por 0 que representarán  el agua.
# Se le irán solicitando al usuario coordenadas de x e y entre 0 y 4 (matriz es 5 x 5). Si en las coordenadas elegidas
# hay un 0 se mostrará un aviso que diga "¡Tu disparo dió en el agua! " y si da a un barco (1) "¡Hundiste un barco!".
# Al derribar los 3 barcos terminará el juego.

import numpy as np # numpy es una librería que proporciona herramientas para manejar matrices entre otras cosas. 
#Si no lo tenemos instalado escribimos en el terminal: "pip install numpy"

# Crear el tablero de juego de 5x5 con ceros
def crear_tablero(): #Definimos la función crear_tablero
    return np.zeros((5, 5), dtype=int) #Crea y devuelve una matriz de 5 x 5 llena de ceros, representando el tablero
#vacío.Con dtype=int le decimos que vamos a trabajar con enteros.

# Colocar tres barcos en posiciones aleatorias en el tablero
def colocar_barcos(tablero):#Defiimos la función colocar_barcos.(tablero) es la variable que representa
    # el valor que se pasará a la función cuando se la llame (el parámetro).
    barcos_colocados = 0# Inicializamos un contador de barcos colocados en 0.
    while barcos_colocados < 3:#Continúa hasta que se hallan colocado 3 barcos
        x = np.random.randint(0, 5)#Ésta función de NumPy nos genera números aleatorios enteros que se 
        #asignan a x. Los parámetros van de 0 (primero) hasta 5(excluído). O sea que x recibe enteros del 0 al 4.
        y = np.random.randint(0, 5)#Hace lo mismo que la línea anterior pero en y.
        if tablero[x, y] == 0:  # Verificar si la posición está vacía. 
            tablero[x, y] = 1 #Colocar un barco en la posición.
            barcos_colocados += 1 #Si hay un 1 se incrementa el contador de barcos en 1.

# Función para verificar si una coordenada dada golpea un barco o cae en el agua
def verificar_disparo(tablero, x, y): #Creamos la función cuyos parámetros son (tablero, x , y)
    if tablero[x, y] == 1:#Verifica si hay un barco en la posición dada.
        print("¡Hundiste un barco!") #Muestra mensaje de acierto.
        tablero[x, y] = 0  # Hundir el barco, es decir marcar posición como vacía (por eso pomenos =0) 
        return True #Devuelve true indicando que el disparo fue acertado
    else:
        print("¡Tu disparo dió en el agua!")#Muestra mensaje de fallar
        return False #Devuelve falso indicando que el disparo fue fallado.

# Función para contar el número de barcos restantes
def contar_barcos(tablero): #definimos la función contar_barcos con el parámetro(tablero)
    return np.sum(tablero) #Cuenta y devuelve el número de barcos restantes en el tablero
#sumando todos los valores de la matriz.

# Función principal para jugar
def jugar():
    tablero = crear_tablero() #Crea un tablero de juego
    colocar_barcos(tablero) #Coloca los barcos en el tablero.
    print("¡Bienvenido a Batalla Naval!")#Mensaje de bienvenida
    print("El tablero de juego es de 5x5.")#Informa sobre el tamaño del tablero

    barcos_restantes = 3 #Inicializa el contador de barcos restantes

    while barcos_restantes > 0:#Continúa el juego mientras queden barcos
        try:
            x = int(input("Introduce la coordenada x (0-4): "))#Solicita y convierte la coordenada x ingresada por el usuario.
            y = int(input("Introduce la coordenada y (0-4): "))#Solicita y convierte la coordenada y ingresada por el usuario.
        except ValueError:#Maneja errores de entrada.Esto es por si el usuario ingresa un dato fuera de lo solicitado (de 0 a 4)
            print("Por favor, introduce números enteros válidos.")#Informa al usuario si los números ingresados están fuera del rango.
            continue
        
        if x < 0 or x > 4 or y < 0 or y > 4: #Comparamos que los datos están dentro de lo solicitado (x menor a 0 o mayor a 4
            #lo mismo para y)
            print("Coordenadas fuera de rango. Intenta nuevamente.")
            continue

        if verificar_disparo(tablero, x, y):#Verifica si el disparo fue un acierto.
            barcos_restantes -= 1 #Decrementa el contador de barcos restantes. 
            print(f"Barcos restantes: {barcos_restantes}") #Informa al usuario sobre el número de barcos resstantes.
        
        if barcos_restantes == 0: #Verifica si no quedan barcos restantes.
            print("¡Felicitaciones! Hundiste todos los barcos.") #Mensaje de victoria.

jugar() #Inicia el juego.

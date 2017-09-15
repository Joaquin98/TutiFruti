import random,os,platform


'''
CARACTERISTICAS:
- Solo se permiten entre 2 y 5 jugadores.
- Se termina el juego cuando algun jugador llega a 200 puntos o cuando se queda sin letras.
- No se permite ingresar dos palabras iguales para distintas categorias (a un mismo jugador).
- Se considera que una palabra es valida cuando empieza con la letra pedida.
'''


# -----------------------------------------------------------
#                  FUNCIONES AUXILIARES
# -----------------------------------------------------------


# Retorna True en caso de que la palabra sea valida, 
# (si empieza con la letra pasada como parametro), 
# en caso contrario retorna False.
# esValida : String , String -> Bool
def esValida(palabra,letra):
	return palabra != "" and palabra[0].upper() == letra

# Toma un numero, y retorna True en caso de que este entre 2 y 6 sin incluir.
# En caso contrario retorna False.
# cantJugadoresValida : Int -> Bool
def cantJugadoresValida(cantJugadores):
	return cantJugadores < 6 and cantJugadores > 1

# Retorna una lista con los caracteres ASCII desde el 65 al 90.
# Los cuales son A,B,...,Z
# abecedarioLista : None -> StringList
def abecedarioLista():
	return [chr(ordenada) for ordenada in range(65,91)]

# Toma una lista de letras y retorna una letra aleatoria, eliminandola
# de la lista.
# letraAleatoria : StringList -> String 
def letraAleatoria(abc):
	letra = abc[random.randint(0,len(abc)-1)]
	abc.remove(letra)
	return letra

# Los numeros representan los puntajes de los jugadores.
# Toma una lista de numeros y devuelve el mayor de ellos.
# buscarMayor : IntList -> Int 
def buscarMayor(lista):
	i , long = 0 , len(lista)
	mayor = -1
	while i < long:
		if lista[i] > mayor:
			mayor = lista[i]
		i += 1
	return mayor

# Toma una lista con los puntajes, y el mayor de esos puntajes
# y retorna una lista de indices de donde se encuentran ese mayor 
# o los mayores (que representarian los numeros de los jugadores que ganaron).
# indicesGanadores : IntList , Number -> IntList
def indicesGanadores(lista,mayor):
	indices = []
	i , long = 0 , len(lista)
	while i < long:
		if mayor == lista[i]:
			indices.append(i)
		i+=1
	return indices

# Toma una palabra y una letra, si la palabra es valida retorna
# la misma palabra, en caso contrario devuelve una cadena vacia.
# filtrarValidas : String , String -> String
def filtrarValidas(palabra,letra):
	if esValida(palabra,letra):
		return palabra
	else :
		return ""



# Toma las palabras escritas por todos los jugadores, para una determinada letra
# y siguiendo las normas del enunciado, le suma los puntos correspondientes a cada jugador.
# sumarPuntosRonda : IntList , List of StringList -> None
def sumarPuntosRonda(puntajes,listaNombres):
	for categoria in listaNombres:
		numeroJugador, validas, indices = 0, [], [] 
		cantJugadores = len(categoria)
		while numeroJugador < cantJugadores:
			if categoria[numeroJugador] != "":
				validas.append(categoria[numeroJugador])
				indices.append(numeroJugador)
			numeroJugador += 1
		if len(validas) == 1:
			puntajes[indices[0]] += 20
		else :
			for i , palabra in enumerate(validas):
				if (palabra in validas[:i]) or (palabra in validas[i+1:]):
					puntajes[indices[i]] += 5
				else :
					puntajes[indices[i]] += 10



# -----------------------------------------------------------
#        INGRESO POR TECLADO E INFORMACION POR PANTALLA
# -----------------------------------------------------------

# Limpia la pantalla de la Terminal.
def limpiarPantalla():
	aux = "clear"
	if(platform.system() == "Windows"): aux = "cls"
	os.system(aux)

# La funcion pide el ingreso de la cantidad de jugadores, y luego pide
# el ingreso de los nombres de cada jugador. Retornando una lista con los
# nombres de todos los jugadores.
# ingresoJugadores : None -> StringList
def ingresoJugadores():

	jugadores = []
	cantJugadores = 6
	limpiarPantalla()
	cantJugadores = int(input("Ingrese la cantidad de jugadores: "))
	while not cantJugadoresValida(cantJugadores):
		limpiarPantalla()
		print("Cantidad de jugadores invalida!")
		cantJugadores = int(input("Ingrese la cantidad de jugadores: "))

	for numeroJugador in range(0,cantJugadores):
		os.system("clear")
		print("Ingrese el nombre del jugador",numeroJugador+1,":")
		jugadores.append(input())

	return jugadores

# Dada una lista de jugadores, lista de categorias, una lista de listas
# (que sera el tablero a completar) y la letra de la ronda actual, pide
# a los jugadores el ingreso de las palabras. Si un jugador intenta
# repetir una palabra, es advertido y se le pide ingresar una distinta.
# rellenarTablero : StringList , StringList , List of List , String -> None
def rellenarTablero(jugadores,categorias,listaNombres,letraActual):
	for indiceJugador , nombreJugador in enumerate(jugadores):
		recienIngresadas = []
		for indiceCategoria , categoria in enumerate(categorias):
			limpiarPantalla()
			print("Turno de",nombreJugador)
			print(categoria,"con la letra",letraActual,":")
			palabra = input().upper()
			if palabra != "":
				while palabra in recienIngresadas:
					print("Ya utilizaste esa palabra, ingresa otra : ")
					palabra = input().upper()

			recienIngresadas.append(palabra)
			listaNombres[indiceCategoria].append(filtrarValidas(palabra,letraActual))



# Toma los puntajes de cada jugador, analiza quien/es son los
# ganadores y lo muestra en pantalla.
# resultados : IntList , StringList -> None
def resultados(puntajes,jugadores):

	mayor = buscarMayor(puntajes)
	ganadores = indicesGanadores(puntajes,mayor)
	cantGanadores = len(ganadores)
	textoFinal = "El ganador es :" if cantGanadores == 1 else "Los ganadores son :"
	
	for indice in ganadores :
		textoFinal += " " + jugadores[indice] + " ,"
 
	print(textoFinal[:len(textoFinal)-1])

# Toma los puntajes de cada jugador, y muestra por pantalla los
# puntajes de cada jugador.
# resultados : IntList , StringList -> None
def finalDeRonda(jugadores,puntajes):
	limpiarPantalla()
	print("--- Ha finalizado la ronda ---\nPuntajes hasta el momento:")
	i,l = 0,len(jugadores)
	while i < l:
		print(jugadores[i]," ----> ",puntajes[i],"Puntos.")
		i+=1
	input()


# -----------------------------------------------------------
#                          JUEGO
# -----------------------------------------------------------


# Es la funcion principal que organiza el juego.
def comenzarJuego():
	abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	categorias = ["Personas","Colores","Animales","Comidas","Flores","Frutas","Paises"]
	jugadores = ingresoJugadores()
	cantCategorias,cantJugadores,maxPuntos = len(categorias), len(jugadores), 200 
	puntajes = [0] * cantJugadores
	tableros = {}
	finDelJuego = False

	while not finDelJuego:

		letraActual = letraAleatoria(abc)
		tableros[letraActual] = [[] for i in range(0,cantCategorias)]

		rellenarTablero(jugadores, categorias, tableros[letraActual],letraActual)

		sumarPuntosRonda(puntajes,tableros[letraActual])

		finalDeRonda(jugadores,puntajes)


		if buscarMayor(puntajes) >= maxPuntos or len(abc) == 0:
			finDelJuego = True

	
	limpiarPantalla()
	resultados(puntajes,jugadores)


if __name__ == "__main__":
	comenzarJuego()
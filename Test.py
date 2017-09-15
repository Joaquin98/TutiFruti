import TP

def test_esValida():
	assert TP.esValida("hola","H") == True
	assert TP.esValida("Hola","H") == True
	assert TP.esValida("","H") == False
	assert TP.esValida("h","H") == True
	assert TP.esValida(" hola","H") == False
	assert TP.esValida("chau","C") == True
	assert TP.esValida("chau","J") == False
	assert TP.esValida("Chau","J") == False

def test_cantJugadoresValida():
	assert TP.cantJugadoresValida(-3) == False
	assert TP.cantJugadoresValida(1) == False
	assert TP.cantJugadoresValida(2000) == False
	assert TP.cantJugadoresValida(6) == False
	assert TP.cantJugadoresValida(5) == True
	assert TP.cantJugadoresValida(2) == True

def test_letraAleatoria():
	inicial , listaLetras = ["A","B","C","D"] , ["A","B","C","D"] 
	r = []
	i,l = 0,len(listaLetras)
	while i < l :
		r.append(TP.letraAleatoria(listaLetras))
		i += 1
	r.sort()
	assert r == inicial

def test_buscarMayor():
	assert TP.buscarMayor([1,2,3,4,5,6]) == 6
	assert TP.buscarMayor([13,3,543,5,1234,2,53,41,-2142,241,0,-123]) == 1234
	assert TP.buscarMayor([0,0,0,0,0,0]) == 0
	assert TP.buscarMayor([898,436,234,123,1,1,1,1]) == 898


def test_indicesGanadores():
	assert TP.indicesGanadores([1,2,3,4,5,2,3,5],5) == [4,7]
	assert TP.indicesGanadores([0,0,0,0,0],0) == [0,1,2,3,4] 
	assert TP.indicesGanadores([213,34223,35,432],34223) == [1]
	assert TP.indicesGanadores([1,23,5],1000) == []

def test_filtrarValidas():
	assert TP.filtrarValidas("juan","P") == ""
	assert TP.filtrarValidas("hola","H") == "hola"
	assert TP.filtrarValidas("","H") == ""
	assert TP.filtrarValidas("hola","J") == ""
	assert TP.filtrarValidas("habia","H") == "habia"

def test_sumarPuntosRonda():
	init = [0,0]
	ingresos = [["","Abc"],["Abd","Abd"],["Abe","Acb"],["",""]]
	TP.sumarPuntosRonda(init, ingresos)
	assert init == [15,35]


def test_ingresoJugadores():
	listaInput = ["1","6","2","Juan","Pepe"]
	listaInput.reverse()
	TP.input = lambda x=None: listaInput.pop()
	assert TP.ingresoJugadores() == ["Juan","Pepe"]


def test_rellenarTablero():
	listaNombres = [[],[],[],[],[],[],[]]
	lista = ["Andres","Amarillo","Mono","Azado","Amelia","Anana","Argentina","Adam","Azul","Oso","Azado","Amarilla","Anana","Alemania"]
	lista.reverse()
	TP.input = lambda: lista.pop()
	TP.rellenarTablero(["Juan","Pepe"], ["Personas","Colores","Animales","Comidas","Flores","Frutas","Paises"],listaNombres,"A")
	assert listaNombres == [['ANDRES', 'ADAM'], ['AMARILLO', 'AZUL'], ['', ''], ['AZADO', 'AZADO'], ['AMELIA', 'AMARILLA'], ['ANANA', 'ANANA'], ['ARGENTINA', 'ALEMANIA']]

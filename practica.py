from typing import Any, List
from collections import deque

class GrafoMatriz:

  def __init__(self):
    self.matrizAdy : List[List[int]] = []
    self.vertices : List[Any] = [] ## Lista con los nodos
    self.tamano : int = 0

  def agregarVertice(self, valor: any): ## Agrega el nodo pero desconectado
    if valor in self.vertices: ## Si el valor ya estaba agregado no hace nada mas
      return None
    self.vertices.append(valor) ## Agrega el vertice a lista de vertices
    self.tamano = self.tamano + 1 ## Incrementa el tamaño del grafo

    for fila in self.matrizAdy:
      fila.append(0) ## Agrega una fila de ceros
    self.matrizAdy.append([0] * self.tamano) ## Agrega una columna de ceros

  def agregarConexion(self, vertice1, vertice2, dirigido = False, peso = 1):
    if vertice1 not in self.vertices:
      self.agregarVertice(vertice1)
    if vertice2 not in self.vertices:
      self.agregarVertice(vertice2)

    posV1 = self.vertices.index(vertice1) ## Entrega la posicion de el vertice 1 en la matriz de ady
    posV2 = self.vertices.index(vertice2) ## Entrega la posicion del vertice 2 en la matriz de adyacencia

    self.matrizAdy[posV1][posV2] = peso ## Hay un camino entre v1 y v2

    if not dirigido: ## Si no es dirigido debo agregar la relacion contraria
      self.matrizAdy[posV2][posV1] = peso

  def recorrerEnAnchura ( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.vertices: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    cola = deque([verticeInicial])  ## Cola de pendientes por visitar
    while cola:  ## Mientras que tenga vertices pendientes por visitar
      vertice = cola.popleft()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        posicionVertice = self.vertices.index(vertice)  ## Obtengo la fila dentro de la matriz en la cual debo buscar los vecinos
        for i in range(self.tamano):  ## Recorrer la matriz ady para buscar vertices relacionados
          if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados: ## Si encuentro un vertice relacionado y que no ha sido visitado
            cola.append(self.vertices[i])  ## Agrego ese vertice a la cola de pendientes por visitar
    return visitados

  def recorrerEnProfundidad( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.vertices: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    pila = [verticeInicial]  ## Pila de pendientes por visitar
    while pila:  ## Mientras que tenga vertices pendientes por visitar
      vertice = pila.pop()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        posicionVertice = self.vertices.index(vertice)  ## Obtengo la fila dentro de la matriz en la cual debo buscar los vecinos
        for i in range(self.tamano - 1, -1, -1):  ## Recorrer la matriz ady para buscar vertices relacionados (Se recorre en sentio inverso)
          if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados: ## Si encuentro un vertice relacionado y que no ha sido visitado
            pila.append(self.vertices[i])  ## Agrego ese vertice a la cola de pendientes por visitar
    return visitados


  def encontrarCaminoMasCorto(self, verticeInicial : Any, verticeFinal : Any) -> tuple:
    if verticeInicial not in self.vertices or verticeFinal not in self.vertices:
      ## Si alguno de los 2 vertices no existe
      return (float('inf'), [])

    ## Crea un diccionario donde inicalmente todas las distancias son infinitas
    distancias = { vertice : float('inf') for vertice in self.vertices }
    ## La distancia al vertice inicial es la unica que se conoce con antelacion
    distancias[verticeInicial] = 0

    ## Crea un diccionario donde inicalmente todas las distancias son infinitas
    predecesores = { vertice : None for vertice in self.vertices }

    visitados = [] ## Lista donde almacenaremos los vertices cuando los hayamos visitado

    verticeActual = verticeInicial

    ## Mientras que el vertice actual sea un nodo valido y sea diferente al vertice final
    while verticeActual is not None and verticeActual != verticeFinal:
      ## Consultar todos los vecinos del vertice actual que no he visitado
      vecinosNoVisitados = []
      posicionVertice = self.vertices.index(verticeActual)
      for i in range(self.tamano):
        if self.matrizAdy[posicionVertice][i] != 0 and self.vertices[i] not in visitados:
          vecinosNoVisitados.append(self.vertices[i])
      ## Actualizar los recorridos de la mejor ruta conocida
      for vecino in vecinosNoVisitados:
        ## Busca en la matriz de ady el peso de la conexion entre el vertice actual y el vecino no visitado
        pesoConexion = self.matrizAdy[posicionVertice][self.vertices.index(vecino)]
        ## acumula la mejor distancia conocida con la conexion actual
        distancia = distancias[verticeActual] + pesoConexion
        ## Si encontre una distancia menor a la que tenia registrada como mejor distancia conocida
        if distancia < distancias[vecino]:
          distancias[vecino] = distancia ## Actualizo mi nueva mejor distancia
          predecesores[vecino] = verticeActual ## Actualizo que la mejor distancia se dio con este predecesor
      visitados.append(verticeActual)

      distanciaMenor = float('inf')
      verticeMenor = None

      for vertice in distancias:
        if distancias[vertice] < distanciaMenor and vertice not in visitados:
          distanciaMenor = distancias[vertice]
          verticeMenor = vertice

      verticeActual = verticeMenor
    caminoMasCorto = []

    if distancias[verticeFinal] == float('inf'):
      return(float('inf'), [])

    pasoActual = verticeFinal

    while pasoActual is not None:
      caminoMasCorto.insert(0, pasoActual)
      pasoActual = predecesores[pasoActual]
    return (distancias[verticeFinal], caminoMasCorto)

  def arbolExpansionMinimo(self) -> tuple:
    if self.tamano == 0:
      return (0, []) ## Si el grafo esta vacio entonces no hay un AEM posible}

    verticesVisitados = [ self.vertices[0] ] ## Empiezo visitando el primer vertice del grafo segun su aparicion en la matriz
    conexionesArbol = [] ## Lista con todas las conexiones que hacen parte del arbol
    pesoTotal = 0 ## Acumular la longitud del AEM

    while len(verticesVisitados) < self.tamano: ## La cantidad de vertices visitados
      pesoMasBajo = float('inf')
      origenElegido = None
      destinoElegido = None

      ## Buscar todos los vecinos no visitados de los nodos del AEM
      for vertice in verticesVisitados: ## Para cada vertice en los vertices visitados
        indiceFila = self.vertices.index(vertice) ## Consultamos la fila en la cual debemos buscar los vecinos

        for indice in range(self.tamano): ## Recorremos la fila desde la posicion inicial hasta el final
          verticeEvaluado = self.vertices[indice]
          pesoEvaluado = self.matrizAdy[indiceFila][indice]

          if pesoEvaluado != 0 and verticeEvaluado not in verticesVisitados: ## Validamos que el V Evaluado sea un vecino y que ademas no haya sido visitado
            if pesoEvaluado < pesoMasBajo: ## Si el vecino evaluado es el mejor vecino hasta el momento
              pesoMasBajo = pesoEvaluado
              origenElegido = vertice
              destinoElegido = verticeEvaluado
      verticesVisitados.append(destinoElegido) ## Como en destino elegido me quedo el mejor vecino entonces lo visito
      conexionesArbol.append((origenElegido,destinoElegido, pesoMasBajo))
      pesoTotal = pesoTotal + pesoMasBajo

    return (pesoTotal, conexionesArbol)






from typing import Any, List, Dict
from collections import deque

class GrafoLista:

  def __init__(self):
    self.listaAdy : Dict[Any, List[Any]] = {}
    self.tamano : int = 0

  def agregarVertice(self, valor: any): ## Agrega el nodo pero desconectado
    if valor in self.listaAdy: ## Si el valor ya estaba agregado no hace nada mas
      return None
    self.listaAdy[valor] = []
    self.tamano = self.tamano + 1 ## Incrementa el tamaño del grafo

  def agregarConexion(self, vertice1, vertice2, dirigido = False, peso = 1):
    if vertice1 not in self.listaAdy: ## Validamos si v1 aun no existe y en ese caso se manda crear
      self.agregarVertice(vertice1)
    if vertice2 not in self.listaAdy:## Validamos si v2 aun no existe y en ese caso se manda crear
      self.agregarVertice(vertice2)

    vecinosVertice1 = [] ## Encontrar los vecinos que ya tiene registrados el v1
    for vertice in self.listaAdy[vertice1]:
      vecinosVertice1.append(vertice[0])

    if vertice2 not in vecinosVertice1: ## Solo agrego la conexion en caso de que no exista previamente
      self.listaAdy[vertice1].append((vertice2, peso))

    if not dirigido: ## Si no es dirigido se debe crear la relacion inversa

      vecinosVertice2 = [] ## Encontar los vecinos que ya tiene registrados el v2
      for vertice in self.listaAdy[vertice2]:
        vecinosVertice2.append(vertice[0])

      if vertice1 not in vecinosVertice2: ## Solo agrego la conexion en caso de que no exista previamente
        self.listaAdy[vertice2].append((vertice1, peso))

  def recorrerEnAnchura ( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.listaAdy: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    cola = deque([verticeInicial])  ## Cola de pendientes por visitar
    while cola:  ## Mientras que tenga vertices pendientes por visitar
      vertice = cola.popleft()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        for vecino, peso in self.listaAdy[vertice]:  ## Recorrer la lista ady para buscar vertices relacionados
          if vecino not in visitados: ## Si el vecino no ha sido visitado
            cola.append(vecino)  ## Agrego ese vecino a la cola de pendientes por visitar
    return visitados

  def recorrerEnProfundidad ( self, verticeInicial : any) -> List[Any] :
    if verticeInicial not in self.listaAdy: ## Validar que el vertice desde el cual quiero empezar efectivamente se encuentre en el grafo
      return [] ## Retorna una lista vacia porque no hay camino posible
    visitados = [] ## Lista que contiene los vertices visitados en el orden apropiado segun el algoritmo
    pila = [verticeInicial]  ## Cola de pendientes por visitar
    while pila:  ## Mientras que tenga vertices pendientes por visitar
      vertice = pila.pop()  ## Tomo el primer vertice que esta en la cola de pendientes
      if vertice not in visitados:  ## Si el vertice que tome de la lista de pendientes no ha sido visitado
        visitados.append(vertice)  ## Lo agrego a lista de visitados
        for vecino, peso in reversed(self.listaAdy[vertice]):  ## Recorrer la lista ady para buscar vertices relacionados
          if vecino not in visitados: ## Si el vecino no ha sido visitado
            pila.append(vecino)  ## Agrego ese vecino a la cola de pendientes por visitar
    return visitados

    """
    ListaAdy = {
         "A": [B, C, E, F],
         "B": [A, D],
         "C": [A, E],
         "D": [B, I],
         "E": [A, C, F, G],
         "F": [A, E],
         "G": [E, H],
         "H": [G],
         "I": [D]
        }
    """

  def encontrarCaminoMasCorto(self, verticeInicial: any, verticeFinal: any) -> tuple:

    # Si el vertice inicial o final no existen en el grafo no hay un camino posible
    if verticeInicial not in self.listaAdy or verticeFinal not in self.listaAdy:
      return (float('inf'), [])

    # Guarda la mejor distancia conocida desde el vértice inicial hasta cada vértice.
    # Al comienzo todas las distancias se dejan en infinito porque todavía no se ha encontrado ningún camino hacia esos vértices.
    distancias = {vertice: float('inf') for vertice in self.listaAdy}

    # La distancia desde el vértice inicial hasta sí mismo es 0.
    distancias[verticeInicial] = 0

    # Lista de vértices ya visitados.
    # Cuando un vértice entra a esta lista significa que ya se revisaron sus vecinos.
    visitados = []

    # Guarda desde qué vértice se llegó a cada vértice usando la mejor distancia.
    predecesores = {vertice: None for vertice in self.listaAdy}

    # El algoritmo comienza revisando el vértice inicial.
    verticeActual = verticeInicial

    while verticeActual is not None and verticeActual != verticeFinal:


      for vecino, peso in self.listaAdy[verticeActual]:

        # Solo se consideran vecinos que todavía no han sido visitados.
        if vecino not in visitados:

          # distancia mínima conocida hasta verticeActual + peso de la conexión desde verticeActual hasta el vecino.
          distancia = distancias[verticeActual] + peso

          # Si la distancia es menor que la distancia guardada para el vecino, se actualiza porque se encontró una ruta más corta.
          if distancia < distancias[vecino]:
            distancias[vecino] = distancia

            # Se registra que la mejor forma conocida de llegar al vecino es pasando primero por verticeActual.
            predecesores[vecino] = verticeActual

      # Después de revisar todas las conexiones del vértice actual, se marca como visitado para no procesarlo de nuevo.
      visitados.append(verticeActual)

      # Se busca el siguiente vértice no visitado con la menor distancia acumulada.

      distanciaMenor = float('inf')
      verticeMenor = None

      for vertice in distancias:
        # El nuevo vértice actual debe ser no visitado y tener la menor distancia conocida hasta el momento.
        if distancias[vertice] < distanciaMenor and vertice not in visitados:
          distanciaMenor = distancias[vertice]
          verticeMenor = vertice

      # Se actualiza el vértice actual con el mejor candidato encontrado.
      verticeActual = verticeMenor

    # Se reconstruye el camino con ayuda de los predecesores.
    camino = []

    # Si la distancia al destino sigue siendo infinita, no existe camino posible.
    if distancias[verticeFinal] == float('inf'):
      return (float('inf'), [])

    # Se empieza desde el vértice final y se va retrocediendo hasta el inicial.
    pasoActual = verticeFinal

    while pasoActual is not None:
      # Se inserta al comienzo para que el resultado quede ordenado desde el origen hasta el destino, sin necesidad de invertir la lista al final.
      camino.insert(0, pasoActual)

      # Se avanza hacia atrás en la ruta usando el predecesor guardado.
      pasoActual = predecesores[pasoActual]

    return (distancias[verticeFinal], camino)



from typing import Any


class GrafoCampus:

    def __init__(self):
        self.listaAdy = {}
        self.tamano = 0

    def agregarVertice(self, valor):

        if valor in self.listaAdy:
            return

        self.listaAdy[valor] = []
        self.tamano += 1

    def agregarConexion(
            self,
            vertice1,
            vertice2,
            distancia,
            tiempo,
            congestion,
            accesible,
            estado='disponible',
            dirigido=False
    ):

        if vertice1 not in self.listaAdy:
            self.agregarVertice(vertice1)

        if vertice2 not in self.listaAdy:
            self.agregarVertice(vertice2)

        conexion = {
            'destino': vertice2,
            'distancia': distancia,
            'tiempo': tiempo,
            'congestion': congestion,
            'accesible': accesible,
            'estado': estado
        }

        self.listaAdy[vertice1].append(conexion)

        if not dirigido:

            conexionInversa = {
                'destino': vertice1,
                'distancia': distancia,
                'tiempo': tiempo,
                'congestion': congestion,
                'accesible': accesible,
                'estado': estado
            }

            self.listaAdy[vertice2].append(conexionInversa)

    def encontrarRuta(self, origen, destino, criterio='distancia'):

        if origen not in self.listaAdy or destino not in self.listaAdy:
            return (float('inf'), [])

        distancias = {
            vertice: float('inf')
            for vertice in self.listaAdy
        }

        distancias[origen] = 0

        visitados = []

        predecesores = {
            vertice: None
            for vertice in self.listaAdy
        }

        verticeActual = origen

        while verticeActual is not None and verticeActual != destino:

            for conexion in self.listaAdy[verticeActual]:

                vecino = conexion['destino']

                if vecino in visitados:
                    continue

                if conexion['estado'] != 'disponible':
                    continue

                if criterio == 'accesible' and not conexion['accesible']:
                    continue

                if criterio == 'distancia':
                    peso = conexion['distancia']

                elif criterio == 'tiempo':
                    peso = conexion['tiempo']

                elif criterio == 'congestion':
                    peso = conexion['congestion']

                elif criterio == 'accesible':
                    peso = conexion['distancia']

                else:
                    peso = conexion['distancia']

                nuevaDistancia = distancias[verticeActual] + peso

                if nuevaDistancia < distancias[vecino]:
                    distancias[vecino] = nuevaDistancia
                    predecesores[vecino] = verticeActual

            visitados.append(verticeActual)

            distanciaMenor = float('inf')
            siguienteVertice = None

            for vertice in distancias:

                if vertice not in visitados:

                    if distancias[vertice] < distanciaMenor:
                        distanciaMenor = distancias[vertice]
                        siguienteVertice = vertice

            verticeActual = siguienteVertice

        if distancias[destino] == float('inf'):
            return (float('inf'), [])

        camino = []
        pasoActual = destino

        while pasoActual is not None:
            camino.insert(0, pasoActual)
            pasoActual = predecesores[pasoActual]

        return (distancias[destino], camino)

    def explicarRuta(self, criterio):

        if criterio == 'distancia':
            return 'La ruta fue seleccionada porque minimiza la distancia total recorrida.'

        elif criterio == 'tiempo':
            return 'La ruta fue seleccionada porque minimiza el tiempo estimado de recorrido.'

        elif criterio == 'congestion':
            return 'La ruta fue seleccionada porque evita las zonas con mayor congestión.'

        elif criterio == 'accesible':
            return 'La ruta fue seleccionada porque solo utiliza caminos accesibles para personas con movilidad reducida.'

        return 'Ruta calculada correctamente.'

    def arbolExpansionMinimo(self):

        if self.tamano == 0:
            return (0, [])

        verticesVisitados = [list(self.listaAdy.keys())[0]]

        conexionesArbol = []

        pesoTotal = 0

        while len(verticesVisitados) < self.tamano:

            mejorPeso = float('inf')
            origenElegido = None
            destinoElegido = None

            for vertice in verticesVisitados:

                for conexion in self.listaAdy[vertice]:

                    if conexion['estado'] != 'disponible':
                        continue

                    vecino = conexion['destino']

                    if vecino not in verticesVisitados:

                        if conexion['distancia'] < mejorPeso:

                            mejorPeso = conexion['distancia']
                            origenElegido = vertice
                            destinoElegido = vecino

            verticesVisitados.append(destinoElegido)

            conexionesArbol.append(
                (
                    origenElegido,
                    destinoElegido,
                    mejorPeso
                )
            )

            pesoTotal += mejorPeso

        return (pesoTotal, conexionesArbol)
    

from typing import Any


class GrafoCampus:

    def __init__(self):
        self.listaAdy = {}
        self.tamano = 0

    def agregarVertice(self, valor):

        if valor in self.listaAdy:
            return

        self.listaAdy[valor] = []
        self.tamano += 1

    def agregarConexion(
            self,
            vertice1,
            vertice2,
            distancia,
            tiempo,
            congestion,
            accesible,
            estado='disponible',
            dirigido=False
    ):

        if vertice1 not in self.listaAdy:
            self.agregarVertice(vertice1)

        if vertice2 not in self.listaAdy:
            self.agregarVertice(vertice2)

        conexion = {
            'destino': vertice2,
            'distancia': distancia,
            'tiempo': tiempo,
            'congestion': congestion,
            'accesible': accesible,
            'estado': estado
        }

        self.listaAdy[vertice1].append(conexion)

        if not dirigido:

            conexionInversa = {
                'destino': vertice1,
                'distancia': distancia,
                'tiempo': tiempo,
                'congestion': congestion,
                'accesible': accesible,
                'estado': estado
            }

            self.listaAdy[vertice2].append(conexionInversa)

    def encontrarRuta(self, origen, destino, criterio='distancia'):

        if origen not in self.listaAdy or destino not in self.listaAdy:
            return (float('inf'), [])

        distancias = {
            vertice: float('inf')
            for vertice in self.listaAdy
        }

        distancias[origen] = 0

        visitados = []

        predecesores = {
            vertice: None
            for vertice in self.listaAdy
        }

        verticeActual = origen

        while verticeActual is not None and verticeActual != destino:

            for conexion in self.listaAdy[verticeActual]:

                vecino = conexion['destino']

                if vecino in visitados:
                    continue

                if conexion['estado'] != 'disponible':
                    continue

                if criterio == 'accesible' and not conexion['accesible']:
                    continue

                if criterio == 'distancia':
                    peso = conexion['distancia']

                elif criterio == 'tiempo':
                    peso = conexion['tiempo']

                elif criterio == 'congestion':
                    peso = conexion['congestion']

                elif criterio == 'accesible':
                    peso = conexion['distancia']

                else:
                    peso = conexion['distancia']

                nuevaDistancia = distancias[verticeActual] + peso

                if nuevaDistancia < distancias[vecino]:
                    distancias[vecino] = nuevaDistancia
                    predecesores[vecino] = verticeActual

            visitados.append(verticeActual)

            distanciaMenor = float('inf')
            siguienteVertice = None

            for vertice in distancias:

                if vertice not in visitados:

                    if distancias[vertice] < distanciaMenor:
                        distanciaMenor = distancias[vertice]
                        siguienteVertice = vertice

            verticeActual = siguienteVertice

        if distancias[destino] == float('inf'):
            return (float('inf'), [])

        camino = []
        pasoActual = destino

        while pasoActual is not None:
            camino.insert(0, pasoActual)
            pasoActual = predecesores[pasoActual]

        return (distancias[destino], camino)

    def explicarRuta(self, criterio):

        if criterio == 'distancia':
            return 'La ruta minimiza la distancia total.'

        elif criterio == 'tiempo':
            return 'La ruta minimiza el tiempo de recorrido.'

        elif criterio == 'congestion':
            return 'La ruta evita zonas congestionadas.'

        elif criterio == 'accesible':
            return 'La ruta solo usa caminos accesibles.'

        return 'Ruta calculada.'

    def arbolExpansionMinimo(self):

        if self.tamano == 0:
            return (0, [])

        verticesVisitados = [list(self.listaAdy.keys())[0]]

        conexionesArbol = []

        pesoTotal = 0

        while len(verticesVisitados) < self.tamano:

            mejorPeso = float('inf')
            origenElegido = None
            destinoElegido = None

            for vertice in verticesVisitados:

                for conexion in self.listaAdy[vertice]:

                    if conexion['estado'] != 'disponible':
                        continue

                    vecino = conexion['destino']

                    if vecino not in verticesVisitados:

                        if conexion['distancia'] < mejorPeso:

                            mejorPeso = conexion['distancia']
                            origenElegido = vertice
                            destinoElegido = vecino

            verticesVisitados.append(destinoElegido)

            conexionesArbol.append(
                (
                    origenElegido,
                    destinoElegido,
                    mejorPeso
                )
            )

            pesoTotal += mejorPeso

        return (pesoTotal, conexionesArbol)        

    

campus = GrafoCampus()

lugares = [
    'Bloque 1',
    'Bloque 2',
    'Bloque 3',
    'Biblioteca',
    'Cafeteria',
    'Teatro',
    'Enfermeria',
    'Parqueadero Norte',
    'Parqueadero Sur',
    'Laboratorio A',
    'Laboratorio B',
    'Zona Deportiva',
    'Administracion',
    'Cancha',
    'Plazoleta Central'
]

for lugar in lugares:
    campus.agregarVertice(lugar)


campus.agregarConexion('Bloque 1', 'Bloque 2', 100, 2, 3, True)
campus.agregarConexion('Bloque 1', 'Biblioteca', 120, 3, 4, True)
campus.agregarConexion('Bloque 2', 'Bloque 3', 80, 2, 5, True)
campus.agregarConexion('Bloque 3', 'Laboratorio A', 90, 3, 2, False)
campus.agregarConexion('Laboratorio A', 'Laboratorio B', 70, 2, 1, True)
campus.agregarConexion('Biblioteca', 'Cafeteria', 60, 2, 7, True)
campus.agregarConexion('Cafeteria', 'Teatro', 110, 4, 8, True)
campus.agregarConexion('Teatro', 'Administracion', 100, 3, 4, True)
campus.agregarConexion('Administracion', 'Enfermeria', 50, 1, 2, True)
campus.agregarConexion('Enfermeria', 'Zona Deportiva', 130, 5, 3, False)
campus.agregarConexion('Zona Deportiva', 'Cancha', 40, 1, 1, True)
campus.agregarConexion('Cancha', 'Parqueadero Sur', 90, 2, 2, True)
campus.agregarConexion('Parqueadero Sur', 'Parqueadero Norte', 140, 4, 5, True)
campus.agregarConexion('Parqueadero Norte', 'Plazoleta Central', 70, 2, 4, True)
campus.agregarConexion('Plazoleta Central', 'Bloque 1', 60, 1, 3, True)

campus.agregarConexion(
    'Biblioteca',
    'Laboratorio B',
    100,
    3,
    5,
    True,
    'mantenimiento'
)

campus.agregarConexion(
    'Bloque 2',
    'Teatro',
    150,
    5,
    9,
    True,
    'bloqueado'
)


# --------------------------------------------------
# MENÚ
# --------------------------------------------------

while True:

    print('\n========= MENÚ =========')
    print('1. Ruta más corta por distancia')
    print('2. Ruta más rápida por tiempo')
    print('3. Ruta con menor congestión')
    print('4. Ruta accesible')
    print('5. Árbol de expansión mínimo')
    print('6. Salir')

    opcion = input('\nSeleccione una opción: ')

    if opcion == '1':

        origen = input('Origen: ')
        destino = input('Destino: ')

        resultado = campus.encontrarRuta(
            origen,
            destino,
            'distancia'
        )

        print('\nCosto Total:', resultado[0])
        print('Ruta:', resultado[1])
        print(campus.explicarRuta('distancia'))

    elif opcion == '2':

        origen = input('Origen: ')
        destino = input('Destino: ')

        resultado = campus.encontrarRuta(
            origen,
            destino,
            'tiempo'
        )

        print('\nCosto Total:', resultado[0])
        print('Ruta:', resultado[1])
        print(campus.explicarRuta('tiempo'))

    elif opcion == '3':

        origen = input('Origen: ')
        destino = input('Destino: ')

        resultado = campus.encontrarRuta(
            origen,
            destino,
            'congestion'
        )

        print('\nCosto Total:', resultado[0])
        print('Ruta:', resultado[1])
        print(campus.explicarRuta('congestion'))

    elif opcion == '4':

        origen = input('Origen: ')
        destino = input('Destino: ')

        resultado = campus.encontrarRuta(
            origen,
            destino,
            'accesible'
        )

        print('\nCosto Total:', resultado[0])
        print('Ruta:', resultado[1])
        print(campus.explicarRuta('accesible'))

    elif opcion == '5':

        resultadoAEM = campus.arbolExpansionMinimo()

        print('\nPeso Total:', resultadoAEM[0])

        print('\nConexiones del Árbol:')

        for conexion in resultadoAEM[1]:
            print(conexion)

    elif opcion == '6':

        print('\nPrograma finalizado.')
        break

    else:
        print('\nOpción inválida.')
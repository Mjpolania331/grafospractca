# Optimización de Recorridos UdeM

## Descripción del Proyecto

Este proyecto implementa una solución basada en grafos para optimizar recorridos dentro del campus de la Universidad de Medellín.

El sistema representa diferentes lugares importantes de la universidad como vértices y los caminos entre ellos como aristas ponderadas.

Cada camino almacena información relacionada con:

- Distancia
- Tiempo estimado
- Nivel de congestión
- Accesibilidad
- Estado del camino

El proyecto utiliza algoritmos de grafos para encontrar rutas óptimas según distintos criterios.

---

# Funcionalidades

El sistema permite:

1. Encontrar la ruta más corta por distancia.
2. Encontrar la ruta más rápida por tiempo.
3. Encontrar la ruta con menor congestión.
4. Encontrar rutas accesibles para personas con movilidad reducida.
5. Ignorar caminos bloqueados o en mantenimiento.
6. Generar un Árbol de Expansión Mínimo.

---

# Tecnologías Utilizadas

- Python 3
- Grafos con listas de adyacencia
- Algoritmo de Dijkstra
- Algoritmo de Prim

---

# Estructura del Proyecto

```bash
practica.py
README.md
```

---

# Cómo Ejecutar el Proyecto

## 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2. Entrar a la carpeta

```bash
cd grafospractca
```

---

## 3. Ejecutar el programa

```bash
python practica.py
```

---

# Funcionamiento del Sistema

El programa funciona mediante un menú interactivo en consola que permite al usuario seleccionar diferentes tipos de rutas dentro del campus de la Universidad de Medellín.

Cuando el programa inicia, se crea automáticamente el grafo del campus con todos los lugares importantes y las conexiones entre ellos.

Cada conexión contiene información sobre:

- Distancia
- Tiempo
- Congestión
- Accesibilidad
- Estado del camino

---

## Inicio del Programa

Al ejecutar el archivo:

```bash
python practica.py
```

aparecerá el siguiente menú:

```bash
========= MENÚ =========
1. Ruta más corta por distancia
2. Ruta más rápida por tiempo
3. Ruta con menor congestión
4. Ruta accesible
5. Árbol de expansión mínimo
6. Salir
```

El usuario debe escribir el número de la opción que desea ejecutar.

---

# Opciones del Sistema

## 1. Ruta Más Corta por Distancia

El programa solicita:

```bash
Origen:
Destino:
```

Después utiliza el algoritmo de Dijkstra adaptado para encontrar la ruta con menor distancia total entre ambos puntos.

El sistema:

- Ignora caminos bloqueados.
- Ignora caminos en mantenimiento.
- Calcula el costo total.
- Reconstruye la ruta óptima.

Ejemplo:

```bash
Costo Total: 320
Ruta: ['Bloque 1', 'Biblioteca', 'Cafeteria']
La ruta minimiza la distancia total.
```

---

## 2. Ruta Más Rápida por Tiempo

Esta opción utiliza el tiempo estimado de recorrido como peso principal del algoritmo.

El objetivo es encontrar el camino que tome menos tiempo entre el origen y el destino.

Ejemplo:

```bash
Costo Total: 8
Ruta: ['Bloque 1', 'Plazoleta Central', 'Parqueadero Norte']
La ruta minimiza el tiempo de recorrido.
```

---

## 3. Ruta con Menor Congestión

El sistema utiliza el nivel de congestión de cada camino para calcular una ruta que evite zonas con mucho tráfico de personas.

La ruta seleccionada será la que tenga menor congestión acumulada.

Ejemplo:

```bash
Costo Total: 10
Ruta: ['Bloque 1', 'Bloque 2', 'Bloque 3']
La ruta evita zonas congestionadas.
```

---

## 4. Ruta Accesible

Esta opción solo utiliza caminos habilitados para personas con movilidad reducida.

Si una conexión no es accesible, el algoritmo la ignora automáticamente.

Ejemplo:

```bash
Costo Total: 400
Ruta: ['Bloque 1', 'Biblioteca', 'Teatro']
La ruta solo usa caminos accesibles.
```

---

## 5. Árbol de Expansión Mínimo

El programa utiliza el algoritmo de Prim para generar un recorrido que conecte todos los lugares del campus utilizando la menor distancia total posible.

El sistema muestra:

- Peso total del árbol
- Conexiones utilizadas

Ejemplo:

```bash
Peso Total: 980

('Bloque 1', 'Bloque 2', 100)
('Bloque 2', 'Bloque 3', 80)
('Biblioteca', 'Cafeteria', 60)
```

---

## 6. Salir

Finaliza la ejecución del programa.

```bash
Programa finalizado.
```

---

# Modelado del Grafo

El grafo contiene más de 15 vértices que representan lugares importantes del campus:

- Bloques académicos
- Biblioteca
- Cafetería
- Teatro
- Enfermería
- Laboratorios
- Parqueaderos
- Zona deportiva
- Administración
- Plazoleta central

Cada conexión almacena:

```python
{
    'destino': 'Biblioteca',
    'distancia': 120,
    'tiempo': 3,
    'congestion': 4,
    'accesible': True,
    'estado': 'disponible'
}
```

---

# Algoritmos Implementados

## Dijkstra Adaptado

Se implementó una versión adaptada del algoritmo de Dijkstra para:

- Minimizar distancia
- Minimizar tiempo
- Minimizar congestión
- Encontrar rutas accesibles

El algoritmo también ignora caminos:

- bloqueados
- en mantenimiento

---

## Árbol de Expansión Mínimo

Se implementó el algoritmo de Prim para conectar todos los vértices utilizando la menor distancia total posible.

---

# Supuestos Asumidos

- Los caminos bloqueados o en mantenimiento no pueden utilizarse.
- Las rutas accesibles solo utilizan caminos habilitados.
- Los pesos utilizados representan valores aproximados.
- El grafo utilizado es no dirigido.

---

# Autores

- Kevin Silva
- Maria Jose Polania
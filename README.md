# LP-AUTONOMO-2 — Adivina el Número

## Descripción
Juego en el que el sistema (computadora) adivina el número que el jugador 
está pensando (entre 1 y 100), utilizando el algoritmo de búsqueda binaria. 
El jugador da pistas ("mayor", "menor" o "correcto") hasta que la computadora 
acierta el número en el menor número de intentos posible.

## Datos del proyecto
- **Estudiante:** Angel Xavier Rezabala Perez
- **Carrera:** Ingeniería en Inteligencia Artificial
- **Materia:** Lógica de Programación
- **Docente:** Heredia Jiménez Estefania Vanessa
- **Actividad:** Trabajo Autónomo 2

## Estructura del repositorio
- `/diagramas` — Diagramas de flujo del sistema (PDF + imágenes):
  - Diagrama 1: Búsqueda Binaria
  - Diagrama 2: Gestión de Sesión
- `/src` — Código fuente en Python (`AdivinaNumero.py`)

## Tecnologías utilizadas
- Lenguaje: Python 3.13
- Entorno de desarrollo: Visual Studio Code

## Cómo ejecutar el programa
1. Clonar o descargar este repositorio
2. Abrir la carpeta `/src` en VS Code
3. Ejecutar `AdivinaNumero.py`
4. Pensar un número del 1 al 100 y responder las pistas que pide el programa

## Lógica del programa
El programa implementa el algoritmo de búsqueda binaria: en cada intento 
calcula el punto medio entre `min` y `max`, y según la respuesta del jugador 
(mayor, menor o correcto) ajusta el rango de búsqueda hasta acertar. 
Los nombres de las variables (`min`, `max`, `intentos`, `intento_pc`, `pista`) 
coinciden exactamente con los diagramas de flujo incluidos en `/diagramas`.
Repositorio renombrado.
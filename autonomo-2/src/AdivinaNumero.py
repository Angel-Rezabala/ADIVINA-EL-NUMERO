"""Juego: Adivina el numero (la COMPUTADORA adivina)
Autónomo 2 - Lógica de programación
Algoritmo: búsqueda binaria
Nombes de variables iguales a los diagramasde flujo:
- Diagrama 1: Búsqueda Binaria
- Diagrama 2: Gestión de Sesión
"""

def jugar ():
    """Ejecuta una partida completa (corresponde al Diagrama 1)."""

# Inicio
min = 1
max = 100
intentos = 0

print("Piensa un número del 1 al 100, no me lo digas.")
# Bucle principal (búsqueda binaria)
while True:
    intentos = intentos + 1
    intento_pc = (min + max) // 2
    
    print(f'\n¿Es {intento_pc}?')
    print("1: Mayor, 2: Menor, 3: Correcto")
    pista = int(input("Ingresa tu pista: "))
    
    # Rombo 1: ¿pista == 3 (Correcto)?
    if pista == 3:
        print(f"\n¡Adiviné tu número en {intentos} intentos!")
        break # Fin del juego
    
    # Rombo 2: ¿pista == 1 (Mayor)?
    elif pista == 1:
        min = intento_pc + 1
    else:
        max = intento_pc - 1

def main():
    """Gestión de sesión: permite reiniciar el juego (Diagrama 2)."""
    opcion = "s"
    
    while opcion == "s":
        jugar()
        print("\n¿Jugar de nuevo? (s/n)")
        opcion = input("Ingresa tu opción: ")
        
    print("¡Gracias por Jugar!")
    
if __name__ =="__main__":
    main()
    
import random

# Etapas del ahorcado (de 7 a 0 intentos)
AHORCADO = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,# 0 intentos (pierde)
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,# 1 intentos restantes
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,# 2 intentos restantes
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,# 3 intentos restantes
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,# 4 intentos restantes
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,# 5 intentos restantes
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,# 6 intentos restantes
    """
     +---+
         |
         |
         |
         |
         |
    =========
    """,# 7 intentos (inicio del juego)
]

# Función que devuelve una palabra secreta elegida al azar de la lista
def obtener_palabra_secreta():
    palabras = [
        "python",
        "javascript",
        "java",
        "angular",
        "django",
        "react",
        "typescript",
        "git",
        "flask",
        "tensorflow",
    ]
    return random.choice(palabras)

# Función que muestra el progreso del jugador
# Reemplaza las letras no adivinadas con "_"
def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

# Función principal del juego
def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("********!¡Bienvenido al juego del ahorcado!********")
    print(f"tenes {intentos} intentos para adivinar la palabra secreta")
    print(" ")
    print(
        mostrar_progreso(palabra_secreta, letras_adivinadas),
        "La cantidad de letras de la palabra es: ",
        len(palabra_secreta),
    )
    print(AHORCADO[-1])  # Dibujo inicial (sin errores)

# Bucle principal del juego
    while not juego_terminado and intentos > 0:
        
        # Solicitamos una letra al usuario
        adivinanza = input("Introduce una letra: ").lower()
        
        #  Validaciones
        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor ingresa una letra válida(solo escribe una letra)")

        elif adivinanza in letras_adivinadas:
            print("ya has utilizado esa letra, prueba con otra")
        else:
            # Si la letra es válida y nueva, la agregamos a la lista
            letras_adivinadas.append(adivinanza)

            # Verificamos si la letra está en la palabra secreta
            if adivinanza in palabra_secreta:
                print(
                    f"!Muy bien has acertado, la letra '{adivinanza}' esta presente en la palabra secreta¡"
                )
            else:
                # Si no está, restamos un intento y mostramos el dibujo
                intentos -= 1
                print(
                    f"Lo siento mucho la letra {adivinanza} no esta presente en la palabra secreta"
                )
                print(f"te quedan {intentos} intentos")
                print(AHORCADO[intentos])  # Mostrar dibujo según intentos
        
        # Actualizamos el progreso
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)
        print("Letras usadas:", ", ".join(letras_adivinadas))

        # Si ya no hay guiones bajos, el jugador ganó
        if "_" not in progreso_actual:
            juego_terminado = True
            palabra_secreta = palabra_secreta.capitalize()
            print(
                f"\n ¡Felicidades has ganado! La palabra completa es '{palabra_secreta}' "
            )
    #  Si se quedaron sin intentos, el jugador pierde
    if intentos == 0:
        print(AHORCADO[0])  # Mostrar dibujo final completo
        palabra_secreta = palabra_secreta.capitalize()
        print(
            f"\n lo sentimos mucho se te han acabado los intentos, la palabra secreta era '{palabra_secreta}'"
        )


juego_ahorcado()

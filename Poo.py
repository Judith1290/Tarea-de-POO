import random


def random():
    colors = ('rojo', 'azul', 'verde', 'amarillo')  
    codigo = []  

    for i in range(4):  
        elegido = random.choice(colors)  # Elige un color aleatorio de la lista
        while elegido in codigo:
            elegido = random.choice(colors)
        codigo.append(elegido)  # Añade el color elegido a la lista de código

    return codigo  

def get_feedback(code, guess):
    posicion_correcta = sum ([1 for c, a in zip(code, guess) if c == a])
    
    colores_correctos = 0
    
    # Crea diccionarios que cuentan las ocurrencias de cada color en el código y en la adivinanza
    code_counts = {color: code.count(color) for color in set(code)}
    attempt_counts = {color: guess.count(color) for color in set(guess)}
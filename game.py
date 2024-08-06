import random
from colored import fg, attr

class Mastermind:
    COLORS = ['red', 'blue', 'green', 'yellow']
    ATTEMPTS = 12
    
    def __init__(self):
        self._board = [[' ' for _ in range(4)] for _ in range(self.ATTEMPTS)]
        self._feedback = [[' ' for _ in range(4)] for _ in range(self.ATTEMPTS)]
        self.__secret_code = []
    
    def __generate_code(self):
        self.__secret_code = [random.choice(self.COLORS) for _ in range(4)]
    
    def set_secret_code(self, code):
        if all(color in self.COLORS for color in code) and len(code) == 4:
            self.__secret_code = code
        else:
            raise ValueError("Código inválido. Usa solo 'red', 'blue', 'green', 'yellow'.")
    
    def __get_feedback(self, guess):
        feedback = [' ' for _ in range(4)]
        temp_code = self.__secret_code[:]
        temp_guess = guess[:]

        # Marca los colores correctos en la posición correcta (verde)
        for i in range(4):
            if temp_guess[i] == temp_code[i]:
                feedback[i] = fg('green') + '🟢' + attr('reset')
                temp_code[i] = None
                temp_guess[i] = None
                
        # Marca los colores correctos en la posición incorrecta (amarillo)
        for i in range(4):
            if temp_guess[i] is not None and temp_guess[i] in temp_code:
                feedback[i] = fg('yellow') + '🟠' + attr('reset')
                temp_code[temp_code.index(temp_guess[i])] = None
                
        return feedback
    
    def __print_board(self):
        # Imprime el tablero y la retroalimentación
        for row, feed in zip(self._board, self._feedback):
            # Formatea las adivinanzas con colores y la retroalimentación correspondiente
            row_colors = ' | '.join([fg(color) + color + attr('reset') if color in self.COLORS else color for color in row])
            feedback_colors = ' '.join(feed)
            print(f"{row_colors} || {feedback_colors}")
    
    def play(self):
         # Controla el flujo del juego
        print("¡Bienvenido a Mastermind!")
        choice = input("¿Quieres ser el creador del código o el adivinador? (creator/guesser): ").strip().lower()
        
        if choice == 'creator':
            code = input("Ingresa tu código secreto (e.g., red blue green yellow): ").strip().lower().split()
            try:
                self.set_secret_code(code)
            except ValueError as e:
                print(e)
                return
        else:
            self.__generate_code()
        
        for attempt in range(self.ATTEMPTS):
            guess = input(f"Intento {attempt + 1}: Ingresa tu suposición (e.g., red blue green yellow): ").strip().lower().split()
            
            if len(guess) != 4 or any(color not in self.COLORS for color in guess):
                print("Suposición inválida. Usa solo 'red', 'blue', 'green', 'yellow'.")
                continue
            
            self._board[attempt] = guess 
            feedback = self.__get_feedback(guess) # Obtiene la retroalimentación para la adivinanza
            self._feedback[attempt] = feedback # Guarda la retroalimentación en el tablero
            self.__print_board()# Imprime el tablero y la retroalimentación
            
            if guess == self.__secret_code:
                 # Mensaje de éxito si el código ha sido adivinado correctamente
                print(f"¡Felicidades! Adivinaste el código secreto: {' '.join(self.__secret_code)}")
                break
        else:
            # Mensaje de fin de juego si no se adivina el código en los intentos permitidos
            print(f"¡Juego terminado! El código secreto era: {' '.join(self.__secret_code)}")

if __name__ == "__main__":
    game = Mastermind()
    game.play()
    
    
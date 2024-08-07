from itertools import product #se puede utilizar para generar todas las posibles combinaciones de colores para el código secreto.
import random
from colored import fg, attr

class Mastermind:
    COLORS = ['red', 'blue', 'green', 'yellow']
    ATTEMPTS = 12
    
    def __init__(self):
        self._board = [[' ' for _ in range(4)] for _ in range(self.ATTEMPTS)]
        self._feedback = [[' ' for _ in range(4)] for _ in range(self.ATTEMPTS)]
        self._secret_code = []
    
    def _generate_code(self):
        self._secret_code = [random.choice(self.COLORS) for _ in range(4)]
    
    def set_secret_code(self, code):
        if all(color in self.COLORS for color in code) and len(code) == 4:
            self._secret_code = code
        else:
            raise ValueError("Código inválido. Usa solo 'red', 'blue', 'green', 'yellow'.")
    
    def _get_feedback(self, guess):
        feedback = [' ' for _ in range(4)]
        temp_code = self._secret_code[:]
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
    
    def _print_board(self):
        # Imprime el tablero y la retroalimentación
        for row, feed in zip(self._board, self._feedback):
            row_colors = ' | '.join([fg(color) + color + attr('reset') if color in self.COLORS else color for color in row])
            feedback_colors = ' '.join(feed)
            print(f"{row_colors} || {feedback_colors}")
    
    def _random_strategy(self, possible_codes):
        return random.choice(possible_codes)
    
    def _brute_force_strategy(self, possible_codes):
        return possible_codes[0]  # Prueba todas las combinaciones posibles, implementa una estrategia aquí
    
    def _knuth_strategy(self, possible_codes):
        return possible_codes[0]  # Implementa la estrategia de Knuth aquí
    
    def play(self):
        print("¡Bienvenido a Mastermind!")
        choice = input("¿Quieres ser el creador del código o el adivinador? (creator/guesser): ").strip().lower()
        
        if choice == 'creator':
            code = input("Ingresa tu código secreto (por ejemplo, red blue green yellow): ").strip().lower().split()
            try:
                self.set_secret_code(code)
            except ValueError as e:
                print(e)
                return
            print("Ahora, la computadora intentará adivinar tu código.")
            possible_codes = list(product(self.COLORS, repeat=4))  # Genera todas las combinaciones posibles
            for attempt in range(self.ATTEMPTS):
                strategies = [self._random_strategy, self._brute_force_strategy, self._knuth_strategy]
                strategy = random.choice(strategies)
                
                guess = strategy(possible_codes)  # Usa la estrategia elegida
                guess = list(guess)  # Convierte la tupla en lista para mantener la consistencia
                self._board[attempt] = guess
                feedback = self._get_feedback(guess)  # Obtiene la retroalimentación para la adivinanza
                self._feedback[attempt] = feedback  # Guarda la retroalimentación en el tablero
                self._print_board()  # Imprime el tablero y la retroalimentación
                
                if guess == self._secret_code:
                    print(f"¡La computadora ha adivinado el código secreto: {' '.join(self._secret_code)}!")
                    break
            else:
                print(f"¡Juego terminado! El código secreto era: {' '.join(self._secret_code)}")
        
        elif choice == 'guesser':
            self._generate_code()  # Genera un código secreto aleatorio para el juego
            print("¡La computadora ha generado un código secreto!")
            for attempt in range(self.ATTEMPTS):
                guess = input(f"Intento {attempt + 1}: Ingresa tu adivinanza (por ejemplo, red blue green yellow): ").strip().lower().split()
                
                if len(guess) != 4 or any(color not in self.COLORS for color in guess):
                    print("Adivinanza inválida. Usa solo 'red', 'blue', 'green', 'yellow'.")
                    continue
                
                self._board[attempt] = guess
                feedback = self._get_feedback(guess)  # Obtiene la retroalimentación para la adivinanza
                self._feedback[attempt] = feedback  # Guarda la retroalimentación en el tablero
                self._print_board()  # Imprime el tablero y la retroalimentación
                
                if guess == self._secret_code:
                    print(f"¡Felicidades! Has adivinado el código secreto: {' '.join(self._secret_code)}!")
                    break
            else:
                print(f"¡Juego terminado! El código secreto era: {' '.join(self._secret_code)}")
        else:
            print("Opción inválida. Por favor, elige 'creator' o 'guesser'.")

# Código para iniciar el juego
if __name__ == "__main__":
    game = Mastermind()
    game.play()


    
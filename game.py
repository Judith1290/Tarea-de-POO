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
                
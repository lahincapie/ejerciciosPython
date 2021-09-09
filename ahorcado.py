import random  
IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
        ========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        ========''','''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        ========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        ========''','''
    '''] 

WORDS = [
    'programador',
    'ingeniero',
    'arquitecto',
    'abogado',
    'militar',
    'politico',
    'presidente',
    'senador',
    'desarrollador'
]
def random_word(): 
    index = random.randint(0, len(WORDS) - 1)  
                                           
    return WORDS[index]  

def display_board(hidden_word, tries):  
    print(IMAGES[tries])  
    print('')  
    print(hidden_word) 
    print('---* ---* ---* ---* ---* ---* ---* ---* ---* ---*') 


def run():  
    word = random_word()  
    hidden_word = ['_'] * len(word)  
    tries = 0

    while True: 
        display_board(hidden_word, tries)  
        current_letter = input('Ingresa una letra: ')  

        letter_indexes = []

        for i in range (len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
                tries += 1

                if tries == 7:
                    display_board(hidden_word, tries)
                    print('')
                    print('Perdiste! La palabra correcta era {}'.format(word))
                    break
        else:
            for index in letter_indexes:
                hidden_word[index] = current_letter

        letter_indexes = []

        if not '_' in hidden_word:
            display_board(hidden_word, tries)
            print('')
            print('Felicidades! Ganaste, la palabra era : {}'.format(word))
            break

if __name__ == "__main__":
    print('BIENVENIDO A EL JUEGO DE AHORCADOS')
    run()

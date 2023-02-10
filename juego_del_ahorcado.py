from functools import reduce
import random
import os

def normalize(chosen_word: str):
    vocals = ("a", "e", "i", "o", "u")
    vocals_with_accent_marks = ("á", "é", "í", "ó", "ú")
    for y in range(5):
        chosen_word = chosen_word.replace(vocals_with_accent_marks[y], vocals[y])
    return chosen_word

def game(incorrect_letters_list: list, incorrect_letters_str: str, win: list, chosen_word: str, hidden_word: str, correct_letters: list) -> list:
    chosen_word = chosen_word.lower()
    guessed_correctly = True
    where_it_is = -1
    retry = True
    hidden_word = reduce(lambda a, b: a + b, correct_letters)
    if hidden_word == chosen_word:
        return [win[0], True, incorrect_letters_str, True]
    for i, v in enumerate(chosen_word):
        if correct_letters[i] == "-":
            continue
    if hidden_word == chosen_word:
        return [win[0], True, incorrect_letters_str, True]      
    while retry == True:
        # This exists so that the loop repeats even if the string isn't numeric
        little_retry = False
        os.system("cls")
        print("Adivina la palabra")
        print("¿Podrás hacerlo?")
        print(hidden_word)
        print(f"Vidas restantes: {win[0]}")
        print(f"Letras incorrectas: {incorrect_letters_str}")
        guessed_letter: str = input("Escribe una letra: ")
        if len(guessed_letter) < 1:
            input("Necesitas ingresar una letra, presiona enter para intentar de nuevo")
            little_retry = True
        elif len(guessed_letter) > 1:
            input("No puedes ingresar más de una letra, presiona enter para intentar de nuevo")
            little_retry = True
        if guessed_letter.isalpha() == True:
            if little_retry == False:
                retry = False
        else:
            input("Solo puedes ingresar letras, presiona enter para intentar de nuevo")
            retry = True
    for y in range(chosen_word.count(guessed_letter)):
        where_it_is: int = chosen_word.find(guessed_letter, where_it_is + 1)
        correct_letters.pop(where_it_is)
        correct_letters.insert(where_it_is, guessed_letter)
    if where_it_is == -1 and incorrect_letters_list.count(guessed_letter) == 0:
        incorrect_letters_list.append(guessed_letter)
        guessed_correctly = False
    return [win[0], False, incorrect_letters_str, guessed_correctly]


def read():
    word_list = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        word_list = [word for word in f]
    chosen_num = random.randint(0, len(word_list) -1)
    chosen_word = word_list[chosen_num]
    chosen_word = chosen_word.replace("\n", "")
    return chosen_word


def run():
    chosen_word = read()
    incorrect_letters = []
    incorrect_letters_str = ""
    win = [10, False]
    print("Bienvenido al juego")
    print("""
 __ __   ____  ____    ____  ___ ___   ____  ____  
|  |  | /    ||    \  /    ||   |   | /    ||    \ 
|  |  ||  o  ||  _  ||   __|| _   _ ||  o  ||  _  |
|  _  ||     ||  |  ||  |  ||  \_/  ||     ||  |  |
|  |  ||  _  ||  |  ||  |_ ||   |   ||  _  ||  |  |
|  |  ||  |  ||  |  ||     ||   |   ||  |  ||  |  |
|__|__||__|__||__|__||___,_||___|___||__|__||__|__|
                                                   
        """)
    input("Presiona enter para continuar")
    normalized_chosen_word = normalize(chosen_word)
    for i in range(len(chosen_word)):
        hidden_word = normalized_chosen_word.replace(normalized_chosen_word[i], "-")
    correct_letters = []
    for i in normalized_chosen_word:
        correct_letters.append("-")
    while win[1] is False and win[0] != 0:
        if incorrect_letters != []:
            incorrect_letters_str = ", ".join(incorrect_letters)
        win = game(incorrect_letters, incorrect_letters_str, win, normalized_chosen_word, hidden_word, correct_letters)
        if win[3] is False:
            win[0] -= 1
    if win[0] == 0:
        os.system("cls")
        print("Game over")
    else:
        print(f"¡Felicidades, has ganado!, la palabra era: {chosen_word}")


if __name__ == "__main__":
    run()
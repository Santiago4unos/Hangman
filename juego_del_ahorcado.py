from functools import reduce
import random
import os

def normalize(chosen_word):
    vocals = ("a", "e", "i", "o", "u")
    vocals_with_accent_marks = ("á", "é", "í", "ó", "ú")
    for y in range(5):
        chosen_word = chosen_word.replace(vocals_with_accent_marks[y], vocals[y])
    return chosen_word

def game(chosen_word, letters, hidden_word, size_of_letters, correct_letters):
    retry = True
    hidden_word = reduce(lambda a, b: a + b, correct_letters)
    if hidden_word == chosen_word:
        return True
    for y in range(len(letters)):
        if correct_letters[y] == "-":
            continue

    if hidden_word == chosen_word:
        return True      
    while retry == True:
        os.system("cls")
        print("Adivina la palabra")
        print("¿Podrás hacerlo?")
        print(hidden_word)
        guessed_letter = input("Escribe una letra: ")
        if len(guessed_letter) < 1:
            input("Necesitas ingresar una letra, presiona enter para intentar de nuevo")

        elif len(guessed_letter) > 1:
            input("No puedes ingresar más de una letra, presiona enter para intentar de nuevo")

        try:
            int(guessed_letter)
            input("No puedes ingresar números, presiona enter para intentar de nuevo")

        except ValueError:
            retry = False
    if hidden_word == chosen_word:
        return True
    for y in range(size_of_letters):
        for y in range(size_of_letters):
            if guessed_letter.lower == letters[y]:
                where_it_is = letters.index(guessed_letter)
                correct_letters.pop(where_it_is)
                correct_letters.insert(where_it_is, guessed_letter)
    return False


def read():
    word_list = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        word_list = [word for word in f]
    size_of_list = len(word_list)
    chosen_num = random.randint(1, size_of_list)
    chosen_word = word_list[chosen_num]
    chosen_word = chosen_word.replace("\n", "")
    return chosen_word


def run():
    chosen_word = read()
    win = False
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
    letters = [g for g in normalize(chosen_word)]
    for i in range(len(chosen_word)):
        hidden_word = chosen_word.replace(chosen_word[i], "-")
    correct_letters = []
    for i in range(len(letters)):
        correct_letters.append("-")
    size_of_letters = len(letters)
    while win == False:
        win = game(chosen_word, letters, hidden_word, size_of_letters, correct_letters)
    print("¡Felicidades, has ganado!, la palabra era: " + chosen_word)


if __name__ == "__main__":
    run()
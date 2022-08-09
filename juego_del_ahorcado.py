import random

def chooseword():
    size_of_list = len(word_list)
    chosen_word = random.randint(1, size_of_list)
    word_list[chosen_word]
        


def read():
    word_list = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for word in f:
            word_list.append(word)
    return word_list


def run():
    read()
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
    while win == False:
        chooseword()
        print()


if __name__ == "__main__":
    run()
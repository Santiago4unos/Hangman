import math

def run():
    numberDictionary = {i: round(i**0.5, 2) for i in range(1,1001) if i % 3 != 0}

    print(numberDictionary)


if __name__ == "__main__":
    run()
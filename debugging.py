from multiprocessing.sharedctypes import Value


def divisors(num):
    try:
        if num < 0:
            raise ValueError("No se pueden ingresar números negativos")
        divisors = [i for i in range(1, num+1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    error = True
    while error == True:
        try:
            num = int(input("Escribe un número: "))
            print(divisors(num))
            error = False
        except ValueError:
            print("No se pueden ingresar strings")
            error = True

if __name__ == "__main__":
    run()
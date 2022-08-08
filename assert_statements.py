from multiprocessing.sharedctypes import Value


def divisors(num):
    assert num > 0, "Debes ingresar un número positivo" 
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors


def run():
        num = input("Escribe un número: ")
        # assert num.isnumeric(), "Debes ingresar un número "
        print(divisors(int(num)))

if __name__ == "__main__":
    run()
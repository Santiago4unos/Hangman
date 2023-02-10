def run():
    numbers = [i for i in range(36,99999) if i % 4 == 0 if i % 6 == 0 if i % 9 == 0]

    print(numbers)


if __name__ == "__main__":
    run()

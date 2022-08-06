def run():
    myList = [23, 54.32, "Good morning", False]
    myDict = {
        "firstname": "Santiago",
        "lastname": "Muñoz",
    }

    super_list = [
        {"firstname": "Santiago", "lastname": "Muñoz",},
        {"firstname": "Kevin", "lastname": "Torres",},
        {"firstname": "Gonzalo", "lastname": "Mantecon",},
        {"firstname": "Roberto", "lastname": "Martínez",},
    ]

    super_dict = {
        "natural_nums": [3, 43, 52, 21],
        "integer_nums": [-1, -23, 2, -5],
        "floating_nums": [20.3, 12.4, 32.7, 17.9]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i)


if __name__ == "__main__":
    run()
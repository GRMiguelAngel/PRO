# ****************************************
# INTERCAMBIAR CLAVE-VALOR EN DICCIONARIOS
# ****************************************


def run(data: dict) -> dict:
    swapped_data = {}
    for value, key in data.items():
        if key not in swapped_data and value > swapped_data[key]:
            swapped_data[key] = value
            
    return swapped_data


if __name__ == '__main__':
    run({'a': 1, 'b': 2, 'c': 3})

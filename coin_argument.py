# Эта программа передаёт объект Coin
# в качестве аргумента в функцию.

import coin


def main():
    # Создать объект Coin.
    my_coin = coin.Coin()

    # Эта инструкция покажет 'Орёл'.
    print(my_coin.get_sideup())

    # Передать объект в функцию flip.
    flip(my_coin)

    # Эта инструкция может показать 'Орёл'
    # либо 'Решка'.
    print(my_coin.get_sideup())


# Эта функция подбрасывает монету.
def flip(coin_obg):
    coin_obg.toss()


main()

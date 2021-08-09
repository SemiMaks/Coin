import random

# Класс Coin имитирует монету,
# которую можно подбрасывать.

class Coin:

    # Метод __init__ инициализирует
    # атрибут данных sideup значением "Орёл"

    def __init__(self):
        self.__sideup = 'Орёл'

    # Метод toss генерирует случайное число
    # в диапазоне от 0 до 1. Если это число
    # равно 0, то __sideup получает значение 'Орёл'.
    # В противном случае __sideup получает значение 'Решка'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Орёл'
            print('Орёл')
        else:
            self.__sideup = 'Решка'
            print('Решка')

    def get_sideup(self):
        return self.__sideup

# my_coin = Coin()
# my_coin.toss()
# print(my_coin.get_sideup())

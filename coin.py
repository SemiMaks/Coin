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
        if random.randint(0, 1) == 0 :
            self.__sideup = 'Орёл'
            print('Орёл')
        else:
            self.__sideup = 'Решка'
            print('Решка')

    def get_sideup(self):
        return self.__sideup
# Главная функция
def main():
    # Создать объект на основе класса Coin
    my_coin = Coin()

    # Показать обращенную вверх сторону монеты
    print('Эта сторона обращена вверх: ', my_coin.get_sideup())

    # Подбросить монету
    print('Подбрасываю монету...')
    my_coin.toss()

    # Показать обращенную вверх монету
    print('Теперь эта сторона обращена вверх: ', my_coin.get_sideup())

    # десять бросков монеты подряд
    print('-' * 40)
    print('10 бросков монеты: ')
    for i in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

# Вызвать главную функцию
main()

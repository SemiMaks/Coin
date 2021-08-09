import coin

# Главная функция
def main():
    # Создать объект на основе класса Coin
    my_coin = coin.Coin()

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

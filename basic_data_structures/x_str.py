print('Арифметические операторы:')
print("Сложение строк: 'йцукен' + 'фывапр' = {result}".format(result = 'йцукен' + 'фывапр'))

print('\nДругие операции:')
print("Выравнивает слово 'йцукен' в строке размером 25 символов: {result}".format(result = ('йцукен').center(25, '-')))
print("Проверяет наличие символа (слова) 'ук' в строке 'йцукеукну' и подсчитывает количество совпадений: {result}".format(result = ('йцукеукну').count('ук')))
print("Кодирует слово 'йцукен': {result}".format(result = ('йцукен').encode()))
print("Проверяет наличие символа (окончания) 'ну' в конце строки 'йцукеукну': {result}".format(result = ('йцукеукну').endswith('ну')))
print("Проверяет наличие символа (слова) 'ук' в строке 'йцукеукну' и показывает его начальную позицию: {result}".format(result = ('йцукеукну').find('ук')))
print("Проверяет наличие символа (слова) 'ук' в строке 'йцукеукну': {result}".format(result = ('йцукеукну').__contains__('ук')))
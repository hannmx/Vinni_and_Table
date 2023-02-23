words = input('Введите строки для определения рифмы: ')

def rif(words):
    split_words = words.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аеёиоуыэюя')
    tmp = f(split_words[0])
    if all([f(i) == tmp for i in split_words]):
        return 'Парам пам-пам'
    return 'Пам парам'
print(rif(words))
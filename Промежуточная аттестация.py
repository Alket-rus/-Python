import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# ______________________________________________

# Мой код

# Создаем пустой DataFrame для хранения результатов one-hot кодирования
one_hot = pd.DataFrame()

# Перебираем уникальные значения из столбца 'whoAmI' и создаем для каждого столбец в one-hot кодировании
unique_values = data['whoAmI']

# Начинаем цикл, чтобы создать столбцы в one-hot кодировании для каждого уникального значения из 'whoAmI'
for value in unique_values:
    # Создаем столбец в one_hot, который содержит True, если значение в 'whoAmI' совпадает с текущим уникальным значением
    one_hot[value] = data['whoAmI'] == value

# Выводим строки преобразованного DataFrame one_hot
print(one_hot)

# Задача: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data.head())
print()

# Решение с использованием get_dummies (для сравнения результатов):
print(pd.get_dummies(data, columns=['whoAmI'], prefix='', prefix_sep=''))
print()


# Решение без использования get_dummies:
lst_out = []
for i in data['whoAmI'].tolist():    # data['whoAmI'].tolist() то же самое, что и lst
    if i == "human":
        lst_out.append([1, 0])
    elif i == "robot":
        lst_out.append([0, 1])

print(pd.DataFrame(lst_out, columns=['human', 'robot']))

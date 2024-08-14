import random
import pandas as pd

lst = ['robot'] * 10 + ['human'] * 10
random.seed(42) # для воспроизводимости
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# One-hot encoding
data = pd.get_dummies(data, columns=['whoAmI'])

print(data.head())
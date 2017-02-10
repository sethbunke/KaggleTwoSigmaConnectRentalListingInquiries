import pandas as pd


data = pd.read_json('data-large/train.json')

print(data[0:1][['description']])
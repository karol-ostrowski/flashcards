import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

row = df.iloc[1]

bob = row['Name']

print(int(df.loc[df['Name'] == 'Bob']['Age']))

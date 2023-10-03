import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [35, 30, 25]}

df = pd.DataFrame(data)

row = df.iloc[1]

bob = row['Name']

# df.loc[df['Age'] == 30, 'Name'] = 'pepe'


print(df.loc[df['Name'] == 'Alice']['Age'])
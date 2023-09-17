import pandas as pd

df = pd.DataFrame(columns = ['jedne', 'dwa', 'trz'])
print(len(df.index))
df.loc[len(df.index)] = ['1', '2', '3']
print(df)

import pandas as pd

scores = {'a' : [1,2,3], 'b' : [4,5,6]}
idx = [1,2,3]
df4 = pd.DataFrame(scores, index=idx)
print(df4)
print(df4.a > 2)

print(df4.loc[df4.a > 1])
print('======================')
print(df4.iloc[1])

import pandas as pd
data=pd.read_csv("C:/Users/win-10/Downloads/matches.csv")
print(data)
print(data.head())
print(data.tail())
print(data[1:100])
print(data.columne)
print(data[data['Season']==2008].shape[0])
print(dat[data['Season']==2009])
print(data[data['Winner']=='Chennai Super Kings'])
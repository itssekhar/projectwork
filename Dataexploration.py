# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv1="D:\\project work\\dim.csv"

df=pd.read_csv(csv1,header=0,encoding = 'unicode_escape')

df.head()

print(df.columns)

print(df.shape)

print(df["ZipCode"])
#sns.countplot(df['ZipCode'])

print(df["NickName"])

print(df["ACVolume"])

print(df['FTVolume'].value_counts())


print(df['ZipCode'].value_counts())

print(df['RegionName'].value_counts())
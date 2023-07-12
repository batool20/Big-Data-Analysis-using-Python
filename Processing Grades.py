import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
list1=pd.read_excel("List.xlsx")
List=list1
final1=pd.read_excel("Final.xlsx")
final_weight=str((final1.iloc[0,[2]])['Final'])
final1cleaned=final1.drop(labels=0, axis=0) #final1 Done
final2=pd.read_excel("Final_2.xlsx")
final2cleaned=final2.drop(labels=0, axis=0)#final2 Done
finals=pd.merge(final1cleaned,final2cleaned,how='outer')
finals.rename(columns={'Final':("Final("+final_weight+")")}, inplace=True)
MT=pd.read_excel("MT.xlsx")
MT_weight=str((MT.iloc[0,[2]])['MT'])
MTcleaned=MT.drop(labels=0, axis=0) #MT Done
Final_MT=pd.merge(finals,MTcleaned,on=['Number','Name'])
Final_MT.rename(columns={'MT':("MT("+MT_weight+")")}, inplace=True)
Final_MT_New=Final_MT=pd.merge(List,Final_MT,on=['Number','Name'])
Q1=pd.read_excel("Q1.xlsx")
Q1_weight=str((Q1.iloc[0,[2]])['Q1'])
del Q1['Notes']
Q1Cleaned=Q1.drop(labels=0, axis=0)
Q2=pd.read_excel("Q2.xlsx")
Q2_weight=str((Q2.iloc[0,[2]])['Q2'])
Q2Cleaned=Q2.drop(labels=0, axis=0)
Final_MT_Q1=pd.merge(Final_MT_New,Q1Cleaned,on=['Number','Name'])
Final_MT_Q1_Q2=pd.merge(Final_MT_Q1,Q2Cleaned,how='outer')
dflist=list(Final_MT_Q1_Q2[['Final(50.0)','MT(30.0)','Q1','Q2']])
Final_MT_Q1_Q2['Total']=Final_MT_Q1_Q2[dflist].sum(axis='columns')
scale=pd.read_excel("Scale.xlsx",header=None)
scale.columns=['s1','s2']
bins=list(scale['s2'])
bins.sort()
bins.append(100)
labels=list(scale['s1'])
labels.reverse()
Final_MT_Q1_Q2['Grade'] = pd.cut(Final_MT_Q1_Q2['Total'].values, bins=bins,right=False,
labels=labels)
Final_MT_Q1_Q2.index=Final_MT_Q1_Q2.Number
del Final_MT_Q1_Q2['Number']
Final_MT_Q1_Q2.rename(columns={'Q1':("Q1("+Q1_weight+")")}, inplace=True)
Final_MT_Q1_Q2.rename(columns={'Q2':("Q2("+Q2_weight+")")}, inplace=True)
print(Final_MT_Q1_Q2)
Final_MT_Q1_Q2.to_excel('Results.xlsx')
#plotting
c=Final_MT_Q1_Q2['Grade'].value_counts()
sns.barplot(x=c.index,y=c.values)
plt.show()
columns=list(Final_MT_Q1_Q2.columns)
for i in columns:
 sns.distplot(Final_MT_Q1_Q2[i])
 plt.show()
 plt.close()
Results=Final_MT_Q1_Q2.iloc[:,[3,4,5,6]]
sns.pairplot(Results,kind="reg")
plt.show()
sns.catplot(x="variable", y="value", data=pd.melt(Results),kind='box')
plt.show()

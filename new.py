import pandas as pd 
import numpy as np
df=pd.read_csv('soil_data.csv')
df = df.dropna()
df = pd.DataFrame(df)
# print(df)
d={}
x = 0
l50=[]
l0=[]
l25=[]
df1=df
for i in df['Records']:
    # print(i)
    x=i.split('_')
    if len(x) > 1:
        if x[0] in d:
            d[x[0]] +=1
        else:
            d[x[0]]=1
l = list(d.values())
print(l)
cnt=0
cnttt=b=0
d=0
d_1={'410':[],'435':[],'460':[],'485':[],'510':[],'535':[],'560':[],'585':[],'610':[],'645':[],'680':[],'705':[],'730':[],'760':[],'810':[],'860':[],'900':[],'940':[],'Capacitity Moist':[],'Temp':[],'Moist':[],'EC (u/10 gram)':[],'Ph':[],'Nitro (mg/10 g)':[],'Posh Nitro (mg/10 g)':[],'Pota Nitro (mg/10 g)':[]}
row_values=row_values_25=row_values_50=list()
d_0={'Records':[],'410':[],'435':[],'460':[],'485':[],'510':[],'535':[],'560':[],'585':[],'610':[],'645':[],'680':[],'705':[],'730':[],'760':[],'810':[],'860':[],'900':[],'940':[],'Capacitity Moist':[],'Temp':[],'Moist':[],'EC (u/10 gram)':[],'Ph':[],'Nitro (mg/10 g)':[],'Posh Nitro (mg/10 g)':[],'Pota Nitro (mg/10 g)':[]}
column_names=list(d_0.keys())
for i in l:
    # if d==1:
    #     break 
    # print(i)
    subset=df1.iloc[cnt:(i+cnt)]
    # print(subset)
    cnt+=i
    # d+=1
    for index,row in subset.iterrows():
        record_value = row['Records']
        if '_0ml' in record_value:
            row_values_0 = row.values.tolist()
            # cnttt+=1
            # print(row_values_0)
            l0.append(row_values_0)
        elif '_25ml' in record_value:
            row_values_25=row.values.tolist()
            l25.append(row_values_25)
            # print(row_values_25)
        elif '_50ml' in record_value:
            row_values_50=row.values.tolist()
            l50.append(row_values_50)
    df2=pd.DataFrame(l0,columns=column_names)
    df2=df2.drop(columns=['Records'])
    mean_values=df2.mean()
    # df3=pd.DataFrame(df2)
    for key in mean_values.index:
        d_1[key].append(mean_values[key])
    df3=pd.DataFrame(l25,columns=column_names)
    df3=df3.drop(columns=['Records'])
    mean_values1=df3.mean()
    # df3=pd.DataFrame(df2)
    for key in mean_values1.index:
        d_1[key].append(mean_values1[key])
    df4=pd.DataFrame(l0,columns=column_names)
    df4=df4.drop(columns=['Records'])
    mean_values2=df4.mean()
    # df3=pd.DataFrame(df2)
    for key in mean_values2.index:
        d_1[key].append(mean_values2[key])
df6=pd.DataFrame(d_1)
# print(len(df6))
print(df6.corr())

import pandas as pd 
import numpy as np
df=pd.read_csv('soil_data.csv')
df = df.dropna()
df = pd.DataFrame(df)
# print(df)
d={}
x = 0
l50=l25=l0=[]
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
row_values=row_values_25=row_values_50=list()
d_0={'Records':[],'410':[],'435':[],'460':[],'485':[],'510':[],'535':[],'560':[],'585':[],'610':[],'645':[],'680':[],'705':[],'730':[],'760':[],'810':[],'860':[],'900':[],'940':[],'Capacitity Moist':[],'Temp':[],'Moist':[],'EC (u/10 gram)':[],'Ph':[],'Nitro (mg/10 g)':[],'Posh Nitro (mg/10 g)':[],'Pota Nitro (mg/10 g)':[]}
for i in l:
    if d==1:
        break 
    # print(i)
    subset=df1.iloc[cnt:(i+cnt)]
    # print(subset)
    cnt+=i
    d+=1
    for index,row in subset.iterrows():
        if '_0ml' in row.values.tolist()[0]:
            row_values_0 = row.values.tolist()
            cnttt+=1
        # print(row_values_0)
        l0.append(row_values_0)
        if '_25ml' in row.values.tolist()[0]:
            row_values_25=row.values.tolist()
        l25.append(row_values_25)   
        if '_50ml' in row.values.tolist()[0]:
            row_values_50=row.values.tolist()
        l50.append(row_values_50)   
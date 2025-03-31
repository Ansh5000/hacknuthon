import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
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
# print(l)
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
# print(df6.corr().to_string())



# To find maximum correlation in the given dataset.

# correlation_matrix = df6.corr()
# abs_corr_matrix = correlation_matrix.abs()
# np.fill_diagonal(abs_corr_matrix.values, 0)
# max_corr_pair = abs_corr_matrix.stack().idxmax()
# max_corr_value = abs_corr_matrix.stack().max()
# print(f"\nHighest correlation is between '{max_corr_pair[0]}' and '{max_corr_pair[1]}' with a correlation value of {max_corr_value}")
# df6.to_csv('compressSoilData.csv')




# Correlation of Wavelength with ph.
wavelength_columns = [col for col in df6.columns if col.isnumeric()]
correlation_with_ph = df[wavelength_columns].corrwith(df['Nitro (mg/10 g)'])
print(abs(correlation_with_ph).max())
# plt.figure(figsize=(10, 6))  # Set the figure size
# plt.bar(correlation_with_ph.index, correlation_with_ph.values, color='skyblue')
# plt.xlabel('Wavelength (nm)', fontsize=12)  # Label for x-axis
# plt.ylabel('Correlation with Ph', fontsize=12)  # Label for y-axis
# plt.title('Correlation of Wavelengths with Ph', fontsize=14)
# plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
# plt.tight_layout()  # Adjust the layout to prevent clipping of labels
# plt.show()

print(f"NumPy Correlation: {0.013531289898704996}")

# 2. Correlation and p-value using SciPy
correlation_scipy, p_value = stats.pearsonr(df6['860'], df6['Ph'])
print(f"SciPy Correlation: {correlation_scipy}, P-value: {p_value}")

# 3. Linear Regression using SciPy (to get the equation)
slope, intercept, r_value, p_value, std_err = stats.linregress(df6['860'], df6['Ph'])
print(f"Slope: {slope}, Intercept: {intercept}")
print(f"Equation: y = {slope:.5f}x + {intercept:.5f}") # formatted equation
print(f"R-squared: {r_value**2}")

# 4. Linear regression using numpy.polyfit
coefficients = np.polyfit(df6['860'], df6['Ph'],1)
slope_np = coefficients[0]
intercept_np = coefficients[1]
print(f"Numpy polyfit Slope: {slope_np}, Intercept: {intercept_np}")
print(f"Equation of correlation between 860nm and Ph: y = {slope_np:.5f}x + {intercept_np:.5f}")

# 5. Correlation using Pandas (if you have data in a DataFrame)
data = {'x': df6['860'], 'y': df6['Ph']}
df = pd.DataFrame(data)
correlation_pd = df['x'].corr(df['y'])
print(f"Pandas Correlation: {correlation_pd}")

print(f"NumPy Correlation: {0.5417731333268474}")

# 2. Correlation and p-value using SciPy
correlation_scipy, p_value = stats.pearsonr(df6['645'], df6['Moist'])
print(f"SciPy Correlation: {correlation_scipy}, P-value: {p_value}")

# 3. Linear Regression using SciPy (to get the equation)
slope, intercept, r_value, p_value, std_err = stats.linregress(df6['645'], df6['Moist'])
print(f"Slope: {slope}, Intercept: {intercept}")
print(f"Equation: y = {slope:.5f}x + {intercept:.5f}") # formatted equation
print(f"R-squared: {r_value**2}")

# 4. Linear regression using numpy.polyfit
coefficients = np.polyfit(df6['645'], df6['Moist'],1)
slope_np = coefficients[0]
intercept_np = coefficients[1]
print(f"Numpy polyfit Slope: {slope_np}, Intercept: {intercept_np}")
print(f"Equation of correlation between 645nm and Moist: y = {slope_np:.5f}x + {intercept_np:.5f}")

# 5. Correlation using Pandas (if you have data in a DataFrame)
data = {'x': df6['645'], 'y': df6['Moist']}
df = pd.DataFrame(data)
correlation_pd = df['x'].corr(df['y'])
print(f"Pandas Correlation: {correlation_pd}")

print(f"NumPy Correlation: {0.6516821537521028}")

# 2. Correlation and p-value using SciPy
correlation_scipy, p_value = stats.pearsonr(df6['645'], df6['Nitro (mg/10 g)'])
print(f"SciPy Correlation: {correlation_scipy}, P-value: {p_value}")

# 3. Linear Regression using SciPy (to get the equation)
slope, intercept, r_value, p_value, std_err = stats.linregress(df6['645'], df6['Nitro (mg/10 g)'])
print(f"Slope: {slope}, Intercept: {intercept}")
print(f"Equation: y = {slope:.5f}x + {intercept:.5f}") # formatted equation
print(f"R-squared: {r_value**2}")

# 4. Linear regression using numpy.polyfit
coefficients = np.polyfit(df6['645'], df6['Nitro (mg/10 g)'],1)
slope_np = coefficients[0]
intercept_np = coefficients[1]
print(f"Numpy polyfit Slope: {slope_np}, Intercept: {intercept_np}")
print(f"Equation of correlation between 645nm and Moist: y = {slope_np:.5f}x + {intercept_np:.5f}")

# 5. Correlation using Pandas (if you have data in a DataFrame)
data = {'x': df6['645'], 'y': df6['Nitro (mg/10 g)']}
df = pd.DataFrame(data)
correlation_pd = df['x'].corr(df['y'])
print(f"Pandas Correlation: {correlation_pd}")


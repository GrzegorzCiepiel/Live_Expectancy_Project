import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('all_data.csv')
print(df.info())
print(df.describe())

#Has life expectancy increased over time in the six nations?
#Has GDP increased over time in the six nations?
#Is there a correlation between GDP and life expectancy of a country?
#What is the average life expectancy in these nations?
#What is the distribution of that life expectancy?
#1
df = df.rename(columns=({'Life expectancy at birth (years)': 'Life_exp'}))
print(df.head())

countries = (df.Country.unique())

le_chile = df.Life_exp[df.Country == 'Chile']
le_china = df.Life_exp[df.Country == 'China']
le_germany = df.Life_exp[df.Country == 'Germany']
le_mexico = df.Life_exp[df.Country == 'Mexico']
le_usa = df.Life_exp[df.Country == 'United States of America']
le_zimbabwe = df.Life_exp[df.Country == 'Zimbabwe']

plt.subplot(3,3,1)
plt.plot(df.Year.unique(), le_chile)
plt.title('Chile', fontsize=10)
plt.subplot(3,3,2)
plt.plot(df.Year.unique(), le_china)
plt.title('China', fontsize=10)
plt.subplot(3,3,3)
plt.plot(df.Year.unique(), le_germany)
plt.title('Germany', fontsize=10)
plt.subplot(3,3,4)
plt.plot(df.Year.unique(), le_mexico)
plt.title('Mexico', fontsize=10)
plt.subplot(3,3,5)
plt.plot(df.Year.unique(), le_usa)
plt.title('USA', fontsize=10)
plt.subplot(3,3,6)
plt.plot(df.Year.unique(), le_zimbabwe)
plt.title('Zimbabwe', fontsize=10)
plt.subplots_adjust(wspace=0.30, hspace=0.50, bottom=0)

plt.show()
plt.clf()

min_chile = df.Life_exp[df.Country == 'Chile'].min()
print(min_chile)

for country in countries:
    print(f'During 15 years starting in 2000 the life expectancy at birth in {country} raised from'
          f' {df.Life_exp[df.Country == country].min()} to {df.Life_exp[df.Country == country].max()}.')


#2
gdp_chile = df.GDP[df.Country == 'Chile']
gdp_china = df.GDP[df.Country == 'China']
gdp_germany = df.GDP[df.Country == 'Germany']
gdp_mexico = df.GDP[df.Country == 'Mexico']
gdp_usa = df.GDP[df.Country == 'United States of America']
gdp_zimbabwe = df.GDP[df.Country == 'Zimbabwe']

plt.subplot(3,3,1)
plt.plot(df.Year.unique(), gdp_chile)
plt.title('Chile', fontsize=10)
plt.subplot(3,3,2)
plt.plot(df.Year.unique(), gdp_china)
plt.title('China', fontsize=10)
plt.subplot(3,3,3)
plt.plot(df.Year.unique(), gdp_germany)
plt.title('Germany', fontsize=10)
plt.subplot(3,3,4)
plt.plot(df.Year.unique(), gdp_mexico)
plt.title('Mexico', fontsize=10)
plt.subplot(3,3,5)
plt.plot(df.Year.unique(), gdp_usa)
plt.title('USA', fontsize=10)
plt.subplot(3,3,6)
plt.plot(df.Year.unique(), gdp_zimbabwe)
plt.title('Zimbabwe', fontsize=10)
plt.subplots_adjust(wspace=0.30, hspace=0.60, bottom=0)

plt.show()
plt.close('all')


for country in countries:
    print(f'During 15 years starting in 2000 the gross domestic product at birth in {country} raised from'
          f' {df.GDP[df.Country == country].min()} to {df.GDP[df.Country == country].max()}.')

#3

plt.subplot(3,3,1)
plt.scatter(gdp_chile, le_chile, s=10)
plt.title('Chile', fontsize=10)
plt.subplot(3,3,2)
plt.scatter(gdp_china, le_china, s=10)
plt.title('China', fontsize=10)
plt.subplot(3,3,3)
plt.scatter(gdp_germany, le_germany, s=10)
plt.title('Germany', fontsize=10)
plt.subplot(3,3,4)
plt.scatter(gdp_mexico, le_mexico, s=10)
plt.title('Mexico', fontsize=10)
plt.subplot(3,3,5)
plt.scatter(gdp_usa, le_usa, s=10)
plt.title('USA', fontsize=10)
plt.subplot(3,3,6)
plt.scatter(gdp_zimbabwe, le_zimbabwe, s=10)
plt.title('Zimbabwe', fontsize=10)
plt.subplots_adjust(wspace=0.30, hspace=0.60, bottom=0)
plt.show()
plt.clf()

#Correlation

print(pearsonr(gdp_chile, le_chile))


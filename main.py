import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt


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

plt.figure()
plt.subplot(3,3,1)
plt.plot(df.Year.unique(), le_chile, color='purple')
plt.title('Chile', fontsize=10)
plt.subplot(3,3,2)
plt.plot(df.Year.unique(), le_china, color='red')
plt.title('China', fontsize=10)
plt.subplot(3,3,3)
plt.plot(df.Year.unique(), le_germany, color='orange')
plt.title('Germany', fontsize=10)
plt.subplot(3,3,4)
plt.plot(df.Year.unique(), le_mexico, color='green')
plt.title('Mexico', fontsize=10)
plt.subplot(3,3,5)
plt.plot(df.Year.unique(), le_usa, color='gray')
plt.title('USA', fontsize=10)
plt.subplot(3,3,6)
plt.plot(df.Year.unique(), le_zimbabwe)
plt.title('Zimbabwe', fontsize=10)
plt.subplots_adjust(wspace=0.30, hspace=0.50, bottom=0)
plt.savefig("Live expectancy over time.png")
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

plt.figure()
plt.subplot(3,3,1)
plt.plot(df.Year.unique(), gdp_chile, color='purple')
plt.title('Chile', fontsize=10)
plt.subplot(3,3,2)
plt.plot(df.Year.unique(), gdp_china, color='red')
plt.title('China', fontsize=10)
plt.subplot(3,3,3)
plt.plot(df.Year.unique(), gdp_germany, color='orange')
plt.title('Germany', fontsize=10)
plt.subplot(3,3,4)
plt.plot(df.Year.unique(), gdp_mexico, color='green')
plt.title('Mexico', fontsize=10)
plt.subplot(3,3,5)
plt.plot(df.Year.unique(), gdp_usa, color='gray')
plt.title('USA', fontsize=10)
plt.subplot(3,3,6)
plt.plot(df.Year.unique(), gdp_zimbabwe)
plt.title('Zimbabwe', fontsize=10)
plt.subplots_adjust(wspace=0.30, hspace=0.60, bottom=0)
plt.savefig("GDP.png")
plt.show()
plt.close('all')


for country in countries:
    print(f'During 15 years starting in 2000 the gross domestic product in {country} raised from'
          f' {round((df.GDP[df.Country == country].min())/1000000000)} bln to {round((df.GDP[df.Country == country].max())/1000000000)} bln.')

#3
plt.figure()
plt.subplot(3,3,1)
plt.scatter(gdp_chile, le_chile, s=10, color='purple')
plt.title('Chile', fontsize=10)
plt.subplot(3,3,2)
plt.scatter(gdp_china, le_china, s=10, color="red")
plt.title('China', fontsize=10)
plt.subplot(3,3,3)
plt.scatter(gdp_germany, le_germany, s=10, color='orange')
plt.title('Germany', fontsize=10)
plt.subplot(3,3,4)
plt.scatter(gdp_mexico, le_mexico, s=10, color='green')
plt.title('Mexico', fontsize=10)
plt.subplot(3,3,5)
plt.scatter(gdp_usa, le_usa, s=10, color='gray')
plt.title('USA', fontsize=10)
plt.subplot(3,3,6)
plt.scatter(gdp_zimbabwe, le_zimbabwe, s=10)
plt.title('Zimbabwe', fontsize=10)
plt.subplots_adjust(wspace=0.30, hspace=0.60, bottom=0)
plt.savefig("Live expectancy vs GDP.png")
plt.show()
plt.clf()

#4
mean_life = []
for country in countries:
    print(f'Average live expectancy in {country} is {round((df.Life_exp[df.Country == country].mean()),2)} years.')
    mean_life.append(round((df.Life_exp[df.Country == country].mean()),2))

print(countries)

colors = ['lightblue', 'CornflowerBlue', 'blue', 'DarkBlue', 'purple', 'DarkOrchid']
plt.figure()
plt.bar(countries, mean_life, color=colors)
plt.title("Average live expectancy in years")
ax = plt.subplot()
ax.set_xticks(range(6))
ax.set_xticklabels(['Chile', 'China', 'Germany', 'Mexico', 'USA', 'Zimbabwe'])
plt.savefig("barplot.png")
plt.show()
plt.clf()

#5
plt.figure()
plt.subplot(3,3,1)
v1 = plt.violinplot(le_chile, showmeans=True)
for pc in v1['bodies']:
    pc.set_facecolor('purple')
    pc.set_edgecolor('black')
plt.title('Chile', fontsize=10)
plt.subplot(3,3,2)
v2 = plt.violinplot(le_china, showmeans=True)
for pc in v2['bodies']:
    pc.set_facecolor('red')
    pc.set_edgecolor('black')
plt.title('China', fontsize=10)
plt.subplot(3,3,3)
v3 = plt.violinplot(le_germany, showmeans=True)
for pc in v3['bodies']:
    pc.set_facecolor('orange')
    pc.set_edgecolor('black')
plt.title('Germany', fontsize=10)
plt.subplot(3,3,4)
v4 = plt.violinplot(le_mexico, showmeans=True)
for pc in v4['bodies']:
    pc.set_facecolor('green')
    pc.set_edgecolor('black')
plt.title('Mexico', fontsize=10)
plt.subplot(3,3,5)
v5 = plt.violinplot(le_usa, showmeans=True)
for pc in v5['bodies']:
    pc.set_facecolor('gray')
    pc.set_edgecolor('black')
plt.title('USA', fontsize=10)
plt.subplot(3,3,6)
v6 = plt.violinplot(le_zimbabwe, showmeans=True )
plt.title('Zimbabwe', fontsize=10)
plt.subplots_adjust(wspace=0.30, hspace=0.50, bottom=0)
plt.savefig("Live expectancy distribution.png")
plt.show()
plt.clf()

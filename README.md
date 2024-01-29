# Live expectancy analyse

## Introduction

In this projekt I analyze data on GDP and life expectancy from the World Health Organization and the World Bank to try and identify the relationship between the GDP and life expectancy of six countries.
I use python 3.11 with pandas and matplotlib.pyplot modules.

There are 5 main questions to answer:
+ Has life expectancy increased over time in the six nations?
+ Has GDP increased over time in the six nations?
+ Is there a correlation between GDP and life expectancy of a country?
+ What is the average life expectancy in these nations?
+ What is the distribution of that life expectancy?

## Analyse

1. Has life expectancy increased over time in the six nations?

To answer this question I plot a line showing the change of live expectancy over time in every country:

![Live expectancy over time](https://github.com/GrzegorzCiepiel/Live_Expectancy_Project/assets/135313652/7cf69d7a-8c67-428e-a007-a3e969185011)

As we can see ***live expectancy increaset*** over time in every country.

Over 15 years starting in 2000 the life expectancy at birth in:
+ Chile raised from 77.3 to 80.5.
+ China raised from 71.7 to 76.1.
+ Germany raised from 78.0 to 81.0.
+ Mexico raised from 74.8 to 76.7.
+ United States of America raised from 76.8 to 79.3.
+ Zimbabwe raised from 44.3 to 60.7.

2. Has GDP increased over time in the six nations?

To answer this question I plot a line showing the change of gross domestic product over time in every country:
![GDP](https://github.com/GrzegorzCiepiel/Live_Expectancy_Project/assets/135313652/fcb2bb34-c4a6-4ed4-b6e8-f3c8b77b9076)

As we can see, this time also ***gross domestic product increaset*** over time in every country.

Over15 years starting in 2000 the gross domestic product in 
+ Chile raised from 70 bln to 278 bln.
+ China raised from 1211 bln to 11065 bln.
+ Germany raised from 1950 bln to 3891 bln.
+ Mexico raised from 684 bln to 1298 bln.
+ United States of America raised from 10300 bln to 18100 bln.
+ Zimbabwe raised from 4 bln to 16 bln.

3. Is there a correlation between GDP and life expectancy of a country?

To answer this question I prepared scatterplot between live expectancy and GDP values for every country:
![Live expectancy vs GDP](https://github.com/GrzegorzCiepiel/Live_Expectancy_Project/assets/135313652/259e8706-06f3-467b-88ec-591dd7f509b4)

As we can see ***there is positive correlation*** between live expectancy in GDP in each surveyed country.

4. What is the average life expectancy in these nations?

To answer this question I had to count mean value of all le values from each country.
I plot the results as a boxplot to compare easily:
![barplot](https://github.com/GrzegorzCiepiel/Live_Expectancy_Project/assets/135313652/8657a63c-fc84-4595-ab05-b99c667b26a2)

As we can see the mean live expectancy is significantly lower in Zimbabwe.  This country represents also the lowest GDP.

5. What is the distribution of that life expectancy?

To answer this question I plot live expectancy values as a violinplot:
![Live expectancy distribution](https://github.com/GrzegorzCiepiel/Live_Expectancy_Project/assets/135313652/dd6047a1-7d21-4231-b339-3db7c92e1dd2)

At first it is significant that the samples are small.
When interpreting the above graphs, it is also worth referr to the change in live expectancy over time.
In China the growth of live expectancy from 72 to 74 years was very fast. that is why wy have more values over 74 years.

In Zimbabwe the live expectancy  dropped in first years and then started to grow. That is why we have more lower values and the mean value also in lower part of the plot.

## Conclusions

From 2000 to 2015 for 6 countries:
+ Chile
+ China
+ Germany
+ Mexico
+ USA
+ Zimbabwe
***live expectancy increaset*** over time in every country and it is clearly correlated with growth of gross domestic product.
 The mean live expectancy is significantly lower in Zimbabwe and started to grow later than in other mentioned countries.  This country represents also the lowest GDP.





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
import statsmodels.formula.api as sm
import seaborn as sns
import requests
import math as m
from scipy import stats
from datetime import datetime

f = open("C:/Users/kmes9/vscode/python/AnIntro_Statistics_Python/Data/babyboom.dat.txt") 
all = []
lines = f.readlines()  # read each line in the file, and covert to array
for line in lines:
    #print(line.split())
    all.append(line.split())
f.close()
#print(all)
Time = []
Sex = []
Weight = []
BirthTime = []

# covert data into integer
for i in range(len(all)):
    Time.append(int(all[i][0]))
    Sex.append(int(all[i][1]))
    Weight.append(int(all[i][2]))
    BirthTime.append(int(all[i][3]))

# covert data into dataframe
df = pd.DataFrame({
    "Sex":Sex,
    "Weight":Weight,
    "BirthTime":BirthTime,
    
},index=Time)
#data frame for boys and girls
df_g = df[df['Sex']==1]
df_b = df[df['Sex']==2]
#print(df)

t = []
bt= list(df['BirthTime'])
bnum = []
for i in range(len(bt)):
    t.append(bt[i]//60)

k = 0
t_24hr = list(np.arange(0,24))
for i in range(len(t_24hr)):
    k = 0
    for j in range(len(t)):
        if t[j] == t_24hr[i]:
            k = k + 1
    bnum.append(k)
print(bnum)
lam =  [1, 2, 5, 11, 22, 44]
fig, ax = plt.subplots(1,6)
for i in range(len(lam)):
  ax[i].plot(t_24hr, stats.poisson.pmf(bnum,lam[i]))
  ax[i].set_xlim(0,24)
  ax[i].set_xticks(t_24hr)


plt.show()

'''
# perform the binomial distribution
# the probability of born girls and boys is 0.5, and there are 44 births
(p, num) = (0.5, 44)
binomDist = stats.binom(num, p)
pmf = binomDist.pmf(np.arange(num+1))
x = np.arange(num+1)
fig, ax = plt.subplots()
ax.set_xlabel('Number of girls')
ax.set_ylabel('PMF')
        
ax.plot(x,pmf,marker='s') 
print(f'the probability of get 22 girls/boys (excepted numbers) is %.2f percent' %(pmf[22]*100))
print(f'the probability of get 18 girls is %.2f percent' %(pmf[18]*100))
print(f'the probability of get 26 boys is %.2f percent' %(pmf[26]*100))
plt.show()'''


'''B. Probability Distributions & Fitting
   * Binomial Distribution: Model the proportion of boys vs. girls out of 44 births and perform binomial tests
     (scipy.stats.binom).
   * Poisson Distribution: Analyze the number of births per hour across the 24-hour period and fit a Poisson model to test
     for Poisson process assumptions (scipy.stats.poisson).
   * Exponential / Geometric Distributions: 
     * Calculate the time intervals (inter-arrival times) between consecutive births and fit an exponential distribution
       (scipy.stats.expon).
     * Model the number of births until a specific gender appears using a geometric distribution (scipy.stats.geom).
   * Normality Testing: Test whether birth weights follow a normal distribution overall versus separately by sex using the
     Shapiro-Wilk test (scipy.stats.shapiro).'''
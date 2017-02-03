import pandas as pd

#imports data file
mpg = pd.readcsv("jp-us-mpg.dat", delim_whitespace = True)
mpg.head()
mpg.tail()


from nupy import mean

#Drops missing and finds mean
mean(mpg["Japan"].dropna())
mean(mpg["US"].drop.na())

from numpy import var
us = mpg["US"].dropna()
jp = mpg["Japan"].dropna()
jp_var = var(jp) (len(jp) / float(len(jp) - 1)
us_var = var(us) (len(us) / float(len(jp) - 1) 


summation : (xsubi - mean)^2 / (n-1)
(20.1 - 30.5) / (sqrt((41.1/149) + (37.3/79))) = 12/94

P avelue
#Two sided ptest
2* (1.0  - t.cdf(abs(12.946), 136.8750))
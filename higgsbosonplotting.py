# This is needed to create the fit
from scipy.stats import norm

import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# Let's choose Dimuon_DoubleMu.csv 
data = pd.read_csv('http://opendata.cern.ch/record/545/files/Dimuon_DoubleMu.csv')

# And save the invariant masses to iMass
iMass = data['M']

# Plus draw the histogram
n, bins, patches = plt.hist(iMass, 300, facecolor='g')
plt.xlabel('Invariant Mass (GeV)')
plt.ylabel('Amount')
plt.title('Histogram of the invariant masses')

plt.show()

# Bump around 90GeV's
min = 85
max = 97

# Let's crop the area. croMass now includes all the masses between the values of min and max
croMass = iMass[(min < iMass) & (iMass < max)]

# Calculate the mean (µ) and standard deviation (sigma) of normal distribution using norm.fit-function from scipy
(mu, sigma) = norm.fit(croMass)

# Histogram of the cropped data. Note that the data is normalized (density = 1)
n, bins, patches = plt.hist(croMass, 300, density = 1, facecolor='g')

#mlab.normpdf calculates the normal distribution's y-value with given µ and sigma
# let's also draw the distribution to the same image with histogram
y = norm.pdf(bins, mu, sigma)
l = plt.plot(bins, y, 'r-.', linewidth=3)


plt.xlabel('Invarian Mass(GeV)')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram \ and\ fit,\ where:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))

plt.show()

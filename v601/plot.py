import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Weglänge
T = np.genfromtxt('content/Temperatur.txt', unpack=True)

<<<<<<< HEAD
T = T+273.15
print("T = ", T)
ps = 5.5 * 10**7 * np.exp(-6876/T)
print("psät= " , ps)
w =0.0029/ps
print("w = ", w)
#Weglänge ende
||||||| 8d653d6

#Weglänge ende
=======

#Weglänge ende


########
>>>>>>> f548493a7ad1b0c1b3e1fbac61cf5a70b5bb2df5

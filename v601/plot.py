import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Weglänge
T = np.genfromtxt('content/Temperatur.txt', unpack=True)

T = T+273.15
print("T = ", T)
ps = 5.5 * 10**7 * np.exp(-6876/T)
print("psät= " , ps)
w =0.0029/ps
print("w = ", w)
#Weglänge ende
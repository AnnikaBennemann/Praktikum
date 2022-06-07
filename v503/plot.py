import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

U, R, t0, tauf, tauff, tab, tabf  = np.genfromtxt('content/Werte.txt', unpack=True)

v0 = 0.5/t0
tauf= unp.uarray(tauf,tauff)
vauf= 0.5/tauf
tab= unp.uarray(tab,tabf)
vab= 0.5/tab


Bed = 2* v0 /(vab-vauf)


print('v0 = ', v0)
print('vauf = ', vauf)
print('vab = ', vab)
print('Bedingung = ', Bed)




import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat

f, U_c , t = np.genfromtxt('Werte.txt', unpack=True)
U_0=9
t=t*10**-3 # zeit in s
phase= t*f*360
print(phase)


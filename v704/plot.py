import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import tools

d , t, N, sigmaN = np.genfromtxt('content/WerteEisen.txt', unpack=True)

Nt= N/t 
sigmaNt=sigmaN/t

print('Nt= ',Nt)
print('sigmaNt= ',sigmaNt)

db , tb, Nb, sigmaNb = np.genfromtxt('content/WerteBlei.txt', unpack=True)

Ntb= Nb/tb 
sigmaNtb=sigmaNb/tb

print('Ntb= ',Ntb)
print('sigmaNtb= ',sigmaNtb)


#Betastrahlung

d, t, N, Nerror, A, Aerror= np.genfromtxt('content/beta.txt', unpack=True)
R = d*1e-6 # Massenbelegung



print('a1 =', a1)
print('b1 =', b1)
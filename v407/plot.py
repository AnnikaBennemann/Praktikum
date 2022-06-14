import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

I_0 = 0.13*10**(-3)
I_dunkel = 5.9*10**(-9)

g, Is = np.genfromtxt('content/senkrecht.txt', unpack=True)
g, Ip = np.genfromtxt('content/parallel.txt', unpack=True)

I_s = Is*10**(-6) - I_dunkel
I_p = Ip*10**(-6) - I_dunkel


def n_spol(a, E):                                                                       # E = E_r/E_e = sqrt(I_r/I_0)
    return np.sqrt((2*E*np.cos(2*a)+ E**2 + 1)/(1-2*E + E**2))

n_s = n_spol(g*np.pi/180, np.sqrt(I_s/I_0))
print("n_s = ", (n_s))
n_s_mean = np.mean(n_s[n_s < 14])
print("mean: " ,n_s_mean)
n_s_std = np.std(n_s[n_s < 14])
print("std: " ,n_s_std)
n_s_err = ufloat(n_s_mean, np.std(n_s[n_s < 14]))
print("s-polarisiert: ", n_s_err)
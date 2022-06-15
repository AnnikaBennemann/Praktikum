import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

##################################### Brewster Winkel ###################################################

# Brechungsindex n aus Brewster Winkel
# Brewster-Winkel bei Minimum von I_p --> 75°

n_brewster = np.tan(75*np.pi/180)
print("Brewster: ", n_brewster)


I_0 = 0.18*10**(-3)
I_dunkel = 5.9*10**(-9)

g, Is = np.genfromtxt('content/senkrecht.txt', unpack=True)
g, Ip = np.genfromtxt('content/parallel.txt', unpack=True)

I_s = Is*10**(-6) - I_dunkel
I_p = Ip*10**(-6) - I_dunkel

#senkrecht
def n_spol(a, E):                                                                       # E = E_r/E_e = sqrt(I_r/I_0)
    return np.sqrt((2*E*np.cos(2*a)+ E**2 + 1)/(1-2*E + E**2))

n_s = n_spol(g*np.pi/180, np.sqrt(I_s/I_0))
print("n_s = ", (n_s))
n_s_mean = np.mean(n_s[n_s < 4.5])
print("mean: " ,n_s_mean)
n_s_std = np.std(n_s[n_s < 4.5])
print("std: " ,n_s_std)
n_s_err = ufloat(n_s_mean, np.std(n_s[n_s < 4.5]))
print("s-polarisiert: ", n_s_err)
np.savetxt("content/n_s.txt", n_s, fmt = '%.4f')


# parallel
def n_ppol(a, E):
    b = ((E+1)/(E-1))**2
    return np.sqrt(b/(2*np.cos(a)**2) + np.sqrt(b**2/(4*np.cos(a)**4) - b*np.tan(a)**2))

n_p = n_ppol(g*np.pi/180, np.sqrt(I_p/I_0))
print("n_p = ", (n_p))
n_p_mean =  np.mean(n_p[n_p < 4.5])
print("mean: " ,n_p_mean)
n_p_std = np.std(n_p[n_p < 4.5])
print("std: " ,n_p_std)
n_p_err = ufloat(n_p_mean, np.std(n_p[n_p < 4.5]))
print("p-polarisiert: ", n_p_err)  
np.savetxt("content/n_p.txt", n_p, fmt = '%.4f')
############################ Plots ###################################

def KurveS(a, n):
    return -(np.cos(a*np.pi/180) - np.sqrt(n**2-np.sin(a*np.pi/180)**2)) / (np.cos(a*np.pi/180) + np.sqrt(n**2-np.sin(a*np.pi/180)**2))

def KurveP(a, n):
    return (n**2*np.cos(a*np.pi/180) - np.sqrt(n**2-np.sin(a*np.pi/180)**2)) / (n**2*np.cos(a*np.pi/180) + np.sqrt(n**2-np.sin(a*np.pi/180)**2))   

alpha_B = 75 # 73.390 Brewster Winkel
alpha = np.linspace(0, 90, 1000)
alpha_1 = np.linspace(0, alpha_B, 1000)
alpha_2 = np.linspace(alpha_B, 90, 1000)

plt.plot(alpha, KurveS(alpha, n_s_mean), color = "cornflowerblue", label = "Theoriekurve s-polarisiert")
plt.plot(alpha_1, KurveP(alpha_1, n_p_mean), color = "forestgreen", label = "Theoriekurve p-polarisiert")
plt.plot(alpha_2, -KurveP(alpha_2, n_p_mean), color = "forestgreen")

plt.plot(g, np.sqrt(I_s/I_0), marker = "x", color = "firebrick", linewidth = 0, label = "Messwerte s-polarisiert")
plt.plot(g, np.sqrt(I_p/I_0), marker = "+", markersize = 8, color = "coral", linewidth = 0, label = "Messwerte p-polarisiert")

plt.grid()
plt.xlabel(r"$\alpha \mathbin{/} °$")
plt.ylabel(r"$\sqrt{I_\text{r} \mathbin{/} I_0}$")
plt.xlim(0, 90)
plt.ylim(0, 1)
plt.legend()
plt.tight_layout()
plt.savefig("build/plot.pdf")
  
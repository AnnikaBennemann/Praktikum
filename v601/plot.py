import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
from mpl_toolkits.axes_grid.axislines import SubplotZero

#Weglänge
T = np.genfromtxt('content/Temperatur.txt', unpack=True)

T = T+273.15
print("T = ", T)
ps = 5.5 * 10**7 * np.exp(-6876/T)
print("psät= " , ps)
w =0.0029/ps
print("w = ", w)
aw = 1/w 
print("aw = ", aw)
#Weglänge ende

#######Franck

###169
x3, y3 = np.genfromtxt('content/Fr169.txt', unpack=True)
x4, y4 = np.genfromtxt('content/Fr179.txt', unpack=True)

plt.figure(3)
plt.plot(x3, y3, 'r-', label=r'$T_1=\qty{169}{\celsius}$')
plt.plot(x4, y4, 'b-', label=r'$T_2=\qty{179}{\celsius}$')
plt.xlabel(r'$U_A / \si{\volt}$')
plt.ylabel(r'$I_A / $Kästchen')
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot3.pdf')
##############plot 


x1, y1 = np.genfromtxt('content/energie23.txt', unpack=True)
x2, y2 = np.genfromtxt('content/energie143.txt', unpack=True)

#matplotlib installiert?

plt.figure(1)
plt.plot(x1, y1, 'r-', label=r'$T_1=\qty{23.3}{\celsius}$')
plt.plot(x2, y2, 'b-', label=r'$T_2=\qty{143}{\celsius}$')
plt.xlabel(r'$U_A / \si{\volt}$')
plt.ylabel(r'$I_A / $Kästchen')
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')



dif1 = np.diff(y1)/np.diff(x1)
x_plot1= np.delete(x1,[70])
dif2 = np.diff(y2)/np.diff(x2)
x_plot2= np.delete(x2,[59])

plt.figure(2)
plt.plot(x_plot1, dif1, 'r-', label=r'$T_1=\qty{23.3}{\celsius}$')
plt.plot(x_plot2, dif2, 'b-', label=r'$T_2=\qty{143}{\celsius}$')
plt.xlabel(r'$U_A / \si{\volt}$')
plt.ylabel(r'$I_A´ / $Kästchen')
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf')

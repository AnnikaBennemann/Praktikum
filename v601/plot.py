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
#Weglänge ende


##############plot 


x1, y1 = np.genfromtxt('content/energie23.txt', unpack=True)
x2, y2 = np.genfromtxt('content/energie143.txt', unpack=True)

#matplotlib installiert?

plt.figure(1)
plt.plot(x1, y1, 'b-', label=r'$T_1=\qty{23.3}{\celsius}$')
plt.plot(x2, y2, 'r-', label=r'$T_2=\qty{143}{\celsius}$')
plt.xlabel(r'$U_A / \si{\volt}$')
plt.ylabel(r'$I_A / $Kästchen')
ax = plt.gca()
#ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
plt.grid()
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot1.pdf')



dif1 = np.diff(y1)/np.diff(x1)
x_plot1= np.delete(x1,[70])
dif2 = np.diff(y2)/np.diff(x2)
x_plot2= np.delete(x2,[59])

plt.figure(2)
plt.plot(x_plot1, dif1, 'b-', label=r'$T_1=\qty{23.3}{\celsius}$')
plt.plot(x_plot2, dif2, 'r-', label=r'$T_2=\qty{143}{\celsius}$')
plt.xlabel(r'$U_A / \si{\volt}$')
plt.ylabel(r'$I_A´ / $Kästchen')
plt.grid()
ax = plt.gca()
#ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/plot2.pdf') 

minx1= np.min(dif1)
ymin= np.where(dif1 == minx1)
print('ymin =' , minx1)
print('xmin =' , x1[ymin])
minx2= np.min(dif2)
ymin2= np.where(dif2 == minx2)
print('ymin2 =' , minx2)
print('xmin2 =' , x2[ymin2])
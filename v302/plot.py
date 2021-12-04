import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)
from scipy import stats
from scipy.optimize import curve_fit


v, U_Br = np.genfromtxt('content/Messwerte.txt', unpack=True)

v_0 = 241.14
y = U_Br/10 #U_Br / U_S

def f(w):
    return np.sqrt((w**2-1)**2/(9*((1-w**2)**2+9*w**2)))

    
#### noch rausfinden v_0, cov = curve_fit(f, v, U, p0=(v_0))

x=np.linspace(0.07,100, 20000)
z=(f(x))


plt.figure()
plt.plot(v/v_0, y,'rx', label='Messdaten')
plt.plot(x,np.sqrt((x**2-1)**2/(9*((1-x**2)**2+9*x**2))) , 'c', label='Theoretische Werte')
plt.xscale('log')
plt.xlabel(r'$\Omega = \nu \mathbin{/} \nu_0$')
plt.ylabel(r'$U_Br \mathbin{/} U_S$')
plt.legend(loc='best')
plt.grid()


# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')



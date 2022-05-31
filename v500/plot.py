import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

def f (x, m, b):
    return m*x+b


Uge, Ige  = np.genfromtxt('content/gelb.txt', unpack=True)


plt.figure(1)
plt.plot(Uge, Ige, 'yx', label='Messdaten gelb')
plt.ylabel(r'$I \mathbin{/} \si{\nano\ampere}$')
plt.xlabel(r'U $\mathbin{/} \si{\V}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot1.pdf')

Uge, Ige  = np.genfromtxt('content/gelb.txt', unpack=True)

Ige = np.sqrt(Ige)
Uge= Uge[0:6]
Ige = Ige[0:6]
params, cov = np.polyfit(Uge, Ige, deg=1, cov=True)
errors = np.sqrt(np.diag(cov))

age = ufloat(params[0], errors[0])
bge = ufloat(params[1], errors[1])
N = -bge/age
 
print('age =', params[0], '±', errors[0])
print('bge =', params[1], '±', errors[1])
print(f'Nge = {N:.3f}')

z = np.linspace(np.min(Uge)-0.1, np.max(Uge)+0.1)

plt.figure(6)
plt.plot(Uge, Ige, 'kx', label='Messdaten gelb')
plt.plot(z, f(z, *params), 'y-', label='Ausgleichsgerade')
plt.ylabel(r'$\sqrt{I} \mathbin{/} \sqrt{\si{\nano\ampere}}$')
plt.xlabel(r'U $\mathbin{/} \si{\V}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot1b.pdf')


Ugr, Igr  = np.genfromtxt('content/grün.txt', unpack=True)

params, cov = np.polyfit(Ugr, np.sqrt(Igr), deg=1, cov=True)
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
N = -b/a
 
print('agr =', params[0], '±', errors[0])
print('bgr =', params[1], '±', errors[1])
print(f'Ngr = {N:.3f}')

z = np.linspace(np.min(Ugr)-0.1, np.max(Ugr)+0.1)

plt.figure(2)
plt.plot(Ugr, np.sqrt(Igr), 'kx', label='Messdaten grün')
plt.plot(z, f(z, *params), 'g-', label='Ausgleichsgerade')
plt.ylabel(r'$\sqrt{I} \mathbin{/} \sqrt{\si{\nano\ampere}}$')
plt.xlabel(r'U $\mathbin{/} \si{\V}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot2.pdf')


Ubl, Ibl  = np.genfromtxt('content/blau.txt', unpack=True)

params, cov = np.polyfit(Ubl, np.sqrt(Ibl), deg=1, cov=True)
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
N = -b/a

print('abl =', params[0], '±', errors[0])
print('bbl =', params[1], '±', errors[1])
print(f'Nbl = {N:.3f}')

z = np.linspace(np.min(Ubl)-0.1, np.max(Ubl)+0.1)

plt.figure(3)
plt.plot(Ubl, np.sqrt(Ibl), 'kx', label='Messdaten blau')
plt.plot(z, f(z, *params), 'b-', label='Ausgleichsgerade')
plt.ylabel(r'$\sqrt{I} \mathbin{/} \sqrt{\si{\nano\ampere}}$')
plt.xlabel(r'U $\mathbin{/} \si{\V}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot3.pdf')


Uvi, Ivi  = np.genfromtxt('content/violett.txt', unpack=True)

params, cov = np.polyfit(Uvi, np.sqrt(Ivi), deg=1, cov=True)
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
N = -b/a

print('avi =', params[0], '±', errors[0])
print('bvi =', params[1], '±', errors[1])
print(f'Nvi = {N:.3f}')

z = np.linspace(np.min(Uvi)-0.1, np.max(Uvi)+0.1)

plt.figure(4)
plt.plot(Uvi, np.sqrt(Ivi), 'kx', label='Messdaten violett')
plt.plot(z, f(z, *params), 'm-', label='Ausgleichsgerade')
plt.ylabel(r'$\sqrt{I} \mathbin{/} \sqrt{\si{\nano\ampere}}$')
plt.xlabel(r'U $\mathbin{/} \si{\V}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot4.pdf')


Ut, It  = np.genfromtxt('content/türkis.txt', unpack=True)

params, cov = np.polyfit(Ut, np.sqrt(It), deg=1, cov=True)
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])
N = -b/a

print('at =', params[0], '±', errors[0])
print('bt =', params[1], '±', errors[1])
print(f'Nt = {N:.3f}')

z = np.linspace(np.min(Ut)-0.2, np.max(Ut)+0.1)

plt.figure(5)
plt.plot(Ut, np.sqrt(It), 'kx', label='Messdaten türkis')
plt.plot(z, f(z, *params), 'c-', label='Ausgleichsgerade')
plt.ylabel(r'$\sqrt{I} \mathbin{/} \sqrt{\si{\nano\ampere}}$')
plt.xlabel(r'U $\mathbin{/} \si{\V}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot5.pdf')


nu = np.array([518.67, 549.07, 609.33, 689.18, 734.79])
U_g = np.array([-0.583, -0.730, -1.012, -1.313, -1.444])


params, cov = np.polyfit(nu, U_g, deg=1, cov=True)
errors = np.sqrt(np.diag(cov))

a = ufloat(params[0], errors[0])
b = ufloat(params[1], errors[1])

print('a =', params[0], '±', errors[0])
print('b =', params[1], '±', errors[1])

z = np.linspace(np.min(nu), np.max(nu))

plt.figure(7)
plt.plot(nu[0], U_g[0], 'yx', label='gelb')
plt.plot(nu[1], U_g[1], 'gx', label='grün')
plt.plot(nu[2], U_g[2], 'cx', label='türkis')
plt.plot(nu[3], U_g[3], 'bx', label='blau')
plt.plot(nu[4], U_g[4], 'mx', label='violett')
plt.plot(z, f(z, *params), 'k-', label='Ausgleichsgerade')
plt.ylabel(r'Grenzspannung $U_g \mathbin{/} \si{\volt}$')
plt.xlabel(r'Frequenz $\nu \mathbin{/} \si{\tera\hertz}$')
#plt.axvline(x=14.00, color='r', linestyle=':', label='Sollwinkel')
plt.grid()
plt.legend(loc='best')
plt.savefig('build/plot7.pdf')
import matplotlib.pyplot as plt
import numpy as np

x,y =np.genfromtxt("Runder_Stab_eins", unpack=True)
plt.plot(x,y)
x=np.linspace(0, 525)
y=np.linspace(0,4)
plt.show

x = np.linspace(0, 10, 1000)
y = x ** np.sin(x)

plt.subplot(1, 2, 1)
plt.plot(x, y, label='Kurve')
plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
plt.legend(loc='best')

plt.subplot(1, 2, 2)
plt.plot(x, y, label='Kurve')
plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

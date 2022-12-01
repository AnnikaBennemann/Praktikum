import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

Daten= np.genfromtxt('content/spektrum0.txt', unpack=True)

y_plot = np.linspace(0,120,120)


plt.figure(1)
plt.errorbar(y_plot, Daten[0:120], yerr=np.sqrt(Daten[0:120]), fmt='rx', elinewidth=0.7, label="Messdaten mit Fehlerbalken",markersize=3, capsize=1.5, markeredgewidth=0.5)
plt.xlabel('Kanal')
plt.ylabel('Anzahl an Impulse')
plt.grid()
plt.legend(loc='best', numpoints=1)
plt.tight_layout()
plt.savefig('build/plot1.pdf')


t= 300 #Messzeit das sie überall gleich ist und immer I / I0 gerechnet wird kann man sie auch weglassen
I0= 54433 #Wert ohne Würfel
dI0= 225 #Fehler ohne Würfel


P1, I1, dI1 = np.genfromtxt('content/1.txt', unpack=True) #Werte Würfel 1 nur Alu
P2, I2, dI2 = np.genfromtxt('content/2.txt', unpack=True) #Werte Würfel 2
P4, I4, dI4 = np.genfromtxt('content/4.txt', unpack=True) #Werte Würfel 4


mu_1 = np.log(I0/I1)/0.2, #Absorptionskoeffizient Alu
dmu_1 = np.log(dI0/dI1)/0.2

print('N= ', np.mean(I1), '+-', np.mean(dI1), #Net area Alu
    'mu_al = ',np.mean(mu_1),'+-', np.mean(dmu_1))

I0= np.mean(I1) #ab hier den Wert von Alu als I0 nutzen
dI0= np.mean(dI1)


def kleinsteQuadrate(y, W, A): 
    temp = np.dot(np.linalg.inv(np.dot(A.T, np.dot(W, A))), A.T) #.T transformiert die Matrix
    a = np.dot(temp, np.dot(W, y))
    a_err = np.linalg.inv(np.dot(A.T, np.dot(W, A)))
    return a, np.sqrt(np.diag(a_err))

b = np.sqrt(2)
A = np.matrix([ [1,0,0,1,0,0,1,0,0],
                [0,1,0,0,1,0,0,1,0],
                [0,0,1,0,0,1,0,0,1],
                [1,1,1,0,0,0,0,0,0],
                [0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,1,1,1],
                [0,b,0,0,0,b,0,0,0],
                [b,0,0,0,b,0,0,0,b],
                [0,0,0,b,0,0,0,b,0],
                [0,0,0,0,0,b,0,b,0],
                [0,0,b,0,b,0,b,0,0],
                [0,b,0,b,0,0,0,0,0]])



I_2 = np.log(I0/I2)

I_4 = np.log(I0/I4)


err_I_2 = np.sqrt((dI2 / I2)**2 + (dI0 / I0)**2)
err_I_4 = np.sqrt((dI4 / I4)**2 + (dI0 / I0)**2)

W_2 = np.diag(1/err_I_2**2)
W_4 = np.diag(1/err_I_4**2)

mu_2, err_mu_2 = kleinsteQuadrate(I_2, W=W_2, A=A)
mu_4, err_mu_4 = kleinsteQuadrate(I_4, W=W_4, A=A)


print('mu_2 = ', mu_2, '+-', err_mu_2 ) #da kommen komische Werte raus, ich weiß nur nicht ganz warum weil die Rechnug eigentlich passen sollte
print('mu_4 = ', mu_4, '+-', err_mu_4 )

print ('Mmu_2 = ', np.mean(mu_2) ,'+-', np.mean(err_mu_2))

mu_41= np.array([0.07994867  , 0.0869508,  0.16159825 , 0.1748935, 0.17845199 , 0.21111067])
mu_42 = np.array([0.9085538,0.91330119,0.69149193])
err_mu_41 = np.array([0.00651977 ,0.00661559, 0.0051716  , 0.00522895, 0.00657183,  0.00650554])
err_mu_42 = np.array([0.00555979, 0.00578365 ,0.00518344])
print ('Mmu_41 = ', np.mean(mu_41) ,'+-', np.mean(err_mu_41))
print ('Mmu_42 = ', np.mean(mu_42) ,'+-', np.mean(err_mu_42))
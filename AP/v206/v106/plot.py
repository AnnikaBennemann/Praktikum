import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

#Konstante Erdbeschleunigung
print('g', const.g)

#Werte auslesen
Tp63 , Tp36 = np.genfromtxt('content/gleichsinnig.txt', unpack=True)
Tm63 , Tm36 = np.genfromtxt('content/gegenseitig.txt', unpack=True)
Ts63 , Ts36 = np.genfromtxt('content/gekoppelt.txt', unpack=True)

#Werte durch 5 für eine Schwingungsdauer
Tp63 /=5
Tp36 /=5
Tm63 /=5
Tm36 /=5
Ts63 /=5
Ts36 /=5


#Funktionen definieren

#Messunsicherheit des Mittelwerts
mTp63  = ufloat(np.mean(Tp63) , np.std(Tp63) /np.sqrt(len(Tp63)))
mTp36  = ufloat(np.mean(Tp36) , np.std(Tp36) /np.sqrt(len(Tp36)))
mTm63  = ufloat(np.mean(Tm63) , np.std(Tm63) /np.sqrt(len(Tm63)))
mTm36  = ufloat(np.mean(Tm36) , np.std(Tm36) /np.sqrt(len(Tm36)))
mTs63  = ufloat(np.mean(Ts63) , np.std(Ts63) /np.sqrt(len(Ts63)))
mTs36  = ufloat(np.mean(Ts36) , np.std(Ts36) /np.sqrt(len(Ts36)))

wp63=2*np.pi/mTp63
wp36=2*np.pi/mTp36
wm63=2*np.pi/mTm63
wm36=2*np.pi/mTm36
ws63=wp63-wm63
ws36=wp36-wm36

print('Tp63', Tp63, 'Tp36', Tp36)
print('mTp63', mTp63, 'mTp36', mTp36)
print('wp63', wp63, 'wp36', wp36)
print('Tm63', Tm63, 'Tm36', Tm36)
print('mTm63', mTm63, 'mTm36', mTm36)
print('wm63', wm63, 'wm36', wm36)
print('Ts63', Ts63, 'Ts36', Ts36)
print('mTs63', mTs63, 'mTs36', mTs36)
print('ws63', ws63, 'ws36', ws36)


#Kopplungskonstante K
K63= ((mTp63**2-mTm63**2)/(mTp63**2+mTm63**2))
K36= ((mTp36**2-mTm36**2)/(mTp36**2+mTm36**2))
print('K63', K63, 'K36', K36)

#Theoriewerte
Tp63_theo= 2*np.pi*unp.sqrt(0.63/const.g)
Tp36_theo= 2*np.pi*unp.sqrt(0.36/const.g)
Tm63_theo= 2*np.pi*unp.sqrt(0.63/(const.g+2*K63))
Tm36_theo= 2*np.pi*unp.sqrt(0.36/(const.g+2*K36))
Ts63_theo= (Tp63_theo*Tm63_theo)/(Tp63_theo-Tm63_theo)
Ts36_theo= (Tp36_theo*Tm36_theo)/(Tp36_theo-Tm36_theo)
wp63_theo=unp.sqrt(const.g/0.63)
wp36_theo=unp.sqrt(const.g/0.36)
wm63_theo=unp.sqrt((const.g+2*K63)/0.63)
wm36_theo=unp.sqrt((const.g+2*K36)/0.36)
ws63_theo=wp63_theo-wm63_theo
ws36_theo=wp36_theo-wm36_theo

print('Tp63_theo', Tp63_theo, 'Tp36_theo', Tp36_theo)
print('wp63_theo', wp63_theo, 'wp36_theo', wp36_theo)
print('Tm63_theo', Tm63_theo, 'Tm36_theo', Tm36_theo)
print('wm63_theo', wm63_theo, 'wm36_theo', wm36_theo)
print('Ts63_theo', Ts63_theo)
print( 'Ts36_theo', Ts36_theo)
print('ws63_theo', ws63_theo, 'ws36_theo', ws36_theo)

#Abweichung vom Theoriewert

abw_Tp63=(mTp63-Tp63_theo)/Tp63_theo
abw_Tp36=(mTp36-Tp36_theo)/Tp36_theo
abw_Tm63=(mTm63-Tm63_theo)/Tm63_theo
abw_Tm36=(mTm36-Tm36_theo)/Tm36_theo
abw_Ts63=(mTs63-Ts63_theo)/Ts63_theo
abw_Ts36=(mTs36-Ts36_theo)/Ts36_theo

abw_wp63=(wp63-wp63_theo)/wp63_theo
abw_wp36=(wp36-wp36_theo)/wp36_theo
abw_wm63=(wm63-wm63_theo)/wm63_theo
abw_wm36=(wm36-wm36_theo)/wm36_theo
abw_ws63=(ws63-ws63_theo)/ws63_theo
abw_ws36=(ws36-ws36_theo)/ws36_theo

print('abw_Tp63', abw_Tp63, 'abw_Tp36', abw_Tp36)
print('abw_Tm63', abw_Tm63, 'abw_Tm36', abw_Tm36)
print('abw_Ts63', abw_Ts63, 'abw_Ts36', abw_Ts36)
print('abw_wp63', abw_wp63, 'abw_wp36', abw_wp36)
print('abw_wm63', abw_wm63, 'abw_wm36', abw_wm36)
print('abw_ws63', abw_ws63, 'abw_ws36', abw_ws36)

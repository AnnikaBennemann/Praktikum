import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat

def amplitudes(temp):
    maxs, _ = find_peaks(temp, distance = 15)
    mins, _ = find_peaks(-temp, distance = 30)
 
    print(maxs)
    print(mins)
    
    
    return maxs, mins
    


###### Statische Messung

n_stat, stat_1, stat_2, stat_3, stat_4, stat_5, stat_6, stat_7, stat_8 = np.genfromtxt('statisch.txt', unpack=True)

t_stat = n_stat*5 #Abtastrate 

stat_1 += 273.15 #Celsius in Kelvin
stat_2 += 273.15
stat_3 += 273.15
stat_4 += 273.15
stat_5 += 273.15
stat_6 += 273.15
stat_7 += 273.15
stat_8 += 273.15

### Plots
plt.figure()
plt.plot(t_stat, stat_1, label = 'Messing, breit')
plt.plot(t_stat, stat_4, label = 'Messing, schmal')

plt.xlabel('Zeit [s]')
plt.ylabel('Temperatur [K]')
plt.legend()

plt.savefig('verlauf_mess.pdf')
plt.clf()

plt.figure()
plt.plot(t_stat, stat_5, label = 'Aluminium')
plt.plot(t_stat, stat_8, label = 'Edelstahl')


plt.xlabel('Zeit [s]')
plt.ylabel('Temperatur [K]')
plt.legend()

plt.savefig('verlauf_alu_edel.pdf')
plt.clf()

plt.figure()
plt.plot(t_stat, stat_7 - stat_8, label = 'Temperaturdifferenz Edelstahl')

plt.xlabel('Zeit [s]')
plt.ylabel('Temperatur [K]')

plt.legend()

plt.savefig('differenz_edel.pdf')
plt.clf()

plt.figure()
plt.plot(t_stat, stat_2 - stat_1, label = 'Temperaturdifferenz Messing, breit')

plt.xlabel('Zeit [s]')
plt.ylabel('Temperatur [K]')

plt.legend()

plt.savefig('differenz_mess.pdf')
plt.clf()


### Wärmestrom
names = np.array(['Messing, breit', 'Messing, schmal', 'Aluminium', 'Edelstahl'])
temps = np.array([stat_1, stat_4, stat_5, stat_8])
diffs = np.array([stat_1 - stat_2, stat_3 - stat_4, stat_5 - stat_6, stat_7 - stat_8])

#Abstand der Thermoelemente
dx = 3 * 1e-2 

#Flächeninhalt der Stäbe
A = (1.2 * 1e-2) * (0.4 * 1e-2) 
A_schmal = (0.7 * 1e-2) * (0.4 * 1e-2)

#Werte aus Versuchsprotokoll
rho_mess = 8520 
rho_alu = 2800
rho_edel = 8000

c_mess = 385
c_alu = 830
c_edel = 400


### Wärmeleitfähigkeit

kappa_mess = 113
kappa_alu = 237
kappa_edel = 20

#arrays für später
n = np.array([9, 39, 69, 99, 129]) #Messpunkte
cs = np.array([c_mess, c_mess, c_alu, c_edel]) 
kappas = np.array([kappa_mess, kappa_mess, kappa_alu, kappa_edel])
As = np.array([A, A_schmal, A, A]) #Flächeninhalte

###Werte nach 650s

k = int(650 / 5)

print(f'Temp. nach 650: 1:{stat_1[k-1]:.3f}, schm:{stat_4[k-1]:.3f}, Alu:{stat_5[k-1]:.3f}, Edel:{stat_8[k-1]:.3f}')


### sachen in 5 versch. Zeiten

j = 0

for name, c, kappa, A, temp, diff in zip(names, cs, kappas, As, temps, diffs):
    print(f'{name}->')
    j = 0
    while j < 5:
        Qdt = - kappa * A * diff[n[j]]/dx
        print(f'{name}_Q: {Qdt:.3f}, diff: {diff[n[j]]:.3f}')
        j += 1


###### dynamische Messung, 80s
n_dyn1, dyn1_1, dyn1_2, dyn1_3, dyn1_4, dyn1_5, dyn1_6, dyn1_7, dyn1_8 = np.genfromtxt('dynamisch80.txt', unpack=True)
t_dyn1 = n_dyn1 * 2

dyn1_1 += 273.15
dyn1_2 += 273.15
dyn1_3 += 273.15
dyn1_4 += 273.15
dyn1_5 += 273.15
dyn1_6 += 273.15
dyn1_7 += 273.15
dyn1_8 += 273.15

plt.figure()
plt.plot(t_dyn1, dyn1_1, label = 'außen')
plt.plot(t_dyn1, dyn1_2, label = 'innen')

plt.xlabel('Zeit [s]')
plt.ylabel('Temperatur [K]')
plt.legend()

#plt.grid()
plt.savefig('dyn_80_mess.pdf')
plt.clf()

plt.figure()
plt.plot(t_dyn1, dyn1_4, label = 'außen')
plt.plot(t_dyn1, dyn1_5, label = 'innen')

plt.xlabel('Zeit [s]')
plt.ylabel('Temperatur [K]')
plt.legend()

#plt.grid()
plt.savefig('dyn_80_alu.pdf')
plt.clf()


#### get amplitudes and phase shift
#
#A1 = amplitudes(dyn1_1)
#A2 = amplitudes(dyn1_2)
#
#A6 = amplitudes(dyn1_6)
#A5 = amplitudes(dyn1_5)
#
#A1_max = np.array([ 32, 72, 110, 149, 189, 228, 268, 308, 348, 388])
#A1_min = np.array([ 45,  87, 127, 167, 207, 247, 287, 327, 368])
#A1 = dyn1_1[A1_max] - dyn1_1[A1_min]
#
#
#A2_max = np.array([ 22,  64, 103, 143, 183, 223, 263, 303, 343, 383])
#A2_min = np.array([ 42,  83, 123, 163, 203, 243, 282, 323, 363])
#A2 = dyn1_2[A2_max] - dyn1_2[A2_min]
#
#dt_12_ = (t_dyn1[A1_max] -  t_dyn1[A2_max])/4
#dt_12 = ufloat(np.mean(dt_12_), np.std(dt_12_, ddof=1))
#
#A1_m = ufloat(np.mean(A1), np.std(A1, ddof = 1))
#A2_m = ufloat(np.mean(A2), np.std(A2, ddof = 1))
#
#print(f'Phasendifferenz Messing {dt_12}, Amp 1 {A1_m}, 2 {A2_m}')
#
#A6_max = np.array([ 21,  63, 103, 142, 182, 222, 262, 302, 342, 382]) #Amplituden selbst eingefügt
#A6_min = np.array([ 42,  82, 123, 163, 202, 242, 282, 322, 362])
#A6 = dyn1_6[A6_max] - dyn1_6[A6_min]
#
#A5_max = np.array([ 26,  65, 106, 146, 186, 226, 265, 306, 345, 385])
#A5_min = np.array([ 44,  85, 125, 165, 205, 245, 285, 325, 365])
#
#A5 = (dyn1_5[A5_max] - dyn1_5[A5_min])
#print('a5', A5)
#
#A6_m = ufloat(np.mean(A6), np.std(A6, ddof=1))
#A5_m = ufloat(np.mean(A5), np.std(A5, ddof=1))
#
#print('a6', A6)
#
#dt_56_ = (t_dyn1[A5_max] -  t_dyn1[A6_max])/4
#dt_56 = ufloat(np.mean(dt_56_), np.std(dt_56_, ddof=1))
#print(f'Phasendifferenz Aluminium {dt_56}, Amp 5 {A5_m}, 6 {A6_m}')
#
#
#kappa_mess_ex = (rho_mess * c_mess * dx**2)/(2 * dt_12 * unp.log(A2_m/A1_m))
#kappa_alu_ex = (rho_alu * c_alu * dx**2)/(2 * dt_56 * unp.log(A6_m/A5_m))
#
#abw_me = 100 * (kappa_mess_ex - kappa_mess)/kappa_mess
#abw_al = 100 * (kappa_alu_ex - kappa_alu)/kappa_alu
#
#print(f'kappa Messing {kappa_mess_ex}, Abweichung {abw_me}')
#print(f'kappa Aluminium {kappa_alu_ex}, Abweichung {abw_al}')
#

###### dynamische Messung, 200s
n_dyn2, dyn2_1, dyn2_2, dyn2_3, dyn2_4, dyn2_5, dyn2_6, dyn2_7, dyn2_8 = np.genfromtxt('dynamisch200.txt', unpack = True)

t_dyn2 = n_dyn2 * 2

dyn2_1 += 273.15
dyn2_2 += 273.15
dyn2_3 += 273.15
dyn2_4 += 273.15
dyn2_5 += 273.15
dyn2_6 += 273.15
dyn2_7 += 273.15
dyn2_8 += 273.15

plt.figure()
plt.plot(t_dyn2, dyn2_7, label = 'außen')
plt.plot(t_dyn2, dyn2_8, label = 'innen')

plt.xlabel('Zeit [s]')
plt.ylabel('Temperatur [K]')
plt.legend()
#plt.grid()
plt.savefig('dyn_2.pdf')
plt.clf()

#plt.figure()
#plt.plot(t_dyn2, dyn2_8, label = 'innen')
#plt.xlabel('Zeit [s]')
#plt.ylabel('Temperatur [K]')
#plt.legend()
##plt.grid()
#plt.savefig('dyn_2_close.pdf')
#plt.clf()


### get amplitudes and phase shift

#A7 = amplitudes(dyn2_7)
#
#A7_max = np.array([ 53 153 252 352 452 552 653])
#A7_min = np.array([  1 102 203 303 403 503 603 703])
#A7 = dyn2_7[A7_max] - dyn2_7[A7_min]
#
#A7_m = ufloat(np.mean(A7), np.std(A7, ddof=1))
#
#A8 = amplitudes(dyn2_8)
##A8_max = np.array([ 85 185 279 377 477 575 673])Kommas dazu
##A8_min = np.array([ 13 115 216 317 419 520 620 720])Kommas dazu
##A8 = dyn2_8[A8_max] - dyn2_8[A8_min]
#
#A8_1 = np.array([29.5, 34, 37.1, 38.3, 40, 43.9])
#A8_2 = np.array([31.7, 37.7, 38, 39.1, 41,  44.9])
#
#A8 = A8_2 - A8_1
#
#A8_m = ufloat(np.mean(A8), np.std(A8, ddof=1))
#print('a8', A8_m, '; a7', A7_m)
#
#dt_78_ = np.array([80, 100, 77, 89, 91])
#
#dt_78 = ufloat(np.mean(dt_78_), np.std(dt_78_))
#
#kappa_edel_ex = (rho_edel * c_edel * dx**2)/(2 * 80 * unp.log(A7_m/A8_m))
#
#abw_ed = 100 * (kappa_edel_ex - kappa_edel)/kappa_edel
#print(f'delta t {dt_78}')
#print(f'kappa Edelstahl {kappa_edel_ex}, Abweichung {abw_ed}')
#
#
#### Wellenlänge und Frequenz

#lam_1 = unp.sqrt((4 * np.pi * kappa_mess_ex * 80)/(rho_mess * c_mess))
#lam_5 = unp.sqrt((4 * np.pi * kappa_alu_ex * 80)/(rho_alu * c_alu))
#lam_7 = unp.sqrt((4 * np.pi * kappa_edel_ex * 200)/(rho_edel * c_edel))
#
#lam_1_t = unp.sqrt((4 * np.pi * kappa_mess * 80)/(rho_mess * c_mess))
#lam_5_t = unp.sqrt((4 * np.pi * kappa_alu* 80)/(rho_alu * c_alu))
#lam_7_t = unp.sqrt((4 * np.pi * kappa_edel * 200)/(rho_edel * c_edel))
#
#abw_1 = 100 * (lam_1 - lam_1_t)/lam_1_t
#abw_2 = 100 * (lam_5 - lam_5_t)/lam_5_t
#abw_3 = 100 * (lam_7 - lam_7_t)/lam_7_t
#
#print(f'lambda: Messing {lam_1}, Alu {lam_5}, Edelstahl {lam_7}')
#print(f'lambda: Messing {lam_1_t}, Alu {lam_5_t}, Edelstahl {lam_7_t}')
#print(f'Abweichung: Messing {abw_1}, Alu {abw_2}, Edelstahl {abw_3}')
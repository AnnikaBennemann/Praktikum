import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat

def amplitudes(temp):
    maxs, _ = find_peaks(temp, distance = 15)
    mins, _ = find_peaks(-temp, distance = 30)
 
    print(f'{maxs,mins}')
   
    
    
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

### Wärmestrom
names = np.array(['Messing, breit', 'Messing, schmal', 'Aluminium', 'Edelstahl'])
temps = np.array([stat_1, stat_4, stat_5, stat_8])
diffs = np.array([stat_2 - stat_1, stat_3 - stat_4, stat_6 - stat_5, stat_7 - stat_8])

print("AAAAAAAH="stat_1)
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

### get amplitudes and phase shift

A1 = amplitudes(dyn1_1)
A2 = amplitudes(dyn1_2)

A6 = amplitudes(dyn1_6)
A5 = amplitudes(dyn1_5)

A1_max = np.array([ 32, 72, 110, 149, 189, 228, 268, 308, 348, 388]) #Werte aus Programmausgabe abgeschrieben
A1_maxx = dyn1_1[A1_max]
print(f'A1_maxx={A1_maxx}')

A1_maxx = np.array([310.93, 317.75, 322.19, 324.93, 327.29, 329.32, 330.87, 332.27, 333.35, 334.16])#Werte aus Programmausgabe abgeschrieben

A1_min = np.array([ 0, 45,  87, 127, 167, 207, 247, 287, 327, 368])#Werte aus Programmausgabe abgeschrieben
A1_minx = dyn1_1[A1_min]
print(f'A1_minx={A1_minx}')

A1_minx = ([300.51, 310.02, 316.05, 319.66, 322.07, 324.36, 326.05, 327.48, 328.84, 329.63])#Werte aus Programmausgabe abgeschrieben
A1 = (A1_maxx-A1_minx)/2

print(f'Amplituden Messing fern {A1}')

A2_max = np.array([ 22,  64, 103, 143, 183, 223, 263, 303, 343, 383])#Werte aus Programmausgabe abgeschrieben
A2_min = np.array([ 0, 42,  83, 123, 163, 203, 243, 282, 323, 363])#Werte aus Programmausgabe abgeschrieben
A2 = (dyn1_2[A2_max] - dyn1_2[A2_min])/2 #Amplitudenberechnung

print(f'Amplituden Messing nah {A2}')

dt_12_ = (t_dyn1[A1_max] -  t_dyn1[A2_max]) #Phasendifferenz
print(f'Phasendifferenzen Messing {dt_12_}')
dt_12 = ufloat(np.mean(dt_12_), np.std(dt_12_, ddof=1)) #Mittelwert Phasendifferenz mit Abweichung


A1_m = ufloat(np.mean(A1), np.std(A1, ddof = 1)) #Mittelwerte Amplituden mit Abweichungen
A2_m = ufloat(np.mean(A2), np.std(A2, ddof = 1))

print(f'Phasendifferenz Messing {dt_12:.3f}, Amp fern {A1_m:.3f}, nah {A2_m:.3f}')

A6_max = np.array([ 21,  63, 103, 142, 182, 222, 262, 302, 342, 382]) #Werte aus Programmausgabe abgeschrieben
A6_min = np.array([0, 42,  82, 123, 163, 202, 242, 282, 322, 362])#Werte aus Programmausgabe abgeschrieben
A6 = (dyn1_6[A6_max] - dyn1_6[A6_min])/2

A5_max = np.array([ 26,  65, 106, 146, 186, 226, 265, 306, 345, 385])#Werte aus Programmausgabe abgeschrieben
A5_min = np.array([0, 44,  85, 125, 165, 205, 245, 285, 325, 365])#Werte aus Programmausgabe abgeschrieben

A5 = (dyn1_5[A5_max] - dyn1_5[A5_min])/2 #Ampltiudenberechnung
print('Amplituden Alu fern', A5)

A6_m = ufloat(np.mean(A6), np.std(A6, ddof=1)) #Mittelwerte Amplituden
A5_m = ufloat(np.mean(A5), np.std(A5, ddof=1))

print('Amplituden Alu nah', A6)

dt_56_ = (t_dyn1[A5_max] -  t_dyn1[A6_max]) #Phasendifferenz
print(f'PhasendifferenzAlu {dt_56_}')
dt_56 = ufloat(np.mean(dt_56_), np.std(dt_56_, ddof=1))#Mittelwert Phasendifferenz
print(f'Phasendifferenz Aluminium {dt_56:.3f}, Amp fern {A5_m:.3f}, nah {A6_m:.3f}')


kappa_mess_ex = (rho_mess * c_mess * dx**2)/(2 * dt_12 * unp.log(A2_m/A1_m)) #Wärmeleitfähigkeit

kappa_alu_ex = (rho_alu * c_alu * dx**2)/(2 * dt_56 * unp.log(A6_m/A5_m))

abw_me = 100 * (kappa_mess_ex - kappa_mess)/kappa_mess #Abweichung vom Literaturwert
abw_al = 100 * (kappa_alu_ex - kappa_alu)/kappa_alu

print(f'kappa Messing {kappa_mess_ex:.3f},  AbweichungLiteraturwert {abw_me:.3f}')
print(f'kappa Aluminium {kappa_alu_ex:.3f}, AbweichungLiteraturwert {abw_al:.3f}')

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



## get amplitudes and phase shift
A7 = amplitudes(dyn2_7)

A7_max = np.array([ 53, 153, 252, 352, 452, 552, 653])
A7_min = np.array([  1, 102, 203, 303, 403, 503, 603])
A7 = (dyn2_7[A7_max] - dyn2_7[A7_min])/2

print(f'Amplitude Edelstahl_nah{A7}')

A8 = amplitudes(dyn2_8)
A8_max = np.array([ 85, 185, 279, 377, 477, 575, 673])
A8_min = np.array([ 13, 115, 216, 317, 419, 520, 620])
A8 = (dyn2_8[A8_max] - dyn2_8[A8_min])/2

print (f'Amplitude Edelstahl_fern{A8}')

A7_m = ufloat(np.mean(A7), np.std(A7, ddof=1))
A8_m = ufloat(np.mean(A8), np.std(A8, ddof=1))

dt_78_ = (t_dyn2[A8_max]-t_dyn2[A7_max])
print(f'Phasendifferenz Edelstahl{dt_78_}')
dt_78 = ufloat(np.mean(dt_78_), np.std(dt_78_, ddof=1))

print(f'Mittelwert Phsadiff{dt_78:.3f} , Ampnah{A7_m:.3f}, Ampfern{A8_m:.3f}')

kappa_edel_ex = (rho_edel * c_edel * dx**2)/(2 * 80 * unp.log(A7_m/A8_m))

abw_ed = 100 * (kappa_edel_ex - kappa_edel)/kappa_edel

print(f'kappa Edelstahl {kappa_edel_ex:.3f}, Abweichung Literatur {abw_ed:.3f}')


## Wellenlänge und Frequenz
lam_1 = unp.sqrt((4 * np.pi * kappa_mess_ex * 80)/(rho_mess * c_mess))
lam_5 = unp.sqrt((4 * np.pi * kappa_alu_ex * 80)/(rho_alu * c_alu))
lam_7 = unp.sqrt((4 * np.pi * kappa_edel_ex * 200)/(rho_edel * c_edel))

lam_1_t = unp.sqrt((4 * np.pi * kappa_mess * 80)/(rho_mess * c_mess))
lam_5_t = unp.sqrt((4 * np.pi * kappa_alu* 80)/(rho_alu * c_alu))
lam_7_t = unp.sqrt((4 * np.pi * kappa_edel * 200)/(rho_edel * c_edel))

abw_1 = 100 * (lam_1 - lam_1_t)/lam_1_t
abw_2 = 100 * (lam_5 - lam_5_t)/lam_5_t
abw_3 = 100 * (lam_7 - lam_7_t)/lam_7_t

print(f'lambda: Messing {lam_1:.3f}, Alu {lam_5:.3f}, Edelstahl {lam_7:.3f}')
print(f'lambda: Messing {lam_1_t}, Alu {lam_5_t}, Edelstahl {lam_7_t}')
print(f'Abweichung: Messing {abw_1:.3f}, Alu {abw_2:.3f}, Edelstahl {abw_3:.3f}')
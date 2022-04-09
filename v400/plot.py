import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit




############Aufageb2

alpha , beta = np.genfromtxt('content/A2.txt', unpack=True)

n= np.sin(alpha*np.pi/180.0)/np.sin(beta*np.pi/180.0)
print ('n =' , n)

c= 2.9979*10**8 
v = c/1.50

print ('v =' , v)


###################Aufgabe3 a
d=5.85
s = d *np.sin((alpha-beta)*np.pi/180.0)/np.cos(beta*np.pi/180.0)
print ('s =' , s)

##############Aufgabe 3 b 

n= ufloat(1.50, 0.01)
beta2= unp.arcsin(np.sin(alpha*np.pi/180)/n)
beta2=beta2*180/np.pi

print ('beta2 =', beta2)

s2 = d *unp.sin((alpha-beta2)*np.pi/180.0)/unp.cos(beta2*np.pi/180.0)

print ('s2 =' , s2)

###############Aufgabe 4
alpha_1 , grün, rot = np.genfromtxt('content/A4.txt', unpack=True)

gammagrün = alpha_1 + grün -60
gammarot= alpha_1 + rot -60

print('gammagrün =', gammagrün)
print('gammarot =', gammarot) 

#############Aufgabe 5
k, grün6, rot6, grün3, rot3, grün1, rot1= np.genfromtxt('content/A5.txt', unpack=True)

lama6grün= 1/600 * (np.sin(grün6*np.pi/180)/k)*1000000
lama6rot= 1/600 * (np.sin(rot6*np.pi/180)/k)*1000000
lama3grün= 1/300 * (np.sin(grün3*np.pi/180)/k)*1000000
lama3rot= 1/300 * (np.sin(rot3*np.pi/180)/k)*1000000
lama1grün= 1/100 * (np.sin(grün1*np.pi/180)/k)*1000000
lama1rot= 1/100 * (np.sin(rot1*np.pi/180)/k)*1000000

print('lama6grün =', lama6grün)
print('lama6rot =', lama6rot)
print('lama3grün =', lama3grün)
print('lama3rot =', lama3rot)
print('lama1grün =', lama1grün) 
print('lama1rot =', lama1rot)

n = ufloat(1.50, 0.01)
a= ((n-1.49)/1.49)*100
print('a=', a)

lg= ufloat(541.91, 9.80)
lr= ufloat(646.78, 7.33)

ag= (lg-532)/532*100
ar= (lr-635)/635*100

print('ag=', ag)
print('ar=' , ar)
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

#Magnetfeld Grafik
x, B = np.genfromtxt('content/Magnetfeld.txt', unpack=True)

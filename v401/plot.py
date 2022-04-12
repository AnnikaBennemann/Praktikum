import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit

lama = ufloat(668.37, 0.58)
lamareal = 635
a= ((lama-lamareal)/lamareal)*100
print('a=', a)
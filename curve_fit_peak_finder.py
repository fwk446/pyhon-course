
# import necessary libraries
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

# global variable definition
n=100    # number of sample points
deg1 = 30    # polynomial order for fit
xs=np.linspace(0,1,n)    # spacing for data
x= np.arange(0, n, 1)

# input data generation
def data_f (f):
    return np.random.normal(0, 0.5, n) +np.sin (np.linspace(0, f*np.pi, n))
    """generate a random signal with noise"""
data = data_f(5)

# curve fitting
def curve_fit(d, deg=20):
    V=np.polynomial.legendre.legvander(xs,deg)
    coeffs=np.linalg.lstsq(V,d,rcond=None)[0]
    g=np.polynomial.legendre.legval(xs,coeffs)
    
    #error calculations
    error2 = ((d-g)**2)
    error = np.abs(d-g)
    c_error = np.sum(error)
    return g, error
curve_data, er = curve_fit(data)

err_bar = max(er)

#peak finder
peaks, _ = find_peaks(curve_data)
fig, axes = plt.subplots()
axes.plot(data)
axes.plot(peaks, curve_data[peaks], "x")
axes.plot(curve_data)

# put error bars on the points, but put no lines between the errorbars
# plotting the different output values
axes.errorbar(x,data, yerr=er, ecolor='b', elinewidth=2, linestyle='')
axes.set_xlabel('wavlength [$nm$]', size=15)
axes.set_ylabel('R', size=15)
axes.set_title('R data and fitting', size=20)
axes.legend()
axes.legend(loc=3)
fig.savefig('data and fitting.png')
# axes.plot(sig)
# axes.plot(er)
fig, axes = plt.subplots()
axes.plot(er)
#axes.legend('error')
fig.savefig('error.png')
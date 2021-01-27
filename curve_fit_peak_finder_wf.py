# import necessary libraries
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
import csv


# global variable definition
n=100    # number of sample points
deg1 = 30    # polynomial order for fit
xs=np.linspace(0,1,n)    # spacing for data
x= np.arange(0, n, 1)

# input data generation
def data_f (f):
    """
    Generate a random signal with noise

    Parameters
    ----------
    f: frequency of the signal

    Returns
    -------
    data of the signal
    """
    return np.random.normal(0, 0.5, n)+np.sin (np.linspace(0, f*np.pi, n))

data = data_f(5)

# curve fitting
def curve_fit(d, deg=20):
    """
    Make curve fitting
    
    Parameters
    ----------
    d: data to be fitted
    deg: polynomial order for fit
         default value = 20

    Returns
    -------
    g: fitted curve data
    error: absolute error of the fit results
    """
    V=np.polynomial.legendre.legvander(xs,deg)
    coeffs=np.linalg.lstsq(V,d,rcond=None)[0]
    g=np.polynomial.legendre.legval(xs,coeffs)
    
    #error calculations
    error2 = ((d-g)**2)
    error = d-g
    c_error = np.sum(error)
    return g, error
curve_data, er = curve_fit(data)

err_max = max(er)

#peak finder
peaks, _ = find_peaks(curve_data)
print(peaks,curve_data[peaks])

with open('peaks.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['peaks'] + ['data'])
    spamwriter.writerow(['peaks(x)', 'peaks value', 'error'])

    
fig, axes = plt.subplots()
axes.plot(data,label='original data',linestyle='solid',linewidth=1,color="k")
axes.plot(peaks, curve_data[peaks], color='r', marker='x', linestyle='',linewidth=5, markersize=14,label='identified peaks')
axes.plot(curve_data,linestyle='--',label='fitting')

# put error bars on the points, but put no lines between the errorbars
# plotting the different output values
axes.errorbar(x,data, yerr=er, ecolor='y', elinewidth=1, linestyle='',label='errorbar')
axes.set_xlabel('wavelength [$nm$]', size=15)
axes.set_ylabel('r', size=15)
axes.set_title('data and fitting', size=20)
axes.legend(loc=0)
fig.savefig('data and fitting-random.png')
fig, axes = plt.subplots()
axes.plot(er, label="error")
axes.legend(loc=0)
axes.set_xlabel('wavelength [$nm$]', size=15)
axes.set_ylabel('error', size=15)
axes.set_title('error', size=20)
#axes.legend('error')
fig.savefig('error_random.png')
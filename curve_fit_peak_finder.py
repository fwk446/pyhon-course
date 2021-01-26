import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


# with open('411A-21-36-01_onLN_trace_1.txt') as f:
#     lines = f.readlines()
n=100
deg1 = 30
xs=np.linspace(0,1,n)

# input data generation
def data_f (f):
    return np.random.normal(0, 0.5, n) +np.sin (np.linspace(0, f*np.pi, n))
# data = np.random.normal(0, 0.5, n) +np.sin (np.linspace(0, 5*np.pi, n))
data = data_f(5)

# curve fitting
def curve_fit(d, deg=20):
    V=np.polynomial.legendre.legvander(xs,deg)
    coeffs=np.linalg.lstsq(V,d,rcond=None)[0]
    g=np.polynomial.legendre.legval(xs,coeffs)
    return g
curve_data = curve_fit(data)

#peak finder
peaks, _ = find_peaks(curve_data, height=1)
fig, axes = plt.subplots()
axes.plot(data)
axes.plot(curve_data)
axes.plot(peaks, curve_data[peaks], "x")
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
# with open('411A-21-36-01_onLN_trace_1.txt') as f:
#     lines = f.readlines()
n=100
data = np.random.normal(0, 0.5, n)+np.random.normal(0, 1, n) * np.abs(np.sin(np.linspace(0, 3*np.pi, n)))+np.sin (np.linspace(0, 5*np.pi, n))
peaks, _ = find_peaks(data, height=1, distance=10, threshold=[0.5,2])
fig, axes = plt.subplots()
axes.plot(data)
axes.plot(peaks, data[peaks], "x")
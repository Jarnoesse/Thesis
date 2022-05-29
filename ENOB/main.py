from readfile import readfile
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

dataframe = readfile("sin.txt")

fig = plt.figure(figsize=(11, 6), dpi=80)

plt.title('ADCH')
plt.ylabel('ADC code')
plt.xlabel('Sample #')
plt.grid(True)
plt.plot(dataframe["H"],
color="dodgerblue",  markeredgecolor = 'black',
    marker = ".", markersize = 8, linestyle = 'dotted')

fig.tight_layout()

plt.show()


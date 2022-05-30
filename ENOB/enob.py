from number_converter import number_converter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy.fft import fft

class enob:


    def __init__(self,filepath,nbit = 12):
        #reading the data from the txt file
        data_df = pd.read_csv(filepath,header = None)

        hl_df = pd.DataFrame(columns = ["H", "L"])
        h_list = []
        l_list = []

        for row in range(0,len(data_df.loc[:, 1])):

            print(row)

            h_odd_list  = [a for a in str(data_df.iloc[row, 0])]
            h_even_list = [a for a in str(data_df.iloc[row, 1])]
            l_odd_list  = [a for a in str(data_df.iloc[row, 2])]
            l_even_list = [a for a in str(data_df.iloc[row, 3])]
            #NOTE: when working w/ exadecimals it also takes the space after the comma, i would fix in the conversion!

            h_1, h_3 = number_converter(h_odd_list)
            h_0, h_2 = number_converter(h_even_list)
            l_1, l_3 = number_converter(l_odd_list)
            l_0, l_2 = number_converter(l_even_list)

            h_temp = [h_0,h_1,h_2,h_3]
            l_temp = [l_0,l_1,l_2,l_3]

            h_list.extend(h_temp)
            l_list.extend(l_temp)

        self.h_array = np.array(h_list)
        self.l_array = np.array(l_list)
        self.nbit = 12




    def fft_method(self):

        #computing fast fourier transforms
        h_fft = fft(self.h_array)
        l_fft = fft(self.l_array)

        #declaring useful variables
        squared_sums = 0
        max_idx = 0

        #finding the index of the max bin
        for i in range(0,len(h_fft)):
            if np.absolute(h_fft[i]) > np.absolute(h_fft[max_idx]):
                max_idx = i

        #computing the squared sums
        for i in range(0,len(h_fft)):
            if i != 0 and i != max_idx and len(h_fft) - max_idx + 2:
                squared_sums += np.absolute(h_fft[i]) * np.absolute(h_fft[i])

        #computing NAD
        self.fft_nad = np.sqrt(squared_sums) / np.sqrt(len(self.h_array) * (len(self.h_array - 3)))

        self.fft_enob = self.nbit - np.log2(self.fft_nad / np.sqrt(1 / 12))
        print("ENOB", self.fft_enob)




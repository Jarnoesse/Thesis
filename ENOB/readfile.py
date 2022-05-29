# This file defines a function capable of reading the txt output from the LiTE-DTU_v2
#Jarno Sandrin

#import libraries
import pandas as pd
import numpy as np

#this simple function convert from exadecimal/binary to decimal.
#the numbers are ordered to reflect the "i+n" order from the documentation, so for example i will come before i+1
def number_converter(list):

    space = False
    is_binary = True

    for digit in list:

        #early checks for format
        if digit == ' ':
            space = True
        #checks if the number is in binary
        if digit != '1' and digit != '0':
            is_binary = False

    #removes some spaces that may have been retained with the string format from the txt document
    if space:
        list = list[1:len(list)]

    if is_binary:

        second = int("".join(list[4:16]),2)
        first = int("".join(list[20:len(list)]),2)

    else:
        #it assumes a exadecimal data format where the word is 8 characters long
        #it join the list as a string again then it converts the string into a decimal number
        second = int("".join(list[1:4]),16)
        first = int("".join(list[5:len(list)]),16)

    return first, second



def readfile(filepath):
    #compiling the dataframe from the txt file and defining the final dataframe
    data_df = pd.read_csv(filepath,header = None)

    hl_df = pd.DataFrame(columns = ["H","L"])
    h_list = []
    l_list = []

    for row in range(0,len(data_df.loc[:,1])):

        print(row)

        h_odd_list  = [a for a in str(data_df.iloc[row,0])]
        h_even_list = [a for a in str(data_df.iloc[row,1])]
        l_odd_list  = [a for a in str(data_df.iloc[row,2])]
        l_even_list = [a for a in str(data_df.iloc[row,3])]
        #NOTE: when working w/ exadecimals it also takes the space after the comma, i would fix in the conversion!

        h_1, h_3 = number_converter(h_odd_list)
        h_0, h_2 = number_converter(h_even_list)
        l_1, l_3 = number_converter(l_odd_list)
        l_0, l_2 = number_converter(l_even_list)

        h_temp = [h_0,h_1,h_2,h_3]
        l_temp = [l_0,l_1,l_2,l_3]

        h_list.extend(h_temp)
        l_list.extend(l_temp)


    h_df = pd.DataFrame(h_list,columns = ["H"])
    l_df = pd.DataFrame(l_list,columns = ["L"])

    combined_df = pd.concat([h_df,l_df],axis = 1)
    hl_df = pd.concat([hl_df,combined_df])

    #returns the final dataframe
    return(hl_df)






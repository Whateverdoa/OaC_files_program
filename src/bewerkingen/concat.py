''' venv maken met pas etc'''

import pandas as pd
import numpy as np


def read_tree_files():
    pass


def concat(df1, df2, df3):
    """ maakt van 3 csv file een dataframe en plakt ze naast elkaar """
    dff = pd.concat([df1, df2, df3], axis=1)
    return dff
    

def convert_sag(file_in,file_out):
    ''' leest een file in geeft er inloop, rol_aantal, wikkels en uitloop aan. en poept deze weer uit '''
    with open("target_3_csv.csv", newline='') as f:
        read_line = f.readlines()
        blok_1 = read_line[0:10] # voorbeeld van 10 voor het overzicht
        blok_2 = read_line[10:20]
        blok_3 = read_line[20:30]
        
        with open("target_voor_drie_files.csv", 'w', newline='') as df:
            for line in blok_1:
                a = print(line, end='')
                a = str(a)
                # print("1,2,3,4,5,stans.pdf\n"*7,end = '')
                print("1,2,3,4,5\n" * 7, end='')

            for line in blok_2:
                print(line, end ='')

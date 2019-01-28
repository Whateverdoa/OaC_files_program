#!#!/usr/bin/env python

'''open folder --> read files --> make list or dict per three ---> calculate if mod == 0 else make dummy file or two '''

import pandas as pd
import numpy as np
import glob

path = "werkbestanden"

df1 = pd.read_csv(path)
df1

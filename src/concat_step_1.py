#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open files to read
reading files
renaming
adding the header pdf(prepress purposes)
os path

@author: mike
"""

import pandas as pd

li_2019_3376 = ["AMS-0007.csv", "AMS-0008.csv", "MAL-0055.csv", "MAL-0056.csv", "MAL-0057.csv", "MAL-0058.csv",
                "MAL-0059.csv", "MAL-0060.csv", "MAL-0061.csv""MAL-0062.csv", "MAL-0063.csv",
                "MAL-0065.csv", "MAL-0062.csv", "MAL-0063.csv", "MAL-0065.csv", "MAL-0066.csv", "MAL-0067.csv",
                "MAL-0068.csv", "MAL-0069.csv", "MAL-0070.csv", "MAL-0071.csv", "MAL-0072.csv", "MAL-0073.csv",
                "MAL-0075.csv", "MAL-0076.csv", "MAL-0077.csv", "MAL-0078.csv", "MAL-0079.csv", "MAL-0080.csv",
                "MAL-0081.csv", "MAL-0082.csv", "MAL-0083.csv", "MAL-0084.csv", "SAG-0033.csv", "SAG-0034.csv"]


# "AMS-0007.csv","AMS-0008.csv","MAL-0055.csv"
#
#
# "MAL-0056.csv","MAL-0057.csv","MAL-0058.csv"
#
#
# "MAL-0059.csv","MAL-0060.csv","MAL-0061.csv"
#
#
# "MAL-0062.csv","MAL-0063.csv","MAL-0065.csv"
#
#
# "MAL-0066.csv","MAL-0067.csv","MAL-0068.csv"
#
#
# "MAL-0069.csv","MAL-0070.csv","MAL-0071.csv"
#
#
# "MAL-0072.csv","MAL-0073.csv","MAL-0075.csv"
#
#
# "MAL-0076.csv","MAL-0077.csv","MAL-0078.csv"
#
#
# "MAL-0079.csv","MAL-0080.csv","MAL-0081.csv"
#
#
# "MAL-0082.csv","MAL-0083.csv","MAL-0084.csv"
#
#
# "SAG-0033.csv","SAG-0034.csv",



lijst_ = ["AMS-0007.csv","AMS-0008.csv","MAL-0055.csv"]
# lijst_ = {'f': 'HIA-0113.csv', 'g': 'OMN-0118.csv', 'h': 'OMN-0119.csv'}

df1 = pd.read_csv(lijst_[0])
df2 = pd.read_csv(lijst_[1])
df3 = pd.read_csv(lijst_[2])
df4 = pd.read_csv("pdf.csv")

df = pd.concat([df1, df2, df3, df4], axis=1)
# writing to csv
df.to_csv("vdp_1.csv")





with open("vdp_1.csv", "r") as f:
    read_line = f.readlines()

with open("vdp_1_def.csv", "w", encoding="utf-8") as target:
    target.writelines(read_line[1:2]) #eerste regel
    target.writelines("*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,stans.pdf\n" * 59)  # inloop
    a = 1
    b = 1001
    for _ in range(8):
        target.writelines("*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,stans.pdf\n" * 6)
        target.writelines(read_line[a:b])

        a += 1000
        b += 1000

    target.writelines("*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,stans.pdf\n" * 59) #  uitloop
    target.writelines(read_line[8000:8001])#  laatste regel

print("done")

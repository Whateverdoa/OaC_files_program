# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
with open("HIA-0113.csv", "r") as f:
    read_line = f.readlines()

with open("output/target.csv", "w", encoding="utf-8") as target:
    target.writelines(read_line[0:1])

    a = 1
    b = 1001
    for _ in range(8):
        target.writelines(read_line[a:b])
        target.writelines("*,*,*,*,*\n")
        a += 1000
        b += 1000

# with open("target.csv", "w", encoding="utf-8") as target:
#         target.writelines(read_line[0:1])
#     a = 1
#     for _ in range(8):
#         target.writelines(read_line[a:a])
#         target.writelines("*,*,*,*,*\n")
#         a += 1000
#

#   todo begin eind regel versie maken

#   todo maak een functie die leeg.pdf en stans.pdf maakt en een functie die deze file kan joinen





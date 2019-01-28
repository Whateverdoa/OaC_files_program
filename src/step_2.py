"""" building the csv files"""

import os
import pandas as pd
from pathlib import Path

name_list = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/src/vdp_namen.csv"
test_list = os.listdir("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")


def concating(naam_van_een_file, naam_lijst):
    """" the first variable here is a list of three, iterating # todo build a list of threes out of the 32
    the second is iterating through the name list"""
    str_df_1 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/{naam_van_een_file[0]}"
    str_df_2 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/{naam_van_een_file[1]}"
    str_df_3 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/{naam_van_een_file[2]}"
    str_df_4 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/src/pdf.csv"

    # lijst_ = ["AMS-0007.csv","AMS-0008.csv","MAL-0055.csv"]
    # lijst_ = {'f': 'HIA-0113.csv', 'g': 'OMN-0118.csv', 'h': 'OMN-0119.csv'}
    data_in = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")
    df1 = pd.read_csv(str_df_1)
    df2 = pd.read_csv(str_df_2)
    df3 = pd.read_csv(str_df_3)
    df4 = pd.read_csv(str_df_4)

    df = pd.concat([df1, df2, df3, df4], axis=1)
    # writing to csv
    df.to_csv("temp.csv")  # is temp file remove after?

    with open("temp.csv", "r") as f:
        read_line = f.readlines()

    with open(naam_lijst, "w", encoding="utf-8") as target:
        target.writelines("index, BC1, TC1, KC1, VVV1, WWW1,BC2,TC2,KC2,VVV2,WWW2,BC3,TC3,KC3,VVV3,WWW3,pdf\n")
        # headers
        target.writelines(read_line[1:2])  # eerste regel

        target.writelines("*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,stans.pdf\n" * 59)  # inloop
        a = 1
        b = 1001
        for _ in range(8):
            target.writelines("*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,stans.pdf\n" * 6)
            target.writelines(read_line[a:b])

            a += 1000
            b += 1000

        target.writelines("*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,*,stans.pdf\n" * 59)  # uitloop
        target.writelines(read_line[8000:8001])  # laatste regel
    os.remove("temp.csv")  # remove temp file
    print("done")



if len(test_list) % 3 == 2:
    mod_lijst = len(test_list) - len(test_list) % 3
    print(mod_lijst)
    for eerste_tien in range(0, mod_lijst, 3):
        """build first 10 liits"""
        #
        naam = test_list[eerste_tien: eerste_tien + 3]
        print(naam)

    naam = test_list[30:32]
    print('last file only consist of two files!')
    print(naam)
else:

    print((len(test_list) % 3))
    print(f"check if file {(len(test_list) % 3)} is a dummy file")

if len(test_list) % 3 == 0:
    """just logic to get it to only use the files that have concatenated three in them"""
    mod_lijst = len(test_list) - len(test_list) % 3
    print(mod_lijst)
    count = 1
    for eerste_tien in range(0, mod_lijst, 3):
        """build first 10 _ 3 lists"""
        c_naam_csv = f"2019_VDP_{count}"

        c_naam_csv = test_list[eerste_tien: eerste_tien + 3]
        print(eerste_tien)
        fnaam_csv = f"2019_VDP_{count}.csv"

        concating(c_naam_csv, fnaam_csv)
        count += 1
        print(fnaam_csv)
        print(c_naam_csv)
#     naam = test_list[30:32]
#     print(naam)
else:
    print((len(test_list) % 3))


""""naming function"""
import os
import pandas as pd
from pathlib import Path


# from pathlib import Path


def naming(order_number, *argh):
    b = os.listdir("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")
    c = len(b)
    if c == 32:

        # b = list(32 * "a") # list that gives a result of 32
        print(b)
        count = 1
        for _ in range(0, c, 3):
            print(f"{order_number}_VDP_{count}")
            count += 1


    else:
        print("no go")


#  or

# order_number = input("ordernummer: ")
# files = len(os.listdir("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/"))
# count = 1
# if files == 32:
#     open("vdp_namen.csv", "w")
#
#     with open("vdp_namen.csv", "a") as naam_lijst:
#         for _ in range(0, files, 3):
#             naam_lijst.write(f"{order_number}_VDP_{count}\n")
#             count += 1
#     print(f"naming of {files} has been done {order_number} + VDP_1 t/m 11 , see file 'vdp_namen.csv'.")
# else:
#     print(f"no go, files must be ->32<-, but !!!!{files}!!!! exist in DIR")

# C:\Users\Dhr. Ten Hoonte\PycharmProjects\OaC_files_program\src\vdp_namen.csv


data_folder_out = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/output")
data_folder_in = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")
files_to_write = data_folder_out / "cont_.csv"

pad_in = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/"

open(files_to_write, "w", encoding="utf-8")

test_list = os.listdir("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")

# for i in range(0,len(test_list)):
#     lijst__a = test_list[i:i+3]


for k in range(0, 30, 3):
    print(f"['{test_list[k]}', '{test_list[k + 1]}', '{test_list[k + 2]}']")


for k in range(30, 31):
    print(f"['{test_list[k]}', '{test_list[k + 1]}']")

drie_lijst_1 = []
for k in range(0, 30, 3):
    drie_lijst_1.append(f'"{test_list[k]}", "{test_list[k + 1]}", "{test_list[k + 2]}"')
print(f"dit is nu drie lijst: {drie_lijst_1}")

print(drie_lijst_1[0])
print(type(drie_lijst_1[0]))


lijst_ = ["AMS-0007.csv", "AMS-0008.csv", "MAL-0055.csv"]

str_df_1 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/{lijst_[0]}"
str_df_2 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/{lijst_[1]}"
str_df_3 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/{lijst_[2]}"
str_df_4 = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/src/pdf.csv"


def concating(lijst_, naam_lijst):
    """" the first variable here is a list of three, iterating # todo build a list of threes out of the 32
    the second is iterating through the name list"""

    # lijst_ = ["AMS-0007.csv","AMS-0008.csv","MAL-0055.csv"]
    # lijst_ = {'f': 'HIA-0113.csv', 'g': 'OMN-0118.csv', 'h': 'OMN-0119.csv'}
    data_in = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")
    df1 = pd.read_csv(str_df_1)
    df2 = pd.read_csv(str_df_2)
    df3 = pd.read_csv(str_df_3)
    df4 = pd.read_csv(str_df_4)

    df = pd.concat([df1, df2, df3, df4], axis=1)
    # writing to csv
    df.to_csv("vdp_1.csv")

    with open("vdp_1.csv", "r") as f:
        read_line = f.readlines()

    with open(naam_lijst, "w", encoding="utf-8") as target:
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

    print("done")


lijsta = ["C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/AMS-0007.csv",
          "C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/AMS-0008.csv",
          "C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/MAL-0055.csv"]

# concating(lijsta,"testnaaaaaaam.csv")
concating(lijst_, "naam_2.csv")

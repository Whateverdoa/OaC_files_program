import os
from pathlib import Path, PureWindowsPath

order_number = input("ordernummer: ")
files = len(os.listdir("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/"))
count = 1
if files == 32:
    open("vdp_namen.csv", "w")

    with open("vdp_namen.csv", "a") as naam_lijst:
        for _ in range(0, files, 3):
            naam_lijst.write(f"{order_number}_VDP_{count}\n")
            count += 1
    print(f"naming of {files} has been done {order_number} + VDP_1 t/m 11 , see file 'vdp_namen.csv'.")
else:
    print(f"no go, files must be ->32<-, but !!!!{files}!!!! exist in DIR")

# C:\Users\Dhr. Ten Hoonte\PycharmProjects\OaC_files_program\src\vdp_namen.csv

# this line reads the dir into a list
arr = os.listdir("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")

data_folder_out = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/output")
data_folder_in = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/")
file_to_write = data_folder_out / "begin_eind_regels.csv"

open(file_to_write, "w", encoding="utf-8")

for file in arr:
    baah = f"C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/Seal&Trace batches/{file}"
    print(baah)
    with open(baah, "r") as target:
        read_line = target.readlines()
        print(read_line[0:1])

        with open(file_to_write, "a", encoding="utf-8") as target_2:
            target_2.writelines(read_line[0:1])
            a = 1
            b = 2
            c = 1000
            d = 1001

            for _ in range(8):
                print(read_line[a:b])
                print(read_line[c:d])
                target_2.writelines(read_line[a:b])
                target_2.writelines(read_line[c:d])
                a += 1000
                b += 1000
                c += 1000
                d += 1000




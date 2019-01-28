"""open folder --> read files --> make list or dict per three ---> calculate if mod == 0 else make dummy file or two """


from pathlib import Path, PureWindowsPath


data_folder_in = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/invoer/")
data_folder_out = Path("C:/Users/Dhr. Ten Hoonte/PycharmProjects/OaC_files_program/output/")

file_to_open = data_folder_in / "HIA-0113.csv"
file_to_write = data_folder_out / "begin_eind_regels.csv"

# his part gets the begin  and end lines per rol
with open(file_to_open, "r") as f:
    read_line = f.readlines()

target_2 = open(file_to_write, "w", encoding="utf-8")
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

target_2.close()


filename_in = Path(data_folder_in)
filename_out = Path(data_folder_out)

# Convert path to Windows format
path_on_windows_in = PureWindowsPath(filename_in)
path_on_windows_out = PureWindowsPath(filename_out)

print(path_on_windows_in)
print(path_on_windows_out)
# prints "source_data\text_files\raw_data.txt"







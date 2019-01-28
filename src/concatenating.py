""" multiple files will be concatenated """
# mnaking a class here
# input list

# generating dict

# TODO create function that generates 3 files into 1 list or dict
# TODO including new headers and an extra column or two

# output is a file with all the beginning and endings per rol using append

# output 10 csv with 3 files each
# and 1 file with two making sure that if there is just one file left
# over this also acceptable using logic

import pandas as pd

# todo the files in these lists should all ready have been made ready and stripped of their headers

test_list = ["HIA-0113.csv",
             "HIA-0118.csv",
             "HIA-0119.csv",
             "HIA-0120.csv",
             "HIA-0121.csv",
             "OMN-0118.csv",
             "OMN-0119.csv"
             "pdf.csv"]  # added pdf.csv for testing

new_list = []
print(len(new_list))
# todo  making everything into a wheel


def read_tree_files():
    """" slicing with a for loop from the list 3 files"""
    for index in range(3):
        new_list.append(test_list[index])
        print(new_list)
    df1 = pd.read_csv(new_list[0]) # df1 will have to come from a for loop and [also_a_var]
    df2 = pd.read_csv(new_list[1])
    df3 = pd.read_csv(new_list[2])
    df4 = pd.read_csv("pdf.csv")   # needs to calculate the length of the file and proceed to make a list this long:)
    dff = pd.concat([df1, df2, df3, df4], axis=1)
    print(dff)
    with open('concatenated_1.csv', 'w') as c_1:
        dff.to_csv(c_1)


def concat():
    """
    enter list of three  : converts 3 csv files into a dataframe concatenating them
    :type : object csv files
    """

read_tree_files()


# with open("HIA-0113.csv", "r") as f:
#     read_line = f.readlines()
#
# with open("target.csv", "w", encoding="utf-8") as target:
#     first_line = 1
#     last_line = 1001
#     for _ in range(8):
#         target.writelines(read_line[first_line:last_line])
#         target.writelines("*,*,*,*,*\n"*8)
#         first_line += 1000
#         last_line += 1000






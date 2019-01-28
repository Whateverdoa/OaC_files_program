""" pop list"""

test_list = ["HIA-0113.csv",
             "HIA-0118.csv",
             "HIA-0119.csv",
             "HIA-0120.csv",
             "HIA-0121.csv",
             "OMN-0118.csv",
             "OMN-0119.csv"]


# list.pop(0)
# print(len(list))
# print(list)


def pop_3_uit_lijst(lijstnaam):
    for index in range(3):
        abc = test_list.pop(0)
        print(len(test_list))
        with open(abc) as a:
            print(abc)
            print(a)
            print(test_list)


pop_3_uit_lijst(test_list)

# print(len(test_list))

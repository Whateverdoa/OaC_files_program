""" one roll"""

# one roll should be made of three things here
# its name == id number or order number
# the number of copies inclusive extras by 110%

# copies = 100
# order = "201900001_1.pdf"
# item_number = "123456789101231254"
# used_name = item_number + ".pdf;;leeg.pdf"
# used_name_wikkel = item_number + ".pdf;" + order + ";stans.pdf"
#
# bar = (copies // 100) * 110   # 10percent extra
# wikkel = 8  # format formula
#
# log = open("goat.txt", "w")
# print(f"{used_name}\n" * bar, end='', file=log)
# log = open("goat.txt", "a")
# print(f"{used_name_wikkel}\n" * wikkel, end='', file=log)
# log.close()

# rollen laten inlezen uit een XML file uit bestelsysteem (dutch)


def roling_stone():
    copies = 15
    order = "201900001_1.pdf"
    item_number = "12345"
    used_name = item_number + ".pdf;;leeg.pdf"
    used_name_wikkel = item_number + ".pdf;" + order + ";stans.pdf"

    bar = int((copies / 100) * 110)  # 10percent extra
    wikkel = 2  # format formula
    # print(bar)
    log = open("goat.csv", "a")
    print(f"{used_name}\n" * bar, end='', file=log)
    print(f"{used_name_wikkel}\n" * wikkel, end='', file=log)


log = open("goat.csv", "w")
print("item_name_as_PDF;order_number;pdf", file=log)
log.close()
roling_stone()
roling_stone()
log.close()



dict1 = {"name": "Wiracha", "age": "21"}
dict2 = {"name": "Wiracha", "age": "21"}
dict3 = dict1

print(dict1 is dict3)  # True

print(dict1 is dict2)  # False ; ค่าเท่ากันแต่ที่อยู่ไม่ใช่ที่เดียวกัน

print(dict1 == dict2)  # True

# is check value and address
# == check value only
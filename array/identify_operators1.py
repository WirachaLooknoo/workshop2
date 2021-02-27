# EX1 การตรวจสอบ
int1 = 5
int2 = 5

string1 = "Hello"
string2 = "Hello"

float1 = 0.1
float2 = 0.1


print(int1 is int2)  # true

print(string1 is string2)  # true

print(float1 is float2)  # true


# a = 10
# b = 10
# check ชี้จากaddressเดียวกัน
# -------------
# == check value
# -------------
# is check value, address
# -------------

# a = {v:10} -> [{v:10}]
#               &A
# b = {v:10}-> [{v:10}]
#               &B

# c = a ------>[{v:10}]
#               &A

# is ใช้รึเปล่า
# c is a ------> True เพราะaddresเดียวกัน valueเดียวกัน
# a id b  ------>False เพราะเป็นvalueเดียวกัน แต่ address [{v:10}] #คนละaddress
#                                                       &A

# a==b True เพระา value เดียวกัน
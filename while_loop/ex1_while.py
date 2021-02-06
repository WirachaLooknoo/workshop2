i = 2
while i <= 12:
    print("   " + "[", i, "]")
    j = 1
    while j <= 12:
        print(i, "*", j, ":", i * j)
        j += 1
    print("")
    print("---------------" "\n")
    i += 1
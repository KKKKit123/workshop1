#while
i = 2
while i <= 12:
    j = 1
    print("  [", i, "]")
    while j <= 12:
        print(i, "*", j, ":", i * j, end="\n")
        j += 1
    print("---------------")
    i += 1

#for
i = 2
for i in range(2, 13):
    j = 1
    print("  [", i, "]")
    for j in range(2, 13):
        print(i, "*", j, ":", i * j, end="\n")
        j += 1
    print("---------------")
    i += 1

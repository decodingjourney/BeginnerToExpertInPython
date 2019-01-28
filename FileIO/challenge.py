with open("sample1.txt", 'w') as table:
    for i in range(2,13):
        for j in range(1,13):
            print("{0} * {1} = {2}".format(i, j, i*j), file=table)
        print("_" * 20, file=table)
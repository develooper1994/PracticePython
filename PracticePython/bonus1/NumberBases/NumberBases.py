
def NumberBases():
    BinaryList=['00000000','00000101','00010000','01010101','11110101','11111111']
    for i in BinaryList:
        print("{0} | {1:3} | {2:2x}".format(int(i),int(i,2),int(i,2)))

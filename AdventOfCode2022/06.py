with open('C:\\Git\\workbook\\data\\advent_06.txt','r') as f:
    line = f.readline()
    for i in range(len(line)-4):
        if len(set(line[i:i+4])) == 4:
            # first answer
            print(i+4)
            break
    for i in range(len(line)-14):
        if len(set(line[i:i+14])) == 14:
            # second answer
            print(i+14)
            break


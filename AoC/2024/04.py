with open('/Users/evgen/projects/workbook/data/advent2024/advent_04.txt','r') as f:
    ans1 = 0
    ans2 = 0
    ar = f.readlines()
    for i in range(len(ar)-1):
        ar[i] = ar[i][:-1]
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j] == 'X':
                if j > 2 and ar[i][j-3:j] == 'SAM':
                    ans1 += 1
                if j > 2 and i > 2 and ar[i-1][j-1] == 'M' and ar[i-2][j-2] == 'A' and ar[i-3][j-3] == 'S':
                    ans1 += 1
                if i > 2 and ar[i-1][j] == 'M' and ar[i-2][j] == 'A' and ar[i-3][j] == 'S':
                    ans1 += 1
                if j < len(ar[0])-3 and i > 2 and ar[i-1][j+1] == 'M' and ar[i-2][j+2] == 'A' and ar[i-3][j+3] == 'S':
                    ans1 += 1
                if j < len(ar[0])-3 and ar[i][j+1:j+4] == 'MAS':
                    ans1 += 1
                if j < len(ar[0])-3 and i < len(ar)-3 and ar[i+1][j+1] == 'M' and ar[i+2][j+2] == 'A' and ar[i+3][j+3] == 'S':
                    ans1 += 1
                if i < len(ar)-3 and ar[i+1][j] == 'M' and ar[i+2][j] == 'A' and ar[i+3][j] == 'S':
                    ans1 += 1
                if j > 2 and i < len(ar)-3 and ar[i+1][j-1] == 'M' and ar[i+2][j-2] == 'A' and ar[i+3][j-3] == 'S':
                    ans1 += 1
            if i > 0 and i < len(ar)-1 and j > 0 and j < len(ar[0])-1 and ar[i][j] == 'A':
                s1 = {ar[i-1][j-1],ar[i+1][j+1]}
                s2 = {ar[i+1][j-1],ar[i-1][j+1]}
                if 'M' in s1 and 'S' in s1 and 'M' in s2 and 'S' in s2:
                    ans2 += 1

# first answer
print(ans1)

# second answer
print(ans2)
arrayfornum = []
for _ in range(9):
    num=int(input())
    arrayfornum.append(num)
print(max(arrayfornum))
print(arrayfornum.index(max(arrayfornum))+1)
list1 = [3,5,7,4,8,8]
list2 = [4,9,8,7,1,1,13]

common = []
for x in list1:
    if x in list2:
        common.append(x)
print(common)

sum = 0
for num in common:
    sum += num
print('Sum:', sum)

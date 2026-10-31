
# List
# a=[12,13,14,15,16,17,18]
# a[2]=100

# print(a[-2])

a=[12,13,14,15,16,17,18]


# for i in range(len(a)):
#      print(a[i])


# for element in a:
#      print(element)

# print(dir(list))
# help(list)

# a.append(24)
# a.insert(2,30)
# a.extend([100,200,300])
# res=a.remove(15)
# num=a.pop(4)
# count=a.count(18)

# print(a)

b=[1,3,4,-1,-2,-5,7,8,9,-9,-11]

# for ele in b:
#     if ele>0:
#         print(ele)

# for ele in b:
#     if ele<0:
#         print(ele)

# sum=0
# for ele in b:
#     sum=sum+ele

# res=sum/len(b)
# print(res)


# max=b[0]
# for i in range(1,len(b),1):
#     if(b[i]>max):
#         max=b[i]


# print(max)



max=b[0]
max2=b[0]
for i in range(1,len(b),1):
    if b[i]>max:
        max2=max
        max=b[i]
    elif b[i]>max2:
        max2=b[i]


print(b)
print(max2)
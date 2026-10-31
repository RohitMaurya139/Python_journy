# a={
#     1:"hello",
#     2:56,
#     3:"Rohit"

# }

# # print(a[1])
# # print(a[2])
# # print(a[3])

# # a[1]="maurya"
# # print(a)

# # a.update({4:600})
# # del a[2]
# # print(a)

# for i in a.values():
#     print(i)


a=[1,2,3,4,5]
d={'a':12,'b':13,'c':14}
d2={'d':12,'e':13,'f':14}
# b=a
# b[0]=100
# print(a)
# print(b)
# print(d.items())

for i in d2:
    d[i]=d2[i]

print(d)

sum=0
for i in d.values():
    sum = sum + i

print(sum)

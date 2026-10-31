# a={2,4,5,5,5,5,5,1,1,1,1,"hello",3,4,5,6}
# print(a)

# for i in a:
#     print(i)

a={1,2,3,4,5,6,7,8}
b={6,7,8,9,10}
c=a.intersection(b)
d=a.union(b)
e=a.difference(b)
f=b.difference(a)
g=a.symmetric_difference(b)
h=b.symmetric_difference(a)

print("Set A")
print(a)
print("Set B")
print(b)
print("intersection")
print(c)
print("union")
print(d)
print("difference : a - b")
print(e)
print("difference : b - a")
print(f)
print("symmetric difference : a - b")
print(g)
print("symmetric difference : b - a")
print(h)


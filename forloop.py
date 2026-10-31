# a = range(10) 
# print("loop1")
# for i in range(1,20,4):
#     print(i)
# print('loop2')
# for i in range(20,51):
#     print(i)
# print("loop3")
# for i in range(16,-1,-1):
#     print(i)    

# table
# n=int(input("Enter the number to generate table: "))

# for i in range(1,11,1):
#     print(f" {n} X {i} = {n*i}")


# loop in string

# a="Rohit"
# for i in range(len(a)):
#     print(a[i])

# a="Rohit"
# for char in a:
#      print(char)

print("Break in For loop")

for i in range(0,10,1):
     if i==6:
          break
     else:
          print(i)
print("Continue in For loop")
for i in range(0,20,1):
     if i%2==0:
          continue
     else:
          print(i)
     
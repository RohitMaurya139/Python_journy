# p=open(r'function.py')
# print(p.read())
r= open("superman.txt",'w')

r.write("Hello i am writing in superman.txt file from filehandle file using python")


s= open("superman.txt",'a')

s.write("i am appending more text data in superman.txt")


r.close()
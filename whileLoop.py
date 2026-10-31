# a=0
# while a<=10 :
#     print(a)
#     a=a+1

# a='Rohit'
# i=0
# j=len(a)-1
# while i<j:
#     if a[i]!=a[j]:
#         print('Not a palindrom')
#         break
#     else:
#         i=i+1
#         j=j-1
#         if i>=j:   
#            print("It is palindrom")

import random

num=random.randint(1,100)
# print(num)
tries=0

while True:
    guess= int(input("Please guess the number between 1 to 100: "))
    tries=tries+1
    if guess> num:
        print(" Higher!!!!!!!!!! Guess Lower Number")
    elif guess<num:
        print(" Lower!!!!!!!!!! Guess Higher Number")
    else:
        print(f"Hurray, You guess the number in {tries} Tries")
        break        
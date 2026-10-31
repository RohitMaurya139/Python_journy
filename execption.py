# a= int(input(" Enter any number: "))

# try:
#     print(10/a)
# except Exception as error:
#     print(f"Sorry there is an error as {error}")
# else:
#     print("Good NO execption occure")
# finally:
#     print("Mai finally hu ree, mai to hamesha chalunga chahe execption aaye ya na aaye")

# print("normal code execution")


age= int(input("Tell me Your Age: "))

try:
    if age<10 or age>19:
        raise ValueError(f"You can Not get admission, because your age {age} is not our permisible limit. out age range is 10 to 19")
except Exception as err:
    print(f"Sorry error occurred as {err}")
else:
    print("ALL THE BEST!!!!!!! You will get admission")

print("The School will start soon")
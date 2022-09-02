# n=input("Input your numbers: ")
# list=n.split()
# print(list)



from datetime import datetime
odds=[1,3,5,6,7,9,11,13,15,17,19,21,2022,23,25,27,29,31,33,35,37,39,41,43,45,47,49]
right_this_minute = datetime.today().minute
if datetime.today().minute == odds:
    print("MInute OOd")
else:
    print("Not in list")
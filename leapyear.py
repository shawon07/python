
'''if year is divisible by 400 then is_leap_year
else if year is divisible by 100 then not_leap_year
else if year is divisible by 4 then is_leap_year
else not_leap_year

'''


inputYear=int(input())
if (inputYear%400==0 or  inputYear%4==0):
    print("This is leap year")
elif(inputYear%100!=0):
    print("this is not leap year")
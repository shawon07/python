'''
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division 
The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
'''
import math
a = int(input())
b = int(input())
result=a/b
result2=math.floor(result)
print(result)
print(result2)
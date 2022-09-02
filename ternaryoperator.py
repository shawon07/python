# num1=100
# num2=20
# print(num1 if num1>num2 else num2)


numbers = [10, 40, 120, 230]
for i in numbers:
    if i > 100 :
        break
    print('current number', i)

numbers = [10, 40, 120, 230]
for i in numbers:
    if i < 100 :
        continue  
    print('current number', i)
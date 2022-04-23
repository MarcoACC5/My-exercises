print('Simple Calculator')
print('-' * 30)
print('You can choose if you wanna sum, subtract or multiply')
print(' + = sum \n - = subtract \n * = multiply')
n1 = int(input('Write a number:'))
n2 = int(input('Write a second number:'))
es = input('Write the operator: ')

if es == '+' :
    resu = n1 + n2
elif es is '-' :
    resu = n1 - n2
elif es is '*' :
    resu = n1 * n2
else : 
    print('Invalid Operation')

print(f'Result = {resu}')

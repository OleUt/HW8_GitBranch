import math

def mane_function(i):
    if i < 5:
        result = 'i<5'
    elif i > 5:
        result = 'i<5'
    else:
        result = 'i=5'
    result = result + '\nDone'
    return result

number = int(input('Enter a number:'))
print(mane_function(number))

j = math.factorial(number)
print('factorial', number, '=', j)


def test_function(i):
    i2 = i*i
    i10 = i * 10
    return i2, i10

print('(i^2, i*10) =', test_function(number))




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

def test_function(i):
    i2 = i*i
    return i2

print('i^2 =', test_function(number))



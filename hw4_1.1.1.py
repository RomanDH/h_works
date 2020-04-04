number1 = int(input('number1:'))
sign = input('operations:')
if sign == 'sqrt':
    sqrt = lambda x: x * x
    print(sqrt(number1))
else:
    number2 = int(input('number2:'))
    lambda_var = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '**': lambda x, y: x ** y,
    }
    if sign in lambda_var:
        print(lambda_var[sign](number1, number2))
    else:
        print('Error')

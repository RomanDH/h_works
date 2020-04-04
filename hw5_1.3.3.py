while True:
    try:
        inpu = int(input('Input:'))
    except ValueError:
        print('введите число')
    else:
        break
if inpu % 4 != 0 or inpu % 400 != 0 and inpu % 100:
    print('Высокосный год')
else:
    print('Не высокосный год')

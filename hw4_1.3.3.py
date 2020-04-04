import random
log = input('Login:')
passw = input('Password:')
dict = {'Serg':['sss',random.randint(1,1000)], 'Lena':['lll',random.randint(1,1000)],
        'Koly':['kkk',random.randint(1,1000)], 'Nika':['nnn',random.randint(1,1000)],
        'Sveta':['sss',random.randint(1,1000)], 'Nikita':['nnn',random.randint(1,1000)],
        'Bill':['bbb',random.randint(1,1000)], 'Den':['ddd',random.randint(1,1000)],
        'Artur':['aaa',random.randint(1,1000)], 'Vas':['vvv',random.randint(1,1000)],}
if log not in dict:
    passw
    print(random.randint(1, 1000))
else:
    true_log = dict[log]
    if passw in true_log:
        if passw == true_log[1]:
            passw
        else:
            print(true_log[1])


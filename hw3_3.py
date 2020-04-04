import random

letters = ['a', 'df', 'c', 'nk', 'qw', 'b', 'j', 'lp', 'uo', 't']
gen_random_list = random.choices(letters, k=10)
print(gen_random_list)
list_num = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
            random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
            random.randint(1, 100), random.randint(1, 100), ]
print(list_num)


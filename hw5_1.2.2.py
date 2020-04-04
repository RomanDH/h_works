num = int(input('Input:'))
not_sifted = list(range(num + 1))
not_sifted[1] = 0
for i in not_sifted:
    if i > 1:
        for j in range(i + i, len(not_sifted), i):
            not_sifted[j] = 0
print(*list(filter(lambda x: x != 0, not_sifted)))

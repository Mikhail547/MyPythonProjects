from itertools import product

k = set()
for i in product('соловей', repeat=6):
    word = ''.join(i)
    if word.count('й') <= 1 and word[0] != 'й' and word[-1] != 'й' and 'ей' not in word and 'йе' not in word:
        k.add(word)
print(len(k))

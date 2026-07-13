with open('ege_24_1.txt', 'r') as f:
    s = f.read().strip()   # читаем весь файл, убираем перевод строки

# Находим все индексы символа 'Z'
pos = [i for i, ch in enumerate(s) if ch == 'Z']

min_len = float('inf')
if len(pos) >= 270:
    for i in range(len(pos) - 269):   # i+269 — последний Z в окне из 270 штук
        length = pos[i+269] - pos[i] + 1
        if length < min_len:
            min_len = length
    print(min_len)
else:
    print("Символов Z меньше 270")
# 1058

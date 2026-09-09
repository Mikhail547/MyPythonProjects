x = '0123456789ABCDEFGHI'
for i in range(len(x)):
    if (int(f'76{x[i]}79645', 19) + int(f'35{x[i]}42', 19) + int(f'332{x[i]}6', 19)) % 18 == 0:
        print((int(f'76{x[i]}79645', 19) + int(f'35{x[i]}42', 19) + int(f'332{x[i]}6', 19)) // 18)

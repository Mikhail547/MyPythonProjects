def f(n, w):
    if n % 2 != 0:
        return False
    m_w = []
    max_w = []
    for i in range(n):
        if i % 2 == 0:
            max_w.append(w[i])
        else:
            m_w.append(w[i])
    for k in range(max(m_w)+1, min(max_w)):
        for i in range(0, n-1, 2):
            if k == w[i] or k == w[i+1]:
                break
            if w[i] > k > w[i+1]:
                    pass
            else:
                break
        else:
            return True
    return False

for _ in range(int(input())):
    n = int(input())
    w = [int(a) for a in input().split()]
    if f(n, w):
        print('YES')
    else:
        print('NO')


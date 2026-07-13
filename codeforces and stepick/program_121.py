n = int(input())
for i in range(n):
    s = input()
    if s.isspace() == True:
        s = 'COMMENT SHOULD BE DELETED'
    print(str(i + 1) + ':', s)
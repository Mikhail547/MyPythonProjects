def R(a):
    l = []
    s = str(a).lower()
    if not(s.isalpha()):
        while '-' in s or '!' in s or ',' in s or '.' in s or '?' in s:
            l = s.split('')


            for i in range(len(l)):
                if not(l[i].isalpha()) and not(l[i].isspace()):
                    del l[i]

    s = ''.join(l)
    print(s)

    if s == s[::-1]:
        return True
    else:
        return False
a = input()
print(R(a))

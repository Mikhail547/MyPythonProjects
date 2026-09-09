l = [a for a in open('claster.txt')]



for i in range(len(l)):
    l[i] = l[:-1]
    print(l[i])

citi_1 = input()
citi_2 = input()
citi_3 = input()
a = len(citi_1)
b = len(citi_2)
c = len(citi_3)
if min(a, b, c) == a and max(a, b, c) == b:
    print(citi_1, citi_2, sep='\n' )
elif min(a, b, c) == b and max(a, b, c) == a:
    print(citi_2, citi_1, sep='\n' )
elif min(a, b, c) == a and max(a, b, c) == c:
    print(citi_1, citi_3, sep='\n' )
elif min(a, b, c) == c and max(a, b, c) == a:
    print(citi_3, citi_1, sep='\n' )
elif min(a, b, c) == c and max(a, b, c) == b:
    print(citi_3, citi_2, sep='\n' )
elif min(a, b, c) == b and max(a, b, c) == c:
    print(citi_2, citi_3, sep='\n' )
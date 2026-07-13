a = int(input())
if a == 0:
    print("зеленый")
elif 0 < a <= 10 and a % 2 == 0:
    print("черный")
elif 0 < a <= 10 and a % 2 != 0:
    print("красный")
elif 10 < a <= 18 and a % 2 == 0:
    print("красный")
elif 10 < a <= 18 and a % 2 != 0:
    print("черный")
elif 10 < a <= 28 and a % 2 == 0:
    print("черный")
elif 10 < a <= 28 and a % 2 != 0:
    print("красный")
elif 28 < a <= 36 and a % 2 == 0:
    print("красный")
elif 28 < a <= 36 and a % 2 != 0:
    print("черный")
else:
    print('ошибка ввода')

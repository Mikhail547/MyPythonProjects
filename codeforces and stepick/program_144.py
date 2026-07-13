import sys


def main():
    # Читаем входные данные
    try:
        a = int(sys.stdin.readline())
        b = int(sys.stdin.readline())
    except ValueError:
        return


    k = (a - 1) // 4 + 1

    # 2. Вычисляем общее количество купе N
    # Исходя из формулы b = 6N - 2k + 1 или b = 6N - 2k + 2
    n = (b + 2*k - 1) // 6

    print(n)


if __name__ == "__main__":
    main()
import sys

def main():

    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])

    y = 11111111

    for i in range(1, t + 1):
        print(y)

if __name__ == '__main__':
    main()



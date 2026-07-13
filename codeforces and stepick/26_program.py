organisms = int(input())
percent = int(input())
days = int(input())

convert_to_floater = percent / 100

for i in range(days - 1):
    organisms += organisms * convert_to_floater
    print(i + 1, organisms)
day = int(input())
ves = float(input())
if ves <= 100 - day * 0.2:
    print('Все идет по плану')
else:
    print('Что-то пошло не так')
print(f'#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {ves} кг, ЦЕЛЬ по ВЕСУ = {100 - day * 0.2} кг')
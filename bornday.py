
year_of_birth = int(input('Введите год рождения А.С.Пушкина:  '))
if year_of_birth == 1799:
    birthday = int(input('Введите день рождения А.С.Пушкина:  '))
    if birthday == 26:
        print('верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')


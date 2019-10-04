
while True:
    answer_es = 0
    answer_no = 0
    year_pushkin = int(input('Введите год рождения А.С.Пушкина:  '))   # 1799
    if year_pushkin == 1799:
        answer_es += 1
    else:
        answer_no += 1
    year_lermontov = int(input('Введите год рождения М.Ю.Лермонтова:  '))    # 1814
    if year_lermontov == 1814:
        answer_es += 1
    else:
        answer_no += 1
    year_esenin = int(input('Введите год рождения С.А.Есенина:  '))    # 1895
    if year_esenin == 1895:
        answer_es += 1
    else:
        answer_no += 1
    year_vycotckiy = int(input('Введите год рождения В.С.Высоцкого:  '))    # 1938
    if year_vycotckiy == 1938:
        answer_es += 1
    else:
        answer_no += 1
    year_choy = int(input('Введите год рождения В.Р.Цоя:  '))    # 1962
    if year_choy == 1962:
        answer_es += 1
    else:
        answer_no += 1
    print('Количество правильных ответов: ' + str(answer_es))
    print('Количество неправильных отведов: ' + str(answer_no))
    print('Процент правильных ответов: ' + str(answer_es * 100 / 5))
    print('Процент неправильных ответов: ' + str(answer_no * 100 / 5))
    new_test = input('Если хотите продолжить тест введите: да,если не хотите, введите: нет ')
    if new_test == 'да':
        continue
    elif new_test == 'нет':
        break
    #else:
        #print('Введите коректные данные')
        #new_test = input('Если хотите продолжить тест введите: да,если не хотите, введите: нет ')









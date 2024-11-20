# Когда пользователь заходит на страницу урока, мы сохраняем время его захода. 
# Когда пользователь выходит с урока (или закрывает вкладку, браузер – в общем как-то разрывает соединение с сервером), 
# мы фиксируем время выхода с урока. Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов. 
# В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах): lesson – начало и конец урока pupil – интервалы присутствия ученика tutor 
# – интервалы присутствия учителя Интервалы устроены следующим образом – это всегда список из четного количества элементов. 
# Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока. 
# Нужно написать функцию appearance, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах).

def appearance(intervals: dict[str, list[int]]) -> int:
    
    # Переводим интервалы в сеты для поиска пересекающихся значений
    lesson = set()
    pupil = set()
    tutor = set()

    # Добавляем диапазон секунд в уроке
    lesson.update(range(intervals['lesson'][0], intervals['lesson'][1]))

    # Добавляем диапазоны секунд присутствия ученика
    for i in range(0, len(intervals['pupil']), 2):
        pupil.update(set(range(intervals['pupil'][i], intervals['pupil'][i + 1])))

    # Добавляем диапазоны секунд присутствия учителя
    for i in range(0, len(intervals['tutor']), 2):
        tutor.update(set(range(intervals['tutor'][i], intervals['tutor'][i + 1])))

    # Ищем пересечения секунд (когда одновременно урок, ученик и учитель)
    intersections = lesson.intersection(pupil, tutor)

    # Возвращаем количество секунд пересечения
    return len(intersections)

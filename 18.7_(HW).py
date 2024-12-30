import random
from types import new_class

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
    {students_marks[student]}''')
print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Удалить оценку ученика по предмету
5. Отредактировать оценку ученика по предмету
6. Добавить  новый предмет
7. Изменить название предмета
8. Удалить предмет из списка
9. Изменить имя ученика
10. Удалить ученика из списка
11. Добавить ученика в список
12. Вывести все оценки одного ученика
13. Вывести средний бал по всем предметам по опеределенному ученику
14. Выход из программы
''')
while True:
            command = int(input('Введите команду: '))
            if command == 1:
                print('1. Добавить оценку ученика по предмету')
                # считываем имя ученика
                student = input('Введите имя ученика: ')
                # считываем название предмета
                class_ = input('Введите предмет: ')
                # считываем оценку
                mark = int(input('Введите оценку: '))
                # если данные введены верно
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    # добавляем новую оценку для ученика по предмету
                    students_marks[student][class_].append(mark)
                    print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
                    print(f'''{student}
                                                                {students_marks[student]}''')
                # неверно введены название предмета или имя ученика
                else:
                    print('ОШИБКА: неверное имя ученика или название предмета')
            elif command == 2:
                print('2. Вывести средний балл по всем предметам по каждому ученику')
                # цикл по ученикам
                for student in students:
                    print(student)
                    # цикл по предметам
                    for class_ in classes:
                    # находим сумму оценок по предмету
                        marks_sum = sum(students_marks[student][class_])
                    # находим количество оценок по предмету
                        marks_count = len(students_marks[student][class_])
                    # выводим средний балл по предмету
                        print(f'{class_} - {marks_sum // marks_count}')
                    print()
            elif command == 3:
                print('3. Вывести все оценки по всем ученикам')
                # выводим словарь с оценками:
               # цикл по ученикам
                for student in students:
                    print(student)
                   # цикл по предметам
                    for class_ in classes:
                        print(f'\t{class_} - {students_marks[student][class_]}')
                print()
            elif command == 4:
                print('4.Ведите оценку, которую хотитет удалить: ')
                # считываем имя ученика
                student = input('Введите имя ученика: ')
                # считываем название предмета
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    mark = int(input('Введите оценку, которую хотите удалить: '))
                    if mark in students_marks[student][class_]:
                        students_marks[student][class_].remove(mark)
                        print(f'Оценка {mark} ученика {student} удалена по предмету {class_}.')
                        print(f'''{student}
                                            {students_marks[student]}''')
                    else:
                        print(f'Оценка {mark} ученика {student} не найдена по предмету {class_}.')
                else:
                    print()
            elif command == 5:
                print('5.Введите данные по оценкам, которые необходимо отредактировать: ')
                # считываем имя ученика
                student = input('Введите имя ученика: ')
                # считываем название предмета
                class_ = input('Введите предмет: ')
                if student in students_marks.keys() and class_ in students_marks[student].keys():
                    mark = int(input('Введите оценку, которую хотите отредактировать: '))
                    newmark = int(input('Введите новую оценку: '))
                    if mark in students_marks[student][class_]:
                        students_marks[student][class_].remove(mark)
                        students_marks[student][class_].append(newmark)
                        print(f'Оценка {mark} ученика {student} отредактирована по предмету {class_}.')
                        print(f'''{student}
                            {students_marks[student]}''')
                    else:
                        print(f'Оценка {mark} ученика {student} не найдена по предмету {class_}.')
                else:
                    print()
            elif command == 6:
                print('6.Добавить новый предмет.')
                newclass = input('Введите название нового предмета: ')
                if newclass not in classes:
                    classes.append(newclass)
                    print(f'Предмет {newclass} добавлен в список')
                    print(classes)
                else:
                    print('ОШИБКА: такой предмет уже существует')
            elif command == 7:
                print('7. Изменить название предмета')
                # считываем название предмета
                class_ = input('Введите старое название предмета: ')
                if class_ in classes:
                    newclass = input('Введите новое название предмета: ')
                    classes.append(newclass)
                    print(f'Предмет {newclass} добавлен')
                    students_marks[student][newclass] = students_marks[student][class_]
                    classes.remove(class_)
                    print(classes)
                else:
                    print('ОШИБКА: такого предмета нет в списке')
            elif command == 8:
                print('8. Удалить предмет из списка')
                class_ = input('Введите название предмета, который необходимо удалить: ')
                if class_ in classes:
                    classes.remove(class_)
                    del students_marks[student][class_]
                    print(f'Предмет {class_} удален из списка')
                    print(classes)
                else:
                    print('Ошибка: такого предмета нет в списке')
            elif command == 9:
                print('9. Изменить имя ученика')
                # считываем имя ученика
                student = input('Введите старое имя ученика: ')
                if student in students_marks.keys():
                    newstudent = input('Введите новое имя ученика: ')
                    students.append(newstudent)
                    print(f'Ученик {newstudent} добавлен')
                    students_marks[newstudent] = students_marks[student]
                    students.remove(student)
                    print(f'''{newstudent}
                                                {students_marks[student]}''')
                else:
                    print('ОШИБКА: такого ученика нет в списке')
            elif command == 10:
                print('10. Удалить ученика из списка')
                student = input('Введите имя ученика, которого необходимо удалить: ')
                if student in students:
                    students.remove(student)
                    del students_marks[student]
                    print(f'Ученик {student} удален из списка')
                    print(students)
                else:
                    print('Ошибка: такого ученика нет в списке')
            elif command == 11:
                print('11. Добавить ученика в список')
                newstudent = input('Введите имя нового ученика: ')
                if newstudent not  in students:
                    students.append(newstudent)
                    print(f'Ученик {newstudent} добавлен в список')
                    print(students)
                else:
                    print('Ошибка: такой ученик уже существует')
            elif command == 12:
                print('12. Вывести все оценки одного ученика')
                student = input('Введите имя ученика: ')
                if student in students_marks.keys():
                    for class_ in classes:
                        print(f'\t{class_} - {students_marks[student][class_]}')
                    print()
                else:
                    print('Ошибка: такого ученика нет в списке')
            elif command == 13:
                print('13. Вывести средний бал по всем предметам по определенному ученику')
                student = input('Введите имя ученика: ')
                if student in students_marks.keys():
                    for classes, marks in students_marks[student].items():
                        marks_sum = sum(marks)
                        marks_count = len(marks)
                        print(f'{classes} - {marks_sum//marks_count}')
                    print()
                else:
                    print('Ошибка: неверное имя ученика')
            elif command == 14:
                print('14.Выход из программы')
                break
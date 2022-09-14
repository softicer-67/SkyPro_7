from functions import *


def main():
    while True:
        user_input = input('Введите номер студента\n')
        if user_input in '1234':
            user = get_student_by_pk(user_input)
            print('Студент', user)
            skill = get_skill(user_input)
            print('Знает', skill)
            work = input(f'Выберите специальность для оценки студента {user}\n')
            while True:
                profession = get_profession_by_title(work)
                if work in ['Backend', 'Frontend', 'Testing']:
                    check_fitness(user, profession, skill)
                    quit()
                else:
                    print('У нас нет такой специальности')
                    break

        else:
            print('У нас нет такого студента')
            continue


if __name__ == '__main__':
    main()


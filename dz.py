from functions import *


def main():
    while True:
        user_input = input('Введите номер студента \n')
        user = get_student_by_pk(user_input, read_file_st())
        if user is False:
            print('У нас нет такого студента')
            continue

        print('Студент', user)

        skill = get_skill(user_input, read_file_st())
        print('Знает', skill)
        work = input(f'Выберите специальность для оценки студента {user}\n')
        while True:
            profession = get_profession_by_title(work, read_file_pr())
            if work in ['Backend', 'Frontend', 'Testing']:
                check_fitness(user, profession, skill)
                quit()
            else:
                print('У нас нет такой специальности')
                break


if __name__ == '__main__':
    main()


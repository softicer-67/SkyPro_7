import json


def read_file_st():
    with open('students.json', 'r', encoding='utf-8') as f:
        file = json.load(f)
    return file


def read_file_pr():
    with open('professions.json', 'r', encoding='utf-8') as f:
        prof = json.load(f)
    return prof


data_st = read_file_st()
data_pr = read_file_pr()


def load_students(data):
    for text in data:
        return text['full_name']


def load_professions(data):
    for text in data_st:
        return text['skills']


def get_student_by_pk(pk, data):
    for text in data_st:
        if str(pk) == str(text['pk']):
            student = text['full_name']
            return student
    return False


def get_skill(pk, data):
    for text in data_st:
        if str(pk) == str(text['pk']):
            lang = text['skills']
            return lang


def get_profession_by_title(title, data):
    for text in data_pr:
        if title in text['title']:
            skils = text['skills']
            return skils


def check_fitness(student, profession, skill):
    yes = []
    no = []
    for i in profession:
        if i in skill:
            yes.append(i)
        elif i in profession or i in skill:
            no.append(i)
    print(f'Пригодность {100 // (len(yes) + len(no)) * len(yes)}%')
    print(f'{student} знает {yes}')
    print(f'{student} не знает {no}')

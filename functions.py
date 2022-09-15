import json


def load_students():
    with open('students.json', 'r', encoding='utf-8') as f:
        stud = json.load(f)

    for text in stud:
        return text['full_name']


def load_professions():
    with open('students.json', 'r', encoding='utf-8') as f:
        stud = json.load(f)

    for text in stud:
        return text['skills']


def get_student_by_pk(pk):
    with open('students.json', 'r', encoding='utf-8') as f:
        stud = json.load(f)

    for text in stud:
        if str(pk) == str(text['pk']):
            student = text['full_name']
            return student


def get_skill(pk):
    with open('students.json', 'r', encoding='utf-8') as f:
        stud = json.load(f)

    for text in stud:
        if str(pk) == str(text['pk']):
            lang = text['skills']
            return lang


def get_profession_by_title(title):
    with open('professions.json', 'r', encoding='utf-8') as f:
        prof = json.load(f)

    for text in prof:
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

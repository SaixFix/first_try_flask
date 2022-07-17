import json


def load_candidates(file):
    """
    Читаем из json файла
    """
    with open(file,  'r', encoding='utf-8') as f:
        list_candidates = json.load(f)
        return list_candidates


def get_all():
    """
    Читаем из списка кандидатов их имена, позиции и навыки, затем возвращаем их форматированной строкой
    """
    candidates = ""
    for i in list_candidates:
        candidates += f"<pre>Имя: {i['name']} \nПозиция кандидата: {i['position']}\nНавыки кандидата: {i['skills']}\n " \
                      f"</pre> "

    return candidates


def get_by_pk(pk):
    """
    Возвращает кандидата по pk
    """
    for i in list_candidates:
        if str(i['pk']) == pk:
            return f"<img src='({i['picture']})'>\n\n<pre>Имя: {i['name']} \nПозиция кандидата: {i['position']}\n" \
                   f"Навыки кандидата: {i['skills']}\n </pre> "
    else:
        return "такого кандидата нет"


def get_by_skill(list, skill_name):
    """
    Возвращает кандидата по навыку
    """
    candidates = ""
    for i in list:
        if skill_name.lower() in i['skills'].lower():
            candidates += f"<pre>Имя: {i['name']} \nПозиция кандидата: {i['position']}\nНавыки кандидата: {i['skills']}\n " \
                      f"</pre> "

    return candidates


list_candidates = load_candidates('candidates.json')


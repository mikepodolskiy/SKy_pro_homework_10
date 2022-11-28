# import required libraries

import json
import requests


def load_candidates(source):
    """
    function imports data from weg or json file
    :param source: source of data - url or filename
    :return: data from file when detecting ".json" in name, or trying to get data from web in another case
    """
    if ".json" in source:
        with open(source, mode='r', encoding='utf-8') as file:
            return json.load(file)
    else:
        response = requests.get(source)
        return response.json()



def get_all(source):
    return load_candidates(source)


def get_by_pk(pk, source):
    candidates = load_candidates(source)
    for person in candidates:
        if person["pk"] == pk:
            return person


def get_by_skill(skill_name, source):
    # names_by_skills = []
    # for person in candidates:
    #     if skill_name.lower() in person["skills"].lower():
    #         names_by_skills.append(person["name"])
    # return ", ".join(names_by_skills)
    candidates = load_candidates(source)
    return [person for person in candidates if skill_name.lower() in person["skills"].lower().split(", ")]

print(get_by_skill("python", "candidates.json"))
print("делегирование, пользоваться календарем, обсуждать важные вопросы".split(", "))
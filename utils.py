# import required libraries

import json
import requests


def load_candidates(source):
    """
    function imports data from web or json file
    :param source: filename or url with json data
    :return: data from file when detecting ".json" in name, or trying to get data from web in another case
    """
    if ".json" in source:
        with open(source, mode='r', encoding='utf-8') as file:
            return json.load(file)
    else:
        response = requests.get(source)
        return response.json()


def get_all(source):
    """
    get all candidates from source
    :param source: filename or url with json data
    :return: load_candidates function value
    """
    return load_candidates(source)


def get_by_pk(pk, source):
    """
    function finds one candidate from data according its primary key
    :param pk: given primary key
    :param source: filename or url with json data
    :return: data of person having given pk (dict)
    """
    candidates = load_candidates(source)
    for person in candidates:
        if person["pk"] == pk:
            return person


def get_by_skill(skill_name, source):
    """
    function searching for persons with required skill
    :param skill_name: required skill
    :param source: filename or url with json data
    :return: list of persons with required skill
    """
    candidates = load_candidates(source)
    return [person for person in candidates if skill_name.lower() in person["skills"].lower().split(", ")]


print(get_by_pk(3, "candidates.json"))
print(get_by_skill("python", "candidates.json"))

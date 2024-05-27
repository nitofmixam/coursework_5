import requests
import json


def parse_vacancies():
    global vacancies_sorted
    companies = ["Tinkoff", "Yandex", "OZON", "Wildberries", "Alfabank", "Sberbank", "SkyPro", "SkyEng", "VK", "QIWI"]
    api_url = "https://api.hh.ru/vacancies"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64)'}
    vacancies = []

    for company in companies:
        params = {'text': company, 'area': 1, 'per_page': 100}
        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()

        for vacancy in data['items']:
            vacancy_data = {}
            vacancy_data['id'] = vacancy['id']
            vacancy_data['name'] = vacancy['name']
            vacancy_data['company_name'] = vacancy['employer']['name']
            vacancy_data['url'] = vacancy['alternate_url']
            salary = vacancy['salary']
            if salary:
                vacancy_data['salary'] = salary['from'] if salary['from'] else None
            else:
                vacancy_data['salary'] = None
            vacancies.append(vacancy_data)
            vacancies_sorted = [dict(s) for s in set(frozenset(d.items()) for d in vacancies)]

    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(vacancies_sorted, file, ensure_ascii=False)

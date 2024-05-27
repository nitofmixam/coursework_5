import psycopg2
import json


def create_table():
    with psycopg2.connect(host="localhost", database="hh", user="postgres", password="12345") as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE vacancies"
                        "("
                        "   id INTEGER PRIMARY KEY,"
                        "   name VARCHAR(150),"
                        "   company_name VARCHAR(100),"
                        "   url VARCHAR,"
                        "   salary INTEGER"
                        ")")


def fill_table():
    with psycopg2.connect(host="localhost", database="hh", user="postgres", password="12345") as conn:
        with conn.cursor() as cur:
            with open('vacancies.json', 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                for item in json_data:
                    cur.execute(
                        "INSERT INTO vacancies (id, name, company_name, url, salary) VALUES (%s, %s, %s, %s, %s)",
                        (item['id'], item['name'], item['company_name'], item['url'], item['salary']))





import requests
import json
import psycopg2
from utils import parse_vacancies
from tables import create_table, fill_table
from DBManager import DBManager


create_table()
parse_vacancies()
fill_table()

print('Готово')


 # Пример использования классом DBManger:
db_manager = DBManager(host='localhost', database='hh', user='postgres', password='12345')

companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
print(companies_and_vacancies_count)

all_vacancies = db_manager.get_all_vacancies()
print(all_vacancies)

avg_salary = db_manager.get_avg_salary()
print(avg_salary)

vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
print(vacancies_with_higher_salary)

vacancies_with_keyword = db_manager.get_vacancies_with_keyword('python')
print(vacancies_with_keyword)

db_manager.close_connection()



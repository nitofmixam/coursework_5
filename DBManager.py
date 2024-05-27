import psycopg2


class DBManager:
    def __init__(self, host, database, user, password):
        self.conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        query = """
        SELECT company_name, COUNT(*) AS vacancies_count
        FROM vacancies
        GROUP BY company_name
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def get_all_vacancies(self):
        query = """
        SELECT company_name, name, salary, url
        FROM vacancies
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return results

    def get_avg_salary(self):
        query = """
        SELECT AVG(salary) AS avg_salary
        FROM vacancies
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    def get_vacancies_with_higher_salary(self):
        avg_salary = self.get_avg_salary()
        query = """
        SELECT company_name, name, salary, url
        FROM vacancies
        WHERE salary > %s
        """
        self.cursor.execute(query, (avg_salary,))
        results = self.cursor.fetchall()
        return results

    def get_vacancies_with_keyword(self, keyword):
        query = """
        SELECT company_name, name, salary, url
        FROM vacancies
        WHERE name ILIKE %s
        """
        self.cursor.execute(query, ('%' + keyword + '%',))
        results = self.cursor.fetchall()
        return results

    def close_connection(self):
        self.cursor.close()
        self.conn.close()



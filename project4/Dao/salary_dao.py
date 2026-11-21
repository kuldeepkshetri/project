from Databases.connection import Databases
from Model.salary import Salary

class SalaryDAO:


    def add_salary(self, salary):

        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        INSERT INTO salary
        (
            employee_id,
            basic_salary,
            allowance,
            deduction,
            overtime_rate
        )
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            salary.employee_id,
            salary.basic_salary,
            salary.allowance,
            salary.deduction,
            salary.overtime_rate
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def get_salary_by_employee(self, employee_id):

        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        SELECT * FROM salary
        WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row:

            return Salary(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

        return None

    def update_salary(self, salary):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        UPDATE salary
        SET basic_salary = %s,
            allowance = %s,
            deduction = %s,
            overtime_rate = %s
        WHERE employee_id = %s
        """

        values = (
            salary.basic_salary,
            salary.allowance,
            salary.deduction,
            salary.overtime_rate,
            salary.employee_id
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def delete_salary(self, employee_id):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        DELETE FROM salary
        WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))

        connection.commit()

        cursor.close()
        connection.close()
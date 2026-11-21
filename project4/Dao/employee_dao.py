from Databases.connection import Databases
from Model.employee import Employee


class EmployeeDAO:


    def add_employee(self, employee):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        insert into employee
        (name, email, phone, department, designation, joining_date, status)
        values (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            employee.name,
            employee.email,
            employee.phone,
            employee.department,
            employee.designation,
            employee.joining_date,
            employee.status
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def get_all_employees(self):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = "select * from employee"

        cursor.execute(query)

        rows = cursor.fetchall()

        employees = []

        for row in rows:

            employee = Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
            employees.append(employee)
        cursor.close()
        connection.close()
        return employees

    def get_employee_by_id(self, employee_id):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = " select * from employee where employee_id = %s"

        cursor.execute(query, (employee_id,))

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row:

            return Employee(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])

        return None

    def update_employee(self, employee):

        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        update employee set name = %s,
            email = %s,
            phone = %s,
            department = %s,
            designation = %s,
            joining_date = %s,
            status = %s
        where employee_id = %s
        """

        values = (
            employee.name,
            employee.email,
            employee.phone,
            employee.department,
            employee.designation,
            employee.joining_date,
            employee.status,
            employee.employee_id
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def delete_employee(self, employee_id):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = "delete from employee where employee_id = %s "

        cursor.execute(query, (employee_id,))

        connection.commit()

        cursor.close()
        connection.close()


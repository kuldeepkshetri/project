from Databases.connection import Databases
from Model.payroll import Payroll


class PayrollDAO:


    def add_payroll(self, payroll):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """insert into payroll ( employee_id, payroll_month, payroll_year, basic_salary, overtime_amount, allowance,
            deduction , gross_salary, net_salary, payment_status, payment_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            payroll.employee_id,
            payroll.payroll_month,
            payroll.payroll_year,
            payroll.basic_salary,
            payroll.overtime_amount,
            payroll.allowance,
            payroll.deduction,
            payroll.gross_salary,
            payroll.net_salary,
            payroll.payment_status,
            payroll.payment_date
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()


    def get_payroll_by_employee(self, employee_id):

        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = "select * from payroll where employee_id = %s order by payroll_year desc, payroll_month desc "

        cursor.execute(query, (employee_id,))

        rows = cursor.fetchall()

        payroll_list = []

        for row in rows:

            payroll = Payroll( row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11] )

            payroll_list.append(payroll)

        cursor.close()
        connection.close()

        return payroll_list


    def get_payroll_by_month(self, month, year):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = "select * from payroll where payroll_month = %s and payroll_year = %s "

        cursor.execute(query, (month, year))

        rows = cursor.fetchall()

        payroll_list = []

        for row in rows:

            payroll = Payroll(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11] )

            payroll_list.append(payroll)

        cursor.close()
        connection.close()

        return payroll_list


    def update_payroll(self, payroll):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """update payroll set basic_salary = %s,
            overtime_amount = %s,
            allowance = %s,
            deduction = %s,
            gross_salary = %s,
            net_salary = %s,
            payment_status = %s,
            payment_date = %s
        where payroll_id = %s
        """

        values = (
            payroll.basic_salary,
            payroll.overtime_amount,
            payroll.allowance,
            payroll.deduction,
            payroll.gross_salary,
            payroll.net_salary,
            payroll.payment_status,
            payroll.payment_date,
            payroll.payroll_id
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def delete_payroll(self, payroll_id):

        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = "delete from payroll where payroll_id = %s"

        cursor.execute(query, (payroll_id,))
        connection.commit()

        cursor.close()
        connection.close()
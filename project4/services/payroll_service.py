from Dao.payroll_dao import PayrollDAO


class PayrollService:

    def __init__(self):
        self.payroll_dao = PayrollDAO()

    def calculate_gross_salary(
        self,
        basic_salary,
        allowance,
        overtime_amount
    ):

        gross_salary = (
            basic_salary
            + allowance
            + overtime_amount
        )

        return gross_salary

    def calculate_net_salary(
        self,
        gross_salary,
        deduction
    ):

        net_salary = gross_salary - deduction

        return net_salary

    def add_payroll(self, payroll):

        payroll.gross_salary = self.calculate_gross_salary(
            payroll.basic_salary,
            payroll.allowance,
            payroll.overtime_amount
        )

        payroll.net_salary = self.calculate_net_salary(
            payroll.gross_salary,
            payroll.deduction
        )

        self.payroll_dao.add_payroll(payroll)

        print("Payroll added successfully.")
        return True

    def get_payroll_by_employee(self, employee_id):

        return self.payroll_dao.get_payroll_by_employee(
            employee_id
        )

    def get_payroll_by_month(self, month, year):

        return self.payroll_dao.get_payroll_by_month(
            month,
            year
        )

    def update_payroll(self, payroll):

        payroll.gross_salary = self.calculate_gross_salary(
            payroll.basic_salary,
            payroll.allowance,
            payroll.overtime_amount
        )

        payroll.net_salary = self.calculate_net_salary(
            payroll.gross_salary,
            payroll.deduction
        )

        self.payroll_dao.update_payroll(payroll)

        print("Payroll updated successfully.")
        return True

    def delete_payroll(self, payroll_id):

        self.payroll_dao.delete_payroll(payroll_id)

        print("Payroll deleted successfully.")
        return True
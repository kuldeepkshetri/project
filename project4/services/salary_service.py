from Dao.salary_dao import SalaryDAO


class SalaryService:

    def __init__(self):
        self.salary_dao = SalaryDAO()

    def add_salary(self, salary):

        if salary.basic_salary <= 0:
            print("Basic salary must be greater than 0.")
            return False

        self.salary_dao.add_salary(salary)

        print("Salary added successfully.")
        return True

    def get_salary_by_employee(self, employee_id):

        return self.salary_dao.get_salary_by_employee(
            employee_id
        )

    def update_salary(self, salary):

        existing_salary = self.salary_dao.get_salary_by_employee(
            salary.employee_id
        )

        if not existing_salary:
            print("Salary record not found.")
            return False

        self.salary_dao.update_salary(salary)

        print("Salary updated successfully.")
        return True

    def delete_salary(self, employee_id):

        existing_salary = self.salary_dao.get_salary_by_employee(
            employee_id
        )

        if not existing_salary:
            print("Salary record not found.")
            return False

        self.salary_dao.delete_salary(employee_id)

        print("Salary deleted successfully.")
        return True
from Dao.employee_dao import EmployeeDAO


class EmployeeService:

    def __init__(self):
        self.employee_dao = EmployeeDAO()

    def add_employee(self, employee):

        if not employee.name:
            print("Employee name is required.")
            return False

        if not employee.email:
            print("Employee email is required.")
            return False

        self.employee_dao.add_employee(employee)

        print("Employee added successfully.")
        return True

    def get_all_employees(self):

        return self.employee_dao.get_all_employees()

    def get_employee_by_id(self, employee_id):

        return self.employee_dao.get_employee_by_id(employee_id)

    def update_employee(self, employee):

        existing_employee = self.employee_dao.get_employee_by_id(
            employee.employee_id
        )

        if not existing_employee:
            print("Employee not found.")
            return False

        self.employee_dao.update_employee(employee)

        print("Employee updated successfully.")
        return True

    def delete_employee(self, employee_id):

        employee = self.employee_dao.get_employee_by_id(employee_id)

        if not employee:
            print("Employee not found.")
            return False

        self.employee_dao.delete_employee(employee_id)

        print("Employee deleted successfully.")
        return True


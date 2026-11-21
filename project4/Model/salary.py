class Salary:

    def __init__(
        self,
        salary_id=None,
        employee_id=None,
        basic_salary=0.00,
        allowance=0.00,
        deduction=0.00,
        overtime_rate=0.00
    ):
        self.salary_id = salary_id
        self.employee_id = employee_id
        self.basic_salary = basic_salary
        self.allowance = allowance
        self.deduction = deduction
        self.overtime_rate = overtime_rate
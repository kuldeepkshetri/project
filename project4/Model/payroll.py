class Payroll:

    def __init__(
        self,
        payroll_id=None,
        employee_id=None,
        payroll_month=None,
        payroll_year=None,
        basic_salary=0.00,
        overtime_amount=0.00,
        allowance=0.00,
        deduction=0.00,
        gross_salary=0.00,
        net_salary=0.00,
        payment_status="Pending",
        payment_date=None
    ):
        self.payroll_id = payroll_id
        self.employee_id = employee_id
        self.payroll_month = payroll_month
        self.payroll_year = payroll_year
        self.basic_salary = basic_salary
        self.overtime_amount = overtime_amount
        self.allowance = allowance
        self.deduction = deduction
        self.gross_salary = gross_salary
        self.net_salary = net_salary
        self.payment_status = payment_status
        self.payment_date = payment_date
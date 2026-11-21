class Employee:

    def __init__(self,
                employee_id=None, 
                name=None, 
                email=None,
                phone=None, 
                department=None, 
                designation=None,
                joining_date=None, 
                status="Active"):

        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.designation = designation
        self.joining_date = joining_date
        self.status = status
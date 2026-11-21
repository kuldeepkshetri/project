class Attendance:

    def __init__(
        self,
        attendance_id=None,
        employee_id=None,
        attendance_date=None,
        check_in=None,
        check_out=None,
        status=None,
        working_hours=0.00
    ):
        self.attendance_id = attendance_id
        self.employee_id = employee_id
        self.attendance_date = attendance_date
        self.check_in = check_in
        self.check_out = check_out
        self.status = status
        self.working_hours = working_hours
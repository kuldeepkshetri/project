from Dao.attendance_dao import AttendanceDAO


class AttendanceService:

    def __init__(self):
        self.attendance_dao = AttendanceDAO()

    def add_attendance(self, attendance):

        if not attendance.employee_id:
            print("Employee ID is required.")
            return False

        if not attendance.attendance_date:
            print("Attendance date is required.")
            return False

        self.attendance_dao.add_attendance(attendance)

        print("Attendance added successfully.")
        return True

    def get_employee_attendance(self, employee_id):

        return self.attendance_dao.get_attendance_by_employee(
            employee_id
        )

    def get_attendance_by_date(self, attendance_date):

        return self.attendance_dao.get_attendance_by_date(
            attendance_date
        )

    def update_attendance(self, attendance):

        self.attendance_dao.update_attendance(attendance)

        print("Attendance updated successfully.")
        return True

    def delete_attendance(self, attendance_id):

        self.attendance_dao.delete_attendance(attendance_id)

        print("Attendance deleted successfully.")
        return True
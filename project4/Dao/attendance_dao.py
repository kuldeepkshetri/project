from Databases.connection import Databases
from Model.attendance import Attendance

class AttendanceDAO:


    def add_attendance(self, attendance):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = """ insert into attendance
        ( employee_id, attendance_date, check_in, check_out, status, working_hours)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            attendance.employee_id,
            attendance.attendance_date,
            attendance.check_in,
            attendance.check_out,
            attendance.status,
            attendance.working_hours
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def get_attendance_by_employee(self, employee_id):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = "select * from attendance  where employee_id = %s order by attendance_date desc"

        cursor.execute(query, (employee_id,))

        rows = cursor.fetchall()

        attendance_list = []

        for row in rows:

            attendance = Attendance(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

            attendance_list.append(attendance)

        cursor.close()
        connection.close()

        return attendance_list

    def get_attendance_by_date(self, attendance_date):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = " select * from attendance where attendance_date = %s"

        cursor.execute(query, (attendance_date,))

        rows = cursor.fetchall()

        attendance_list = []

        for row in rows:

            attendance = Attendance(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            attendance_list.append(attendance)

        cursor.close()
        connection.close()

        return attendance_list

    def update_attendance(self, attendance):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = "update attendance set attendance_date = %s , check_in = %s, check_out = %s, status = %s, working_hours = %s where attendance_id = %s"

        values = (
            attendance.attendance_date,
            attendance.check_in,
            attendance.check_out,
            attendance.status,
            attendance.working_hours,
            attendance.attendance_id
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def delete_attendance(self, attendance_id):
        db = Databases()
        connection = db.connect()
        cursor = connection.cursor()

        query = " delete from attendance where attendance_id = %s"

        cursor.execute(query, (attendance_id,))

        connection.commit()

        cursor.close()
        connection.close()
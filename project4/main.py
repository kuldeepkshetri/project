from Model.employee import Employee
from Model.attendance import Attendance
from Model.salary import Salary
from Model.payroll import Payroll

from services.employee_service import EmployeeService
from services.attendance_service import AttendanceService
from services.salary_service import SalaryService
from services.payroll_service import PayrollService

employee_service = EmployeeService()
attendance_service = AttendanceService()
salary_service = SalaryService()
payroll_service = PayrollService()

def employee_menu():
    while True:
        print("\n========== EMPLOYEE MANAGEMENT ==========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Back")

        choice = input("Enter your choice: ")
        if choice == "1":

            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            department = input("Enter department: ")
            designation = input("Enter designation: ")
            joining_date = input("Enter joining date (YYYY-MM-DD): ")

            employee = Employee(name=name,email=email,phone=phone,department=department,designation=designation,joining_date=joining_date)

            employee_service.add_employee(employee)

        elif choice == "2":

            employees = employee_service.get_all_employees()

            if not employees:
                print("No employees found.")
            else:
                for employee in employees:
                    print("\n-----------------------------")
                    print("Employee ID:", employee.employee_id)
                    print("Name:", employee.name)
                    print("Email:", employee.email)
                    print("Phone:", employee.phone)
                    print("Department:", employee.department)
                    print("Designation:", employee.designation)
                    print("Joining Date:", employee.joining_date)
                    print("Status:", employee.status)

        elif choice == "3":

            employee_id = int(input("Enter employee ID: "))

            employee = employee_service.get_employee_by_id(
                employee_id
            )

            if employee:

                print("\n-----------------------------")
                print("Employee ID:", employee.employee_id)
                print("Name:", employee.name)
                print("Email:", employee.email)
                print("Phone:", employee.phone)
                print("Department:", employee.department)
                print("Designation:", employee.designation)
                print("Joining Date:", employee.joining_date)
                print("Status:", employee.status)

            else:
                print("Employee not found.")

        elif choice == "4":

            employee_id = int(input("Enter employee ID: "))

            employee = employee_service.get_employee_by_id(
                employee_id
            )

            if not employee:
                print("Employee not found.")
                continue

            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            department = input("Enter new department: ")
            designation = input("Enter new designation: ")
            joining_date = input(
                "Enter new joining date (YYYY-MM-DD): "
            )
            status = input("Enter status: ")

            employee = Employee(employee_id,name,email,phone,department,designation,joining_date,status)

            employee_service.update_employee(employee)

        elif choice == "5":

            employee_id = int(input("Enter employee ID: "))

            employee_service.delete_employee(employee_id)

        elif choice == "6":

            break

        else:
            print("Invalid choice.")


def attendance_menu():

    while True:

        print("\n========== ATTENDANCE MANAGEMENT ==========")
        print("1. Add Attendance")
        print("2. View Employee Attendance")
        print("3. View Attendance By Date")
        print("4. Update Attendance")
        print("5. Delete Attendance")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            employee_id = int(input("Enter employee ID: "))
            attendance_date = input(
                "Enter date (YYYY-MM-DD): "
            )
            check_in = input("Enter check-in time (HH:MM:SS): ")
            check_out = input("Enter check-out time (HH:MM:SS): ")
            status = input("Enter status: ")
            working_hours = float(
                input("Enter working hours: ")
            )

            attendance = Attendance(employee_id=employee_id,attendance_date=attendance_date,check_in=check_in,check_out=check_out,status=status,working_hours=working_hours )

            attendance_service.add_attendance(attendance)

        elif choice == "2":

            employee_id = int(input("Enter employee ID: "))

            records = attendance_service.get_employee_attendance(
                employee_id
            )

            if not records:
                print("No attendance records found.")
            else:

                for record in records:

                    print("\n-----------------------------")
                    print("Attendance ID:", record.attendance_id)
                    print("Employee ID:", record.employee_id)
                    print("Date:", record.attendance_date)
                    print("Check In:", record.check_in)
                    print("Check Out:", record.check_out)
                    print("Status:", record.status)
                    print("Working Hours:", record.working_hours)

        elif choice == "3":

            attendance_date = input(
                "Enter date (YYYY-MM-DD): "
            )

            records = attendance_service.get_attendance_by_date(
                attendance_date
            )

            if not records:
                print("No attendance records found.")
            else:

                for record in records:

                    print("\n-----------------------------")
                    print("Attendance ID:", record.attendance_id)
                    print("Employee ID:", record.employee_id)
                    print("Date:", record.attendance_date)
                    print("Status:", record.status)
                    print("Working Hours:", record.working_hours)

        elif choice == "4":
            attendance_id = int(input("Enter attendance ID: ")   )
            employee_id = int(input("Enter employee ID: "))
            attendance_date = input("Enter date (YYYY-MM-DD): " )
            check_in = input( "Enter check-in time (HH:MM:SS): " )
            check_out = input("Enter check-out time (HH:MM:SS): "  )
            status = input("Enter status: ")
            working_hours = float(input("Enter working hours: ") )
            attendance = Attendance(attendance_id,employee_id,attendance_date,check_in,check_out,status,working_hours )
            attendance_service.update_attendance(attendance)

        elif choice == "5":

            attendance_id = int(
                input("Enter attendance ID: ")
            )

            attendance_service.delete_attendance(
                attendance_id
            )

        elif choice == "6":

            break

        else:
            print("Invalid choice.")

def salary_menu():

    while True:

        print("\n========== SALARY MANAGEMENT ==========")
        print("1. Add Salary")
        print("2. View Salary")
        print("3. Update Salary")
        print("4. Delete Salary")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            employee_id = int(
                input("Enter employee ID: ")
            )

            basic_salary = float(
                input("Enter basic salary: ")
            )

            allowance = float(
                input("Enter allowance: ")
            )

            deduction = float(
                input("Enter deduction: ")
            )

            overtime_rate = float(
                input("Enter overtime rate: ")
            )

            salary = Salary(employee_id=employee_id,basic_salary=basic_salary,allowance=allowance,deduction=deduction,overtime_rate=overtime_rate
            )

            salary_service.add_salary(salary)

        elif choice == "2":

            employee_id = int(
                input("Enter employee ID: ")
            )

            salary = salary_service.get_salary_by_employee(
                employee_id
            )

            if salary:

                print("\n-----------------------------")
                print("Salary ID:", salary.salary_id)
                print("Employee ID:", salary.employee_id)
                print("Basic Salary:", salary.basic_salary)
                print("Allowance:", salary.allowance)
                print("Deduction:", salary.deduction)
                print("Overtime Rate:", salary.overtime_rate)

            else:
                print("Salary record not found.")

        elif choice == "3":

            employee_id = int(
                input("Enter employee ID: ")
            )

            basic_salary = float(
                input("Enter basic salary: ")
            )

            allowance = float(
                input("Enter allowance: ")
            )

            deduction = float(
                input("Enter deduction: ")
            )

            overtime_rate = float(
                input("Enter overtime rate: ")
            )

            salary = Salary(
                employee_id=employee_id,
                basic_salary=basic_salary,
                allowance=allowance,
                deduction=deduction,
                overtime_rate=overtime_rate
            )

            salary_service.update_salary(salary)

        elif choice == "4":

            employee_id = int(
                input("Enter employee ID: ")
            )

            salary_service.delete_salary(
                employee_id
            )

        elif choice == "5":

            break

        else:
            print("Invalid choice.")

def payroll_menu():

    while True:

        print("\n========== PAYROLL MANAGEMENT ==========")
        print("1. Add Payroll")
        print("2. View Employee Payroll")
        print("3. View Payroll By Month")
        print("4. Update Payroll")
        print("5. Delete Payroll")
        print("6. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            employee_id = int(
                input("Enter employee ID: ")
            )

            month = int(
                input("Enter payroll month: ")
            )

            year = int(
                input("Enter payroll year: ")
            )

            basic_salary = float(
                input("Enter basic salary: ")
            )

            overtime_amount = float(
                input("Enter overtime amount: ")
            )

            allowance = float(
                input("Enter allowance: ")
            )

            deduction = float(
                input("Enter deduction: ")
            )

            payment_status = input(
                "Enter payment status: "
            )

            payment_date = input(
                "Enter payment date (YYYY-MM-DD): "
            )

            payroll = Payroll(employee_id=employee_id,payroll_month=month,payroll_year=year,basic_salary=basic_salary,overtime_amount=overtime_amount,allowance=allowance,deduction=deduction,payment_status=payment_status,payment_date=payment_date
            )

            payroll_service.add_payroll(payroll)

        elif choice == "2":

            employee_id = int(
                input("Enter employee ID: ")
            )

            payrolls = payroll_service.get_payroll_by_employee(
                employee_id
            )

            if not payrolls:
                print("No payroll records found.")
            else:

                for payroll in payrolls:

                    print("\n-----------------------------")
                    print("Payroll ID:", payroll.payroll_id)
                    print("Employee ID:", payroll.employee_id)
                    print("Month:", payroll.payroll_month)
                    print("Year:", payroll.payroll_year)
                    print("Basic Salary:", payroll.basic_salary)
                    print("Overtime:", payroll.overtime_amount)
                    print("Allowance:", payroll.allowance)
                    print("Deduction:", payroll.deduction)
                    print("Gross Salary:", payroll.gross_salary)
                    print("Net Salary:", payroll.net_salary)
                    print("Payment Status:", payroll.payment_status)
                    print("Payment Date:", payroll.payment_date)

        elif choice == "3":

            month = int(
                input("Enter month: ")
            )

            year = int(
                input("Enter year: ")
            )

            payrolls = payroll_service.get_payroll_by_month(
                month,
                year
            )

            if not payrolls:
                print("No payroll records found.")
            else:

                for payroll in payrolls:

                    print("\n-----------------------------")
                    print("Payroll ID:", payroll.payroll_id)
                    print("Employee ID:", payroll.employee_id)
                    print("Net Salary:", payroll.net_salary)
                    print("Payment Status:", payroll.payment_status)

        elif choice == "4":

            payroll_id = int(
                input("Enter payroll ID: ")
            )

            employee_id = int(
                input("Enter employee ID: ")
            )

            month = int(
                input("Enter payroll month: ")
            )

            year = int(
                input("Enter payroll year: ")
            )

            basic_salary = float(
                input("Enter basic salary: ")
            )

            overtime_amount = float(
                input("Enter overtime amount: ")
            )

            allowance = float(
                input("Enter allowance: ")
            )

            deduction = float(
                input("Enter deduction: ")
            )

            payment_status = input(
                "Enter payment status: "
            )

            payment_date = input(
                "Enter payment date (YYYY-MM-DD): "
            )

            payroll = Payroll(payroll_id,employee_id,month,year,basic_salary,overtime_amount,allowance,deduction,0,0,payment_status,payment_date
            )

            payroll_service.update_payroll(
                payroll
            )

        elif choice == "5":

            payroll_id = int(
                input("Enter payroll ID: ")
            )

            payroll_service.delete_payroll(
                payroll_id
            )

        elif choice == "6":

            break

        else:
            print("Invalid choice.")

def main():

    while True:

        print("\n")
        print("========================================")
        print("     EMPLOYEE PAYROLL SYSTEM")
        print("========================================")
        print("1. Employee Management")
        print("2. Attendance Management")
        print("3. Salary Management")
        print("4. Payroll Management")
        print("5. Exit")
        print("========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_menu()

        elif choice == "2":
            attendance_menu()

        elif choice == "3":
            salary_menu()

        elif choice == "4":
            payroll_menu()

        elif choice == "5":
            print("Thank you for using Employee Payroll System.")
            break

        else:
            print("Invalid choice. Please try again.")

main()
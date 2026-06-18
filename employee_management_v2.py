import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kittu@123",
    database="employee_db"
)

cursor = conn.cursor()


# Add Employee
def add_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    query = """
    INSERT INTO employees(name, age, department, salary)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, age, department, salary)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Added Successfully!")


# View Employees
def view_employees():
    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    print("\nEmployee Records")
    print("-" * 50)

    for row in rows:
        print(row)


# Update Employee
def update_employee():
    emp_id = int(input("Enter Employee ID: "))

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    department = input("Enter New Department: ")
    salary = float(input("Enter New Salary: "))

    query = """
    UPDATE employees
    SET name=%s, age=%s, department=%s, salary=%s
    WHERE emp_id=%s
    """

    values = (name, age, department, salary, emp_id)

    cursor.execute(query, values)
    conn.commit()

    print("Employee Updated Successfully!")


# Delete Employee
def delete_employee():
    emp_id = int(input("Enter Employee ID to Delete: "))

    query = "DELETE FROM employees WHERE emp_id=%s"

    cursor.execute(query, (emp_id,))
    conn.commit()

    print("Employee Deleted Successfully!")


# Menu
while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

conn.close()

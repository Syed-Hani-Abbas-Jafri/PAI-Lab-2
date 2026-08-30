employees = {
    "E101": {"name": "Ali",   "department": "IT",      "salary": 85000, "title": "Developer"},
    "E102": {"name": "Sara",  "department": "HR",      "salary": 75000, "title": "HR Manager"},
    "E103": {"name": "Ahmed", "department": "IT",      "salary": 95000, "title": "Team Lead"},
}


def search_employee(emp_id):
    return employees.get(emp_id)


def update_salary(emp_id, new_salary):
    if emp_id in employees:
        employees[emp_id]["salary"] = new_salary
    else:
        print(f"Employee {emp_id} not found.")


def add_employee(emp_id, name, department, salary, title):
    if emp_id in employees:
        print(f"Employee {emp_id} already exists.")
    else:
        employees[emp_id] = {
            "name": name,
            "department": department,
            "salary": salary,
            "title": title,
        }


def remove_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
    else:
        print(f"Employee {emp_id} not found.")


print("Search E101:", search_employee("E101"))

update_salary("E102", 78000)
print("\nAfter salary update, E102:", search_employee("E102"))

add_employee("E104", "Zain", "Finance", 90000, "Analyst")
print("\nAfter adding E104:", search_employee("E104"))

remove_employee("E103")
print("\nAfter removing E103, all employees:")
for emp_id, details in employees.items():
    print(f"  {emp_id}: {details}")

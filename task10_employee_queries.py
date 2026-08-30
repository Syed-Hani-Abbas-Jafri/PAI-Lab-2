from collections import Counter

employees = [
    ("E101", "Ali",   "IT",      85000),
    ("E102", "Sara",  "HR",      75000),
    ("E103", "Ahmed", "IT",      95000),
    ("E104", "Zain",  "Finance", 90000),
]

employees_by_id = {}
for emp_id, name, dept, salary in employees:
    employees_by_id[emp_id] = {"name": name, "department": dept, "salary": salary}


def get_employees_by_department(department):
    result = []
    for emp_id, name, dept, salary in employees:
        if dept == department:
            result.append(name)
    return result


def get_average_salary():
    total = 0
    for emp_id, name, dept, salary in employees:
        total += salary
    return total / len(employees)


def get_highest_paid():
    top_emp = employees[0]
    for emp in employees:
        if emp[3] > top_emp[3]:
            top_emp = emp
    return top_emp


def get_departments():
    result = set()
    for emp_id, name, dept, salary in employees:
        result.add(dept)
    return result


def get_department_counts():
    dept_list = []
    for emp_id, name, dept, salary in employees:
        dept_list.append(dept)
    return Counter(dept_list)


def get_employee_by_id(emp_id):
    return employees_by_id.get(emp_id)


print("IT department employees:", get_employees_by_department("IT"))
print("Average salary:", get_average_salary())

top_emp = get_highest_paid()
print(f"Highest paid: {top_emp[1]} (${top_emp[3]})")

print("Departments:", get_departments())
print("Employee count per department:", dict(get_department_counts()))

print("\nFast lookup by ID (E103):", get_employee_by_id("E103"))

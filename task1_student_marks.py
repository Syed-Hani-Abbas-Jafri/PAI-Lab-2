students = {
    "Ali":   {"Math": 85, "Physics": 78, "English": 90},
    "Sara":  {"Math": 92, "Physics": 88, "English": 95},
    "Ahmed": {"Math": 60, "Physics": 55, "English": 70},
    "Zain":  {"Math": 40, "Physics": 45, "English": 50},
}


def calculate_average(marks_dict):
    total = 0
    count = 0
    for mark in marks_dict.values():
        total += mark
        count += 1
    return total / count


def get_all_averages(students_dict):
    averages = {}
    for name, marks in students_dict.items():
        averages[name] = calculate_average(marks)
    return averages


def get_top_student(students_dict):
    averages = get_all_averages(students_dict)
    top_name = None
    top_avg = -1
    for name, avg in averages.items():
        if avg > top_avg:
            top_name = name
            top_avg = avg
    return top_name, top_avg


def students_above_threshold(students_dict, threshold):
    averages = get_all_averages(students_dict)
    result = []
    for name, avg in averages.items():
        if avg > threshold:
            result.append((name, avg))
    return result


print("All student averages:")
for name, avg in get_all_averages(students).items():
    print(f"  {name}: {avg:.2f}")

top_name, top_avg = get_top_student(students)
print(f"\nTop performing student: {top_name} ({top_avg:.2f})")

threshold = 75
print(f"\nStudents with average above {threshold}:")
for name, avg in students_above_threshold(students, threshold):
    print(f"  {name}: {avg:.2f}")

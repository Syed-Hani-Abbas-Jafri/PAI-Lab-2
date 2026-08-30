course_a = {"S001", "S002", "S003", "S004", "S005"}
course_b = {"S003", "S004", "S006", "S007"}


def students_in_both(a, b):
    return a & b


def students_only_in_a(a, b):
    return a - b


def students_only_in_b(a, b):
    return b - a


def all_unique_students(a, b):
    return a | b


print("Course A:", course_a)
print("Course B:", course_b)

print("\nEnrolled in both courses:", students_in_both(course_a, course_b))
print("Only in Course A:", students_only_in_a(course_a, course_b))
print("Only in Course B:", students_only_in_b(course_a, course_b))
print("All unique students:", all_unique_students(course_a, course_b))

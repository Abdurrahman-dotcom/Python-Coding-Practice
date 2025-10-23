student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
    else:
        student_records[name]= {"age": age, "grades": set(), "courses": set(courses)}
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name in student_records:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:
        print(f"Student '{name}' not found.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    elif course in student_records[name]["courses"]:
        return True
    else:
        return False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    elif not student_records[name]["grades"]:
        return 0
    else: 
        grades = student_records[name]["grades"]
        avg = sum(grades) / len(grades)
        return float(avg)

def list_students_by_course(course):
    students = []
    for name in student_records:
        if course in student_records[name]["courses"]:
            students.append(name)
    return students

def filter_top_students(treshold):
    top_students = []
    for name in student_records:
        avg = calculate_average_grade(name)
        if avg > treshold:
            top_students.append(name)
    return top_students

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
# ============================================================
# Case Study 10: Campus Management System - Final Project
# Roll: 26000985 | Section: CSM2
# Name: Yarlagadda Divya Sita Maha Lakshmi
# ============================================================
# Problem Statement:
# Create a complete campus management system combining all concepts
# Manage students, courses, attendance, fees in single system
#
# Objectives: Use all concepts - nested lists, dict, tuple, loops, functions, strings
# Algorithm:
# 1. Start
# 2. Initialize students database as nested list
# 3. Initialize courses tuple
# 4. Initialize fees dictionary
# 5. Define functions for add, search, display
# 6. Calculate total students, total fees collected
# 7. Find course with max enrollment
# 8. Display complete campus report
# 9. Stop
#
# Flowchart: Start -> Init Data -> Functions -> Process -> Analysis -> Report -> Stop
# ============================================================

# Tuple - Fixed courses
COURSES = ("CSE", "CSM", "CSD", "ECE", "EEE")

# Dictionary - Course fees
FEES_STRUCTURE = {
    "CSE": 100000,
    "CSM": 110000,
    "CSD": 105000,
    "ECE": 95000,
    "EEE": 90000
}

def add_student(database, roll, name, course, attendance):
    """Add new student to database"""
    if course not in COURSES:
        return False
    database.append([roll, name, course, attendance])
    return True

def search_student(database, roll):
    """Search student by roll number"""
    for student in database:
        if student[0] == roll:
            return student
    return None

def calculate_total_fees(database):
    """Calculate total fees collected"""
    total = 0
    for student in database:
        course = student[2]
        total += FEES_STRUCTURE.get(course, 0)
    return total

def main():
    # Nested List - Student Database [Roll, Name, Course, Attendance%]
    students_db = [
        [26000985, "Divya Sita Maha Lakshmi", "CSM", 92],
        [26000901, "Rahul Kumar", "CSE", 85],
        [26000902, "Priya Sharma", "CSD", 88],
        [26000903, "Anjali Reddy", "ECE", 78],
        [26000904, "Karthik Rao", "CSM", 90],
        [26000905, "Suresh Babu", "EEE", 75],
        [26000906, "Geetha Lakshmi", "CSE", 95]
    ]

    print("===== Campus Management System - 26000985 =====")
    print(f"College: NRI Institute | Section: CSM2")
    print("-" * 75)

    # Display all students
    print(f"{'Roll':<12} {'Name':<25} {'Course':<8} {'Attend%':<8} {'Fees'}")
    print("-" * 75)
    for student in students_db:
        roll, name, course, attend = student
        fees = FEES_STRUCTURE[course]
        print(f"{roll:<12} {name:<25} {course:<8} {attend:<8} {fees}")

    print("-" * 75)

    # Analysis 1: Total students
    print(f"\nTotal Students: {len(students_db)}")

    # Analysis 2: Course wise count - Using dictionary
    course_count = {}
    for c in COURSES:
        course_count[c] = 0

    for student in students_db:
        course = student[2]
        if course in course_count:
            course_count[course] += 1

    print("\n--- Course Wise Enrollment ---")
    for course, count in course_count.items():
        print(f"{course}: {count} students")

    # Find max enrollment course
    max_course = ""
    max_count = 0
    for course, count in course_count.items():
        if count > max_count:
            max_count = count
            max_course = course
    print(f"Most Popular Course: {max_course} ({max_count} students)")

    # Analysis 3: Total fees
    total_fees = calculate_total_fees(students_db)
    print(f"\nTotal Fees Collected: Rs. {total_fees}")

    # Analysis 4: Attendance audit
    print("\n--- Attendance Audit (<75% Alert) ---")
    low_attendance = []
    for student in students_db:
        if student[3] < 75:
            low_attendance.append(student)
            print(f"  ALERT: {student[1]} ({student[0]}) - {student[3]}%")
    
    if len(low_attendance) == 0:
        print("  All students have good attendance!")

    # Analysis 5: Search function demo
    print("\n--- Search Demo: Roll 26000985 ---")
    result = search_student(students_db, 26000985)
    if result:
        print(f"Found: {result[1]} - Course: {result[2]}, Attendance: {result[3]}%")
    else:
        print("Not Found")

    # Analysis 6: Add new student demo
    print("\n--- Adding New Student ---")
    added = add_student(students_db, 26000907, "New Student", "CSM", 82)
    if added:
        print(f"Added Successfully! New Total: {len(students_db)}")
    else:
        print("Failed to add")

    print("\n===== Campus Report Generated Successfully =====")

if __name__ == "__main__":
    main()

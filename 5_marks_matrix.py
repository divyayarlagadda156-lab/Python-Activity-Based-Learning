# ============================================================
# Case Study 5: Student Marks Matrix Analysis
# Original Case 44 | Roll: 26000985 | Section: CSM2
# Name: Yarlagadda Divya Sita Maha Lakshmi
# ============================================================
# Problem Statement:
# Analyze student marks stored in matrix format
#Find topper,subject averages,and failed students
# Objectives: Use nested lists, loops, lists operations
# Algorithm:
# 1. Start
# 2. Initialize nested list marks where each row is [Name, Python, DBMS, DSA, Total]
# 3. Loop through each student to calculate total and average
# 4. For each subject, calculate class average using column loop
# 5. Find student with maximum total (Topper)
# 6. Find students with average < 40 (Fail)
# 7. Display formatted mark sheet report
# 8. Stop
# ============================================================

def main():
    # Nested list: [StudentName, Python, DBMS, DSA, OS]
    marks_matrix = [
        ["Divya_26000985", 85, 90, 78, 88],
        ["Rahul", 45, 35, 40, 30],
        ["Priya", 92, 88, 95, 90],
        ["Anjali", 60, 65, 58, 62],
        ["Karthik", 30, 25, 35, 28],
        ["Suresh", 78, 82, 80, 75]
    ]

    subjects = ["Python", "DBMS", "DSA", "OS"]
    
    print("===== Marks Matrix Analysis - 26000985 =====")
    print(f"{'Name':<18} {'Py':<5} {'DBMS':<6} {'DSA':<5} {'OS':<5} {'Total':<7} {'Avg':<6} {'Result'}")
    print("-" * 85)

    class_totals = [0, 0, 0, 0]  # For each subject
    topper_name = ""
    topper_total = 0
    fail_students = []

    # Row-wise analysis
    for i in range(len(marks_matrix)):
        row = marks_matrix[i]
        name = row[0]
        # Unpacking marks using slicing
        subject_marks = row[1:]
        
        total = 0
        for m in subject_marks:
            total += m
        
        average = total / len(subject_marks)
        
        # Update class totals (column wise)
        for j in range(len(subject_marks)):
            class_totals[j] += subject_marks[j]

        # Check result
        result = "PASS"
        if average < 40:
            result = "FAIL"
            fail_students.append(name)

        # Find topper
        if total > topper_total:
            topper_total = total
            topper_name = name

        print(f"{name:<18} {subject_marks[0]:<5} {subject_marks[1]:<6} {subject_marks[2]:<5} {subject_marks[3]:<5} {total:<7} {average:<5.1f} {result}")

    print("-" * 85)
    
    # Column-wise average
    print("\n--- Subject Wise Class Average ---")
    for idx in range(len(subjects)):
        avg = class_totals[idx] / len(marks_matrix)
        print(f"{subjects[idx]}: {avg:.2f}")

    print(f"\nTopper of Class: {topper_name} with {topper_total} marks")
    print(f"Total Fail Students: {len(fail_students)}")
    if len(fail_students) > 0:
        print("Fail List:")
        for f in fail_students:
            print(f"  - {f}")

if __name__ == "__main__":
    main()

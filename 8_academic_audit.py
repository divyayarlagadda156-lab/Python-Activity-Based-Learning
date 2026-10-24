# ============================================================
# Case Study 8: Academic Audit and Performance Analysis
# Roll: 26000985 | Section: CSM2
# Name: Yarlagadda Divya Sita Maha Lakshmi
# ============================================================
# Problem Statement:
# Perform academic audit for students based on attendance and marks
# Categorize students into Excellent, Good, Average, Risk categories
#
# Objectives: Use nested lists, dictionary, loops, conditions
# Algorithm:
# 1. Start
# 2. Initialize student data as nested list [Name, Attendance%, Marks%]
# 3. Loop through each student
# 4. Calculate performance category based on attendance and marks
# 5. If attendance <75 and marks <60 -> Risk
# 6. If attendance >=90 and marks >=80 -> Excellent
# 7. Else categorize as Good or Average
# 8. Store results in dictionary
# 9. Display audit report with category counts
# 10. Stop
# ============================================================

def main():
    # Nested list: [Name, Attendance%, Marks%]
    students = [
        ["Divya_26000985", 92, 85],
        ["Rahul", 65, 55],
        ["Priya", 95, 92],
        ["Anjali", 80, 70],
        ["Karthik", 60, 45],
        ["Suresh", 88, 78],
        ["Geetha", 72, 65],
        ["Arjun", 95, 58],
        ["Sneha", 78, 88]
    ]

    print("===== Academic Audit Report - 26000985 =====")
    print(f"{'Name':<18} {'Attend%':<10} {'Marks%':<8} {'Category':<12} {'Action'}")
    print("-" * 75)

    audit_results = {}
    category_count = {"Excellent": 0, "Good": 0, "Average": 0, "Risk": 0}

    for i in range(len(students)):
        data = students[i]
        name = data[0]
        attendance = data[1]
        marks = data[2]

        # Categorization logic
        category = ""
        action = ""
        
        if attendance >= 90 and marks >= 80:
            category = "Excellent"
            action = "Appreciate"
        elif attendance >= 75 and marks >= 60:
            category = "Good"
            action = "Encourage"
        elif attendance >= 75 and marks < 60:
            category = "Average"
            action = "Need Support"
        elif attendance < 75 and marks >= 60:
            category = "Average"
            action = "Improve Attendance"
        else:
            category = "Risk"
            action = "Immediate Meeting"

        audit_results[name] = category
        category_count[category] += 1

        print(f"{name:<18} {attendance:<10} {marks:<8} {category:<12} {action}")

    print("-" * 75)
    print("\n--- Category Wise Summary ---")
    for cat, count in category_count.items():
        print(f"{cat}: {count} students")

    print(f"\n--- Risk Students List (Need Immediate Attention) ---")
    risk_found = False
    for name, cat in audit_results.items():
        if cat == "Risk":
            print(f"  - {name}")
            risk_found = True
    
    if not risk_found:
        print("  No risk students - Good performance!")

    print("\n--- Dictionary Data for Verification ---")
    print(f"Audit Results: {audit_results}")

if __name__ == "__main__":
    main()

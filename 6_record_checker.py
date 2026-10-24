# ============================================================
# Case Study 6: Student Record ID Checker
# Roll: 26000985 | Section: CSM2
# Name: Yarlagadda Divya Sita Maha Lakshmi
# ============================================================
# Problem Statement:
# Validate student record ID format like NRI-2023-CSE-0123
# Check if ID follows college-year-branch-number pattern
#
# Objectives: Use strings, tuples, string slicing
# Algorithm:
# 1. Start
# 2. Take student ID as input
# 3. Split ID by '-' delimiter
# 4. Check if split parts count is 4
# 5. Validate Part1 is NRI, Part2 is year 2020-2026, Part3 is branch code, Part4 is digits
# 6. Use tuple for valid branch codes
# 7. Display valid or invalid with reason
# 8. Stop
#
# Flowchart: Start -> Input ID -> Split -> Validate Each Part -> Display Result -> Stop
# ============================================================

def main():
    # Tuple for valid branches - Unpacking concept
    valid_branches = ("CSE", "CSM", "CSD", "ECE", "EEE", "MECH", "CIVIL")
    valid_college = "NRI"
    
    print("===== Student Record Checker - 26000985 =====")
    
    # Simulated IDs (No input needed for auto-run)
    test_ids = [
        "NRI-2023-CSM-0985",
        "NRI-2025-CSE-0123",
        "NRI-2020-ECE-0001",
        "ABC-2023-CSE-0123",
        "NRI-2019-CSE-0123",
        "NRI-2023-XYZ-0123",
        "NRI-2023-CSE-ABCD"
    ]

    print(f"Valid Branches: {valid_branches}")
    print("-" * 60)

    for student_id in test_ids:
        print(f"\nChecking ID: {student_id}")
        
        parts = student_id.split("-")
        
        # Validation
        if len(parts) != 4:
            print("  Result: INVALID - Format should be COLLEGE-YEAR-BRANCH-NUMBER")
            continue

        college, year, branch, number = parts  # Tuple unpacking

        # Check college
        if college != valid_college:
            print(f"  Result: INVALID - College should be {valid_college}")
            continue

        # Check year
        if not year.isdigit():
            print("  Result: INVALID - Year should be numeric")
            continue
        
        year_int = int(year)
        if year_int < 2020 or year_int > 2026:
            print("  Result: INVALID - Year should be between 2020-2026")
            continue

        # Check branch using tuple
        if branch not in valid_branches:
            print(f"  Result: INVALID - Branch {branch} not in valid list")
            continue

        # Check number
        if not number.isdigit() or len(number) != 4:
            print("  Result: INVALID - Number should be 4 digits")
            continue

        # String slicing example
        year_prefix = year[0:2]
        print(f"  Result: VALID - Year Prefix: {year_prefix}, Branch: {branch}")
        print(f"  Details: College={college}, Year={year}, Branch={branch}, No={number}")

    print("\n===== Validation Completed =====")

if __name__ == "__main__":
    main()

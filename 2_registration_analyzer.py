# ============================================================
# Case Study 2: Campus Registration Identifier Analyzer
# Name: Yarlagadda Divya Sita Maha Lakshmi
# Roll: 26000985
#Section: CSM2
# ============================================================

def main():
    test_ids = [
        "NRI-2023-CSE-0123",
        "NRI-2023-CSM-26000985",
        "NRI-23-CSE-123",
        "NRI-2023-ECE-0456",
        "NRI-2023-CSE-12AB",
        "ABC-2023-CSE-0123"
    ]

    valid_branches = ["CSE", "CSM", "ECE", "EEE", "MECH"]
    valid_colleges = ["NRI", "NRIIT"]

    print("===== Registration ID Analysis - 26000985 =====")
    
    for sid in test_ids:
        print(f"\nChecking ID: {sid}")
        parts = sid.split("-")

        if len(parts) != 4:
            print("  INVALID -> Parts should be 4")
            continue

        college, year, branch, num = parts  # Unpacking

        # College Check
        if college not in valid_colleges:
            print(f"  INVALID -> College {college} not valid")
            continue

        # Year Check
        if len(year) != 4 or not year.isdigit():
            print(f"  INVALID -> Year {year} must be 4 digits")
            continue
        if not (2000 <= int(year) <= 2026):
            print(f"  INVALID -> Year {year} out of range")
            continue

        # Branch Check
        if branch not in valid_branches:
            print(f"  INVALID -> Branch {branch} not valid")
            continue

        # Number Check
        if not num.isdigit() or len(num) != 4:
            print(f"  INVALID -> Number {num} must be 4 digits")
            continue

        print(f"  VALID -> College:{college} Year:{year} Branch:{branch} No:{num}")

    print("\n===== End =====")

if __name__ == "__main__":
    main()

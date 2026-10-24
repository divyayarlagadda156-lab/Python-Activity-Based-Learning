# ============================================================
# Case Study 29: Password Policy Validation Engine
# Name: Yarlagadda Divya Sita Maha Lakshmi
# Roll: 26000985 Section: CSM2
# ============================================================
# Problem Statement: Passwords ni 6 rules tho validate cheyali
# Objectives: loops, strings, lists, tuples, unpacking vadali
# Algorithm:
# 1. Start
# 2. List of (username, password) tuples teesuko
# 3. Prati password ki loop
# 4. Length, upper, lower, digit, special, prohibited checks
# 5. Errors list lo store cheyi
# 6. Valid/Invalid print cheyi
# 7. Stop
# ============================================================

def main():
    test_passwords = [
        ("Divya", "Divya@123"),
        ("Rahul", "abc"),
        ("Priya", "DIVYA12345"),
        ("Admin", "Divya123"),
        ("Test", "Divya@abc"),
        ("User1", "Div@1"),
        ("26000985", "Maha@2023Lakshmi")
    ]
    prohibited = ("password", "123", "abc", "qwerty")
    special_chars = ["@", "#", "$", "%", "&"]

    print("===== Password Validation Report - 26000985 =====")
    
    for username, pwd in test_passwords:
        print(f"\nChecking: {username} -> {pwd}")
        errors = []

        if len(pwd) < 8:
            errors.append("Length < 8")

        upper_found = False
        for ch in pwd:
            if ch.isupper():
                upper_found = True
                break
        if not upper_found:
            errors.append("No Uppercase letter")

        lower_found = False
        for ch in pwd:
            if ch.islower():
                lower_found = True
                break
        if not lower_found:
            errors.append("No Lowercase letter")

        digit_found = False
        for ch in pwd:
            if ch.isdigit():
                digit_found = True
                break
        if not digit_found:
            errors.append("No Digit")

        special_found = False
        for sp in special_chars:
            if sp in pwd:
                special_found = True
                break
        if not special_found:
            errors.append("No Special Char @#$%&")

        pwd_lower = pwd.lower()
        for bad in prohibited:
            if bad in pwd_lower:
                errors.append(f"Contains prohibited '{bad}'")

        for i in range(len(pwd)-2):
            if pwd[i] == pwd[i+1] == pwd[i+2]:
                errors.append(f"Repeated '{pwd[i]}' 3 times")
                break

        if len(errors) == 0:
            print("  Result: VALID PASSWORD")
        else:
            print("  Result: INVALID")
            for err in errors:
                print("   -", err)

if __name__ == "__main__":
    main()

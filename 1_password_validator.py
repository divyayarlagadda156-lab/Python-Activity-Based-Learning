# ============================================================
# Case Study 1: Password Policy Validation Engine
# Name: Yarlagadda Divya Sita Maha Lakshmi
# Roll: 26000985 Section: CSM2
# ============================================================
# Problem Statement:validate passwords using 6 rules:length,uppercase,lowercase,digit,special character,no prohibited words
# Objectives:use loops,strings,lists,tuples,unpacking
# Algorithm:
# 1. Start
# 2. List of (username, password) tuples 
# 3.loop for each password
# 4.check Length, upper, lower, digit, special, prohibited 
# 5. store errors in error list
# 6. print valid/invaild
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

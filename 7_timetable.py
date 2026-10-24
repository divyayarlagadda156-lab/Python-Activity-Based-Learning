# ============================================================
# Case Study 7: Timetable Slots to Days Mapping
# Roll: 26000985 | Section: CSM2
# Name: Yarlagadda Divya Sita Maha Lakshmi
# ============================================================
# Problem Statement:
# Map timetable slots to days and find free periods
# Manage weekly schedule using dictionary and list concepts
#
# Objectives: Use dictionary, list, tuple, loops
# Algorithm:
# 1. Start
# 2. Initialize timetable dictionary with day as key and slots list as value
# 3. Display full timetable
# 4. Find free slots for each day
# 5. Count total classes per day
# 6. Find day with maximum classes
# 7. Search for a specific subject in timetable
# 8. Display final report
# 9. Stop
#
# Flowchart: Start -> Init Timetable -> Loop Days -> Find Free Slots -> Count -> Display -> Stop
# ============================================================

def main():
    # Dictionary with list values - Timetable
    timetable = {
        "Monday": ["Python", "DBMS", "FREE", "DSA", "OS", "FREE"],
        "Tuesday": ["DBMS", "Python", "OS", "FREE", "DSA", "Library"],
        "Wednesday": ["DSA", "FREE", "Python", "DBMS", "Sports", "OS"],
        "Thursday": ["OS", "DSA", "DBMS", "Python", "FREE", "FREE"],
        "Friday": ["Python Lab", "DBMS Lab", "DSA Lab", "FREE", "Seminar", "FREE"],
        "Saturday": ["FREE", "FREE", "FREE", "FREE", "FREE", "FREE"]
    }

    periods = ("9-10", "10-11", "11-12", "12-1", "2-3", "3-4")  # Tuple for periods

    print("===== Timetable Analysis - 26000985 =====")
    
    # Display timetable
    print(f"{'Day':<10} ", end="")
    for p in periods:
        print(f"{p:<12}", end="")
    print()
    print("-" * 85)

    total_classes_per_day = {}
    max_classes = 0
    max_day = ""

    for day, slots in timetable.items():
        print(f"{day:<10} ", end="")
        free_count = 0
        class_count = 0
        
        for slot in slots:
            print(f"{slot:<12}", end="")
            if slot == "FREE":
                free_count += 1
            else:
                class_count += 1
        
        total_classes_per_day[day] = class_count
        
        if class_count > max_classes:
            max_classes = class_count
            max_day = day

        print(f" | Free: {free_count}")

    print("-" * 85)
    
    # Analysis
    print("\n--- Daily Class Count ---")
    for day, count in total_classes_per_day.items():
        print(f"{day}: {count} classes")

    print(f"\nBusiest Day: {max_day} with {max_classes} classes")
    
    # Search subject
    search_subject = "Python"
    print(f"\n--- Searching for {search_subject} ---")
    found_days = []
    for day, slots in timetable.items():
        # Check if Python appears (exact or partial)
        for idx, slot in enumerate(slots):
            if search_subject in slot:
                found_days.append(f"{day} ({periods[idx]})")
    
    if found_days:
        print(f"{search_subject} found on:")
        for fd in found_days:
            print(f"  - {fd}")
    else:
        print(f"{search_subject} not found")

if __name__ == "__main__":
    main()

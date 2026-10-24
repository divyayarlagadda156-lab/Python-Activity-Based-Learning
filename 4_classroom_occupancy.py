# ============================================================
# Case Study 4: Classroom Occupancy Analysis
# Roll: 26000985 | Section: CSM2
# Name: Yarlagadda Divya Sita Maha Lakshmi
# ============================================================
# Problem Statement:
# Each classroom has different time slots and student counts
#
# Objectives: Use nested lists, loops, string formatting
# Algorithm:
# 1. Start
# 2. Initialize nested list of classrooms with [room_no, capacity, occupied, time_slot]
# 3. Loop through each classroom data
# 4. Calculate occupancy percentage = (occupied/capacity)*100
# 5. Check if occupancy is Low (<30%), Medium (30-70%), High (>70%)
# 6. Find classroom with maximum occupancy
# 7. Find total students in all classrooms
# 8. Display report with status
# 9. Stop
#
# Flowchart: Start -> Input Data -> Loop Classrooms -> Calculate % -> Check Status -> Display -> Stop
# ============================================================

def main():
    # Nested list - Each inner list is [Room, Capacity, Occupied, Time]
    classrooms = [
        ["CSM2-A", 60, 55, "9AM-10AM"],
        ["CSM2-B", 60, 25, "9AM-10AM"],
        ["CSE-A", 70, 68, "10AM-11AM"],
        ["ECE-LAB", 30, 10, "11AM-12PM"],
        ["CSM2-A", 60, 45, "11AM-12PM"],
        ["NRI-AUDIT", 200, 180, "2PM-3PM"]
    ]

    print("===== Classroom Occupancy Report - 26000985 =====")
    print(f"{'Room':<12} {'Capacity':<10} {'Occupied':<10} {'%':<8} {'Status'}")
    print("-" * 60)

    total_students = 0
    max_occupancy = 0
    max_room = ""

    # Loop using index and nested list access
    for i in range(len(classrooms)):
        room_data = classrooms[i]
        room_no = room_data[0]
        capacity = room_data[1]
        occupied = room_data[2]
        time_slot = room_data[3]

        total_students += occupied

        # Calculate percentage
        percentage = (occupied / capacity) * 100

        # Check status
        status = ""
        if percentage < 30:
            status = "LOW"
        elif percentage <= 70:
            status = "MEDIUM"
        else:
            status = "HIGH"

        # Find max occupancy
        if percentage > max_occupancy:
            max_occupancy = percentage
            max_room = room_no + " (" + time_slot + ")"

        print(f"{room_no:<12} {capacity:<10} {occupied:<10} {percentage:<7.1f}% {status}")

    print("-" * 60)
    print(f"Total Students Present in Campus: {total_students}")
    print(f"Maximum Occupied Room: {max_room} with {max_occupancy:.1f}%")
    
    # Additional Analysis using tuple unpacking
    print("\n--- Time Slot Wise Analysis ---")
    time_slots = {}
    for room, cap, occ, time in classrooms:  # Tuple unpacking
        if time not in time_slots:
            time_slots[time] = 0
        time_slots[time] += occ

    for time, count in time_slots.items():
        print(f"Time {time}: {count} students")

if __name__ == "__main__":
    main()

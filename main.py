import math
def ski_jump_calculator():
    hill_type = input("Enter hill type (normal/large): ").strip().lower()

    if hill_type == "normal":
        speed = 46
        points_per_meter = 2
        par = 90
        height = 60
    elif hill_type == "large":
        speed = 70
        points_per_meter = 1.8
        par = 120
        height = 100
    else:
        print("Invalid hill type.")
        return

    time_in_air = math.sqrt((2 * height) / 9.8)

    distance_traveled = speed * time_in_air

    points = 60 + (distance_traveled - par) * points_per_meter

    print(f"The Olympic ski jumper traveled {distance_traveled:.2f} meters.")
    print(f"Points earned: {points:.2f}")

    if points >= 61:
        print("Great job for doing better than par!")
    elif points < 10:
        print("What happened??")
    else:
        print("Sorry you didn’t go very far.")


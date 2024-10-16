#Max Rice and Jenna Cuti
#Lab 2
#Program takes a ski jump and based on the hill type calculates air time, distance traveled, and points scored



import math

#input from user hill type
hill_type = input("Enter hill type (normal/large): ").strip().lower()

#stores info for different hill types
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

#variables which calculate the outputs
time_in_air = math.sqrt((2 * height) / 9.8)

distance_traveled = speed * time_in_air

points = 60 + (distance_traveled - par) * points_per_meter

print(f"The Olympic ski jumper traveled {distance_traveled:.2f} meters.")
print(f"Points earned: {points:.2f}")

#if statements which tell user how good they do
if points >= 61:
    print("Great job for doing better than par!")
elif points < 10:
    print("What happened??")
else:
    print("Sorry you didn’t go very far.")


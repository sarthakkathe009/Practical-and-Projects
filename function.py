def thing():
    print("Hello")
    print("Fun")

thing()
#================== datetime lib ======================#
from datetime import datetime, timedelta

now = datetime.now()
print("ISO:",now.strftime("%Y-%m-%d %H:%M:%S"))
print("Pretty:",now.strftime("%d-%b-%Y %I:%M %p"))
print("Weekday:",now.strftime("%A %H:%M"))

target_str = input("Enter target data(DD/MM/YYYY): ")
target_dt = datetime.strptime(target_str,"%d/%m/%Y")

today = datetime.today()
delta = target_dt - today
print("Days Remaining:",delta.days)

start_str = input("Start time (HH:MM 24h): ")
duration = float(input("Duration in hours: "))

start = datetime.strptime(start_str,"%H:%M")
end = start + timedelta(hours=duration)

print("Ends at: ",end.strftime("%H:%M"))


#================== math lib ======================#
import math

r = float(input("Radius of circle: "))
area = math.pi * r**2
circum = 2 * math.pi * r
sphere_vol = 4/3 * math.pi * math.pow(r,3)
sphere_area = 4 * math.pi * r**2

print(f"Area of Circle: {area:.3f}")
print(f"Circumference of Circle: {circum:.3f}")
print(f"Volume of Sphere: {sphere_vol:.3f}")
print(f"Area of Circle: {sphere_area:.3f}")

angle_deg = float(input("Enter angle in degrees: "))
angle_rad = math.radians(angle_deg)

print("Radians:",angle_rad)
print("Back in degree:",math.degrees(angle_rad))
print(f"sin {angle_deg}:",math.sin(angle_rad))
print(f"cos {angle_deg}:",math.cos(angle_rad))
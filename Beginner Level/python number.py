#Number

def format_number(num, fmt):
    return format(num, fmt)

result = format_number(145, 'o')
print("Formatted result:", result)
print("Representation used: Octal")

radius = 84
pi = 3.14

area = pi * radius * radius
print("Area of the pond:", area)


water_per_sq_meter = 1.4
total_water = area * water_per_sq_meter

print("Total water in the pond:", int(total_water))

distance = 490      
time_minutes =7
time_seconds = time_minutes * 60

speed = distance / time_seconds
print("Speed in meters per second:", int(speed))

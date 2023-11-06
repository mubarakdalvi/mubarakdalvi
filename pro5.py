import math
AB = int(input())
BC = int(input())
AB_BC_rad = math.atan2(AB,BC)
AB_BC_deg = round(math.degrees(AB_BC_rad))
print(f"{int(AB_BC_deg)}" + "\N{DEGREE SIGN}")

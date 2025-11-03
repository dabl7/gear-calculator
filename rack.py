#gear rack calculator calculator 2025 Oct 31 (by @dabl2928 on youtube)
import math

m=float(input("Teeth size (module): "))

pi = math.pi

def calculate(m):
    clone_distance=m*pi

    tooth_height=2.2*m
    tooth_arc_length=1.1*m
    slope_length=tooth_height/math.cos(12*pi/180)

    AIS0=round(tooth_height-2,2)
    AIS1=round(tooth_arc_length/2-1,2)
    AIS2=round((slope_length-tooth_height),2)

    p_x = 2+2*AIS1 #perpindicular x
    p_y = 2+AIS0
    a_x = p_x        #angled x
    a_y = p_y+AIS2   

    #########################################
    print("\n\n========RACK-INFO========")
    print(f"Module (teeth size): {m}\n")
    print(f"Tooth height: {tooth_height:.2f} (amount in scale: {AIS0})")
    print(f"Tooth length: {tooth_arc_length:.2f} (amount in scale: {AIS1})")
    print("Angle: 12 (use mirror)")
    print(f"Slope length: {slope_length:.2f} (amount in scale: {AIS2})\n")
    print(f"Clone distance: {clone_distance:.2f}")
    print("\n==========CHECK-DIMENSIONS==========")
    print(f"Perpendicular piece: {p_x:.2f} x {p_y:.2f}")
    print(f"Angled pieces: {a_x:.2f} x {a_y:.2f}")

if m==0 or m<0:
    print(f"ERROR: Invalid module (can't be negative or zero) (module: {m})")
    exit()
else:
    calculate(m)

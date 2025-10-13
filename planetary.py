#planetary gear set calculator 2025 Oct 13 (by @dabl2928 on youtube)
s=int(input("Sun gear teeth: "))
r=int(input("Ring gear teeth: "))
n_p=int(input("Number of planet gears: "))

if s<r and round(s/n_p)-s/n_p==0 and round(r/n_p)-r/n_p==0:
    valid=1
else:
    valid=0

if valid==1:
    print('\nINFO: valid planetary gear set\n')
else:
    print("\nWARNING: planetary gear set cannot mesh (calculating ratios anyway)\n")

R=(-r)/s

f_c=(1/R) #carrier fixed
print("Carrier fixed:")
print(" -Sun as input (outputs with ring): "+str(1/f_c)+" torque multiplication (reversed)")
print(" -Ring as input (outputs with sun): "+str(f_c)+" torque multiplication (reversed)")

f_s=(R-1)/R #sun fixed
print("\nSun fixed:")
print(" -Carrier as input (outputs with ring): "+str(1/f_s)+" torque multiplication")
print(" -Ring as input (outputs with carrier): "+str(f_s)+" torque multiplication")

f_r=(-1)*(R-1) #ring gear fixed
print("\nRing fixed:")
print(" -Sun as input (outputs with carrier): "+str(f_r)+" torque multiplication")
print(" -Carrier as input (outputs with sun): "+str(1/f_r)+" torque multiplication")

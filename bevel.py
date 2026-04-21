import math

#started 2026 Apr 16 (@dabl2928)
#finished 2026 Apr 20 (@dabl2928)

pi=math.pi

r1=float(input("Radius1 [studs]: "))
r2=float(input("Radius2 [studs]: "))
m=float(input("Module: "))
k=float(input("Height percentage [0 to 25]: "))/100 #100% would be a full cone
a=float(input("Angle between the shafts [0 to 180 deg]: "))

ratio=r1/r2

dp1=r1*2 #planning cone diameter
dp2=r2*2
hp1=(r2-math.cos((180-a)*pi/180)*r1)/(math.cos((90-a)*pi/180)) #planning cone height
hp2=(r1-math.cos((180-a)*pi/180)*r2)/(math.cos((90-a)*pi/180))
hyp=math.hypot(r1,hp1) #planning cone hypotenuse, same for both
angle1=math.atan(hp1/r1)*180/pi #planning cone angle (at the thin edge, not the apex)
angle2=math.atan(hp2/r2)*180/pi

dangle=math.atan((1.2*m)/(math.hypot(hp1,r1)))*180/pi #dedendum angle, same for both
aangle=math.atan((1*m))/(math.hypot(hp1,r1))*180/pi #addendum angle, same for both

n1=round(dp1/m) #number of teeth
n2=round(dp2/m)
deg1=round(360/n1,2) #degrees for rotating
deg2=round(360/n2,2)

valid=(r1>0.05)and(r2>0.05)and(a>0)and(a<180)and(k>0)and(k<=25)and(m>0)and(hp1>0.05)and(hp2>0.05)and(dp1%m<0.1)and(dp2%m<0.1)and(n1>=6)and(n2>=6)
if valid:
    print("VALID")
else:
    print("INVALID")

hb1=round(m*n2/8,2) #base height, equal to how much you have to move back hinges
hb2=round(m*n1/8,2)

da1=dp1-2*math.sin((angle1)*pi/180)*(1.2*m) #widest physical part (where teeth start)
da2=dp2-2*math.sin((angle2)*pi/180)*(1.2*m)
dtop1=da1*(1-k) #top diameter (after only trimming)
dtop2=da2*(1-k)
daa1=round(da1*(1-k)/2,2)*2 #top diameter (after trimming)
daa2=round(da2*(1-k)/2,2)*2
ha1=hp1*k-math.cos(angle1*pi/180)*1.2*m*(1-k) #height of it (not actually needed for the angled part)
ha2=hp2*k-math.cos(angle2*pi/180)*1.2*m*(1-k) #perpindicular line calculated height
la1=round(hyp*k/math.cos(dangle*pi/180),2) #part length (root hypotenuse)
la2=round(hyp*k/math.cos(dangle*pi/180),2)
ta1=round(m*2,2) #fix this, very inaccurate now
ta2=round(m*2,2) 
ca1=round(daa1*math.tan(math.pi/n1)/2,2)*2 #circle piece angled piece
ca2=round(daa2*math.tan(math.pi/n2)/2,2)*2
a1=[la1,ta1,ca1] #dimensions table for angled part
a2=[la2,ta2,ca2] #hyp, thickness, circle piece

ht1=round(hp1*k-math.sin((a-angle1)*pi/180)*1.2*m*(1-k)+hb1,2) #height of the upper cylinder
ht2=round(hp2*k-math.sin((a-angle2)*pi/180)*1.2*m*(1-k)+hb2,2)
ct1=round(daa1*math.tan(math.pi/n1)/2,2)*2 #circle piece of the upper cylinder
ct2=round(daa2*math.tan(math.pi/n2)/2,2)*2
u1=[daa1,ht1,ct1] #dimensions table for upper part
u2=[daa2,ht2,ct2] #d, height, circle piece

di1=dp1/math.cos(angle1*pi/180) #imaginary diameter
di2=dp1/math.cos(angle2*pi/180)
ni1=round(di1/m) #imaginary number of teeth
ni2=round(di2/m)
if 4<=ni1<=5: #these are the top of the tooth values at the end of the involute curve (taken from pressure angle 12)
    g1=0.6
elif 6<=ni1<=7:
    g1=0.7
elif 8<=ni1<=12:
    g1=0.8
elif 13<=ni1<=22:
    g1=0.9
elif 23<=ni1<=57:
    g1=1
else:
    g1=1.1
if 4<=ni2<=5:
    g2=0.6
elif 6<=ni2<=7:
    g2=0.7
elif 8<=ni2<=12:
    g2=0.8
elif 13<=ni2<=22:
    g2=0.9
elif 23<=ni2<=57:
    g2=1
else:
    g2=1.1
tarc1=round(m*g1*(1-k)/2,2)*2 #tooth arc length
tarc2=round(m*g2*(1-k)/2,2)*2
corr1=1 #correction factor? (takes into account the longer diagonal on the n-gon from opposite gear)
corr2=1
th1=round(2.2*m,2)*corr1 #tooth height
th2=round(2.2*m,2)*corr2
t1=[la1,th,tarc1] #dimensions table for tooth part
t2=[la2,th,tarc2]

v1=hyp/math.cos(dangle*pi/180)*k*math.sin((angle1+dangle)*pi/180)
v2=hyp/math.cos(dangle*pi/180)*k*math.sin((angle2+dangle)*pi/180)
h1=(da1-dtop1)/2
h2=(da2-dtop2)/2
tilt1=math.atan(v1/h1)*180/pi
tilt2=math.atan(v2/h2)*180/pi
align1=math.atan(t1[1]*k/a1[0])*180/pi #almost impossible that its wrong
align1=math.atan(t2[1]*k/a2[0])*180/pi

out="\n\n========BEVEL-GEAR-PAIR========\n"
out+=f"Height percentage: {k:.2f}\n"
out+=f"Module: {m:.2f}\n"
out+=f"Gear ratio: {ratio:.2f} or {1/ratio:.2f}\n\n"

out+=f"====FIRST-GEAR====\n"
out+=f"1. Number of teeth: {n1:.0f}\n"
out+=f"1. Planning diameter: {dp1:.2f}\n\n"

out+=f"1. Move back hinge/wheel for {hb1:.2f}\n"
out+=f"1. Top diameter: {u1[0]:.2f} (amount in scale: {u1[0]/2-1:.2f}, both sides)\n"
out+=f"1. Top thickness: {u1[1]:.2f} (amount in scale: {u1[1]-2:.2f})\n"
out+=f"1. Top circle piece: {u1[2]:.2f} (amount in scale: {u1[2]/2-1:.2f}, both sides)\n\n"

out+=f"1. Slope angle: {tilt1:.2f}\n"
out+=f"1. Slope length: {a1[0]:.2f} (amount in scale: {a1[0]-u1[0]:.2f})\n" #quadrouple mirror for corners
out+=f"1. Slope depth: {a1[1]:.2f} (amount in scale: {a1[1]-u1[1]:.2f})\n\n"

out+=f"1. Mirror slope 2x and angle {align1:.2f} on outer corner\n"
out+=f"1. Tooth height: {t1[1]:.2f} (amount in scale: {t1[1]-a1[1]:.2f})\n"
out+=f"1. Tooth width: {t1[2]:.2f} (amount in scale: {(t1[2]-a1[2])/2:.2f}, both sides)\n\n"

out+=f"1. Degrees for rotating and cloning: {deg1:.2f}\n\n"

out+="==========FIRST-GEAR-CHECK-DIMENSIONS==========\n"
out+=f"├─Top part: {u1[0]:.2f} x {u1[1]:.2f} x {u1[2]:.2f}\n"
out+=f"├─Angled part: {a1[0]:.2f} x {a1[1]:.2f} x {a1[2]:.2f}\n" #make a1[2] = u1[2] because its the same (once got 2.18 and 2.2 for some reason)
out+=f"└─Tooth part: {t1[0]:.2f} x {t1[1]:.2f} x {t1[2]:.2f}\n\n\n"


out+=f"====SECOND-GEAR====\n"
out+=f"2. Number of teeth: {n2:.0f}\n"
out+=f"2. Planning diameter: {dp2:.2f}\n\n"

out+=f"2. Move back hinge/wheel for {hb2:.2f}\n"
out+=f"2. Top diameter: {u2[0]:.2f} (amount in scale: {u2[0]/2-1:.2f}, both sides)\n"
out+=f"2. Top thickness: {u2[1]:.2f} (amount in scale: {u2[1]-2:.2f})\n"
out+=f"2. Top circle piece: {u2[2]:.2f} (amount in scale: {u2[2]/2-1:.2f}, both sides)\n\n"

out+=f"2. Slope angle: {tilt2:.2f}\n"
out+=f"2. Slope length: {a2[0]:.2f} (amount in scale: {a2[0]-u2[0]:.2f})\n" #quadrouple mirror for corners
out+=f"2. Slope depth: {a2[1]:.2f} (amount in scale: {a2[1]-u2[1]:.2f})\n\n"

out+=f"2. Mirror slope 2x and angle {align1:.2f} on outer corner\n"
out+=f"2. Tooth height: {t2[1]:.2f} (amount in scale: {t2[1]-a2[1]:.2f})\n"
out+=f"2. Tooth width: {t2[2]:.2f} (amount in scale: {(t2[2]-a2[2])/2:.2f}, both sides)\n\n"

out+=f"2. Degrees for rotating and cloning: {deg2:.2f}\n\n"

out+="==========SECOND-GEAR-CHECK-DIMENSIONS==========\n"
out+=f"├─Top part: {u2[0]:.2f} x {u2[1]:.2f} x {u2[2]:.2f}\n"
out+=f"├─Angled part: {a2[0]:.2f} x {a2[1]:.2f} x {a2[2]:.2f}\n"
out+=f"└─Tooth part: {t2[0]:.2f} x {t2[1]:.2f} x {t2[2]:.2f}\n"

print(locals())
print(out)
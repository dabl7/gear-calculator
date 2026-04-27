import math

#started 2026 Apr 16 (@dabl2928)
#finished 2026 Apr 20 (@dabl2928)
#updated 2026 Apr 27 (@dabl2928)

r1=float(input("Radius1 [studs]: "))
r2=float(input("Radius2 [studs]: "))
m=float(input("Module: "))
k=float(input("Height percentage [0 to 35]: "))/100 #100% would be a full cone
a=float(input("Angle between the shafts [0 to 180 deg]: "))

def ASCIIbevel():
    a='\n'
    a+='                                                                     :.\n'
    a+='                                                                  ~+oo~\n'
    a+='                                                                :+o+++.\n'
    a+='                                                             .:++++++o~\n'
    a+='                                                           .:++++ooooo~\n'
    a+='                                                        ~+++oooooo++++~...\n'
    a+='                                                        +o+++++++++++oo+o+\n'
    a+='                                                        +++o+ooooooooo++++\n'
    a+='                                                        :+++++++++++++++++\n'
    a+='                                                        ++++oooooooo+o++++\n'
    a+='                                                        +++++++++oooooo+++\n'
    a+='                                                        :ooooo+++++++++:+:\n'
    a+='              ~+++++:::+++~:++::++::++~+++:~+++::+++++:   ~:+++ooooooo.\n'
    a+='            :ooooo+++ooo++oooo:ooo++oo++ooo+++ooo+++oooo+.   :+++++ooo~\n'
    a+='         .:ooo++++oooo::+oooo:+ooo:+ooo:+oooo+:+ooo++++ooo+:   :++++:+.\n'
    a+='       ~+ooo++++oooo+:+ooooo+:oooo++oooo:oooooo+++oooo++++ooo+   ~+oo+.\n'
    a+='     :ooo+++oooooo+:+ooooooo:ooooo:+oooo++oooooo+:+oooooo++++oo+~   :o~\n'
    a+='  .+oo++++ooooooo:+oooooooo++ooooo:+ooooo:+ooooooo+:+ooooooo++++oo:\n'
    a+='~+oo+++oooooooo+:+oooooooo+:oooooo:+ooooo+:ooooooooo+:+oooooooo+++oo+\n'
    a+='                    ~o++++++o++o+++++o+++++++++++\n'
    a+='                     +::::+::::::::+:::+:+:+:+:+:\n'
    print(a)

def bevel(r1,r2,m,k,a):
    ASCIIbevel()

    ratio=r1/r2

    pi=math.pi

    dp1=r1*2 #planning cone diameter
    dp2=r2*2
    hp1=(r2-math.cos((180-a)*pi/180)*r1)/(math.cos((90-a)*pi/180)) #planning cone height (the entire bevel calculator depends on this)
    hp2=(r1-math.cos((180-a)*pi/180)*r2)/(math.cos((90-a)*pi/180))
    hyp=math.hypot(r1,hp1) #planning cone hypotenuse, same for both
    angle1=math.atan(hp1/r1)*180/pi #planning cone angle (at the thin edge, not the apex)
    angle2=math.atan(hp2/r2)*180/pi

    dangle=math.atan((1.2*m)/(math.hypot(hp1,r1)))*180/pi 

    
    n1=round(dp1/m,2) #number of teeth
    n2=round(dp2/m,2)
    if n1==0 or n2==0:
        print(f"ERROR: Module too small")
        exit()

    deg1=round(360/n1,2) #degrees for rotating
    deg2=round(360/n2,2)
    odd1=n1%2 #True if odd
    odd2=n2%2

    hb1=round(m*n2/8,2) #base height, equal to how much you have to move back hinges
    hb2=round(m*n1/8,2)

    da1=dp1-2*math.sin((angle1)*pi/180)*(1.2*m) #widest physical part (where teeth start)
    da2=dp2-2*math.sin((angle2)*pi/180)*(1.2*m)
    dtop1=da1*(1-k) #top diameter (after only trimming)
    dtop2=da2*(1-k)
    daa1=round(da1*(1-k)/2,2)*2 #top diameter (after trimming)
    daa2=round(da2*(1-k)/2,2)*2
    la1=round(hyp*k/math.cos(dangle*pi/180),2) #part length (root hypotenuse)
    la2=round(hyp*k/math.cos(dangle*pi/180),2)
    ta1=round(1.5*m,2) #could be improved, kind of guessed now
    ta2=round(1.5*m,2)
    ca1=round(daa1*math.tan(pi/n1)/2,2)*2 #circle piece angled piece
    ca2=round(daa2*math.tan(pi/n2)/2,2)*2

    ht1=round(hp1*k-math.sin((a-angle1)*pi/180)*1.2*m*(1-k)+hb1,2) #height of the upper cylinder
    ht2=round(hp2*k-math.sin((a-angle2)*pi/180)*1.2*m*(1-k)+hb2,2)
    ct1=round(daa1*math.tan(pi/n1)/2,2)*2 #circle piece of the upper cylinder
    ct2=round(daa2*math.tan(pi/n2)/2,2)*2

    di1=dp1/math.cos(deg1*pi/180) #imaginary diameter
    di2=dp1/math.cos(deg2*pi/180)
    ni1=round(di1/m) #imaginary number of teeth
    ni2=round(di2/m)

    if ni1<=5:
        g1=0.6 #these are the top of the tooth values at the end of the involute curve (taken from pressure angle 12)
    elif ni1<=7:
        g1=0.7
    elif ni1<=12:
        g1=0.8
    elif ni1<=22:
        g1=0.9
    elif ni1<=57:
        g1=1
    else:
        g1=1.1
        
    if ni2<=5:
        g2=0.6
    elif ni2<=7:
        g2=0.7
    elif ni2<=12:
        g2=0.8
    elif ni2<=22:
        g2=0.9
    elif ni2<=57:
        g2=1
    else:
        g2=1.1
        
    tarc1=round(m*g1*(1-k)/2,2)*2 #tooth arc length
    tarc2=round(m*g2*(1-k)/2,2)*2
    corr1=math.hypot(daa2/2,ct2/2)-dtop2/2
    corr2=math.hypot(daa1/2,ct1/2)-dtop1/2 #correction value (takes into account the longer diagonal on the n-gon from other gear)
    th=2.2*m
    th1=round(2.2*m-corr1,2) #corrected tooth height
    th2=round(2.2*m-corr2,2)
        
    v1=hyp/math.cos(dangle*pi/180)*k*math.sin((angle1+dangle)*pi/180)
    v2=hyp/math.cos(dangle*pi/180)*k*math.sin((angle2+dangle)*pi/180)
    h1=(da1-dtop1)/2
    h2=(da2-dtop2)/2
    tilt1=math.atan(v1/h1)*180/pi
    tilt2=math.atan(v2/h2)*180/pi
    align=math.atan(th*k/la1)*180/pi #how much to angle teeth so that it meets at the same point
        
    u1=[daa1,ht1,ct1] #dimensions table for upper part
    u2=[daa2,ht2,ct2] #d, height, circle piece
        
    a1=[la1,ta1,ca1] #dimensions table for angled part
    a2=[la2,ta2,ca2] #hyp, thickness, circle piece
        
    t1=[la1,th1,tarc1] #dimensions table for tooth part
    t2=[la2,th2,tarc2] #hyp, height, arc length

    valid=(r1>0.05) and (r2>0.05) and (a>0) and (a<180) and (k>0) and (k<=0.35) and (m>0) and (hp1>0.05) and (hp2>0.05) and (dp1%m<0.1) and (dp2%m<0.1) and (n1>=6) and (n2>=6) and (odd1==False) and (odd2==False) and (u1[0]>=0.05) and (u1[1]>=0.05) and (u1[2]>=0.05) and (u2[0]>=0.05) and (u2[1]>=0.05) and (u2[2]>=0.05) and (a1[0]>=0.05) and (a1[1]>=0.05) and (a1[2]>=0.05) and (a2[0]>=0.05) and (a2[1]>=0.05) and (a2[2]>=0.05) and (t1[0]>=0.05) and (t1[1]>=0.05) and (t1[2]>=0.05) and (t2[0]>=0.05) and (t2[1]>=0.05) and (t2[2]>=0.05)
    
    if valid:
        upart1=math.ceil(u1[0]*u1[1]*u1[2]/8)
        if upart1<1:
            upart1=1
        upart2=math.ceil(u2[0]*u2[1]*u2[2]/8)
        if upart2<1:
            upart2=1
        
        apart1=math.ceil(a1[0]*a1[1]*a1[2]/8)
        if apart1<1:
            apart1=1
        apart2=math.ceil(a2[0]*a2[1]*a2[2]/8)
        if apart2<1:
            apart2=1
        
        tpart1=math.ceil(t1[0]*t1[1]*t1[2]/8)
        if tpart1<1:
            tpart1=1
        tpart2=math.ceil(t2[0]*t2[1]*t2[2]/8)
        if tpart2<1:
            tpart2=1
        
        slice1=upart1+apart1*2+tpart1*2 #how many blocks one "slice" has (before cloning and rotating)
        slice2=upart2+apart2*2+tpart2*2
        ab1=n1*slice1/2 #number of blocks
        ab2=n2*slice2/2
            
        out=f"=============================BEVEL-PAIR-INFO==============================\n"
        out+=f"Module: {round(m,2)}\n"
        out+=f"First gear: {round(ab1)} blocks ({n1} teeth)\n"
        out+=f"Second gear: {round(ab2)} blocks ({n2} teeth)\n"
        out+=f"Height percentage: {round(k,2)} ({round(k*100,2)}%)\n"
        out+=f"Gear ratio: {round(ratio,2)} or {round(1/ratio,2)}\n"
        out+=f"Teeth: {n1} to {n2}\n\n\n"
        
        out+=f"================================FIRST-GEAR================================\n"
        out+=f" 1. Number of teeth: {round(n1)}\n"
        out+=f" 1. Planning diameter: {round(dp1,2)}\n\n"
        
        out+=f" 1. Move hinge/wheel back for {round(hb1,2)}\n"
        out+=f" 1. Top diameter: {round(u1[0],2)} (amount in scale: {round(u1[0]/2-1,2)}, both sides)\n"
        out+=f" 1. Top thickness: {round(u1[1],2)} (amount in scale: {round(u1[1]-2,2)})\n"
        out+=f" 1. Top circle piece: {round(u1[2],2)} (amount in scale: {round(u1[2]/2-1,2)}, both sides)\n\n"
            
        out+=f" 1. Mirror 2x and angle {round(tilt1,2)} degrees on corner\n"
        out+=f" 1. Slope length: {round(a1[0],2)} (amount in scale: {round(a1[0]-u1[0],2)})\n" #or 4x mirror
        out+=f" 1. Slope depth: {round(a1[1],2)} (amount in scale: {round(a1[1]-u1[1],2)})\n\n"
        
        out+=f" 1. Mirror slope 2x and angle {round(align,2)} degrees on outer corner\n"
        out+=f" 1. Tooth height: {round(t1[1],2)} (amount in scale: {round(t1[1]-a1[1],2)})\n"
        out+=f" 1. Tooth width: {round(t1[2],2)} (amount in scale: {round((t1[2]-a1[2])/2,2)}, both sides)\n\n"
        
        out+=f" 1. Degrees for rotating and cloning: {round(deg1,2)}\n\n"
        
        out+=f"===FIRST-GEAR-DIMENSIONS===\n"
        out+=f"1. Top part: {round(u1[0],2)} x {round(u1[1],2)} x {round(u1[2],2)}\n"
        out+=f"1. Angled part: {round(a1[0],2)} x {round(a1[1],2)} x {round(a1[2],2)}\n"
        out+=f"1. Tooth part: {round(t1[0],2)} x {round(t1[1],2)} x {round(t1[2],2)}\n\n\n"
        out+=f"================================SECOND-GEAR================================\n"
        out+=f" 2. Number of teeth: {round(n2)}\n"
        out+=f" 2. Planning diameter: {round(dp2,2)}\n\n"
        
        out+=f" 2. Move hinge/wheel back for {round(hb2,2)}\n"
        out+=f" 2. Top diameter: {round(u2[0],2)} (amount in scale: {round(u2[0]/2-1,2)}, both sides)\n"
        out+=f" 2. Top thickness: {round(u2[1],2)} (amount in scale: {round(u2[1]-2,2)})\n"
        out+=f" 2. Top circle piece: {round(u2[2],2)} (amount in scale: {round(u2[2]/2-1,2)}, both sides)\n\n"
        
        out+=f" 2. Mirror 2x and angle {round(tilt2,2)} degrees on corner\n"
        out+=f" 2. Slope length: {round(a2[0],2)} (amount in scale: {round(a2[0]-u2[0],2)})\n" #or 4x mirror
        out+=f" 2. Slope depth: {round(a2[1],2)} (amount in scale: {round(a2[1]-u2[1],2)})\n\n"
        
        out+=f" 2. Mirror slope 2x and angle {round(align,2)} degrees on outer corner\n"
        out+=f" 2. Tooth height: {round(t2[1],2)} (amount in scale: {round(t2[1]-a2[1],2)})\n"
        out+=f" 2. Tooth width: {round(t2[2],2)} (amount in scale: {round((t2[2]-a2[2])/2,2)}, both sides)\n\n"
        
        out+=f" 2. Degrees for rotating and cloning: {round(deg2,2)}\n\n"
        
        out+=f"===SECOND-GEAR-DIMENSIONS===\n"
        out+=f"2. Top part: {round(u2[0],2)} x {round(u2[1],2)} x {round(u2[2],2)}\n"
        out+=f"2. Angled part: {round(a2[0],2)} x {round(a2[1],2)} x {round(a2[2],2)}\n"
        out+=f"2. Tooth part: {round(t2[0],2)} x {round(t2[1],2)} x {round(t2[2],2)}\n\n\n"
    else:
        if a<=0 or a>=180:
            out=f"ERROR: Incorrect shaft angle ({a})"
        elif dp1%m>=0.1 or dp2%m>=0.1 or m<=0 or n1<6 or n2<6:
            out=f"ERROR: Incorrect module (not a full number or less than 6 teeth: {round(dp1/m,2)} and {round(dp2/m,2)} teeth)\n\n"
            out+=f"List of modules that would work (choose any):\n"
            for n in range(6,500,2):
                mn=min(dp1,dp2)/n #checks situations all the way to 500 teeth to find suitable modules
    
                tn1=round(dp1/mn) #number of teeth
                tn2=round(dp2/mn)
    
                todd1=tn1%2 #true if odd
                todd2=tn2%2
    
                thick=round(mn*1.1*(1-k)/2,2)*2
                thick>=0.06 #tooth thickness has to be atleast 0.06
    
                nicenumber=(round(mn,4)==mn) #nice number means it has 4 decimal places max
    
                if not todd1 and not todd2 and dp1%mn<0.1 and dp2%mn<0.1 and thick and nicenumber: #only if not odd, less than 0.1 when diameter/module, tooth thick enough, 2 decimals
                    out+=f" -module: {mn}\n"
        elif hp1<0 or hp2<0:
            out=f"ERROR: Not possible to make, cone's height goes negative, reduce shaft angle or change radii\n(calculated: ${round(hp1)}, ${round(hp2)})"
        elif r1<0.05:
            out=f"ERROR: Invalid radius1 (smaller than 0.05: ${r1})"
        elif r2<0.05:
            out=f"ERROR: Invalid radius2 (smaller than 0.05: ${r2})"
        elif k<=0 or k>0.35:
            out=f"ERROR: Invalid height percentage"
        elif odd1 or odd2:
            out=f"ERROR: Odd number of teeth on first gear\n"
            out+=f"(not supported, because i think its almost useless since you can\n"
            out+=f"just halve the module and get double the teeth with the same ratio)\n\n"
            out+=f"Module ${m/2} will work (teeth will double)"
        elif u1[0]<0.05 or u1[1]<0.05 or u1[2]<0.05 or u2[0]<0.05 or u2[1]<0.05 or u2[2]<0.05 or a1[0]<0.05 or a1[1]<0.05 or a1[2]<0.05 or a2[0]<0.05 or a2[1]<0.05 or a2[2]<0.05 or t1[0]<0.05 or t1[1]<0.05 or t1[2]<0.05 or t2[0]<0.05 or t2[1]<0.05 or t2[2]<0.05:
            out=f"ERROR: one of the parts' dimensions' get smaller than 0.05 (impossible to make)\n"
            out+=f" increasing the module or height percentage or diameter will fix this"
        else:
            out=f"ERROR: Unknown (comment which values you used and I will fix it)"
    print(out)

bevel(r1,r2,m,k,a)

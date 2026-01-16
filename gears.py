#combined gear calculator 2026 Jan 16 (by @dabl2928 on youtube)
import math

mode=input("Gear type: (basic/worm/rack/planetary): ").lower()

def basic(t,d,m,o):
    n_teeth = d/m

    if t.lower() == "external":
        inner_d = d-2.4*m
        outer_d = d+2*m
        circle_piece = round(inner_d*math.tan(math.pi/n_teeth),2)
    else:           #INTERNAL
        thickness = float(input("Outside thickness (studs): "))
        inner_d = d+2.4*m
        outer_d = d+2.4*m+2*thickness
        circle_piece = round(outer_d*math.tan(math.pi/n_teeth),2)

    if t.lower() == "external": #ASCII
        ASCIIexternal()
    else:
        ASCIIinternal()

    if t.lower()=="internal":
        correction_factor = 0.6 #IMPROVES SMOOTHNESS (smaller tooth height)
        tooth_height = round(correction_factor*2.2*m,2)
    else:
        tooth_height = round(2.2*m,2)

    if 4 <= n_teeth <= 5:
        g = 0.6
    elif 6 <= n_teeth <= 7:
        g = 0.7
    elif 8 <= n_teeth <= 12:
        g = 0.8
    elif 13 <= n_teeth <= 22:
        g = 0.9
    elif 23 <= n_teeth <= 57:
        g= 1
    else:
        g = 1.1

    tooth_arc_length = round(m*g,2)
    deg = round(360/n_teeth,2)

    if t.lower()=="internal":
        AIS0 = round(inner_d/2+1,2)
    else:
        AIS0 = round(inner_d/2-1,2)

    AIS1 = round((circle_piece-2)/2,2)
    AIS2 = round((tooth_arc_length-2)/2,2)
    AIS3 = round(tooth_height-2,2)

    ##############################################
    print("\n\n========GEAR-INFO========")
    print("Type: "+str(t))
    print("Number of teeth: "+str(round(n_teeth)))
    print("Module (teeth size): "+str(m)+"\n")

    if odd==True:
        if t.lower()=="internal":
            print("Inner radius: "+str(round(inner_d/2,2))+" studs  (move for: "+str(AIS0)+")")
            print("Outer diameter: "+str(outer_d)+" studs  ")
            print("Thickness: "+str(thickness)+" studs  (amount in scale: "+str(round(thickness-2,2))+")")
        else:
            print("Inner radius: "+str(round(inner_d/2),2)+" studs  (amount in scale: "+str(AIS0)+")")

    else: #EVEN
        if t.lower()=="internal":
            print("Inner diameter: "+str(inner_d)+" studs  (move for: "+str(AIS0)+" on both sides)")
            print("Outer diameter: "+str(outer_d)+" studs")
            print("Thickness: "+str(thickness)+" studs  (amount in scale: "+str(round(thickness-2,2))+")")
        else:
            print("Inner diameter: "+str(inner_d)+" studs  (amount in scale: "+str(AIS0)+" for both sides)")

    print("Circle piece: "+str(circle_piece)+" studs  (amount in scale: "+str(AIS1)+")")
    print("Tooth length: "+str(tooth_arc_length)+" studs  (amount in scale: "+str(AIS2)+")")
    print("Tooth height: "+str(tooth_height)+" studs  (amount in scale: "+str(AIS3)+")")

    print("\nDegrees for rotating and cloning: "+str(deg))

    print("\n==========CHECK-DIMENSIONS==========\nTooth part dimensions: "+str(round(2+2*AIS2,2))+" x "+str(tooth_height))
    if odd==True:
        if t.lower()=="internal": #ODD
            print("Other part dimensions: "+str(round(2+2*AIS1,2))+" x "+str(thickness))
        else:          #EXTERNAL  ODD
            print("Other part dimensions: "+str(round(2+2*AIS1,2))+" x "+str(inner_d/2))
    else:                                  
        if t.lower()=="internal": #EVEN  
            print("Other part dimensions: "+str(round(2+2*AIS1,2))+" x "+str(thickness))
        else:          #EXTERNAL   EVEN
            print("Other part dimensions: "+str(round(2+2*AIS1,2))+" x "+str(inner_d))

    if odd==True:print("\nWARNING: gear has an odd number of teeth (add another large part for cloning and rotating)")

def worm(d,m,q):
    ASCIIworm()

    n = 360/q #number of circle sides

    inner_d = round(d-2.4*m,2)
    AIS_1 = round(inner_d/2-1,2) #inner diameter
    outer_d = round(d+2*m,2)

    circle_piece = round(inner_d*math.tan(math.pi/n),2)
    AIS_0 = round(circle_piece/2-1,2) #circle piece

    pitch = round(m*math.pi,2)
    gamma = 180/math.pi*math.atan(m/inner_d)
    middle_part = round(0.5*m*math.pi,2)

    tooth_height = round(2.2*m,2)
    AIS_2 = round(tooth_height-2,2) #tooth height

    tooth_top = round(outer_d*math.tan(math.pi/n),2)
    AIS_3 = round(tooth_top/2-1,2) #circle piece but for tooth

    tooth_width = round(1.1*m,2)
    AIS_4 = round(tooth_width/2-1,2) #1.1m tooth width thing

    s_x=round(2+AIS_2,2)
    s_y=round(2+2*AIS_4,2)
    s_z=round(2+2*AIS_3,2)

    t_x=round(2+2*AIS_0,2)
    t_y=round(2+2*AIS_1,2)
    t_z=round(pitch,2)

    spiral_block = s_x*s_y*s_z/8
    stem_block = t_x*t_y*t_z/8
    
    spiral = n*spiral_block
    if spiral_block<1:
        spiral = n

    stem = n/2*stem_block
    if stem_block<1:
        stem = n/2

    blocks = math.ceil(spiral+stem)

    print("\n========WORM GEAR INFO:========")
    print(f"Module: {m}\n")
    print(f"Circle piece: {circle_piece} (amount in scale: {AIS_0} for both sides)")
    print(f"Inner diameter: {inner_d} (amount in scale: {AIS_1} for both sides)\n")
    print(f"Helical angle: {gamma:.2f}")
    print(f"Tooth height: {tooth_height} (amount in scale: {AIS_2})")
    print(f"Tooth top length: {tooth_top} (amount in scale: {AIS_3} for both sides)")
    print(f"Tooth width: {tooth_width} (amount in scale: {AIS_4} for both sides)")
    print(f"\nCloning table:")
    print(f"-180 degrees: {pitch/2:.2f} once")
    print(f"-90 degree: {pitch/4:.2f} once") 
    print(f"-45 degree: {pitch/8:.2f} once")
    print(f"-15 degree: {pitch/24:.2f} three times")
    if q==5:
        print(f"-5 degree: {pitch/72:.2f} three times")
    print(f"\nFull pitch: {pitch}  ({blocks:.0f} blocks per pitch/loop)")
    print(f"\n==========CHECK-DIMENSIONS==========")
    print(f"Center part: {t_x} x {t_y}")
    print(f"Spiral part: {s_x} x {s_y} x {s_z}")

def rack(m):
    ASCIIrack()

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

def planetary(s,r,n_p):
    ASCIIplanetary()

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



def ASCIIexternal():
    a='\n'
    a+='                 ..     .+=+~      .\n'
    a+='               ~oo=.     ooo.     +==:\n'
    a+='                :=o+~~~::==o+:~~~+==+\n'
    a+='       .+o:~   .:==oooo==ooooooooo==:~   .:=+~\n'
    a+='       .:=o=+:=oo==oo====oooo=o==oooo==:+oo=:.\n'
    a+='          :oooo=ooooooooooooooooooooo=ooo=+\n'
    a+='   :~..  :ooo=ooooooooooooooooooooooooo==o=+.  .~:.\n'
    a+='  ~==oo+=ooooooooooooooooooooooooooooooooooo=+oooo:\n'
    a+='    .~:oo=ooooooooooooooooooooooooooooooooo=oo:~.\n'
    a+='      :o=ooooooooooooooooooooooooooooooooooo==+\n'
    a+='.~~~~~=oooooooooooooooooooooooooooooooooooooooo:~~~~.\n'
    a+='.oooooooooooooooooooooooooooooooooooooooooooooo==ooo~\n'
    a+='      =ooooooooooooooooooooooooooooooooooooooo=.\n'
    a+='      ~ooooooooooooooooooooooooooooooooooooo==:\n'
    a+='  .~::=oo==oooooooooooooooooooooooooooooooo==o=+:~.\n'
    a+='  ~===+::o=ooooooooooooooooooooooooooooooooo+~++oo:\n'
    a+='   .     ~+o===oooooooooooooooooooooooo====~     .\n'
    a+='         .+ooooooooooo=ooooooooo=oooooooo=+~\n'
    a+='       ~=oo+~.:+=oo=ooooooooooooooooo=:~~+=o=~\n'
    a+='        ~:~     ~==o===ooooooo==+o==~     ~:~.\n'
    a+='               .=oo:  ..~==o~..  :oo=~\n'
    a+='               ~:+:      ooo~     :+:~\n'
    a+='                         ~::\n'
    print(a)

def ASCIIinternal():
    a='\n'
    a+='                  ~~~::::::::~~~.\n'
    a+='            ~~:+=oooooooo===ooooo=++~~\n'
    a+='        .~+=ooooo=+~~..~oo: ..~:ooooooo+~.\n'
    a+='      ~:ooo=:~~ :oo.   .++~   .=o+ .~:=ooo+~\n'
    a+='    ~+ooo=o=~    ~~.          .~~    .+ooooo=~\n'
    a+='   :ooo+~.~=o~                      ~==:..+oo=+.\n'
    a+=' .+ooo+                                    :o=o=.\n'
    a+=' +ooo==o=:                              ~======o=.\n'
    a+=':ooo:  .~                                ~~  :ooo:\n'
    a+='=ooo~                                        .oooo.\n'
    a+='oooo====~                                .====oooo.\n'
    a+='=ooo~..                                    ...oooo.\n'
    a+=':ooo:   ~                                ~.  :ooo+\n'
    a+=' =ooo+===:                              ~oo=+ooo=.\n'
    a+=' .=ooo+.                                   :ooo=~\n'
    a+='  .+oo=+. ~+o~                      ~=+~ .:=oo+.\n'
    a+='    ~=o=o=o=~    ~.            .~    ~+o=oo==:\n'
    a+='      ~+ooo=:~  :o=~   .::~   ~=o:  ~:+oo=+~.\n'
    a+='        .:+=ooo=o=+..  ~o=:  ..:oo=oo==+:~\n'
    a+='           .~:+=ooooooooo=oooooo=o=+:~.\n'
    a+='                 ~~~:::+:+::::~~~.\n'
    print(a)

def ASCIIworm():
    a='\n'
    a+=' .~~~.       ~~~.       ~~~.       ~~~~       ~~~~\n'
    a+=' ~=++:      ~=+++      .++++      .++++       ++++\n'
    a+=' ~++++.     ~++++.     .=+++~      ++++~      ++++\n'
    a+=' ~=+++~     .o+++~     .=+++:      =++++      =+++\n'
    a+='.+o++++~:~:~+o++++~:~:::o++++::~:~:o++++:~:~~:=+++\n'
    a+='~=o++++ooooooo++++ooooooo=+++=oooooo=+++=oooooo=++\n'
    a+='.=o=++++=ooooo=++++oooooo=++++ooo=ooo++++=oooooo++\n'
    a+='~=o=++++ooooooo++++=oooooo++++=oooooo++++=oooooo++\n'
    a+='~=oo++++=oooooo++++=oooooo=++++oooooo=++++oooooo=+\n'
    a+='~ooo=++++oooooo=++++ooooooo++++ooooooo++++ooooooo+\n'
    a+='.ooo=++++ooooooo++++=oooooo++++=oooooo++++=oooooo+\n'
    a+='~=ooo=+++=oooooo=+++=ooooooo++++ooooooo++++ooooooo\n'
    a+=' ~~~~~++++o:~~~~~++++o:~~~~~++++o:~~~~~++++o+~~~~~\n'
    a+='      ++++=      :+++o.     :+++=~     ~+++=~\n'
    a+='      ~++++.     ~+++=.     .++++~     .++++~\n'
    a+='      .++++       ++++.      +++=~      :++=~\n'
    a+='       ~.~~       .~.~       ..~~       .~.~.\n'
    print(a)

def ASCIIrack():
    a='\n'
    a+='    ~++:+++           ~++++++           ~++:+++.          .++++++.          .++:+++.\n'
    a+='    ooooooo~          =oooooo:          +oooooo:          +oooooo+          +oooooo+\n'
    a+='   ~ooooooo+         ~ooooo=o+         ~ooooooo=         .oooooooo          oooooooo.\n'
    a+='   +oooooooo.        +oooooooo~        +oooooooo~        :oooooooo~        ~oooooooo:\n'
    a+='  .ooooooooo:       .ooooooo==+        =oooooooo+        =oooooooo=        =oooooooo=\n'
    a+='  +ooooooooo=       :ooooooooo=       ~oooooooooo.      ~oooooooooo.      ~oooooooooo~\n'
    a+='~~ooooooooooo:~~~~~~=oooooooooo+~~~~~~=oooooooooo+~~~~~~+oooooooooo+~~~~~~+=ooooooooo+~.\n'
    a+='ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+\n'
    a+='oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo=+\n'
    a+='ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+\n'
    a+='ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo+\n'
    a+='+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++:\n'
    print(a)

def ASCIIplanetary():
    a='\n'
    a+='             .~~:++++++++:~~.\n'
    a+='         .:+==oo=oo====o===o==+:.\n'
    a+='      .:=ooo=+:..        .~~+=ooo=:.\n'
    a+='    .+ooo+~.                  .~+ooo+.\n'
    a+='   :ooo=+::~~                ~~::+=ooo:\n'
    a+='  +=oo==ooooo=. .~:++++:~. .=oooo=o=ooo:\n'
    a+=' ~o=o:~ooooooo++oooooooooo++ooooooo.+o=o~\n'
    a+=' ====. .:+++:+ooo=o=====oooo+:+++:. .==o=\n'
    a+='.=oo=        ==ooooooooooo===        =oo=\n'
    a+=' =oo=        +oo===ooooo=ooo+        oo==\n'
    a+=' :o=o:        :=oo==oooooo=:        +o==:\n'
    a+='  +o=o~         ~:+====+:~         :==o+\n'
    a+='   +ooo+.        .+====:         .+ooo+\n'
    a+='    ~=ooo+.      ooooooo=      ~+o=o=~\n'
    a+='      ~+ooo=+~.  ~+==o=+~ ..~+=ooo+~\n'
    a+='        .~+=oooo=++=oo=++=oooo=+~.\n'
    a+='            .~:++========++:~.\n'
    print(a)



if mode=="basic":
    t=input("Gear type (internal/external): ")
    d=float(input("Gear diameter (planning circle diameter in studs): "))
    m=float(input("Teeth size (module): "))

    if round(d/m)%2==1:
        odd = True
    else:
        odd = False

    if d==0:
        print("ERROR: Invalid diameter (Diameter: "+str(d)+")")
        exit()
    elif m==0:
        print("ERROR: Invalid module (Module: "+str(m)+")")
        exit()
    elif (d/m)<4:
        print("ERROR: Invalid diameter to module ratio (not enough teeth) (Number of teeth: "+str(d/m)+")")
        exit()
    elif round(d/m)!=round(d/m,5):
        print("ERROR: Invalid diameter to module ratio (number of teeth isn't a full number) (Number of teeth: "+str(d/m)+")")
        exit()
    elif t.lower()!="internal" and t.lower()!="external":
        print("ERROR: Specify if the gear is internal or external")
        exit()
    else:
        basic(t,d,m,odd)

elif mode=="worm":
    d=float(input("Worm gear diameter (in studs): "))
    m=float(input("Teeth size (module): "))
    q=float(input("Degrees for rotating (5 or 15):"))

    if d<=0:
        print(f"\nERROR: Invalid diameter ({d})")
    elif m<=0:
        print(f"\nERROR: Invalid module ({m})")
    elif q!=5 and q!=15:
        print(f"\nERROR: Invalid degrees, you can choose between 5 and 15 ({q})")
    else:
        worm(d,m,q)

elif mode=="rack":
    m=float(input("Teeth size (module): "))
    pi = math.pi

    if m==0 or m<0:
        print(f"ERROR: Invalid module (can't be negative or zero) (module: {m})")
        exit()
    else:
        rack(m)

elif mode=="planetary":
    s=int(input("Sun gear teeth: "))
    r=int(input("Ring gear teeth: "))
    n_p=int(input("Number of planet gears: "))
    planetary(s,r,n_p)

else:
    print("Choose a correct mode")

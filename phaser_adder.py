#!/usr/bin/env python


import math
import cmath
def makePhaserArray(phrStr):
       phArry = []
       for i in phrStr.split("+"):
                spt = i.split("<")
                if(len(spt)==2):
                        phArry.append(spt)
                else:
                        spt.append(0)
                        phArry.append(spt)
       return phArry
def addPhaserArray(Parray):
        allreal = 0;
        allimg  = 0;

        for ph in Parray:
                if(len(ph)==2):
                        mag = float(ph[0])
                        deg = float(ph[1])*math.pi/180

                        allreal += mag*math.cos(deg)
                        allimg += mag*math.sin(deg)
        return complex(allreal,allimg)

in1 = input(">")

f =  addPhaserArray(makePhaserArray(in1));
realS = "{:.4f}".format(f.real)
imagS = "{:.4f}".format(f.imag)

mag = "{:.4f}".format(abs(f))
phase = "{:.4f}".format(cmath.phase(f)*180/math.pi)


print(realS,"+j",imagS)
print(mag,"<",phase)

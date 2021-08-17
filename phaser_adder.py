#!/usr/bin/env python


import math   ## used for pi cos() sin()
import cmath  ## used for phase() to calculate phase from complex

##
##  this will make array of phasers from a string 
##            if for example for 12<21+32<12
##            the phase arry will be [ [12,21] , [32,0]  ]
##            and if no degree is given it will add zero 
##            sof for string 12<12+21
##            ther phase array will be [ [12,21] ,[32,0] ]
def makePhaserArray(phrStr):
       phArry = []
       for i in phrStr.split("+"): 
                spt = i.split("<")
                if(len(spt)==2): ## if the split by < has two parts
                        phArry.append(spt)
                else: ## this happes when there is zero phase .. so we add zero 
                        spt.append(0)
                        phArry.append(spt)
       return phArry
## 
## this function will add given the phase array discibed above 
## it will add the phaser representations in complex form 
##     it will return the sum in complex form 
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




## this is where we get the string input 
in1 = input(">")

## the addphaser willl retrun it in complex format 
zsum =  addPhaserArray(makePhaserArray(in1));

## we print it in complex format 
## it used string fromating to make it 4 decimal places
realS = "{:.4f}".format(zsum.real)
imagS = "{:.4f}".format(zsum.imag)
print(realS,"+j",imagS)


## we also print it in phaser format 
## it used string fromating to make it 4 decimal places 
mag = "{:.4f}".format(abs(zsum))
phase = "{:.4f}".format(cmath.phase(zsum)*180/math.pi) 
print(mag,"<",phase)

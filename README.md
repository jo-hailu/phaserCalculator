# phaserCalculator
This programm adds phaser 

 Phasers are data structures used mostly by electrical power engineers to calcuate impedences in power system.
 they are basicly complex numbers with format: if z is the complex number 
                abs(z)<phase(z)
              where abs(z) is the magnitude .. sqrt(z.real^2 + z.imag^2)
              and phase(z) is the phase .. atan(z.imag /z.real)
 where we only need the magnitude and the phase of the number to express it fully 
 thus for example of z = 3 + 4j the phaser representatoin will be 
          abs(3+4j) is sqrt(3^2 + 4^2) = 5
          phase(z) is atan(4/3) = 45 degrees 
          5<45

and we have two phaser z1 and z2
    z1 * z2
is easey to calculate which is 
    abs(z1) * abs(z2) <(phase(z)+phse(z) )
which is multiplying there magnute while adding there phase 

this easyness is the advantage of useing phaser representation of complex numbers. 
while this is advantages adding two phasers is pain. 

so I have wrote this program in python to add phaser representation of complex numbers 

# Ussage 
  type in your command 
    python phasser_adder 
    > 23<32 + 43<32
  and you will see there added 
 
 the phaser representation should be like discribed above 
 if you have negative magnitude use
    > 23<32 + -43<32
 use degrees not radiance 
 
 
# Contrbute
  
  the programm is not finished yet 
    contrbut by adding more flexibility to input 
        add features of multiplication and devision 
    
 

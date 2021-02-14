import time

#variablen

seconden = input("Sec: ")

s = int(seconden)

minuut = input("minuut:")

m = int(minuut)

uur = input("uur:")

h = int(uur)

# als s -> seconden kleiner is dan 60 loopt hij de print en doet er telkens 1 bij op 60 wordt seconden gereset en begint hij opnieuw

while (s < 60):

 print (""+str(h)+""+":"+str(m)+""+":"+str(s))

 time.sleep(1)

 s=s+1

#als seconden op 60 zit +1 minuut reset timer

 if (s == 60):

  m=m+1

  s = 0

#als minuut op 60 zit +1 uur en reset minuten

 elif(m == 60):

   h=h+1

   m = 0

#zodra uur op 24 zit reset uren

 elif(h == 24):

    h = 0


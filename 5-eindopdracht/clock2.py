import time ## Importeert de tijd 

## Standaardwaarden van de counter
counter=0

hours = int(input(" Uren: "))
print("")

minutes = int(input(" Minuten: "))
print("")

seconds = int(input(" Seconde: "))
print("")

## Standaardwaarden van de uren
h = hours
## Standaardwaarden van de minuten
m = minutes
## Standaardwaarden van de secondes
s = seconds

## Maakt een functie aan met uur,minuten
def klok(h, m, s):
    print('{:02d}:{:02d}:{:02d}'.format(h,m,s))


while True:
    klok(hours, minutes, seconds)
## Maakt een time delay aan tussen de secondes in
    time.sleep(0.2)

## Hier voegt de counter elke keer een seconde toe
    seconds += 1

## Hier voegt de counter ook een seconde toe, zodat als de counter stopt het niet gelijk is aan <=n en dan wordt er een print gerunt
    counter+=1

## Als de variabele secondes op 60 staat, wordt er een minuut bijgevoegd en wordt secondes gereset

    for uren in range(hours,24):
        time.sleep(1)
        hours = 0
        for minuten in range(minutes,60):
            time.sleep(1)
            minutes = 0
            for secondes in range(seconds,60):
                time.sleep(1)
                seconds = 0
                klok(uren, minuten, secondes)
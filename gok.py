#tafels oefenen
import random
    
#tafel genereren
getal1 = random.randint(1, 10)
getal2 = random.randint(1, 10)

#score bijhouden
score = 0

def tafelgenereren():
    #vragen stellen
    getal1 = random.randint(1, 10)
    getal2 = random.randint(1, 10)
    antwoord = getal1 * getal2

print(f"Wat is {getal1} x {getal2}?")
antwoord = int(input("Antwoord: "))

if antwoord == getal1 * getal2:
    score += 1
    print(score)

if antwoord == getal1 * getal2:
    print("Goed zo!")
else:
    print(f"Helaas, het juiste antwoord is {getal1 * getal2}")








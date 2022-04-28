import csv
import itertools
import random

guessedNumber = None
counter = 1


# Daten werden aus der data.csv gelesen und in Data gespeichert.
with open('data.csv', newline='', encoding='utf-8-sig') as csvfile:
    data = list(csv.reader(csvfile))    
numbersList = list(itertools.chain.from_iterable(data))

# Die NumbersList wird in Int gecastet, um den maximalen und minimale Wert der gesamten Nummern zu ermitteln.
numbersListMaxMinValues = list(map(int, numbersList))
maxValue = max(numbersListMaxMinValues)
minValue = min(numbersListMaxMinValues)

# Wahl einer willkürlichen Zahl aus der eingelesen Liste.  
randomNumber = random.choice(numbersList)

# Iteriert bis guessedNumber und randomNumber gleich sind.
while guessedNumber != randomNumber:
    # Aufforderung eine Nummer von dem mindesten Wert bis zum höchsten Wert der Daten zu liefern. 
    guessedNumber = input(f"Give me a number between {minValue} and {maxValue}: ")

    # Abfrage, ob guessedNumber groeßer oder kleiner als die Random Number ist. Wenn eins der beiden zutrifft, wird ein Counter hochgesetzt und der Nutzende wird darauf hingewiesen, dass die Nummer darüber bzw. darunter liegt.
    if guessedNumber > randomNumber:
        counter += 1
        print("The Random Number is under your guessed Number.")

    else:
        counter += 1
        print("The Random Number is over your guessed Number.")
        

    # Abfrage, ob die guessedNumber mit der randomNumber übereinstimmt UND ob der zuvor angelegte Counter auf dem initialen Wert 1 (Anzahl der Versuche) liegt. Wenn dem so ist, wird dem Nutzenden zum Lucky guess gratuliert und die While-Schleife unterbrochen. 
    if guessedNumber == randomNumber and counter == 1:
        print("Lucky guess! You won on the first try")
        break
    # Abfrage, ob die guessedNumber mit der randomNumber übereinstimmt. Wenn dem so ist, wird dem Nutzenden gratuliert, eine Anzahl der Versuche ausgegeben und die While-Schleife unterbrochen. 
    if guessedNumber == randomNumber:
        print("Congrats. You won!")
        print("You needed " + str(counter) + " tries.")
        break
    








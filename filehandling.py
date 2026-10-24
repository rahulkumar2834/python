import os

def readandwrite():
    for number, name in enumerate(os.listdir(), start=1):
        print(f"{number}. {name}")


print("Hello buddy, what do you want?")
print("Press 1 to read a file")
print("Press 2 to append a file")
print("Press 3 to create a new file")

try:
    choise = int(input("Please enter your number: "))

    if choise == 1:
        readandwrite()
        filename = input("Kaun si file read karna chahte ho? ")

        with open(filename, "r") as file:
            print(file.read())

    elif choise == 2:
        readandwrite()
        filename2 = input("Kaun si file mein add karna chahte ho? ")

        if os.path.isfile(filename2):
            filewrite = input("File mein kya likhna chahte ho? ")

            with open(filename2, "a") as file:
                file.write("\n" + filewrite)

            print("Text add ho gaya!")
        else:
            print("Is naam ki file nahi mili.")

    elif choise == 3:
        filename = input("Nayi file ka naam likho, jaise notes.txt: ")

        if os.path.exists(filename):
            print("Is naam ki file ya folder pehle se hai.")
        else:
            text = input("File mein kya likhna hai? ")

            with open(filename, "w") as file:
                file.write(text)

            print("File successfully create ho gayi!")

    else:
        print("Sirf 1, 2 ya 3 choose karo.")

except ValueError:
    print("Please number enter karo, text nahi.")

except Exception as err:
    print(f"Exception occur hui: {err}")
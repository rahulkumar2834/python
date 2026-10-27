import os

filename = "students.txt"

while True:
    print("\n--- Student Marks Record ---")
    print("1. Naya record add karo")
    print("2. Saare records dekho")
    print("3. Exit")

    choice = input("Apna option likho: ")

    try:
        if choice == "1":
            name = input("Student ka naam: ").strip()

            if name == "":
                print("Naam khali nahi ho sakta.")
                continue

            marks = int(input("Marks likho (0 se 100): "))

            if marks < 0 or marks > 100:
                print("Marks 0 se 100 ke beech hone chahiye.")
                continue

            with open(filename, "a", encoding="utf-8") as file:
                file.write(f"{name} | {marks}\n")

            print("Record save ho gaya!")

        elif choice == "2":
            if os.path.isfile(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    content = file.read()

                if content.strip() == "":
                    print("Abhi koi record nahi hai.")
                else:
                    print("\nNaam | Marks")
                    print(content)
            else:
                print("Pehle koi record add karo.")

        elif choice == "3":
            print("Program band ho gaya.")
            break

        else:
            print("Sirf 1, 2 ya 3 choose karo.")

    except ValueError:
        print("Marks mein poora number likho, jaise 85.")

    except OSError as err:
        print(f"File ka error: {err}")
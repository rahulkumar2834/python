import random

print("🎮 Number Guessing Game")

while True:
    secret_number = random.randint(1, 100)
    chances = 7

    print("\nMaine 1 se 100 ke beech ek number chuna hai.")
    print("Tumhare paas 7 chances hain!")

    while chances > 0:
        try:
            guess = int(input("\nApna guess likho: "))
        except ValueError:
            print("Sirf poora number likho, jaise 25.")
            continue

        if guess < 1 or guess > 100:
            print("Number 1 se 100 ke beech hona chahiye.")
            continue

        chances -= 1

        if guess == secret_number:
            print("🏆 Sahi jawab! Tum jeet gaye!")
            break
        elif guess < secret_number:
            print("Thoda BADA number try karo.")
        else:
            print("Thoda CHHOTA number try karo.")

        print(f"Bache hue chances: {chances}")

    else:
        print(f"😅 Game over! Sahi number tha: {secret_number}")

    again = input("\nDobara kheloge? (yes/no): ").strip().lower()

    if again != "yes":
        print("Khelne ke liye shukriya!")
        break
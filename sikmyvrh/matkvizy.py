import random
import math

# ===============================
# Generátory příkladů
# ===============================

def generate_basic_example():
    """
    Vygeneruje jednoduchý příklad (sčítání, odčítání, násobení, dělení)
    a vrátí (text_příkladu, správný_výsledek).
    """
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-', '*', '/'])

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    else:
        # dělení – aby vyšel pěkný výsledek
        a = a * b
        result = a / b

    text = f"{a} {op} {b} = ?"
    return text, result


def generate_trig_example():
    """
    Vygeneruje goniometrický příklad (sin/cos/tan)
    a vrátí (text_příkladu, správný_výsledek_zaokrouhlený_na_3_desetinná_místa).
    """
    angle = random.choice([0, 30, 45, 60, 90])
    func = random.choice(['sin', 'cos', 'tan'])

    rad = math.radians(angle)

    # speciální případ: tan(90°) není definován – přeskočíme
    if func == 'tan' and angle == 90:
        return "tan 90° není definováno (přeskočeno)", None

    if func == 'sin':
        value = math.sin(rad)
    elif func == 'cos':
        value = math.cos(rad)
    else:
        value = math.tan(rad)

    value = round(value, 3)
    text = f"{func} {angle}° = ? (zaokrouhli na 3 desetinná místa)"
    return text, value


def generate_log_example():
    """
    Vygeneruje logaritmický příklad log_zaklad(hodnota)
    a vrátí (text_příkladu, správný_výsledek).
    """
    base = random.choice([2, 3, 10])
    exponent = random.randint(1, 5)
    value = base ** exponent

    text = f"log_{base}({value}) = ?"
    correct = exponent
    return text, correct


# ===============================
# Kvízové funkce
# ===============================

def quiz_basic(num_questions=5):
    score = 0
    for i in range(1, num_questions + 1):
        print(f"\nPříklad {i}/{num_questions}:")
        text, correct = generate_basic_example()
        print(text)
        try:
            ans = float(input("Tvoje odpověď: "))
            if abs(ans - correct) < 1e-6:
                print("Správně!")
                score += 1
            else:
                print(f"Špatně. Správná odpověď: {correct}")
        except ValueError:
            print(f"Neplatný vstup. Správná odpověď: {correct}")

    print(f"\nSkóre: {score} z {num_questions}")


def quiz_trig(num_questions=5):
    score = 0
    for i in range(1, num_questions + 1):
        print(f"\nPříklad {i}/{num_questions}:")
        text, correct = generate_trig_example()
        print(text)

        # speciální případ: nedefinováno / přeskočeno
        if correct is None:
            print("Tento příklad nelze vyčíslit – přeskočeno.")
            continue

        try:
            ans = float(input("Tvoje odpověď: "))
            if abs(ans - correct) < 0.0015:  # tolerance k zaokrouhlení
                print("Správně!")
                score += 1
            else:
                print(f"Špatně. Správná odpověď: {correct}")
        except ValueError:
            print(f"Neplatný vstup. Správná odpověď: {correct}")

    print(f"\nSkóre: {score} z {num_questions}")


def quiz_log(num_questions=5):
    score = 0
    for i in range(1, num_questions + 1):
        print(f"\nPříklad {i}/{num_questions}:")
        text, correct = generate_log_example()
        print(text)
        try:
            ans = float(input("Tvoje odpověď: "))
            if abs(ans - correct) < 1e-6:
                print("Správně!")
                score += 1
            else:
                print(f"Špatně. Správná odpověď: {correct}")
        except ValueError:
            print(f"Neplatný vstup. Správná odpověď: {correct}")

    print(f"\nSkóre: {score} z {num_questions}")


# ===============================
# Hlavní menu
# ===============================

def main():
    while True:
        print("\n=== MATEMATICKÝ KVÍZ ===")
        print("1) Základní početní operace")
        print("2) Goniometrie")
        print("3) Logaritmy")
        print("4) Konec")

        choice = input("Vyber možnost (1-4): ")

        if choice == '4':
            print("Konec programu.")
            break

        num = input("Kolik příkladů chceš? ")
        try:
            num = int(num)
        except ValueError:
            print("Musíš zadat celé číslo.")
            continue

        if choice == '1':
            quiz_basic(num)
        elif choice == '2':
            quiz_trig(num)
        elif choice == '3':
            quiz_log(num)
        else:
            print("Neplatná volba.")


if __name__ == "__main__":
    main()

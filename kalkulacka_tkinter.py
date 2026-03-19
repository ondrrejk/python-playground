import tkinter as tk

# Vytvoření okna
okno = tk.Tk()
okno.title("Kalkulačka")

# Vstupní pole
vstup = tk.Entry(okno, width=20, font=("Arial", 18))
vstup.grid(row=0, column=0, columnspan=4)

# Funkce pro přidání znaků
def stisk(t):
    vstup.insert(tk.END, t)

# Funkce pro výpočet
def spocitej():
    try:
        vysledek = eval(vstup.get())
        vstup.delete(0, tk.END)
        vstup.insert(0, vysledek)
    except:
        vstup.delete(0, tk.END)
        vstup.insert(0, "Chyba")

# Funkce pro smazání
def smazat():
    vstup.delete(0, tk.END)

# Tlačítka kalkulačky
tlacitka = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

radek = 1
sloupec = 0

for t in tlacitka:
    if t == "=":
        btn = tk.Button(okno, text=t, width=5, height=2, command=spocitej)
    else:
        btn = tk.Button(okno, text=t, width=5, height=2, command=lambda x=t: stisk(x))

    btn.grid(row=radek, column=sloupec)
    sloupec += 1
    if sloupec > 3:
        sloupec = 0
        radek += 1

# Tlačítko pro smazání
btn_c = tk.Button(okno, text="C", width=5, height=2, command=smazat)
btn_c.grid(row=radek, column=0)

# Spuštění aplikace
okno.mainloop()
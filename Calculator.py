import tkinter as tk
from tkinter import messagebox

def dodaj():
    try:
        # Pobranie wartości z pól i zamiana na liczby
        liczba1 = float(entry1.get())
        liczba2 = float(entry2.get())
        wynik = liczba1 + liczba2
        # Wyświetlenie wyniku
        label_wynik.config(text=f"Wynik: {wynik}")
    except ValueError:
        # Komunikat, jeśli wpisano coś innego niż liczby
        messagebox.showerror("Błąd", "Wpisz poprawne liczby!")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Prosty kalkulator")

# Etykiety i pola wejściowe
label1 = tk.Label(root, text="Pierwsza liczba:")
label1.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

label2 = tk.Label(root, text="Druga liczba:")
label2.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

# Przycisk "Dodaj"
przycisk = tk.Button(root, text="Dodaj", command=dodaj)
przycisk.grid(row=2, column=0, columnspan=2, pady=10)

# Miejsce na wynik
label_wynik = tk.Label(root, text="Wynik: ")
label_wynik.grid(row=3, column=0, columnspan=2)

# Uruchomienie pętli GUI
root.mainloop()
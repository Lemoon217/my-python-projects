import tkinter as tk
import random

number = random.randint(1, 10)
max_attempts = 3

attempts = 0

def check():
    global attempts, number

    text = entry.get().strip()

    if not text.isdigit():
        result["text"] = "❌ Введи число!"
        return

    guess = int(text)
    attempts += 1

    if guess == number:
        result["text"] = f"🎉 Угадал за {attempts} попыток!"
        entry.config(state="disabled")
        return

    elif guess < number:
        result["text"] = f"🔼 Больше\nОсталось попыток: {max_attempts - attempts}"
    else:
       result["text"] = f"🔽 Меньше\nОсталось попыток: {max_attempts - attempts}"

    if attempts >= max_attempts:
        result["text"] = f"💀 Ты проиграл! Число было {number}"
        entry.config(state="disabled")


def restart():
    global number, attempts
    number = random.randint(1, 10)
    attempts = 0
    entry.config(state="normal")
    entry.delete(0, tk.END)
    result["text"] = "Игра началась заново"
window = tk.Tk()
window.title("Угадай число 🎮")
window.geometry("400x300")

tk.Label(window, text="Угадай число от 1 до 10",
         font=("Arial", 16)).pack(pady=10)

entry = tk.Entry(window, font=("Arial", 20), justify="center")
entry.pack(ipady=10)

tk.Button(window, text="Проверить", command=check,
font=("Arial", 14), width=15, height=2).pack(pady=5)
tk.Button(window, text="Заново", command=restart,
 font=("Arial", 14), width=15, height=2).pack(pady=5)

result = tk.Label(window, text="")
result.pack()

window.mainloop()
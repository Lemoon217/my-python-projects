import tkinter as tk

# словарь операций
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Ошибка"
}

# функция для нажатия кнопок
def click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(symbol))

# очистка
def clear():
    entry.delete(0, tk.END)

# вычисление БЕЗ eval
def calculate():
    try:
        text = entry.get()

        for op in operations:
            if op in text:
                a, b = text.split(op)
                a = float(a)
                b = float(b)

                result = operations[op](a, b)

                entry.delete(0, tk.END)
                entry.insert(0, str(result))
                return

        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

# окно
window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x400")

# поле ввода
entry = tk.Entry(window, font=("Arial", 20))
entry.pack(fill="both", ipadx=8, ipady=8, padx=10, pady=10)

# кнопки
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','C','=','+'
]

frame = tk.Frame(window)
frame.pack()

row = 0
col = 0

for button in buttons:
    if button == "C":
        action = clear
    elif button == "=":
        action = calculate
    else:
        action = lambda x=button: click(x)

    tk.Button(frame, text=button, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
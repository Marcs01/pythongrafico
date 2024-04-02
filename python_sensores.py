import tkinter as tk
from tkinter import Toplevel


def open_new_window(title):
    new_win = Toplevel(root)
    new_win.title(title)
    tk.Label(new_win, text=title).pack(expand=True, fill="both")


def close_app():
    root.destroy()


def square_size(root, rows, columns):
    width = root.winfo_screenwidth() // columns
    height = root.winfo_screenheight() // rows
    return min(width, height)


root = tk.Tk()
root.state("zoomed")  # Maximiza la ventana principal

# Botón para salir
exit_button = tk.Button(root, text="Salir", command=close_app)
exit_button.place(x=0, y=0, width=50, height=50)

# Número de botones deseados
num_buttons = 21
button_dim = square_size(root, rows=3, columns=7)

for i in range(7):
    root.grid_columnconfigure(i, weight=1)
for i in range(3):
    root.grid_rowconfigure(i, weight=1)

buttons = []
for i in range(num_buttons):
    button = tk.Button(
        root,
        text=f"Botón {i+1}",
        command=lambda i=i: open_new_window(f"Botón {i+1}"),
        height=button_dim,
        width=button_dim,
    )
    button.grid(row=i // 7, column=i % 7, sticky="nsew", padx=2, pady=2)
    buttons.append(button)

root.mainloop()

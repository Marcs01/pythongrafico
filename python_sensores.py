<<<<<<< HEAD
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

for i in range(10):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

buttons = []
# boton 1

img = tk.PhotoImage(file="./buzz.jpg")


button = tk.Button(
    root,
    text=f"Buzzer",
    command=lambda i=i: open_new_window(f"Botón {1}"),
    height=button_dim,
    width=button_dim,
    image=img,
)
button.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 2
button = tk.Button(
    root,
    text=f"Botón {2}",
    command=lambda i=i: open_new_window(f"Botón {2}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 3
button = tk.Button(
    root,
    text=f"Botón {3}",
    command=lambda i=i: open_new_window(f"Botón {3}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 4
button = tk.Button(
    root,
    text=f"Botón {4}",
    command=lambda i=i: open_new_window(f"Botón {4}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 5
button = tk.Button(
    root,
    text=f"Botón {5}",
    command=lambda i=i: open_new_window(f"Botón {5}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=1, column=5, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 6
button = tk.Button(
    root,
    text=f"Botón {6}",
    command=lambda i=i: open_new_window(f"Botón {6}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=1, column=6, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 7
button = tk.Button(
    root,
    text=f"Botón {7}",
    command=lambda i=i: open_new_window(f"Botón {7}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton 8
button = tk.Button(
    root,
    text=f"Botón {8}",
    command=lambda i=i: open_new_window(f"Botón {8}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton 9
button = tk.Button(
    root,
    text=f"Botón {9}",
    command=lambda i=i: open_new_window(f"Botón {9}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 10
button = tk.Button(
    root,
    text=f"Botón {10}",
    command=lambda i=i: open_new_window(f"Botón {10}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=2, column=4, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton 11
button = tk.Button(
    root,
    text=f"Botón {11}",
    command=lambda i=i: open_new_window(f"Botón {11}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=2, column=5, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton 12
button = tk.Button(
    root,
    text=f"Botón {12}",
    command=lambda i=i: open_new_window(f"Botón {12}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=2, column=6, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 13
button = tk.Button(
    root,
    text=f"Botón {13}",
    command=lambda i=i: open_new_window(f"Botón {13}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton 14
button = tk.Button(
    root,
    text=f"Botón {14}",
    command=lambda i=i: open_new_window(f"Botón {14}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton 15
button = tk.Button(
    root,
    text=f"Botón {15}",
    command=lambda i=i: open_new_window(f"Botón {15}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=3, column=3, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton 16
button = tk.Button(
    root,
    text=f"Botón {16}",
    command=lambda i=i: open_new_window(f"Botón {16}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=3, column=4, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton17
button = tk.Button(
    root,
    text=f"Botón {17}",
    command=lambda i=i: open_new_window(f"Botón {17}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=3, column=5, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton18
button = tk.Button(
    root,
    text=f"Botón {18}",
    command=lambda i=i: open_new_window(f"Botón {18}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=3, column=6, sticky="nsew", padx=2, pady=2)
buttons.append(button)


# boton19
button = tk.Button(
    root,
    text=f"Botón {19}",
    command=lambda i=i: open_new_window(f"Botón {19}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=4, column=1, sticky="nsew", padx=2, pady=2)
buttons.append(button)

# boton20
button = tk.Button(
    root,
    text=f"Botón {20}",
    command=lambda i=i: open_new_window(f"Botón {20}"),
    height=button_dim,
    width=button_dim,
)
button.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)
buttons.append(button)


root.mainloop()
=======
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
>>>>>>> 15a049739c40c410b276a2c98f90b28e916ba031

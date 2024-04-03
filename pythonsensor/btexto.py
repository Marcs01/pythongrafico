import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

# Creamos un botón con texto centrado
button_centered = tk.Button(root, text="Text centered", justify="center")
button_centered.pack(pady=10)

# Creamos un botón con texto a la izquierda
button_left = tk.Button(root, text="Text left", justify="left")
button_left.pack(pady=10)

# Creamos un botón con texto a la derecha
button_right = tk.Button(root, text="Text right", justify="right")
button_right.pack(pady=10)

root.mainloop()

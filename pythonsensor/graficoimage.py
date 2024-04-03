from tkinter import *
import tkinter as tk
root = Tk()




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

root.state("zoomed")  # Maximiza la ventana principal


# Botón para salir
exit_button = tk.Button(root, text="Exit", command=close_app)
exit_button.place(x=0, y=0, width=50, height=50)

# Número de botones deseados
num_buttons = 21
button_dim = square_size(root, rows=5, columns=5)

for i in range(10):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

buttons = []


def thing():
   my_label.config(text="you can click")
   print("Botón clickeado")
#boton1
login_btn = PhotoImage(file='buzz.png')
my_button = Button(root, image = login_btn, command=lambda i=i: open_new_window(f"Botón {1}"), text="holamundo")
my_label = Label(root, text= 'hola')
my_button.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
buttons.append(my_button)

#boton2
login_btn2 = PhotoImage(file='vibra.png')
my_button2 = Button(root, image = login_btn2, command=lambda i=i: open_new_window(f"Botón {2}"), text="holamundo",justify="center")
my_label2 = Label(root, text= 'Holomundo', anchor="e")
my_button2.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
buttons.append(my_button2)

#boton3
login_btn3 = PhotoImage(file='sound.png')
my_button3 = Button(root, image = login_btn3, command=lambda i=i: open_new_window(f"Botón {3}"), text="holamundo",justify="center")
my_label3 = Label(root, text= 'Holomundo', anchor="e")
my_button3.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
buttons.append(my_button3)

#boton4
login_btn4 = PhotoImage(file='light.png')
my_button4 = Button(root, image = login_btn4, command=lambda i=i: open_new_window(f"Botón {4}"), text="holamundo",justify="left")
my_label4 = Label(root, text= 'Holomundo', anchor="e")
my_button4.grid(row=1, column=4, sticky="nsew", padx=2, pady=2)
buttons.append(my_button4)

#boton5
login_btn5 = PhotoImage(file='temp.png')
my_button5 = Button(root, image = login_btn5, command=lambda i=i: open_new_window(f"Botón {5}"), text="holamundo",justify="left")
my_label5 = Label(root, text= 'Holomundo', anchor="e")
my_button5.grid(row=1, column=5, sticky="nsew", padx=2, pady=2)
buttons.append(my_button5)

#boton6
login_btn6 = PhotoImage(file='Matrix.png')
my_button6 = Button(root, image = login_btn6, command=lambda i=i: open_new_window(f"Botón {6}"), text="holamundo",justify="left")
my_label6 = Label(root, text= 'Holomundo', anchor="e")
my_button6.grid(row=1, column=6, sticky="nsew", padx=2, pady=2)
buttons.append(my_button6)



mainloop()

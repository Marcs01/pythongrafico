import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Inicializar los datos de los animales
animales = ['X', 'Y', 'Z']
cantidad = [25, 30, 15]

# Altura fija de la gráfica
altura_fija = 50

# Función para actualizar los datos en tiempo real
def actualizar_datos(frame):
    # Generar nuevos datos aleatorios para la cantidad de animales
    for i in range(len(cantidad)):
        cantidad[0] += random.randint(-3, 3)
        cantidad[1] += random.randint(-3, 3)
        cantidad[2] += random.randint(-3, 3)
    
    # Limpiar la gráfica
    plt.clf()
    
    # Crear la gráfica de barras actualizada
    plt.bar(animales, cantidad, color=['yellow', 'brown', 'gray'])
    
    # Establecer los límites de los ejes y mantener la altura fija
    plt.ylim(0, altura_fija)
    
    # Añadir etiquetas y título
    plt.xlabel('.')
    plt.ylabel('.')
    plt.title('.')
    
# Crear la animación con save_count
ani = animation.FuncAnimation(plt.gcf(), actualizar_datos, interval=200, save_count=10)

# Mostrar la animación
plt.show()
plt.close()

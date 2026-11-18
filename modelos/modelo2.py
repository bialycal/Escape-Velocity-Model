import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11
M = 5.972e24
R = 6.371e6

#Características del cohete
m = 40000 #Masa del cohete (kg)
T = 800000 #Fuerza de empuje (N)
tiempo_motor = 100 #Duración del empuje (s)

#Condiciones iniciales
h = 0
v = 0
dt = 1
tiempo_max = 20000

tiempos = []
alturas = []
velocidades = []

#Simulación con Euler
for t in np.arange(0, tiempo_max, dt):

    tiempos.append(t)
    alturas.append(h / 1000)
    velocidades.append(v / 1000)

    #Empuje del motor
    if t < tiempo_motor:
        empuje = T
    else:
        empuje = 0

    #Aceleración total
    a = empuje / m - G * M / (R + h)**2

    #Actualizar posición y velocidad
    h = h + v * dt
    v = v + a * dt

    #Detener si regresa a la Tierra
    if h < 0:
        break

#Velocidad de escape teórica (la ideal, sin fuerzas ajenas)
v_escape = np.sqrt(2 * G * M / R)

print("Velocidad de escape:", round(v_escape / 1000, 2), "km/s")
print("Altura máxima:", round(max(alturas), 2), "km")

# Gráficas
plt.figure(figsize=(10, 4))
plt.plot(tiempos, alturas)
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (km)")
plt.title("Altura del cohete")
plt.grid()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(tiempos, velocidades)
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (km/s)")
plt.title("Velocidad del cohete")
plt.grid()
plt.show()

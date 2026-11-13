import numpy as np
import matplotlib.pyplot as plt

# Constantes
G = 6.67430e-11 #Constante gravitacional
M = 5.972e24 #Masa de la Tierra en kg
R = 6.371e6 #Radio de la Tierra en metros (estamos lanzando un objeto desde el nivel del mar)

# Condiciones iniciales
h = 0 #Altura inicial en metros
v = 11200 #Velocidad inicial (m/s)
dt = 1 #Paso de tiempo (s)
tiempo_max = 20000 #Tiempo máximo (s)(aprox 333 minutos, o sea 5 horas y cachito)

tiempos = []
alturas = []
velocidades = []

#Usaremos el método de Euler
for t in np.arange(0, tiempo_max, dt):

    #Guardar resultados
    tiempos.append(t)
    alturas.append(h / 1000)
    velocidades.append(v / 1000)

    #Aceleración gravitacional
    a = -G * M / (R + h)**2

    #Actualizar posición y velocidad
    h = h + v * dt
    v = v + a * dt

    #Detener si regresa a la Tierra
    if h < 0:
        break

#Velocidad de escape teórica
v_escape = np.sqrt(2 * G * M / R)

print("Velocidad de escape:", round(v_escape / 1000, 2), "km/s")
print("Altura final:", round(h / 1000, 2), "km")

# Graficar
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

#La luna está a 384000 km de la Tierra (363300 en el perigeo y a 405500 en el apogeo)
#A los 100 km un avión "entraría en órbita" (la atmósfera es tan delgada que el avión necesitaría volar a 28000 km/h para mantenerse a flote)
#Los satélites Low Earth orbit están entre los 160km y los 2000km
#Los Medium Earth Orbit están entre los 2000 y los 35786
#Los Geostationary Earth Orbit están a 35786 kkm de altura

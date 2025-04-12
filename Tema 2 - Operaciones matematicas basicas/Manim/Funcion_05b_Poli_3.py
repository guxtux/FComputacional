import numpy as np
import matplotlib.pyplot as plt

# Tamaño de la malla
res = 800
x = np.linspace(-4, 4, res)
y = np.linspace(-4, 4, res)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

# Definir la función f(z)
f = Z**3 - 2*Z**2 - 3*Z + 10

# Módulo y ángulo
abs_f = np.abs(f)
angle_f = np.angle(f)

# Crear imagen HSV (Hue = ángulo, Value = brillo)
hue = (angle_f + np.pi) / (2 * np.pi)  # normalizar fase a [0,1]
value = 1 - np.tanh(abs_f / 5)         # menor módulo = más brillante

# Crear imagen HSV y convertir a RGB
HSV = np.zeros(f.shape + (3,))
HSV[..., 0] = hue           # tono
HSV[..., 1] = 1             # saturación
HSV[..., 2] = value         # brillo

RGB = plt.cm.hsv(HSV[..., 0]) * value[..., None]
RGB[..., 3] = 1  # opacidad

# Mostrar imagen
plt.figure(figsize=(6, 6))
plt.imshow(RGB, extent=[-4, 4, -4, 4], origin='lower')
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.title("Colormap 2D de f(z) = z³ - 2z² - 3z + 10")
plt.grid(False)
plt.show()

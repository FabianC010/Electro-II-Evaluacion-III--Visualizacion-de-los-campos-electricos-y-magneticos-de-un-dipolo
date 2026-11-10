import numpy as np


import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider

#Constantes

mu0 = 4 * np.pi * 1e-7  # Permeabilidad del vacío (H/m)
p0 = 1
c = 3e8  # Velocidad de la luz (m/s)
lam = 1.0    
frec = c/lam              # longitud de onda (m)
w = 2 * np.pi * frec    # frecuencia angular (rad/s)
T = 2 * np.pi / w           # período (s)

r = np.linspace(1, 100, 1000)  # Distancia radial (m)
t = np.linspace(0.0, 10, 1000)  # Tiempo (s)
theta = np.linspace(0, np.pi, 1000)  # Ángulo polar (rad, porque numpy toma los angulos en radianes)

def Campo_E(r, ang, t):
    return -p0 * mu0 * w**2 / (4 * np.pi * r) * np.sin(ang) * np.cos(w * (t - r/c))

def Campo_B(r, ang, t):
    return -p0 * mu0 * w**2 / (4 * np.pi * r*c) * np.sin(ang) * np.sin(w * (t - r/c))

fig, ax = plt.subplots()
line, = ax.plot(t, Campo_E(r, theta, t), lw=2)
ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Campo Eléctrico [V/m]')
ax.grid()
ax.set_ylim(-p0 * mu0 * w**2 / (4 * np.pi) * 1.2, p0 * mu0 * w**2 / (4 * np.pi) * 1.2)


fig.subplots_adjust(left=0.45, bottom=0.2, right=0.95, top=None)


axang = fig.add_axes((0.25, 0.25, 0.0225, 0.63))
freq_slider = Slider(
    ax = axang,
    label = 'Angulo polar[rad]',
    valmin = 0,
    valmax = np.pi,
    valinit = 0,
    orientation = "vertical"
)


axdist = fig.add_axes((0.1, 0.25, 0.0225, 0.63))
dist_slider = Slider(
    ax=axdist,
    label="Distancia [m]",
    valmin=1,
    valmax=100,
    valinit= 1,
    orientation="vertical"
)

def update(val):
    line.set_ydata(Campo_E(dist_slider.val, freq_slider.val, t))
    fig.canvas.draw_idle()

freq_slider.on_changed(update)
dist_slider.on_changed(update)

resetax = fig.add_axes((0.8, 0.025, 0.1, 0.04))
button = Button(resetax, 'Reset', hovercolor='0.975')

def reset(event):
    freq_slider.reset()
    dist_slider.reset()
button.on_clicked(reset)

plt.show()
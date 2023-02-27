import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the golden ratio
phi = (1 + np.sqrt(5)) / 2

# Initialize the figure and axis
fig, ax = plt.subplots()

# Plot the golden ratio spiral
n = 100
theta = np.linspace(0, 10*np.pi, n)
r = np.linspace(0, 1, n)
x = r * np.cos(theta * phi)
y = r * np.sin(theta * phi)

line, = ax.plot(x, y, '-r')

# Define the animation update function
def update(frame):
    line.set_ydata(y * frame)
    return line,

# Animate the plot
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)

# Display the animation
plt.show()





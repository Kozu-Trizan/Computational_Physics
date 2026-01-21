import numpy as np  # Modern replacement for scipy/pylab in this context
import matplotlib.pyplot as plt
import time

# Use 'complex' for type hinting in Python
def Mandelbrot(z_not: complex, max_steps: int) -> int:
    z = 0j 
    for step in range(max_steps):
        if abs(z) > 2:
            return step
        z = z*z + z_not
    return max_steps

def main():
    grid_x = 1000
    grid_y = 1000
    max_steps_to_count = 1000

    graph_boundary = {
        "x_min": -2.,
        "x_max": 1.,
        "y_min": -1.,
        "y_max": 1.
    }

    # FIX: In Python, you can't initialize a 2D array with [][]
    # We use NumPy to create a grid efficiently
    mandelbrot_steps = np.zeros((grid_x, grid_y))
    
    start_time = time.time()

    for i in range(grid_x):
        for j in range(grid_y):
            # Calculate coordinates
            real = graph_boundary["x_min"] + (graph_boundary["x_max"] - graph_boundary["x_min"])/(grid_x-1.)*i
            imag = graph_boundary["y_min"] + (graph_boundary["y_max"] - graph_boundary["y_min"])/(grid_y-1.)*j
            
            # Call the function
            mandelbrot_steps[i, j] = Mandelbrot(complex(real, imag), max_steps_to_count)
    
    print(f'Clock time: {time.time() - start_time}')
    
    # Quick visualization (since you were using pylab)
    x_min, x_max, y_min, y_max = graph_boundary.values()
    plt.imshow(mandelbrot_steps.T, extent=(x_min, x_max, y_min, y_max), origin='lower', cmap='magma')
    plt.show()

if (__name__ == '__main__'):
    main()
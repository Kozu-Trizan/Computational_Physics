import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import time
from numba import jit, prange

@jit(nopython = True, parallel = True)
def Mandelbrot(graph_boundary:list[float], max_steps:int, grid_x:int, grid_y:int):
    mandelbrot_steps = np.zeros((grid_x, grid_y))
 
    for x in prange(grid_x):
        for y in range(grid_y):
            real = graph_boundary[0] + (graph_boundary[1] - graph_boundary[0])/grid_x*x
            imaginary = graph_boundary[2] + (graph_boundary[3] - graph_boundary[2])/grid_y*y
            comp = complex(real, imaginary)
            z = 0j
            iteration = max_steps
            for step in range(max_steps):
                if (z.real*z.real + z.imag*z.imag) > 4.0:
                    iteration = step
                    break
                z = z*z + comp
            mandelbrot_steps[x, y] = iteration

    return mandelbrot_steps

def update_axis(axis):
    fig = axis.get_figure()
    img = axis.get_images()[-1]

    (x_start, y_start), (x_end, y_end) = axis.viewLim.get_points()
    new_graph_boundary = [x_start, x_end, y_start, y_end]

    new_mandelbrot_steps = Mandelbrot(new_graph_boundary, max_steps=1000, grid_x=1000, grid_y=1000)
    
    #prevents infinite callbacks
    with axis.callbacks.blocked():
        img.set_data(new_mandelbrot_steps.T)
        img.set_extent(tuple(new_graph_boundary))
        
        img.set_norm(colors.PowerNorm(gamma=0.3, vmin=1, vmax=1000))
        
        fig.canvas.draw_idle()

def main():
    graph_boundary = [-2., 1., -1., 1.]
    max_steps = 1000
    grid_x = 1000
    grid_y = 1000

    start_time = time.time()
    mandelbrot_steps = Mandelbrot(graph_boundary, max_steps, grid_x, grid_y)
    end_time = time.time()
    print(f'Using Numba Clock time: {end_time - start_time}')

    fig, axis = plt.subplots(figsize=(10, 8))
    img = axis.imshow(mandelbrot_steps.T,
                      extent=(-2., 1., -1., 1.),
                      origin="lower",
                      cmap='twilight_shifted',
                      norm=colors.PowerNorm(gamma=0.3, vmin=1, vmax=1000)
                    )
    plt.colorbar(img, label='Iteration Depth')
    axis.set_title("Mandelbrot Explorer - Use the Zoom Tool!")

    axis.callbacks.connect('xlim_changed', update_axis)
    plt.show()


if (__name__ == '__main__'):
    main()



            

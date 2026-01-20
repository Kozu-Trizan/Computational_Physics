# Mandelbrot Set Visualization (OpenMP)

This project explores the Mandelbrot set using C++ and parallel computing.

## Features
- **Parallelization**: Uses OpenMP to distribute fractal calculations across multiple CPU cores.
- **Optimization**: Compiled with `-O3` for high-performance floating-point math.
- **Visualization**: Includes a Gnuplot script to generate high-resolution heatmaps.

## Performance
- **Processor**: Pentium Dual Core
- **Threads**: 2
- **Grid Size**: 1000x1000

## How to Compile
Using the MSYS2 UCRT64/MinGW64 toolchain:
```bash
g++ -fopenmp -O3 mandelbrot.cpp -o mandelbrot.exe

## How to plot
gnuplot mandelbrot_plot.plt
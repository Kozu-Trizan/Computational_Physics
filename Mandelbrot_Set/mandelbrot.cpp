#include <iostream>
#include <complex>
#include <ctime>
#include <vector>
#include <omp.h>

using namespace std;

int Mandelbrot(const complex<double>& z_not, int max_steps){
    /*complex<double>&z_not specifies a complex number of double and pass by reference--> &*/
    
    complex<double> z = 0;
    for (int i = 0; i < max_steps; i++){
        if(abs(z) > 2.) return i;
        z = z*z + z_not;
    }
    return max_steps;
}

int main(){
    const int grid_x = 1000;
    const int grid_y = 1000;
    int max_steps_to_check = 1000;

    // x --> real part/real axis y--> imaginary part/imaginary axis
    double graph_boundary[] = {-2, 1, -1, 1}; //{x_min, x_max, y_min, y_max}
    
    vector<int> mandel_steps(grid_x * grid_y);
    vector<complex<double>> mandel_coords(grid_x * grid_y);
    clock_t start_time = clock();
    double wall_start = omp_get_wtime();

    #pragma omp parallel for
    for(int i = 0; i < grid_x; i++){
        for(int j = 0; j < grid_y; j++){
            double real = graph_boundary[0] + (graph_boundary[1] - graph_boundary[0])/(grid_x - 1.) * i;
            double imaginary = graph_boundary[2] + (graph_boundary[3] - graph_boundary[2])/(grid_y - 1.) * j;
            // convert 2D points in grid to match 1D array
            mandel_coords[i*grid_y + j] = complex<double>(real, imaginary);
            mandel_steps[i*grid_y + j] = Mandelbrot(complex<double>(real, imaginary), max_steps_to_check);
        }
    }

    clock_t end_time = clock();
    double clock_time = double(end_time - start_time)/CLOCKS_PER_SEC;
    double wall_time = omp_get_wtime() - wall_start;

    //printing clock times and wall times
    clog<<"Clock time: "<<clock_time<<" s "<<"with Wall time: "<<wall_time<<"s"<<endl;

    //printing the complex numbers with steps required
    for (int i = 0; i < grid_x; i++)
    {
        for (int j = 0; j < grid_y; j++)
        {
            cout<<mandel_coords[i*grid_y + j].real()<<" "<<mandel_coords[i*grid_y + j].imag()<<" "<<1./mandel_steps[i*grid_y + j]<<endl;
        }
        
    }
    
    
    return 0;
}
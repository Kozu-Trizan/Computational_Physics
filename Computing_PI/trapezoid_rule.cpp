#include <iostream>
#include <ctime>
#include <cmath>
#include <omp.h>

using namespace std;

// integrate from 0 to 1 the function 4/(1+x^2) gives pi
// Trapezoid rule -> integrate_a_to_b f(x)dx = 1/2 * dx[f(x0) + 2{f(x1)+f(x2)+...}+f(xn)]
// dx = (b-a)/n, x0 = a, xi = a + i*dx 
double func_to_integrate(double x){
    return 4.0/(1.0 + x*x);
}

double calculate_pi(int steps){
    const double upper_lim = 1.0;
    const double lower_lim = 0.0;
    const double dx = (upper_lim - lower_lim)/steps;
    double sum = 0.0;

    /*Here sum variable must be used by all the thereads to make the sum chohernt*/
    /*So we use the reduction(+:sum) to tell the compiler to use multiple threads but the variable is neither private nor shared*/
    /*Valid reduction operators are: +,-,*,min,max,&,|,^,&&,|| */
    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < steps; ++i){
        double x = (i + 0.5)*dx;
        sum += func_to_integrate(x);
    }
    return sum*dx;
}

int main(){
    int steps_to_calculate_over = 100000;

    clock_t start_time = clock();
    double wall_start = omp_get_wtime();
    double pi;

    for (int test = 0; test < 100; test++)
    {
        pi = calculate_pi(steps_to_calculate_over);
    }
    
    clock_t end_time = clock();
    double clock_time = double(end_time - start_time)/CLOCKS_PER_SEC;
    double wall_time = omp_get_wtime() - wall_start;

    clog<<"Clock Time: "<<clock_time<<" s with Wall Time: "<<wall_time<<" s"<<endl;
    std::cout<<"For steps = "<<steps_to_calculate_over<<" approximate value for PI = "<<pi<<" with error= "<<std::abs(pi-M_PI)<<std::endl;
    
    return 0;
}
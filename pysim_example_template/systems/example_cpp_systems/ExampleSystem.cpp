#include "ExampleSystem.hpp"

#include "factory.hpp"

REGISTER_SYSTEM(ExampleSystem);

using  std::string;

string ExampleSystem::getDocs(){
    return string(
"Example System representing the Van Der Pol oscillator\n\n"

"In dynamics, the Van der Pol oscillator is a non-conservative oscillator "
"with non-linear damping. It evolves in time according to the second order "
"differential equation: "
"$$\\\\frac{d^2y}{dt^2} +a(y^2-b)\\\\frac{dy}{dt}+y$$ \n"
"where x is the position coordinate - which is a function of the time t, and "
"a is a scalar parameter indicating the nonlinearity and the strength of the "
"damping.\n"
"For further info see: http://en.wikipedia.org/wiki/Van_der_Pol_oscillator \n"
"\n"
"===== ===== ==============================\n"
"input type  description\n"
"===== ===== ==============================\n"
"a     float Non-linear damping coefficient\n"
"b     float Scaling coefficient\n"
"===== ===== ==============================\n"
"\n"
"===== ===== ==============================\n"
"state type  description\n"
"===== ===== ==============================\n"
"x     float first dimension\n"
"y     float second dimension\n"
"===== ===== ==============================\n"
"\n"    
);
}

ExampleSystem::ExampleSystem(void)
{
    INPUT(a, "Description of a")
    INPUT(b, "Description of b")

    STATE(x, dx, "Description of x")
    STATE(y, dy, "Description of y")

    OUTPUT(v, "Description of v");

    x = 1;
    y = 0;
    a = 1;
    b = 1;
}

void ExampleSystem::doStep(double time){
    dy = x;
    dx=a*x*(b-y*y)-y;
}
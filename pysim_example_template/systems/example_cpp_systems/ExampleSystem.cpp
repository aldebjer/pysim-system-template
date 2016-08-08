#include "ExampleSystem.hpp"


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
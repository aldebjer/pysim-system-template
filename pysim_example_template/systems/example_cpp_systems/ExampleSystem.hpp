#pragma once
#include "CppSystem.hpp"

class ExampleSystem :
    public pysim::CppSystem
{
public:
    ExampleSystem(void);

    static std::string getDocs();

    //First calculation in a simulation, only done once
    void preSim(){};

    //This function is called for each evaluation
    void doStep(double time);

    //After each set of evaluations when a new state value 
    //has been calculated this section is called
    void postStep(){};

    //Before finishing the simulation this function is called
    void finally(){};

protected:

    //Inputs
    double a,b;
    
    //States
    double x,dx;
    double y,dy;

    //Ouputs
    double v;
};
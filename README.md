# MetaheuristicFunctionMinimalization

Program uses three different approaches (local search, particle swarm optimalization and simulated annealing) to find global minimum for various functions.  
Program takes 2 arguments. One for specifying optimalization approach (--swarm, --annealing or --localsearch) and one for specyfying what function it will optimalize (--happycat, --griewank or --salomon).  
As an input, program takes 5 parameters separated with spaces. First parameter is integer type and specifies program exectuion time (in seconds). Four other parameters are decimal numbers and they represent the point, which will be given for an algorithm as an initial solution.  
First line of program output is an argument of the best solution and second line is value/fitness of the best solution.  
Example of usage:  
$ python main.py --swarm --griewank  
3 4 1 -2 3  
3.1400226127838695 -6.047434851938951e-10 7.277019066692724e-09 6.2706439166674315  
0.012316072519261478

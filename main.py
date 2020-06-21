import sys

from Functions import Functions
from LocalSearch import LocalSearch
from ParticleSwarm import ParticleSwarm
from SimulatedAnnealing import SimulatedAnnealing

arguments = input()
try:
    (t, x1, x2, x3, x4) = arguments.split(" ", 5)
    x = (float(x1), float(x2), float(x3), float(x4))
    seconds_to_run = int(t)
except:
    print("Bad args")
    exit(1)

if "--happycat" in sys.argv:
    function = Functions.happy_cat
elif "--griewank" in sys.argv:
    function = Functions.griewank
elif "--salomon" in sys.argv:
    function = Functions.griewank
else:
    print("Bad args")
    exit(1)

if "--localsearch" in sys.argv:
    result = LocalSearch.minimalize_function(function, x, seconds_to_run)
elif "--annealing" in sys.argv:
    result = SimulatedAnnealing.minimalize_function(function, x, seconds_to_run)
elif "--swarm" in sys.argv:
    result = ParticleSwarm.minimalize_function(function, x, seconds_to_run)
else:
    print("Bad args")
    exit(1)

output = ""
for i in range(4):
    output += str(result[0][i]) + " "

print(output)
print(result[1])

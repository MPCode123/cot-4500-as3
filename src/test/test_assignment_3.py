import sys
import os

# For using functions from assignment_1 to test in test_assignment_1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.main.assignment_3 import *

def f(t,y):
    return t - y**2

# Euler Method
Euler(0,1,f,0.2,10)




# Runge-Kutta
RK(0,1,f,0.2,10) 


def Euler(t0, y0, f, h, N):
    
    t = t0
    y = y0
    
    # Euler Formula
    for _ in range(N):
        y = y + h * f(t,y) # standard calculation
        t = t + h # increment to next value
    
    print(y) # Prints final value after N iterations
    
    
def RK(t0, w0, f, h, N):
    
    t = t0
    y = w0
    
    # Runge-Kutta order 4
    for _ in range(N):
        k1 = h * f(t,y) 
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y = y + 1/6 * (k1 + 2*k2 + 2*k3 + k4) # this is w_i+1
        t = t + h # increment to next value
        
    print(y) # Prints final value after N iterations

        
    

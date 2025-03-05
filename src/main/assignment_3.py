def Euler(t0, y0, f, h, N):
    
    t = t0
    y = y0
    
    for _ in range(N):
        y = y + h * f(t,y)
        t = t + h
    
    print(y)
    
    
def RK(t0, y0, f, h, N):
    
    t = t0
    y = y0
    
    for _ in range(N):
        k1 = h * f(t,y)
        k2 = h * f(t + h/2, y + k1/2)
        k3 = h * f(t + h/2, y + k2/2)
        k4 = h * f(t + h, y + k3)
        
        y = y + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h
        
    print(y)

        
    

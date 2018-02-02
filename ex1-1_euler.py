# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:36:41 2018

@author: cmcfaul
"""

import numpy as np

def PDE_EulerExp(fun,u0,t0,t1,n):
    """
    Solves the Absorption Equation
    u'(t) + au(t) = f(t), u(0) = u0
    
    Input arguments:
     fun is f(t), the RHS function depending only on time
     t0 initial time
     u0 initial condition at t0
     t1 final time
     n number of time steps between t0 and t1
     
    Output:
     u dimension (n+1) vector containing the numberical solution 
       at times t0+i*h, with h=(t1-t0)/n
    """

    u = np.zeros(n+1)
    h = (t1-t0)/n
    t = np.arange(t0,t1,h)
    u[0] = u0
    for i in range(n):
        u[i+1] = u[i] + h*fun(t[i]) 
    
    return u
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 10:32:25 2022
the aim is to analyze the P and N positions of the combinatoric game chomp
@author: laurin
"""
import copy
import numpy as np
import matplotlib.pyplot as plt
import keyboard
from pynput.mouse import Button, Controller

def chomp(field, N, P):
    
    next_boole = True
    if field in N or field in P:
        return N,P
    for i in range(n):
        for j in range(n):
            #bottom left piece is soure, therefore weird index with rows
            if field[n-1-i][j] == 1:
                #collects info about P Position
                #check if a move at this position is possible
                #copy of entries instead of references
                next_field = copy.deepcopy(field)
                #remove other pieces
                for k in range(n-i):
                    for l in range(n-j):
                        next_field[k][j+l] = 0
                        
                N,P = chomp(next_field, N, P)
                #check for N positons
                if next_field in P:
                    if not field in N:
                        N.append(field)
                    next_boole = False 
            else:
                break
    if next_boole:
        if not field in P:
            P.append(field)
    return N,P
                
def categories(n):
    #define positions that are already known
    N0 = [[0 for i in range(n)] for j in range(n)]
    N1 = copy.deepcopy(N0)
    N2 = copy.deepcopy(N0)
    P1 = copy.deepcopy(N0)
    P2 = copy.deepcopy(N0)
    for i in range(n):
        for j in range(n):
            N1[n-1][j] = 1
            N2[i][0] = 1
            P1[n-1][0] = 1
            P2[n-1][j] = 1
            P2[i][0] = 1
    N = [N0, N1, N2]
    P = [P1, P2]
    return N, P
    
    
if __name__ == '__main__':
    #the following block closes plots in the stupidest way possible. 
    #just for shits and giggles
    mouse = Controller()
    mouse.position = (917,257)
    keyboard.press_and_release('ctrl+shift+g')
    mouse.press(Button.left)
    mouse.release(Button.left)
    keyboard.press_and_release('ctrl+shift+w')  
    
    #game size. currently only quadratic games, general is very easy to do
    n = 7
    #some positions are already known
    N, P = categories(n)
    field = [[1 for x in range(n)] for y in range(n)]
    N, P = chomp(field, N, P)
    #plot N and P positions
    for i in range(len(N)):
        A = np.array(N[i])
        plt.imshow(A, interpolation = 'none')
        plt.axis('off')
        plt.title('N Position')
        plt.grid(True)
        plt.show()
    for i in range(len(P)):
        A = np.array(P[i])
        plt.imshow(A, interpolation = 'none')
        plt.axis('off')
        plt.title('P Position')
        plt.grid(True)
        plt.show()
        
    
        
        
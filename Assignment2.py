#!/usr/bin/env python
# coding: utf-8

# # Joint Probability Disribution

import numpy as np
import random

X=int(input("Enter a variable X: "))
Y=int(input("Enter a variable Y: "))
matrix=np.arange(X*Y).reshape(X,Y)
while(True):
    isIndependent=True
    sum=0
    for i in range(0,X):
        for j in range(0,Y):
            matrix[i][j]=random.randint(1,10)
            sum+=matrix[i][j]
    new_sum=0
    matrix=np.asfarray(matrix)
    
    for i in range(0,X):
        for j in range(0,Y):
            matrix[i][j]=float(matrix[i][j]/sum)
            new_sum+=matrix[i][j]
            
    X_marginal=[]
    Y_marginal=[]
    
    for i in range(0,X):
        x_sum=0
        for j in range(0,Y):
            x_sum+=matrix[i][j]
        X_marginal.append(x_sum)

    for i in range(0,Y):
        y_sum=0
        for j in range(0,X):
            y_sum+=matrix[j][i]
        Y_marginal.append(y_sum)
    
    for i in range(0,X):
        for j in range(0,Y):
            if(matrix[i][j]!=X_marginal[i]*Y_marginal[j]):
                isIndependent=False
                
    if(isIndependent):
        print(matrix)
        print(X_marginal)
        print(Y_marginal)
        break


# # Monty Hall Problem
import random

n_doors = int(input("How many doors would you like to have? "))
while n_doors < 3:
    n_doors = int(input("Please enter a valid number of doors (should be greater than 2): "))
    
n_open = int(input("How many doors would you like to open randomly? "))
while n_open >= n_doors-1 or n_open<=0:
    n_open = int(input(f"Please enter a valid number of doors to be opened randomly (should be less than {n_doors-1}) and greater than zero: "))

win_stay = 0
win_switch = 0

for i in range(1000):
    car_door=random.randint(1, n_doors)
    player_door = random.randint(1, n_doors)
    open_doors = []
    for j in range(n_open):
        open_door = random.randint(1, n_doors)
        while open_door == car_door or open_door == player_door or open_door in open_doors:
            open_door = random.randint(1, n_doors)
        open_doors.append(open_door)
    if player_door == car_door:
        win_stay += 1
    else:
        switch_door = list(set(range(1, n_doors+1)) - set(open_doors) - {player_door})
        switch_door = random.choice(switch_door)
        if switch_door==car_door:
            win_switch+=1
            
prob_while_staying = win_stay /(1000)
prob_while_switching = win_switch /(1000)
print(f"Win rate by staying: {prob_while_staying:.3f}")
print(f"Win rate by switching: {prob_while_switching:.3f}")

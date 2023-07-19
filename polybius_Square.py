import numpy as np
import pandas as ph

letters=['A'	,'B'	,'C'	,'D'	,'E'	,'F'	,'G'	,'H'	,'I/J'	,'K'	,'L'	,'M'	,'N'	,'O'	,'P'	,'Q'	,'R'	,'S'	,'T'	,'U'	,'V'	,'W'	,'X'	,'Y'	,'Z']
mat=[]
counter=0
mat_temp=[]
for alph in letters:
    if counter<5:
        mat_temp.append(alph)
        counter+=1
    if counter==5:
        mat.append(mat_temp)
        mat_temp=[]
        counter=0
a='M'
for i in range (5):
    for j in range(5):
        if a==mat[i][j]:
            print(i+1,j+1)



















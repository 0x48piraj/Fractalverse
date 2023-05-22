# coding: utf-8

import matplotlib.pyplot as plt


def cantor_set(x1,x2,y,n,
               bar_height=5,between_interval=10):
    """
    Cantor set is one of the simplest fractal shape where we start with a simple line,
    divide into three equal parts, erase the middle of the line,
    repeat step 2 with the remaining lines, over, and over, and over effectively creating a binary tree.

    ref: https://www.math.stonybrook.edu/~scott/Book331/Cantor_sets.html
    """    

    if n==0:
        return
    
    else:
        
        # first 1/3 and the last 1/3
        plt.fill_between([x1,x1+(x2-x1)/3],
                         [y-between_interval]*2,
                         [y-bar_height-between_interval]*2,)
        plt.fill_between([x2-(x2-x1)/3,x2],
                         [y-between_interval]*2,
                         [y-bar_height-between_interval]*2,)

        cantor_set(x1,x1+(x2-x1)/3,
                   y-between_interval,
                   n-1)        
        cantor_set(x2-(x2-x1)/3,x2,
                   y-between_interval,
                   n-1)

x1=0
x2=3
y=0
bar_height=5
between_interval=10
n=6

ax=plt.figure(figsize=(10,10))
plt.fill_between([x1,x2],
                 [y]*2,
                 [y-bar_height]*2,)
cantor_set(x1,x2,y,n)
plt.axis('off')
plt.show()

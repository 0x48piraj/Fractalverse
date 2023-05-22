
# coding: utf-8

import matplotlib.pyplot as plt


def euclidean_distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

def jerusalem_cross(top_left,top_right,bottom_left,bottom_right,n):
    """
    Recursively plot jerusalem cross, actually cross menger square, jerusalem square (2D version of jerusalem cube)

    reference to jerusalem cube: https://robertdickau.com/jerusalemcube.html
    do not confuse it with quadratic cross which creates new crosses from the tips: https://onlinemathtools.com/generate-quadratic-cross-fractal
    or fibonacci snowflakes, which is more like koch snowflake: http://www.slabbe.org/Publications/2011-fibo-snowflakes.pdf
    or vicsek fractal which is more similar to crosslet cross: https://en.wikipedia.org/wiki/Vicsek_fractal
    """

    if n<=0:
        return
    else:
        
        # compute the length
        length=euclidean_distance(top_left,top_right) 
    
        # create the cross
        plt.fill_between(
            [top_left[0]+length*(2**0.5-1),top_right[0]-length*(2**0.5-1)],
            [bottom_left[1]+length*(2**0.5-1)**2,bottom_left[1]+length*(2**0.5-1)**2],
            [top_left[1]-length*(2**0.5-1)**2,top_left[1]-length*(2**0.5-1)**2],
            color='k')
        plt.fill_between(
            [top_left[0]+length*(2**0.5-1)**2,top_right[0]-length*(2**0.5-1)**2],
            [bottom_left[1]+length*(2**0.5-1),bottom_left[1]+length*(2**0.5-1)],
            [top_left[1]-length*(2**0.5-1),top_left[1]-length*(2**0.5-1)],
            color='k')
        
        # top left corner recursion
        jerusalem_cross(top_left,(top_left[0]+length*(2**0.5-1),top_left[1]),
                        (top_left[0],top_left[1]-length*(2**0.5-1)),
                        (top_left[0]+length*(2**0.5-1),
                        top_left[1]-length*(2**0.5-1)),n-1)
        
        # top right corner recursion
        jerusalem_cross((top_right[0]-length*(2**0.5-1),top_left[1]),top_right,
                        (top_right[0]-length*(2**0.5-1),
                         top_left[1]-length*(2**0.5-1)),
                        (top_right[0],top_left[1]-length*(2**0.5-1)),n-1)
        
        # bottom left corner recursion
        jerusalem_cross((bottom_left[0],bottom_left[1]+length*(2**0.5-1)),
                        (bottom_left[0]+length*(2**0.5-1),
                         bottom_left[1]+length*(2**0.5-1)),
                        bottom_left,
                        (bottom_left[0]+length*(2**0.5-1),bottom_left[1]),n-1)
        
        # bottom right corner recursion
        jerusalem_cross((bottom_right[0]-length*(2**0.5-1),
                         bottom_right[1]+length*(2**0.5-1)),
                        (bottom_right[0],
                         bottom_right[1]+length*(2**0.5-1)),
                        (bottom_right[0]-length*(2**0.5-1),
                         bottom_right[1]),
                        bottom_right,n-1)
        
        # top mid corner recursion
        jerusalem_cross((top_left[0]+length*(2**0.5-1),top_left[1]),
                        (top_right[0]-length*(2**0.5-1),top_left[1]),
                        (top_left[0]+length*(2**0.5-1),
                         top_left[1]-length*(2**0.5-1)**2),
                        (top_right[0]-length*(2**0.5-1),
                         top_left[1]-length*(2**0.5-1)**2),n-2)  
        
        # bottom mid corner recursion
        jerusalem_cross((bottom_left[0]+length*(2**0.5-1),
                         bottom_left[1]+length*(2**0.5-1)**2),
                        (bottom_right[0]-length*(2**0.5-1),
                         bottom_left[1]+length*(2**0.5-1)**2),
                        (bottom_left[0]+length*(2**0.5-1),
                         bottom_left[1]),
                        (bottom_right[0]-length*(2**0.5-1),
                         bottom_left[1]),n-2)
        
        # left mid corner recursion
        jerusalem_cross((bottom_left[0],
                         top_left[1]-length*(2**0.5-1)),
                        (bottom_left[0]+length*(2**0.5-1)**2,
                         top_left[1]-length*(2**0.5-1)),
                        (bottom_left[0],bottom_left[1]+length*(2**0.5-1)),
                        (bottom_left[0]+length*(2**0.5-1)**2,
                         bottom_left[1]+length*(2**0.5-1)),n-2)
        
        # right mid corner recursion
        jerusalem_cross((bottom_right[0]-length*(2**0.5-1)**2,
                         top_right[1]-length*(2**0.5-1)),
                        (bottom_right[0],
                         top_right[1]-length*(2**0.5-1)), 
                        (bottom_right[0]-length*(2**0.5-1)**2,
                         bottom_right[1]+length*(2**0.5-1)),
                        (bottom_right[0],bottom_right[1]+length*(2**0.5-1)),
                        n-2)

top_left=(0,0)
top_right=(1,0)
bottom_left=(0,-1)
bottom_right=(1,-1)
n=5

ax=plt.figure(figsize=(10,10))
jerusalem_cross(top_left,top_right,bottom_left,bottom_right,n)
plt.xlim(top_left[0],top_right[0])
plt.ylim(bottom_right[1],top_left[1],)
plt.axis('off')
plt.show()

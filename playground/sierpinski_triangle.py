
# coding: utf-8

import matplotlib.pyplot as plt


def sierpiński_triangle(coordinates,lvl,colour='k'):
    
    # stop recursion
    if lvl==0:
        return
    
    # unpack coordinates
    # coordinates have to follow the order of left, mid, right
    left=coordinates[0];mid=coordinates[1];right=coordinates[2]
    
    # compute mid point for each line
    left_new=((mid[0]-left[0])/2+left[0],(mid[1]-left[1])/2+left[1])
    mid_new=((right[0]-left[0])/2+left[0],(right[1]-left[1])/2+left[1])
    right_new=((right[0]-mid[0])/2+mid[0],(mid[1]-right[1])/2+right[1])

    for i in coordinates:
        for j in coordinates:
            if i!=j:            
                plt.plot([i[0],j[0]],[i[1],j[1]],c=colour)    
    
    # recursive plot sub triangles
    sierpiński_triangle([left,left_new,mid_new],lvl-1)
    sierpiński_triangle([left_new,mid,right_new],lvl-1)
    sierpiński_triangle([mid_new,right_new,right],lvl-1)

sierpiński_triangle([(0,0),(0.5,1),(1,0)],4)
plt.show()

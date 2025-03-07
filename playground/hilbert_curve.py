
# coding: utf-8

import matplotlib.pyplot as plt


def hilbert_curve(point1,point2,n):

    # unpack
    x_start,y_start=point1
    x_end,y_end=point2

    # the function consists four different parts
    # which are 4 different rotations plus flips of a second order hilbert curve
    # 0 degree second order hilbert curve
    if x_start<x_end and y_start==y_end:

        # compute the grid length
        L=x_end-x_start

        # keypoints are starting and ending points
        # of 4 different first order hilbert curves
        # on a second order hilbert curve
        keypoints=[(x_start,y_start),(x_start,y_start-(L-1)/2),
        (x_start,y_start-(L-1)/2-1),(x_start+(L-1)/2,y_start-(L-1)/2-1),
        (x_start+(L-1)/2+1,y_start-(L-1)/2-1),(x_start+L,y_start-(L-1)/2-1),
        (x_start+L,y_start-(L-1)/2),(x_start+L,y_start)]

        # base case
        if n==1:
            yield keypoints
        else:

            # recursion
            for i in range(0,8,2):
                yield from hilbert_curve(keypoints[i],keypoints[i+1],n-1)

    # 180 degree second order hilbert curve
    if x_start>x_end and y_start==y_end:
        L=x_start-x_end
        keypoints=[(x_start,y_start),(x_start,y_start+(L-1)/2),
        (x_start,y_start+(L-1)/2+1),(x_start-(L-1)/2,y_start+(L-1)/2+1),
        (x_start-(L-1)/2-1,y_start+(L-1)/2+1),(x_start-L,y_start+(L-1)/2+1),
        (x_start-L,y_start+(L-1)/2),(x_start-L,y_start)]
        if n==1:
            yield keypoints
        else:
            for i in range(0,8,2):
                yield from hilbert_curve(keypoints[i],keypoints[i+1],n-1)

    # clockwise 90 degree horizontal flipped second order hilbert curve
    if x_start==x_end and y_start>y_end:
        L=y_start-y_end
        keypoints=[(x_start,y_start),(x_start+(L-1)/2,y_start),
        (x_start+(L-1)/2+1,y_start),(x_start+(L-1)/2+1,y_start-(L-1)/2),
        (x_start+(L-1)/2+1,y_start-(L-1)/2-1),(x_start+(L-1)/2+1,y_start-L),
        (x_start+(L-1)/2,y_start-L),(x_start,y_start-L)]
        if n==1:
            yield keypoints
        else:
            for i in range(0,8,2):
                yield from hilbert_curve(keypoints[i],keypoints[i+1],n-1)

    # clockwise 270 degree horizontal flipped second order hilbert curve
    if x_start==x_end and y_start<y_end:
        L=y_end-y_start
        keypoints=[(x_start,y_start),(x_start-(L-1)/2,y_start),
        (x_start-(L-1)/2-1,y_start),(x_start-(L-1)/2-1,y_start+(L-1)/2),
        (x_start-(L-1)/2-1,y_start+(L-1)/2+1),(x_start-(L-1)/2-1,y_start+L),
        (x_start-(L-1)/2,y_start+L),(x_start,y_start+L)]
        if n==1:
            yield keypoints
        else:
            for i in range(0,8,2):
                yield from hilbert_curve(keypoints[i],keypoints[i+1],n-1)


# starting and ending points and the order of hilbert curve
n=4
starting_point=(0,0)
ending_point=(2**n-1,0)

coordinates=[i for arr in hilbert_curve(
    starting_point,ending_point,n) for i in arr]

plt.plot([i[0] for i in coordinates],
        [i[1] for i in coordinates])
plt.show()

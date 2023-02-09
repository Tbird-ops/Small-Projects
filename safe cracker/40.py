#!/usr/bin/python3

# This is my automated solution for the safe cracker 40 puzzle. (I did complete this by hand)
# My goal is to automatedly solve the safe cracker 50 puzzle

# Notes:
# All values in ring 4 must be used
# All "above" values must be used
# "Below" values are utilized in sets of 8.
# All below values attach to the ring beneath it
# Ring 4 and 3b never rotate
# Ring pairs <lower>(3a2b) <upper>(2a1b) must rotate together
# Cannot use a number from both above and below on the same ring
#
#
#
#


# The rings and numbers of the disk based puzzle. Numbers aligned in columns similar to method for summation

ring4   = [15, 23, 19,  3,  2,  3, 27, 20, 11, 27, 10, 19, 10, 13, 10,  2]  # Ring 4: Outer most ring.
ring3b  = [ 9,  5, 10,  5,  1, 24,  2, 10,  9,  7,  3, 12, 24, 10,  9, 22]  # Ring 3 below.
ring3a  = [ 0,  6,  0,  9,  0, 16,  0, 17,  0,  2,  0,  2,  0, 10,  0, 15]  # Ring 3 above.
ring2b  = [15, 22,  6,  1,  1, 11, 27, 14,  5,  5,  7,  8, 24,  8,  3,  6]  # Ring 2 below.
ring2a  = [ 0, 10,  0,  2,  0, 22,  0,  2,  0, 17,  0, 15,  0, 14,  0,  5]  # Ring 2 above. 
ring1b  = [ 6,  3,  1,  6, 10,  6, 10,  2,  6, 10,  4,  1,  5,  5,  4,  8]  # Ring 1 below. 
ring1a  = [ 0,  6,  0, 13,  0,  3,  0,  3,  0,  6,  0, 10,  0, 10,  0, 10]  # Ring 1 above.


# Used to rotate arrays
def rotate_ring(ring):
    front = ring.pop(0)
    ring.append(front)
    return

# Rotate fixed pairs
def rotate_pair(pair):
    if pair == 'l' or pair == 'lower':
        rotate_ring(ring3a)
        rotate_ring(ring2b)
    elif pair == 'u' or pair == 'upper':
        rotate_ring(ring2a)
        rotate_ring(ring1b)
    else:
        print("Invalid pair")
    return

# Calculate the sum of the rings (Determinant of the above below pair)
def calc_vector(r1, r2, r3, r4, loc):
    return r1[loc]+r2[loc]+r3[loc]+r4[loc]

def check_solve():
    pass

def main():
    for i in range(16):
        for j in range(16):
            for k in range (16):
                if ring1a[k] != 0 and ring2a[k] != 0 and ring3a[k] != 0:
                    value = calc_vector(ring1a, ring2a, ring3a, ring4, k)
                    print(value)
    return 


main()
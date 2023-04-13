import math
import sys
import matplotlib.pyplot as plt 

'''
Calculates chromaticity coordinates (x,y) from RGB values
'''
def chromaticity(R, G, B):
    # Calculate Remote Sensing Reflectance (Rrs)
    RrsR = R/math.pi
    RrsG = G/math.pi
    RrsB = B/math.pi

    # Normalize trisimulus values X, Y, Z
    X = 12.04*RrsB + 53.696*RrsG + 32.087*RrsR
    Y = 23.122*RrsB + 65.702*RrsG + 16.830*RrsR
    Z = 61.055*RrsB + 1.778*RrsG + 0.015*RrsR

    # Calculate chromaticity coordinates
    x = X / (X + Y + Z)
    y = Y / (X + Y + Z)

    return x, y

def main():
    input = open("./data/" + sys.argv[1], 'r',)
    output = open("./data/" + sys.argv[2], 'w')
    input.readline()
    for line in input:
        data = line.split(',')
        B = float(data[1])
        G = float(data[2])
        R = float(data[3])
        x, y = chromaticity(R, G, B)
        output.write(str(data[0]) + "," + str(x) + "," + str(y) + "\n")
    input.close()
    output.close()


main()


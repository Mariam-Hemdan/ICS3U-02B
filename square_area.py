#!/usr/bin/env python3

# Created by: Mariam Hemdan
# Created on: October 2019
# This program calculates the area of a square
#     where the user gets to enter the length  in mm

import math


def main():
    # main function
    print("We will be calculating the area of a square. ")
    # input
    length = int(input("Enter the length (mm): "))
    # process
    area = length**2
    # output
    print("Area is {} mm2".format(area))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# Created By: Minab Berhane
# Date: December 1 2022
# This program gets the perimeter of a triangle


def calculate_perimeter(side_a, side_b, side_c):

    # calculating perimeter
    perimeter = side_a + side_b + side_c

    return perimeter


def calculate_area(height, base):
    # calculate area

    # process
    area = (height * base) / 2

    return area


def main():
    # This program calculates the perimeter of a triangle

    # Get user input
    side_a_as_a_string = input("Enter side_a (cm): ")
    side_b_as_a_string = input("Enter side_b (cm): ")
    side_c_as_a_string = input("Enter side_c or base (cm): ")
    height_as_a_string = input("Enter the height (cm): ")
    print("")

    try:
        # converting strings to floats
        side_a_as_a_float = float(side_a_as_a_string)
        side_b_as_a_float = float(side_b_as_a_string)
        side_c_as_a_float = float(side_c_as_a_string)
        height_as_a_float = float(height_as_a_string)
        # Make sure input is greater than 0
        if side_a_as_a_float > 0 and side_b_as_a_float > 0 and side_c_as_a_float > 0:
            # calling the function
            calculated_perimeter = calculate_perimeter(side_a_as_a_float, side_b_as_a_float, side_c_as_a_float)
            print("The perimeter is {0} cm".format(calculated_perimeter))
            calculated_area = calculate_area(height_as_a_float, side_c_as_a_float)
            print("The area is {0} cm²".format(calculated_area))

        else:
            print("please enter a positive number")
    # Check if input is a string
    except Exception:
        print("Invalid data entered! Only numbers can be accepted!")


if __name__ == "__main__":
    main()

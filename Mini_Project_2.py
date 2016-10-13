""" TODO: Put your header comment here """
"""Sandy Ta - Mini Project #2: Computational Art"""
import random
from PIL import Image
import math


def build_random_function(min_depth, max_depth):
    funct = ["prod","avg", "sin_pi", "cos_pi","tan_pi","neg"]
    base = ["x","y"] #for base case
    index_funct = random.randint(0,5) #selects which function in funct to return
    if max_depth == 1:
        index_base = random.randint(0,1)
        return base[index_base] #once the max_depth reaches 1, return either x or y
    else:
        return [funct[index_funct], build_random_function(min_depth - 1, max_depth - 1), build_random_function(min_depth - 1, max_depth - 1)]
    """The function sets the base case at max_depth = 1 at which point the recursion stop.
       At the base case, the functions x or y are returned.
       If the function is has not yet reached the base case, it will continue to
       return a random function from the function list and iterate the build_random_function again
       while decreasing the min_depth and max_depth of the random function by - 1 until the max_depth = 1."""

    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    # TODO: implement this
    pass


def evaluate_random_function(f, x, y):
    if len(f) == 1:
        if f[0] == "x":
            return x
        elif f[0] == "y":
            return y
    else:
        res_1 = evaluate_random_function(f[1], x, y)
        res_2 = evaluate_random_function(f[2], x, y)
        if f[0] == "prod":
            return res_1 * res_2
        elif f[0] == "avg":
            return 0.5*(res_1 + res_2)
        elif f[0] == "sin_pi":
            return math.sin(math.pi * res_1)
        elif f[0] == "cos_pi":
            return math.cos(math.pi * res_1)
        elif f[0] == "tan_pi":
            return math.tan(math.pi * res_1)
        elif f[0] == "neg":
            return -res_1



    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    # TODO: implement this
    pass


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    scaling = (float(val) - float(input_interval_start))/(float(input_interval_end - input_interval_start))
    adj_val = float(output_interval_end - output_interval_start)*scaling + float(output_interval_start)
    return adj_val

    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # TODO: implement this
    pass


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = ["x"]
    green_function = ["y"]
    blue_function = ["x"]
    red_function = build_random_function(7, 9)
    green_function = build_random_function(7, 9)
    blue_function = build_random_function(7, 9)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("example1.png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    #test_image("noise.png")

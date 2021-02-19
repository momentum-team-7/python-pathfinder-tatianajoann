from PIL import Image
# 1: Read the data from `elevation_small.txt` into an appropriate data structure to get the elevation data.
# This file is made up of multiple lines. Each line has a list of numbers representing elevation in meters.
# The elevation is the maximum elevation for a 90m x 90m square.

# - read the file and store it as a list of lists. check out readlines.
# - print out what you have and think about how it corresponds to elevations on a map.
# - how to match each elevation to its corresponding coordinates. probably by finding its index.

#  2: - using the pillow library, make a black or white square that matches dimensions (how to make a square of certain dimensions in pillow)
# - figure out the percentage ; lowest elevation (black) highest elevation (white). figure out the percentage of the difference that each elevation is. lower places have lower percentage closer to zero so they will be darker, higher places have higher percentage so they will be lighter.
# - try to match one pixel grayscale intensity it according to elevation

coordinates = []
with open("elevation_small.txt", "r") as file:
    for line in file.readlines():
        coordinates.append(line.split())
# turning each line into list, then putting all the list in the big lists
    height = len(coordinates)
    width = len(coordinates[0])
# defining dimensions

    min_el = int(min(map(min, coordinates)))
    max_el = int(max(map(max, coordinates)))  # finding min and max elevations
    new_coordinates = []  # making a new list
    for coordinatelist in coordinates:
        new_coordinatelist = []  # making the little list that goes in the big list
        for coordinate in coordinatelist:
            new_coordinate = int(((int(coordinate) - min_el) /
                                  (max_el - min_el)) * 255)  # taking elevation data and turning to rgb
            new_coordinate = (new_coordinate, new_coordinate, new_coordinate)
            # appending new rgb coordinate to little list
            new_coordinatelist.append(new_coordinate)
        # appending little list to big list
        new_coordinates.append(new_coordinatelist)

    # creating new image and putting in dimensions
    img = Image.new('RGB', (width, height))
    for x in range(width):  # this will iterate through the range of the width
        for y in range(height):  # this will iterate through the range of the height

            # get little list with position/index of x from the big list
            value_list = new_coordinates[x]

            # get color value with position/index of y from the little list
            color_value = value_list[y]

            # use x and y for the position of the pixel. and get the rgb value from the variable above
            img.putpixel((x, y), color_value)

    img.save('pil_read.png')

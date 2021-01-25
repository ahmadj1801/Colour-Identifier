import argparse as ap
import cv2
import pandas as pd

# python Colours.py -i test.jpg

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global red, green, blue, x_point, y_point, clicked
        clicked = True
        x_point, y_point = x, y
        blue, green, red = image[y, x]
        red = int(red)
        green = int(green)
        blue = int(blue)

def get_nearest_colour(r, g, b):
    min_value = 10000
    colour_name = "Undefined"
    for index, row in data_frame.iterrows():
        distance = abs(r - int(row['R'])) + abs(r - int(row['G'])) + abs(r - int(row['B']))
        if distance <= min_value:
            min_value = distance
            colour_name = row['Colour Name']
    return colour_name

# Code to get the image. Initial Setup.
ap_var = ap.ArgumentParser()
ap_var.add_argument('-i', '--image', required=True, help='Insert Image Path')
args = vars(ap_var.parse_args())
image_path = args['image']
image = cv2.imread(image_path)

# Variables
red=green=blue=x_point=y_point = 0
clicked = False

# Read the Datafile into a Dataframe.
headings = ['Colour', 'Colour Name', 'Hex', 'R', 'G', 'B']
data_frame = pd.read_csv('Data/colours.csv', names=headings, encoding='utf-8')
print(data_frame)

# Create a window
cv2.namedWindow("Picture")
cv2.setMouseCallback("Picture", draw)

while 1:
    cv2.imshow("Picture", image)
    if clicked:
        cv2.rectangle(image, (20, 20), (750, 60), (blue, green, red), -1)
        text = get_nearest_colour(red, green, blue)
        cv2.putText(image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if red + green + blue >= 600:
            cv2.putText(image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
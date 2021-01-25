import argparse as ap
import cv2

ap_var = ap.ArgumentParser()
ap_var.add_argument('-i', '--image', required=True, help='Insert Image Path')
args = vars(ap_var.parse_args())
image_path = args['image']
image = cv2.imread(image_path)

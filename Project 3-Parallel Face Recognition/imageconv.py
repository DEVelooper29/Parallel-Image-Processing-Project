import cv2
import numpy as np
import os

def save_pgm_as_txt(image, filename):
    with open(filename, 'w') as f:
        f.write("180 200\n")  # Width and height of the image
        for row in image:
            for pixel in row:
                f.write(f"{pixel} ")
            f.write("\n")

def jpg_to_txt(jpg_filename, txt_filename):
    # Read JPEG image
    img = cv2.imread(jpg_filename, cv2.IMREAD_GRAYSCALE)

    # Resize the image to match the required dimensions (180x200)
    if img is not None and img.size != 0:
        resized_img = cv2.resize(img, (180, 200))
    else:
        print("Error: Failed to read image or empty image.")
        return

    # Specify the directory where you want to save the output file
    output_dir = os.path.dirname(txt_filename)

    # Ensure the output directory exists, create it if necessary
    os.makedirs(output_dir, exist_ok=True)

    # Save the image as a text file
    save_pgm_as_txt(resized_img, txt_filename)

# Example usage:
jpg_filename = 'Project 3-Parallel Face Recognition/test1.jpg'  # Specify your JPEG image filename
txt_filename = 'Project 3-Parallel Face Recognition/output.txt'  # Specify the output text filename
jpg_to_txt(jpg_filename, txt_filename)

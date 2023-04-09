# Segmentation Project Main script
# We keep the main file in def main so that when it only runs when it is called
import os
from PIL import Image
from tkinter import filedialog


def get_image_path():
    # Prompt user to select an image file
    root = Tk()
    root.withdraw() # hide the Tkinter root window
    file_path = filedialog.askopenfilename(title="Select Image",
                                           filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    # Check if file format is supported
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported file format: {ext}")
    return file_path


def main():
    # Add your code here
    print("Hello Friends :)")
if __name__ == '__main__':
    main()

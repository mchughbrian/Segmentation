import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2

def cartoonize_image(image, ksize=5, n_colors=10):
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
    blur = cv2.medianBlur(gray, ksize)

    edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)

    color = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    color = cv2.medianBlur(color, ksize)
    color = cv2.resize(color, None, fx=1.0 / n_colors, fy=1.0 / n_colors, interpolation=cv2.INTER_AREA)
    color = cv2.resize(color, (image.width, image.height), interpolation=cv2.INTER_LINEAR)

    cartoon = cv2.bitwise_and(color, edges)
    cartoon = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)

    return Image.fromarray(cartoon)

def open_image(image_label):
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif"), ("All files", "*.*")])
    if file_path:
        try:
            image = Image.open(file_path)
            image = cartoonize_image(image)  # Cartoonize the image
            image.thumbnail((700, 700))  # Resize the image to fit the label

            photo = ImageTk.PhotoImage(image)
            image_label.config(image=photo)
            image_label.image = photo
        except IOError:
            messagebox.showerror("Error", "The selected file is not a supported image format.")


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Image Viewer")

    # Create a label to display the image
    image_label = tk.Label(root)
    image_label.pack()

    # Create a button for opening the image
    open_button = tk.Button(root, text="Open Image", command=lambda: open_image(image_label))
    open_button.pack()

    # Run the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()

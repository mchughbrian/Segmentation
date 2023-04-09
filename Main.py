import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


def open_image(image_label):
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif"), ("All files", "*.*")])
    if file_path:
        try:
            image = Image.open(file_path)
            image.thumbnail((400, 400))  # Resize the image to fit the label

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

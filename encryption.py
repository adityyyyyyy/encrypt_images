import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os

def operate(key):
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return
    
    try:
        # Read the image file
        with open(file_path, 'rb') as file:
            data = bytearray(file.read())  # read file data into a bytearray for mutable operations
        
        # XOR operation
        for i in range(len(data)):
            data[i] ^= key
        
        # Write the modified data back to the same file
        with open(file_path, 'wb') as file:
            file.write(data)
        
        messagebox.showinfo("Success", "Operation completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    root.title("Image Operation")
    root.geometry("400x200")
    root.resizable(False, False)

    # Font setup (optional, requires additional handling in tkinter for custom fonts)
    # font = ('Roboto', 25, 'bold')

    # Button setup
    button = tk.Button(root, text="Open Image", command=lambda: get_key_and_operate(), font=('Arial', 14))
    button.pack(pady=20)

    # Get key from user
    def get_key_and_operate():
        key = simpledialog.askinteger("Input", "Enter the key (integer):", minvalue=0, maxvalue=255)
        if key is not None:
            operate(key)

    root.mainloop()

if __name__ == "__main__":
    main()

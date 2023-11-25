from tkinter import *
from tkinter import filedialog

# GUI Instance
root = Tk()

# window size
root.geometry("200x160")

def encrypt_image():
    # 'r' to extract data
    file1 = filedialog.askopenfile(mode='r', filetypes=[('image files', '.png .jpg .jpeg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END)      # takes the key from user
        fi = open(file_name, 'rb')      # opens the file in binary read mode
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)     # XOR Operation
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()

def decrypt_image():
    # 'r' to extract data
    file1 = filedialog.askopenfile(mode='r', filetypes=[('image files', '.png .jpg .jpeg')])
    if file1 is not None:
        file_name = file1.name
        key = entry1.get(1.0, END)
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, value in enumerate(image):
            image[index] = value ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()

# Create buttons for encryption and decryption
encrypt_button = Button(root, text="Encrypt", command=encrypt_image)
decrypt_button = Button(root, text="Decrypt", command=decrypt_image)

# Position the buttons
encrypt_button.place(x=30, y=10)
decrypt_button.place(x=110, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=65, y=60)

root.mainloop()
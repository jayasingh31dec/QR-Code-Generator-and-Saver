from tkinter import *
from tkinter import filedialog

import qrcode as qr
from PIL import ImageTk


def generate_qr():
    link = Useridvalue.get()
    img = qr.make(link)
    img = img.resize((300, 300))  # Resize the image for better display
    img_tk = ImageTk.PhotoImage(img)

    # Display the image in a new window
    qr_window = Toplevel(root)
    qr_window.title("Generated QR Code")
    qr_label = Label(qr_window, image=img_tk)
    qr_label.pack()

    # Keep a reference to the image to prevent it from being garbage collected
    qr_label.image = img_tk

    print("QR Code generated successfully for:", link)


def save_qr():
    link = Useridvalue.get()
    img = qr.make(link)
    img = img.resize((300, 300))  # Resize the image for better display
    filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if filename:
        img.save(filename)
        print("QR Code saved successfully as:", filename)


root = Tk()
root.geometry("500x300")
root.title("QR Code Registration Form")

# Labels
Label(root, text="QR Code Registration Form", font="Arial 15 bold").grid(row=0, column=3)
Label(root, text="User Link:").grid(row=1, column=2)

# Entry fields
Useridvalue = StringVar()
Useridentry = Entry(root, textvariable=Useridvalue)
Useridentry.grid(row=1, column=3)

# Submit button
Button(root, text="Generate QR Code", command=generate_qr).grid(row=2, column=2)

# Save button
Button(root, text="Save QR Code", command=save_qr).grid(row=2, column=3)

root.mainloop()


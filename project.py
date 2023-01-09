from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog
import os
import sys
root = Tk()
root.title("Image Viewer")
root.geometry("650x650") 
root.configure (background="sky blue")
title_label = Label(root, text="Image Viewer", font=("Verdana", 40, "bold"),bg="red",fg="white", borderwidth=5, relief=SOLID,width=65 )
title_label.pack() 
copyright_label = Label(root, text="Developed in Python By Rudraksh", font=("Castellar", 24, "bold"),fg="white",bg="black")
copyright_label.place(relx=0.5, rely= 0.94, anchor=CENTER)
img_path = ""
def openImage():
    global img_path
    img_path= filedialog.askopenfilename(title="Open Image File", filetypes=[("Image Files","*.jpg")])
    print(img_path)
    img_path= os.path.basename(img_path) 
    theImage = ImageTk.PhotoImage(Image.open(img_path))
    image_place["image"] = theImage
    
def rotate_image():
    global img_path
    print(img_path) 
    im = Image.open(img_path)
    rotated_img= im.rotate(180) 
    img = ImageTk.PhotoImage(rotated_img)
    image_place['image'] = img
    img.close()
   
    

btn_rotate =  Button(root, text="Rotate Image", relief = FLAT, bg="gray", fg="white", font=("Verdana", 18, "bold"), command = rotate_image) 
btn_rotate.place(relx= 0.8, rely= 0.4, anchor= CENTER)
image_place = Label(root, relief = FLAT) 
image_place.place(relx= 0.5, rely= 0.5, anchor=CENTER)
btn_open = Button(root, text="Open Image", relief =FLAT,bg="gray",fg="white", font=("Verdana", 18, "bold"), command =openImage) 
btn_open.place(relx= 0.2, rely =0.4, anchor=CENTER)
#Run Statement
root.mainloop()
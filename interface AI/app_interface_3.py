from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
import cv2 as cv 
import numpy as np
import tumor_detection_code_vscode as my

win= Tk()
win.geometry("1600x840")
win.resizable(False,False)
win.title("parham tumor detection")
win.resizable= False
bg=Image.open("bg.png")
resized=bg.resize((2120,1100))
can=Canvas(win,width=2000,height=2000,bg="red")
can.place(x=0,y=0)
pic=ImageTk.PhotoImage(resized)
can.create_image(540,300,image=pic)
imlabel=Label()



text_file=""

def scan():
    global yes_label, no_label,er_label
    if text_file=="":
      er_label=Label(text="no image selected",width=22,height=2,bg="red",fg="white",font=("hellvetica",20)) 
      er_label.place(x=650,y=500) 
    
    else:
        g_1=my.predict_on_custome_image(text_file)
        value=list(g_1.values())
        print(value)
        if value==['have tumor']:
            yes_label=Label(text="tumor has been detected!",width=22,height=2,bg="red",fg="white",font=("hellvetica",20))
            yes_label.place(x=650,y=500)

    
        else:
            no_label=Label(text="tumor has not been detected!",width=22,height=2,bg="green",fg="white",font=("hellvetica",20))
            no_label.place(x=650,y=500)


def open_file():
    global text_file,im,width,height,imge
    mult=0
    x=0
    y=0
    try:
        er_label.destroy()
        no_label.destroy()
        yes_label.destroy()

    except:
        pass
    text_file= filedialog.askopenfilename(title="Choose an Image",filetypes=(("Png files","*.png"),("Jpg Files","*.jpg"),("All files","*.*")))

    img=cv.imread(text_file,0)
    img=cv.resize(img,(100,100))
    im = Image.fromarray(img)
    try:
        left.destroy()
        right.destroy()
    except:
        pass
    imge=ImageTk.PhotoImage(image=im)
    imlabel.configure(image=imge)
    imlabel.pack()
    # except:
    #     pass
    print(text_file)
    
def forward():
    global x,imlabel,im,imge,text_file,ind,er_label,no_label,yes_label
    try:

        no_label.destroy()


    except:
        pass
    try:

        no_label.destroy()
        yes_label.destroy()

    except:
        pass
    try:
        er_label.destroy()

    except:
        pass
    if ind> list_len-2:
        pass
    if ind>list_len-3:
        right.configure(state=DISABLED)
        print(ind)
        ind=ind+1
        text_file=image_dir[ind]
        img=cv.imread(text_file,0)
        img=cv.resize(img,(100,100))
        im = Image.fromarray(img)
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
        left.configure(state=NORMAL)
        try:
            er_label.destroy()
            no_label.destroy()
            yes_label.destroy()

        except:
            pass
            
    else:
        print(ind)
        ind=ind+1
        text_file=image_dir[ind]
        img=cv.imread(text_file,0)
        img=cv.resize(img,(100,100))
        im = Image.fromarray(img)
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
        left.configure(state=NORMAL)
        try:
            er_label.destroy()
            no_label.destroy()
            yes_label.destroy()

        except:
            pass
    

def back():
    global x,ind,imlabel,im,imge,text_file
    try:

        no_label.destroy()


    except:
        pass
    try:

        
        yes_label.destroy()

    except:
        pass
    try:
        er_label.destroy()

    except:
        pass
    if ind==1:
        left.configure(state=DISABLED)
        ind=ind-1
        text_file=image_dir[ind]
        img=cv.imread(text_file,0)
        img=cv.resize(img,(100,100))
        im = Image.fromarray(img)
        imge=ImageTk.PhotoImage(im)
        # imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
        try:
            er_label.destroy()
            no_label.destroy()
            yes_label.destroy()

        except:
            pass
    else:
        ind=ind-1
        text_file=image_dir[ind]
        img=cv.imread(text_file,0)
        img=cv.resize(img,(100,100))
        im = Image.fromarray(img)
        imge=ImageTk.PhotoImage(im)

        imlabel.configure(image=imge)
        imlabel.pack()
        right.configure(state=NORMAL)
        try:
            er_label.destroy()
            no_label.destroy()
            yes_label.destroy()

        except:
            pass
def folder():
    global text_file,im,width,height,imge,x,right,left,ind,image_dir,list_len
    image_dir=[]
    dir= filedialog.askdirectory(title="Choose a folder")
    try:
        for i in os.listdir(dir):
            if "jpeg"in i:
                image_dir.append(f"{dir}/{i}")
        for i in os.listdir(dir):
            if "jpg"in i:
                image_dir.append(f"{dir}/{i}")
        for i in os.listdir(dir):
            if "png"in i:
                image_dir.append(f"{dir}/{i}")
        list_len=len(image_dir)
        ind=0
        text_file=image_dir[0]
        print(text_file)
        img=cv.imread(text_file,0)
        img=cv.resize(img,(100,100))
        im = Image.fromarray(img)
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
        left=Button(text="<<",width=5,height=3,bg="#07011E",font=("helvetica",10),fg="white",command=back,state=DISABLED)
        left.place(x=0,y=400)
        right=Button(text=">>",width=5,height=3,bg="#07011E",font=("helvetica",10),fg="white",command=forward)
        right.place(x=1540,y=400)

    except:
        pass


scan=Button(text="Scan",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=scan)
scan.place(x=950,y=600)

open_i=Button(text="Select Image",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=open_file)
open_i.place(x=150,y=550)

open_f=Button(text="Select folder",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=folder)
open_f.place(x=150,y=700)


mainloop()
from tkinter import *
from tkinter import ttk
import os
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import messagebox
import cv2 as cv 
import history.tumor_detection_code_vscode as my

win= Tk()
win.geometry("1600x840")
win.resizable(False,False)
win.title("bank")
win.resizable= False
bg=Image.open("bg.png")
resized=bg.resize((2120,1100))
can=Canvas(win,width=2000,height=2000,bg="red")
can.place(x=0,y=0)
pic=ImageTk.PhotoImage(resized)
can.create_image(540,300,image=pic)
imlabel=Label()

flag=True


def scan():
    global yes_label, no_label
    g_1=my.predict_on_custome_image(text_file)
    
    if g_1=='have tumor':
        yes_label=Label(text="Yes",width=10,height=2,bg="green",fg="white",font=("hellvetica",20))
        yes_label.place(x=700,y=500)

    #else
    else:
        no_label=Label(text="No",width=10,height=2,bg="green",fg="white",font=("hellvetica",20))
        no_label.place(x=700,y=500)


def open_file():
    global text_file,im,width,height,imge
    mult=0
    x=0
    y=0
    try:
        no_label.destroy()
        yes_label.destroy()
    except:
        pass
    text_file= filedialog.askopenfilename(title="Choose an Image",filetypes=(("Png files","*.png"),("Jpg Files","*.jpg"),("All files","*.*")))
    #دایرکتوری عسک
    try:
        im = Image.open(text_file)
        width, height = im.size
        try:
            left.destroy()
            right.destroy()
        except:
            pass
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
    except:
        pass
    print(text_file)
    
def forward():
    global x,imlabel,im,imge,text_file,ind
    if ind> list_len-2:
        pass
    if ind>list_len-3:
        right.configure(state=DISABLED)
        print(ind)
        ind=ind+1
        text_file=image_dir[ind]
        im = Image.open(image_dir[ind])
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
        left.configure(state=NORMAL)
    else:
        print(ind)
        ind=ind+1
        text_file=image_dir[ind]
        im = Image.open(image_dir[ind])
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
        left.configure(state=NORMAL)

def back():
    global x,ind,imlabel,im,imge,text_file
    if ind==1:
        left.configure(state=DISABLED)
        ind=ind-1
        text_file=image_dir[ind]
        im = Image.open(image_dir[ind])
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
    else:
        ind=ind-1
        text_file=image_dir[ind]
        im = Image.open(image_dir[ind])
        imge=ImageTk.PhotoImage(im)
        imlabel.configure(image=imge)
        imlabel.pack()
        right.configure(state=NORMAL)
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
    except:
        pass
    # im = Image.open(image_dir[0])
    # imge=ImageTk.PhotoImage(im)
    # imlabel.configure(image=imge)
    # imlabel.pack()
    # left=Button(text="<<",width=5,height=3,bg="#07011E",font=("helvetica",10),fg="white",command=back,state=DISABLED)
    # left.place(x=0,y=400)
    # right=Button(text=">>",width=5,height=3,bg="#07011E",font=("helvetica",10),fg="white",command=forward)
    # right.place(x=1540,y=400)

scan=Button(text="Scan",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=scan)
scan.place(x=950,y=600)

open_i=Button(text="Select Image",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=open_file)
open_i.place(x=150,y=550)

open_f=Button(text="Select folder",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=folder)
open_f.place(x=150,y=700)


mainloop()
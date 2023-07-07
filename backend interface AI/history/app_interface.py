from tkinter import * 
from tkinter import ttk 
import os 
from PIL import ImageTk,Image 
from tkinter import filedialog 
from tkinter import messagebox 
 
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
 
def scan(): 
    response=messagebox.askyesno("Are you sure?","Are you sure?") 
    #وقتی اسکن میزنن یه پاپ اپ باز میشه یا کیزنی اره یا نه 
    if response== True: 
        pass 
    #اگه اره گفته باشه 
 
    if response== False: 
        pass 
        #اگه نه گفته باشه 
def open_file(): 
    global text_file,im,width,height,imge 
    mult=0 
    x=0 
    y=0 
    text_file= filedialog.askopenfilename(title="Choose an Image",filetypes=(("Png files","*.png"),("Jpg Files","*.jpg"),("All files","*.*"))) 
    #دایرکتوری عسک 
    im = Image.open(text_file) 
    print(type(im))
    width, height = im.size 
    try: 
        left.destroy() 
        right.destroy() 
    except: 
        pass 
    imge=ImageTk.PhotoImage(im) 
    imlabel.configure(image=imge) 
    imlabel.pack() 
     
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
        print(type(im))
        imge=ImageTk.PhotoImage(im) 
        imlabel.configure(image=imge) 
        imlabel.pack() 
        left.configure(state=NORMAL) 
    else: 
        print(ind) 
        ind=ind+1 
        text_file=image_dir[ind] 
        im = Image.open(image_dir[ind]) 
        print(type(im))
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
    im = Image.open(image_dir[0]) 
    imge=ImageTk.PhotoImage(im) 
    imlabel.configure(image=imge) 
    imlabel.pack() 
    left=Button(text="<<",width=5,height=3,bg="#07011E",font=("helvetica",10),fg="white",command=back,state=DISABLED) 
    left.place(x=0,y=400) 
    right=Button(text=">>",width=5,height=3,bg="#07011E",font=("helvetica",10),fg="white",command=forward) 
    right.place(x=1540,y=400) 
 
scan=Button(text="Scan",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=scan) 
scan.place(x=950,y=600) 
 
open_i=Button(text="Select Image",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=open_file) 
open_i.place(x=150,y=550) 
 
open_f=Button(text="Select folder",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=folder) 
open_f.place(x=150,y=700) 
 
 
mainloop()
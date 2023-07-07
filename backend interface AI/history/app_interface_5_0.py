from tkinter import *
import os
from PIL import ImageTk,Image
from tkinter import filedialog
import backend_code_interface_vscode as bci
import cv2 as cv 
win= Tk()
win.geometry("1600x840")
win.resizable(False,False)
win.title("Tumor Detection App")
win.resizable= False
bg=Image.open("bg.png")
resized=bg.resize((2120,1100))
can=Canvas(win,width=2000,height=2000,bg="red")
can.place(x=0,y=0)
pic=ImageTk.PhotoImage(resized)
can.create_image(540,300,image=pic)
imlabel=Label()
flag=True
text_file=""
pimage=""
def chat():
    root = Tk()
    root.configure(bg="#07011E")
    root.title("Chatbot")
    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#07011E"
    TEXT_COLOR = "#EAECEE"
    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"
    answer=''
    # Send function
    def send(*args):
        txt.configure(state=NORMAL)
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)
        user_q = e.get().lower()
        #user_q سوالیه که یوزر میپرسه


        #answer جوابیه که چت جی پی تی میده

        txt.insert(END, "\n" + "Bot -> " +str(answer))

        e.delete(0, END)
        txt.configure(state=DISABLED)
    root.bind('<Return>', send)
    
    lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)
    
    txt = Text(root, bg="#07011E", fg=TEXT_COLOR, font=FONT, width=60,state=DISABLED)
    txt.grid(row=1, column=0, columnspan=2)
    
    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    
    e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)
    
    send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                command=send).grid(row=2, column=1)
    
    root.mainloop()




def scan():
    global yes_label, no_label,er_label ,pimage
    if text_file=="":
      er_label=Label(text="no image selected",width=17,height=2,bg="red",fg="white",font=("hellvetica",20)) 
      er_label.place(x=700,y=500) 
    
    else:
        g_1=bci.predict_on_custome_image(text_file)
        value=list(g_1.values())
        # print(value)
        if value==['Tumor Detected']:
            g_2=bci.combine_pred_original(text_file)
            im = Image.fromarray(g_2)
            # print(g_2.shape)
            im = ImageTk.PhotoImage(im)
            pimage=im
            imlabel.configure(image=pimage)
            yes_label=Label(text="Tumor Detected !",width=17,height=2,bg="red",fg="white",font=("hellvetica",20))
            yes_label.place(x=650,y=600)

        else:
            no_label=Label(text="Tumor not Detected",width=17,height=2,bg="green",fg="white",font=("hellvetica",20))
            no_label.place(x=650,y=600)


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

    img=cv.imread(text_file)
    img=cv.resize(img,(512,512),interpolation=cv.INTER_CUBIC)
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
        img=cv.imread(text_file)
        img=cv.resize(img,(512,512),interpolation=cv.INTER_CUBIC)
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
        img=cv.imread(text_file)
        img=cv.resize(img,(512,512),interpolation=cv.INTER_CUBIC)
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
        img=cv.imread(text_file)
        img=cv.resize(img,(512,512),interpolation=cv.INTER_CUBIC)
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
        img=cv.imread(text_file)
        img=cv.resize(img,(512,512),interpolation=cv.INTER_CUBIC)
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
        img=cv.imread(text_file)
        img=cv.resize(img,(512,512))
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
scan.place(x=950,y=550)

chat_b=Button(text="chat with AI Doctor",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=chat)
chat_b.place(x=950,y=700)

open_i=Button(text="Select Image",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=open_file)
open_i.place(x=150,y=550)

open_f=Button(text="Select folder",width=30,height=3,bg="#07011E",font=("helvetica",20),fg="white",command=folder)
open_f.place(x=150,y=700)


mainloop()
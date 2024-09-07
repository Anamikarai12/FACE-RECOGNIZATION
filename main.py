from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first img
        img1=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (2).jfif")
        img1=img1.resize((400,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=400,height=100)

        #second img
        img2=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (3).jfif")
        img2=img2.resize((600,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=400,y=0,width=600,height=100)

        #third img
        img4=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (2).jfif")
        img4=img4.resize((400,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=1000,y=0,width=400,height=100)


        #background img
        img3=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (5).jfif")
        img3=img3.resize((1400,810),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1400,height=810)

        title_lbl=Label(bg_img,text="Face Recognition Attendance System Software",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        #student button
        img5=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (6).jfif")
        img5=img5.resize((220,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=100,y=70,width=220,height=200)

        b1_1=Button(bg_img,text="Student Details" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=100,y=270,width=220,height=40)

        #Detact button
        img6=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (1).jfif")
        img6=img6.resize((220,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=400,y=70,width=220,height=200)

        b1_1=Button(bg_img,text="Face Detactor" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=400,y=270,width=220,height=40)

        #Attendance button
        img7=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (7).jfif")
        img7=img7.resize((220,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=700,y=70,width=220,height=200)

        b1_1=Button(bg_img,text="Attendance" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=700,y=270,width=220,height=40)

        #Help Desk button
        img8=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\download.jfif")
        img8=img8.resize((220,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=1000,y=70,width=220,height=200)

        b1_1=Button(bg_img,text="Help Desk" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=1000,y=270,width=220,height=40)

        #Train data button
        img9=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (4).jfif")
        img9=img9.resize((220,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=100,y=330,width=220,height=200)

        b1_1=Button(bg_img,text="Train Data" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=100,y=530,width=220,height=40)

        #Photos button
        img10=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\download (1).jfif")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=400,y=330,width=220,height=220)

        b1_1=Button(bg_img,text="Photos" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=400,y=530,width=220,height=40)

        #Developer button
        img11=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (9).jfif")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=700,y=330,width=220,height=220)

        b1_1=Button(bg_img,text="Developer" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=700,y=530,width=220,height=40)

        #Exit button
        img12=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (8).jfif")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2")
        b1.place(x=1000,y=330,width=220,height=220)

        b1_1=Button(bg_img,text="Exit" ,cursor="hand2",font=("times new roman",15,"bold"),bg="orange", fg="darkblue")
        b1_1.place(x=1000,y=530,width=220,height=40)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()

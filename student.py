from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first img
        img1=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (10).jfif")
        img1=img1.resize((500,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=100)

        #second img
        img2=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\a.jpg")
        img2=img2.resize((500,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=100)

        #third img
        img4=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\download (3).jfif")
        img4=img4.resize((500,100),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=1000,y=0,width=500,height=100)


        #background img
        img3=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (5).jfif")
        img3=img3.resize((1400,810),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1400,height=810)

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=3,y=45,width=1348,height=535)

        #left label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        left_frame.place(x=5,y=5,width=660,height=520)

        img_left=Image.open(r"C:\Users\Varun\OneDrive\Desktop\FACERECOGNIZATION\FACE-RECOGNIZATION\College_images\OIP (11).jfif")
        img_left=img_left.resize((650,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=650,height=100)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information", font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=110,width=650,height=220)

        #Department
        dep_label=Label(current_course_frame,text="Department", bg="white",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame, font=("times new roman",12,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","CSD","CSE","EC","ME","AIML")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course", bg="white",font=("times new roman",12,"bold"))
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame, font=("times new roman",12,"bold"),state="readonly",width=17)
        course_combo["values"]=("Select Course","SE","TE","BE","FE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year", bg="white",font=("times new roman",12,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame, font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        sem_label=Label(current_course_frame,text="Semester", bg="white",font=("times new roman",12,"bold"))
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame, font=("times new roman",12,"bold"),state="readonly",width=17)
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # right label frame

        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details", font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=5,width=660,height=520)















if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
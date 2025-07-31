
from tkinter import Tk
import tkinter as tk
from operations.students_crud import StudentCrud


class StudentPage:
    is_opened = False
    
    def __init__(self):
        if StudentPage.is_opened:
            return
        st_root = tk.Toplevel()
        st_root.geometry("700x500")
        st_root.title("Hostel Student Add Page")
        self.root=st_root
        StudentPage.is_opened=True
        
        # Reset flag when window is closed
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.Title_Frame=tk.Frame(self.root,background="yellow")
        self.Title_Frame.pack(fill="x")
        
        title_label=tk.Label(self.Title_Frame,text="Hostel Management System",height=2,background="yellow",font=("Arial",16,"bold"))
        title_label.pack(fill="x")

        self.Form_Frame=tk.Frame(self.root,background="cyan",width=250,bd=2,relief="groove")
        self.Form_Frame.pack(side="left",fill="y",expand=False)
        self.Form_Frame.pack_propagate(0)

                # Student Name
        tk.Label(self.Form_Frame, text="Student Name:", background="cyan", anchor="w").pack(fill="x", padx=10, pady=(10, 0))
        self.st_name = tk.Entry(self.Form_Frame)
        self.st_name.pack(fill="x", padx=10, pady=2)

        # Age
        tk.Label(self.Form_Frame, text="Age:", background="cyan", anchor="w").pack(fill="x", padx=10, pady=(10, 0))
        self.st_age = tk.Entry(self.Form_Frame)
        self.st_age.pack(fill="x", padx=10, pady=2)

        # Date of Birth
        tk.Label(self.Form_Frame, text="Date of Birth (DOB):", background="cyan", anchor="w").pack(fill="x", padx=10, pady=(10, 0))
        self.st_dob = tk.Entry(self.Form_Frame)
        self.st_dob.pack(fill="x", padx=10, pady=2)

        # Parent Contact Number
        tk.Label(self.Form_Frame, text="Parent Contact No:", background="cyan", anchor="w").pack(fill="x", padx=10, pady=(10, 0))
        self.st_parent = tk.Entry(self.Form_Frame)
        self.st_parent.pack(fill="x", padx=10, pady=2)

        #add button
        tk.Button(self.Form_Frame,text="Add Student",command=lambda : StudentCrud(student_name=self.st_name.get(),student_age=self.st_age.get(),student_dob=self.st_dob.get(),parents_number=self.st_parent.get()).add_student()).pack(fill="x",padx=10,pady=(30,1))
        tk.Button(self.Form_Frame,text="Edit Student",).pack(fill="x",padx=10,pady=1)
        tk.Button(self.Form_Frame,text="Delete Student").pack(fill="x",padx=10,pady=1)
        tk.Button(self.Form_Frame,text="Show Student").pack(fill="x",padx=10,pady=1)
    def on_close(self):
        """Handle window closing event to reset the open flag"""
        StudentPage.is_opened = False
        self.root.destroy()
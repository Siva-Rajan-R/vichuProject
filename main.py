import tkinter as tk
from ui.student import StudentPage


root=tk.Tk()
root.title("Hostel Management System")
root.geometry("700x500")

class HomePage:
    def __init__(self,root:tk.Tk):
        self.root=root
        
        self.Title_Frame=tk.Frame(self.root,background="yellow")
        self.Title_Frame.pack(fill="x")
        
        
        title=tk.Label(self.Title_Frame,text="Hostel Management System",font=("Arial",16,"bold"),background="yellow",height=2)
        title.pack(fill="x")
        
        self.Button_Frame=tk.Frame(self.root)
        self.Button_Frame.pack(pady=30)
        tk.Button(self.Button_Frame,text="Add Hostel Students",width=20,command=StudentPage).grid(row=1,column=0,pady=5,padx=10)
        tk.Button(self.Button_Frame,text="Show students",width=20).grid(row=1,column=1,pady=5)
        tk.Button(self.Button_Frame,text="Add Food Menus",width=20).grid(row=3,column=0,pady=5)
        tk.Button(self.Button_Frame,text="Show Food Menus",width=20).grid(row=3,column=1,pady=5)

HomePage(root=root)
root.mainloop()




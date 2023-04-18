from tkinter import *
from tkinter import ttk

def main():
    app=Tk()
    ob=LoginPage(app)
    app.mainloop()
class LoginPage:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750")
        self.win.title("Pharmacy Manegment System | Login")

        self.title_lbl=Label(self.win,text="Pharmacy Manegement System",bg='brown',fg="yellow",bd=8,relief=GROOVE,font=('arial',30,"bold"))
        self.title_lbl.pack(side=TOP,fill=X)

        self.login_lbl=Label(self.win,text="login",bg="blue",fg='yellow',bd='8',relief=GROOVE,font=('arial',30,"bold"))
        self.login_lbl.pack(side=TOP,fill=X)

        self.main_frame=Frame(self.win,bg="lightgrey",bd=10,relief=RIDGE)
        self.main_frame.place(x=335,y=185,width=725,height=470)

        self.entry_frame=LabelFrame(self.main_frame,text="enter details",bg="lightgrey",bd=8,relief=RIDGE)
        self.entry_frame.pack(side=TOP,fill=BOTH)

        self.username_lbl=Label(self.entry_frame,text='username:',font=('arial',15),bg='lightgrey',anchor=CENTER)
        self.username_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.username_ent=Entry(self.entry_frame,border=9,textvariable=None,font=('arial',15))
        self.username_ent.grid(row=0,column=1,padx=2,pady=2)

        self.password_lbl=Label(self.entry_frame,text="password:",bg="lightgrey",font=('arial',15),anchor=CENTER)
        self.password_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.password_ent=Entry(self.entry_frame,border=9,textvariable=None,font=('arial',15),show="*")
        self.password_ent.grid(row=1,column=1,padx=2,pady=2)

        self.false_frame1=Frame(self.entry_frame,bd=0,bg="lightgrey")

        self.button_frame=LabelFrame(self.main_frame,text="options",bg="lightgrey",bd=8,relief=RIDGE,font=("arial",18))
        self.button_frame.pack(side=TOP,fill=BOTH)



if __name__=="__main__":
    main()
        



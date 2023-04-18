from tkinter import *
import sqlite3
class addpatient:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root,height=800,width=1000,bg='pink')
        self.f.propagate(0)
        self.lname=Label(self.f,text='Enter Name:',font=('roman',20,'bold'))
        self.lcost=Label(self.f,text='Enter Age :',font=('roman',20,'bold'))
        self.lnomed=Label(self.f,text='Enter disease :',font=('roman',20,'bold'))
        self.lname.place(x=100,y=100)
        self.lcost.place(x=100,y=200)
        self.lnomed.place(x=100,y=300)
        self.ename=Entry(self.f,font=('arial',20,'bold'),width=20)
        self.eage=Entry(self.f,font=('arial',20,'bold'),width=20)
        self.ediesease=Entry(self.f,font=('arial',20,'bold'),width=20)
        self.f.pack()
        self.ename.place(x=500,y=100)
        self.eage.place(x=500,y=200)
        self.ediesease.place(x=500,y=300)
        self.bclose=Button(self.f,font=('arial',20,'bold'),height=1,width=8,text='close',fg='red')
        self.bnext=Button(self.f,font=('arial',20,'bold'),height=1,width=8,text='next',fg='green')
        self.bclose.bind('<Button-1>',self.addpdetailsclose)
        self.bnext.bind('<Button-1>',self.addpdetails)
        self.bclose.place(x=200,y=500)
        self.bnext.place(x=500,y=500)

    def addpdetails(self,event):
        self.conn=sqlite3.connect('pharmacy.db')
        pname=self.ename.get()
        page=self.eage.get()
        pdiesease=self.ediesease.get()
        if pname=='' or page=='' or pdiesease=='':
            return
        q=f"insert into pdetails values('{pname}',{page},'{pdiesease}')"
        self.conn.commit()
        print(q)
        self.conn.executescript(q)
        print('added new patient')
        self.conn.close()
        self.eage.delete(0,END)
        self.ename.delete(0,END)
        self.ediesease.delete(0,END)

    def addpdetailsclose(self,event):
        self.addpdetails(event)
        self.root.destroy()
        
r=Tk()
c=addpatient(r)
r.mainloop()
from tkinter import *
import sqlite3
class createmed:
    def __init__(self,root):
        self.root=root
        self.f=Frame(root,height=800,width=1000,bg='pink')
        self.f.propagate(0)
        self.lname=Label(self.f,text='enter new medicine name :',font=('roman',20,'bold'))
        self.lcost=Label(self.f,text='enter the cost of medicine :',font=('roman',20,'bold'))
        self.lnomed=Label(self.f,text='enter the no of medicines :',font=('roman',20,'bold'))
        self.lname.place(x=100,y=100)
        self.lcost.place(x=100,y=200)
        self.lnomed.place(x=100,y=300)
        self.ename=Entry(self.f,font=('arial',20,'bold'),width=20)
        self.ecost=Entry(self.f,font=('arial',20,'bold'),width=20)
        self.enomed=Entry(self.f,font=('arial',20,'bold'),width=20)
        self.f.pack()
        self.ename.place(x=500,y=100)
        self.ecost.place(x=500,y=200)
        self.enomed.place(x=500,y=300)
        self.bsub=Button(self.f,font=('arial',20,'bold'),height=1,width=8,text='submit',fg='red')
        self.bnext=Button(self.f,font=('arial',20,'bold'),height=1,width=8,text='NewEntry',fg='green')
        self.bp=Button(self.f,font=('arial',20,'bold'),height=1,width=8,text='AddPaitent',fg='green')
        

        self.bsub.bind('<Button-1>',self.addmedicineclose)        
        self.bp.bind('<Button-1>',self.addpatient)        

        self.bnext.bind('<Button-1>',self.addmedicine)
        self.bsub.place(x=200,y=500)
        self.bnext.place(x=400,y=500)
        self.bp.place(x=600,y=500)


    def addmedicine(self,event):
        self.conn=sqlite3.connect('pharmacy.db')
        mname=self.ename.get()
        mcost=self.ecost.get()
        nomed=self.enomed.get()
        if mname=='' or mcost=='' or nomed=='':
            return
        q=f"insert into medicines values('{mname}',{mcost},{nomed})"
        self.conn.commit()
        print(q)
        self.conn.executescript(q)
        print('added new medicine')
        self.conn.close()
        self.ecost.delete(0,END)
        self.ename.delete(0,END)
        self.enomed.delete(0,END)

    def addmedicineclose(self,event):
        self.addmedicine(event)
        self.root.destroy()
        

    def addpatient(self,event):
        import paitentdetails.py
r=Tk()
c=createmed(r)
r.mainloop()
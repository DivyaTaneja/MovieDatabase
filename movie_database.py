from tkinter import *
from tkinter import messagebox
import os
f=open("movie_database",'a+')
m = Tk()
m.configure(background='black')
abcde=-1


def add():
    global abcde
    no_lines = 0
    with open("movie_database", 'r') as f12:
        for line in f12:
            no_lines += 1
    abcde=no_lines-1
    e1= ent1.get()
    e2=ent2.get()
    e3=ent3.get()
    e4=ent4.get()
    e5=ent5.get()
    e6=ent6.get()
    e7=ent7.get()
    f.write('{0} {1} {2} {3} {4} {5} {6}\n'.format(str(e1),e2,str(e3),str(e4),str(e5),e6,str(e7)))
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent4.delete(0, END)
    ent3.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)


def delete():
    e1=ent1.get()
    with open(r"movie_database") as f, open(r"movie_database1", "w") as running:
        for line in f:
            if str(e1) not in line:
                running.write(line)
    os.remove(r"movie_database")
    os.rename(r"movie_database1", r"movie_database")
    f.close()
    running.close()
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent4.delete(0, END)
    ent3.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)

def to_first():
    global abcde
    abcde=0
    f.seek(abcde)
    c=f.readline()
    jkl=list(c.split(" "))
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent4.delete(0, END)
    ent3.delete(0, END)
    ent5.delete(0, END)
    ent6.delete(0, END)
    ent7.delete(0, END)
    ent1.insert(0,str(jkl[0]))
    ent2.insert(0,str(jkl[1]))
    ent4.insert(0,str(jkl[3]))
    ent3.insert(0,str(jkl[2]))
    ent5.insert(0,str(jkl[4]))
    ent6.insert(0,str(jkl[5]))
    ent7.insert(0,str(jkl[6]))

def to_next():
    global abcde
    abcde = abcde + 1
    f.seek(abcde)
    try:
        c=f.readlines()
        xyz = c[abcde]
        jkl = list(xyz.split(" "))
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent4.delete(0, END)
        ent3.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)
        ent7.delete(0, END)
        ent1.insert(0, str(jkl[0]))
        ent2.insert(0, str(jkl[1]))
        ent4.insert(0, str(jkl[3]))
        ent3.insert(0, str(jkl[2]))
        ent5.insert(0, str(jkl[4]))
        ent6.insert(0,str(jkl[5]))
        ent7.insert(0,str(jkl[6]))
    except:
        messagebox.showinfo("Title", " SORRY NO RECORDS LEFT ")
def to_previous():
        global abcde
        abcde=abcde-1
        f.seek(abcde)
        try:
            z = f.readlines()
            xyz=z[abcde]
            jkl = list(xyz.split(" "))
            ent1.delete(0, END)
            ent2.delete(0, END)
            ent4.delete(0, END)
            ent3.delete(0, END)
            ent5.delete(0, END)
            ent6.delete(0, END)
            ent7.delete(0, END)
            ent1.insert(0, str(jkl[0]))
            ent2.insert(0, str(jkl[1]))
            ent4.insert(0, str(jkl[3]))
            ent3.insert(0, str(jkl[2]))
            ent5.insert(0, str(jkl[4]))
            ent6.insert(0,str(jkl[5]))
            ent7.insert(0,str(jkl[6]))
        except:
            messagebox.showinfo("Title", " SORRY NO RECORDS LEFT ")


def to_last():
    global abcde
    f4=open("movie_database",'r')
    x=f4.read().splitlines()
    lst= x[-1]
    no_lines = 0
    with open("movie_database", 'r') as f8:
        for line in f8:
            no_lines += 1
    abcde=no_lines-1
    print(lst)
    try:
        jkl = list(lst.split(" "))
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent4.delete(0, END)
        ent3.delete(0, END)
        ent5.delete(0, END)
        ent6.delete(0, END)
        ent7.delete(0, END)
        ent1.insert(0, str(jkl[0]))
        ent2.insert(0, str(jkl[1]))
        ent4.insert(0, str(jkl[3]))
        ent3.insert(0, str(jkl[2]))
        ent5.insert(0, str(jkl[4]))
        ent6.insert(0,str(jkl[5]))
        ent7.insert(0,str(jkl[6]))
    except:
        messagebox.showinfo("Title", " SORRY NO RECORDS LEFT ")


def update():

    e1 = ent1.get()
    e2 = ent2.get()
    e3 = ent3.get()
    e4 = ent4.get()
    e5 = ent5.get()
    e6 = ent6.get()
    e7 = ent7.get()
    with open(r"movie_database") as f1, open(r"movie_database1", "w") as running:
        for line in f1:
            if str(e1) not in line:
                running.write(line)
            else:
                running.write('{0} {1} {2} {3} {4} {5} {6}'.format(str(e1),e2,str(e3),str(e4),str(e5),e6,str(e7)))
    os.remove(r"movie_database")
    os.rename(r"movie_database1", r"movie_database")


def search():
    i=0
    e11 = ent1.get()
    with open(r"movie_database") as running:
        for line in running:
            i=i+1
            if str(e11) in line:
                break
        try:
            jkl = list(line.split(" "))
            ent1.delete(0, END)
            ent2.delete(0, END)
            ent4.delete(0, END)
            ent3.delete(0, END)
            ent5.delete(0, END)
            ent6.delete(0, END)
            ent7.delete(0, END)
            ent1.insert(0, str(jkl[0]))
            ent2.insert(0, str(jkl[1]))
            ent4.insert(0, str(jkl[3]))
            ent3.insert(0, str(jkl[2]))
            ent5.insert(0, str(jkl[4]))
            ent6.insert(0,str(jkl[5]))
            ent7.insert(0,str(jkl[6]))
        except:
            messagebox.showinfo("Title", "error end of file")
    running.close()


lbl0= Label(m,text="MOVIE DATABASE MANAGEMENT SYSTEM", font=("Algerian", 30))
lbl1=Label(m,text="MOVIE NAME", font=("Comic Sans MS", 12))
ent1=Entry(m , font=("Helvetica", 12))
lbl2=Label(m, text="DURATION", font=("Comic Sans MS", 12))
ent2= Entry(m, font=("Helvetica", 12))
lbl3=Label(m, text="LANGUAGE", font=("Comic Sans MS", 12))
ent3= Entry(m, font=("Helvetica", 12))
lbl4=Label(m, text="STAR CASTE", font=("Comic Sans MS", 12))
ent4= Entry(m, font=("Helvetica", 12))
lbl5=Label(m, text="GENRE", font=("Comic Sans MS", 12))
ent5= Entry(m, font=("Helvetica", 12))
lbl6=Label(m, text="RATING", font=("Comic Sans MS", 12))
ent6= Entry(m, font=("Helvetica", 12))
lbl7=Label(m, text="REVIEW", font=("Comic Sans MS", 12))
ent7= Entry(m, font=("Helvetica", 12))
b1= Button(m, text="ADD ITEM", bg="white", fg="black", width=20, font=("Comic Sans MS", 12), command=add)
b2= Button(m, text="DELETE ITEM", bg="white", fg="black", width =20, font=("Comic Sans MS", 12), command=delete)
b3= Button(m, text="<<" , bg="white", fg="black", width =20, font=("Comic Sans MS", 12), command=to_first)
b4= Button(m, text=">" , bg="white", fg="black", width =20, font=("Comic Sans MS", 12), command=to_next)
b5= Button(m, text="<", bg="white", fg="black", width =20, font=("Comic Sans MS", 12), command=to_previous)
b6= Button(m, text=">>", bg="white", fg="black", width =20, font=("Comic Sans MS", 12), command=to_last)
b7= Button(m, text="UPDATE ITEM", bg="white", fg="black", width =20, font=("Comic Sans MS", 12), command=update)
b8= Button(m, text="SEARCH ITEM", bg="white", fg="black", width =20, font=("Comic Sans MS", 12), command=search)
lbl0.grid(columnspan=6, padx=12, pady=12)
lbl1.grid(row=6,column=1, sticky=W, padx=12, pady=12)
lbl2.grid(row=7,column=1, sticky=W, padx=12, pady=12)
lbl3.grid(row=8,column=1, sticky=W, padx=12, pady=12)
lbl4.grid(row=9,column=1, sticky=W, padx=12, pady=12)
lbl5.grid(row=12,column=1, sticky=W, padx=12, pady=12)
lbl6.grid(row=11,column=1, sticky=W, padx=12, pady=12)
lbl7.grid(row=12,column=1, sticky=W, padx=12, pady=12)
ent1.grid(row=6,column=2, padx=12, pady=12)
ent2.grid(row=7,column=2, padx=12, pady=12)
ent3.grid(row=8,column=2, padx=12, pady=12)
ent4.grid(row=9,column=2, padx=12, pady=12)
ent5.grid(row=12,column=2, padx=12, pady=12)
ent6.grid(row=11,column=2, padx=12, pady=12)
ent7.grid(row=12,column=2, padx=12, pady=12)
b1.grid(row=14,column=0, padx=4, pady=12)
b2.grid(row=14,column=1, padx=4, pady=12)
b3.grid(row=13,column=0, padx=4, pady=12)
b4.grid(row=13,column=2, padx=4, pady=12)
b5.grid(row=13,column=1, padx=4, pady=12)
b6.grid(row=13,column=3, padx=4, pady=12)
b7.grid(row=14,column=2, padx=4, pady=12)
b8.grid(row=14,column=3, padx=4, pady=12)
m.mainloop()

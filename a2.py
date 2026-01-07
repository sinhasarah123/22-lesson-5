from tkinter import * 
from tkinter import messagebox 
from PIL import Image, ImageTk 
root = Tk()
root.title("Denomination Calculator")   
root.geometry("650x400")
root.configure(bg="lightblue")
upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
img = ImageTk.PhotoImage(upload)
lbl=Label(root,image=img,bg="lightblue")
lbl.place(x=180,y=20)
lbl2=Label(root, text="hello user welcome to Denomination Calculator",  bg="lightblue")
lbl2.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    msg=messagebox.showinfo ("alert","do u want to calculate the Denomination count ?")
    if msg=="ok":
        topwin()
    btn=Button(root, text="lets get started", command=msg, bg="brown", fg="white")
    btn.place(x=260,y=360)
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.geometry("400x400")
    top.configure(bg="lightgreen")
    lbl = Label(top, text="enetr the total amount", bg="lightgreen")
    entry=Entry(top)
    lbl2=Label(top, text="here are number of notes for each denomination", bg="lightgrey")
    l1=Label(top, text="2000", bg="lightpink")
    l2=Label(top, text="500", bg="lightpink")
    l3=Label(top, text="100", bg="lightpink")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculate():
        amount=int(entry.get())
        n2000=amount//2000
        amount=amount%2000
        n500=amount//500
        amount=amount%500
        n100=amount//100
        t1.insert(0,str(n2000))
        t2.insert(0,str(n500))
        t3.insert(0,str(n100))
    btn=Button(top, text="calculate", command=calculate, bg="brown", fg="white")
    lbl.pack(x=230,y=20)
    entry.pack(x=200,y=80)
    btn.pack(x=240,y=120)
    lbl2.pack(x=140,y=170)
    l1.pack(pady=5)
    t1.pack(pady=5)
    l2.pack(pady=5)
    t2.pack(pady=5)
    l3.pack(pady=5)
    t3.pack(pady=5)
    top.mainloop()
root.mainloop()
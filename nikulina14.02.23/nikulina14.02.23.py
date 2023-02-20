from logging import PlaceHolder
from msilib import RadioButtonGroup
from msilib.schema import RadioButton
from tkinter import *
from tkinter import ttk
k=0
def klikker(event):
    global k
    k+=1
    lbl.configure(text=k)
def klikker1(event):
    global k
    if k>0:
        k-=1
    lbl.configure(text=k)
def entry_to_label(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)
def valik():
    text=var.get()
    ent.insert(END,text)
def uus_aken(ind:int):
    def tab_valik(ind,int):
        uusaken.title(texts[ind])
    uusaken=Toplevel()
    tabs=ttk.Notebook(uusaken)
    texts=["Esimene","Teine","Kolmas","Neljas"]
    tab=[]
    for i in range(len(texts)):
        tab.append("tab"+str(i))
        tab[i]=Frame(tabs)
        tabs.add(tab[i],text=texts[i])
        tab[i].bind("<Button-1>",tab_valik)
    tabs.grid(row=0,column=0)
    tabs.select(ind)
    uusaken.title(texts[ind])
    uusaken.mainloop()



aken=Tk()
aken.title("Minu esimene aken")
aken.geometry("600x300")
m=Menu(aken)
aken.config(menu=m)
m1=Menu(m)
m.add_cascade(label="Kaardid",menu=m1)
m1.add_command(label="1.Kaart",accelerator="Command+A",command=lambda:uus_aken(0))
m1.add_command(label="2.Kaart",accelerator="Command+A",command=lambda:uus_aken(1))
m1.add_command(label="3.Kaart",accelerator="Command+A",command=lambda:uus_aken(2))
m1.add_command(label="4.Kaart",accelerator="Command+A",command=lambda:uus_aken(3))



lbl=Label(aken,
          text="...",
          font="Arial 20",
          fg="#61091c")

btn=Button(aken,text="Vajuta siia",font="Arial 20",fg="grey",bg="#752742",width=30,height=5,relief=GROOVE) #SUNKEN,RAISED
ent=Entry(aken,
          fg="black",
          bg="#c96d81",
          width=30,
          justify=CENTER)
var=IntVar() #StringVar()
r1=Radiobutton(aken,
               text="Esimene",
               fg="black",
               bg="#c96d81",
               width=20,
               variable=var,
               value=1,
               command=valik)
r2=Radiobutton(aken,
               text="Teine",
               fg="black",
               bg="#c96d81",
               width=20,
               variable=var,
               value=2,
               command=valik)

btn.bind("<Button-1>",klikker) #LKM
btn.bind("<Button-3>",klikker1) #PKM
ent.bind("<Return>",entry_to_label)#Enter
btn.pack()
lbl.pack()
ent.pack()
r1.pack(side=LEFT)
r2.pack(side=RIGHT)
aken.mainloop()


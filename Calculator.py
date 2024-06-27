from tkinter import *
root=Tk()
root.configure(bg="light grey") 
def click(event):
    global scval
    text=event.widget.cget("text")
    print(text)
    
    if text=="=":
        if screen.get().isdigit():
            value=int(scval.get())
        else:
            value=eval(screen.get())
        scval.set(value)
        screen.update()
    elif text=="C":
        scval.set("")
        screen.update()
    else:
        scval.set(scval.get() + text) 
        screen.update()
root.geometry("800x700")
scval=StringVar()
scval.set("")
screen=Entry(root,textvar=scval,font="lucida 25 bold",bg="white")
screen.pack(padx=30,pady=30,fill=X,ipadx=8)
f=Frame(root,bg="light grey")
#b=Button(f,text="9",font="lucida 25 bold",padx=28,pady=22)
#b.pack(side=LEFT,padx=18,pady=12)
#b.bind("<Button-1>",click)
#b=Button(f,text="8",font="lucida 25 bold",padx=28,pady=22)
#b.pack(side=LEFT,padx=18,pady=12)
#b.bind("<Button-1>",click)
#b=Button(f,text="7",font="lucida 25 bold",padx=28,pady=22)
#b.pack(side=LEFT,padx=18,pady=12)
#b.bind("<Button-1>",click)
for i in range(7,10):
    b=Button(f,text=str(i),font="lucida 25 bold",padx=28,pady=22,bg="white")
    b.pack(side=LEFT,padx=12,pady=5)
    b.bind("<Button-1>",click)
 
b=Button(f,text="+",font="lucida 25 bold",padx=28,pady=22,bg="yellow")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)

f.pack()
f=Frame(root,bg="light grey")
for i in range(4,7):
    b=Button(f,text=str(i),font="lucida 25 bold",padx=28,pady=22,bg="white")
    b.pack(side=LEFT,padx=13,pady=5)
    b.bind("<Button-1>",click)

b=Button(f,text="-",font="lucida 25 bold",padx=28,pady=22,bg="yellow")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="light grey")
for i in range(1,4):
    b=Button(f,text=str(i),font="lucida 25 bold",padx=28,pady=22,bg="white")
    b.pack(side=LEFT,padx=12.2,pady=5)
    b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 25 bold",padx=28,pady=22,bg="yellow")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
f.pack()
f=Frame(root,bg="light grey")  
b=Button(f,text="C",font="lucida 25 bold",padx=28,pady=22,bg="Red")
b.pack(side=LEFT,padx=3,pady=5)
b.bind("<Button-1>",click) 
b=Button(f,text="0",font="lucida 25 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 25 bold",padx=28,pady=22)
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)
b=Button(f,text="/",font="lucida 25 bold",padx=28,pady=22,bg="yellow")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",click)


f.pack()

f=Frame(root,bg="white")   
  
b=Button(f,text="=",font="lucida 25 bold",padx=180,pady=15,bg="light green")
b.pack(side=LEFT,padx=18,pady=2)
b.bind("<Button-1>",click)






f.pack()
root.mainloop()

from tkinter import *
import createEncoding
import runFaceid

root = Tk()
def run():
    runFaceid.runCamera()
def updatedb():
    createEncoding.update()

photo = PhotoImage(file="UIBG.png")
label0 = Label(root,image=photo)
#label1 = Label(root,text="Update Changes in Database")
button1 = Button(root,text="Update Database",fg="red", command=updatedb)
button2 = Button(root,text="Run Camera",bg="black",fg="white",command=run)

label0.grid(row=0,column=0)
button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
root.mainloop()
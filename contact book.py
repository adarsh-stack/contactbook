import random
from tkinter import *
from tkinter import messagebox
root =Tk()
root.geometry('800x400')
root.config(bg='#FFFDD0')
root.title("Your Personalised contact book")
root.resizable(0,0)
# cl= open('contactlist','+w')
contactlist=[]
Name=StringVar()
Number= StringVar()


f=Frame(root)
f.pack(side=RIGHT)

S=Scrollbar(f, orient=VERTICAL)
select= Listbox(f, yscrollcommand=S.set,font=('Bold',20),width=10, height=10,borderwidth=4, relief="groove")
S.config(command=select.yview())
S.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,fill=BOTH,expand=1)


def  Selected():
    print("Hello",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("Error","Please select the Name")
    else:
        return int(select.curselection()[0])

def addcontact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get(),Number.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("confirmation","successfully Added new contact")
    else:
        messagebox.showerror("Error", "please fille the information")


def update():
    if Name.get() and Number.get():
        contactlist[ Selected()]=[Name.get(), Number.get()]
        messagebox.showinfo("Confirmation ", "Successfully updated the contact")
        EntryReset()
        Select_set()
    elif not(Name.get())and not(Number.get()) and not(len(select.curselection())==0):
        messagebox.showerror("Error ", "Please fill in details")
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error"," Please selecct the name and nnumber")
        else:
            message1="""to load all information of \n selected row press load button"""
            messagebox.showerror('Error',message1)
def EntryReset():
	Name.set('')
	Number.set('')

def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0,END)
    for name, phone in contactlist:
        select.insert(END,name)
Select_set()

Label(root, text='Name', font=("Times",20),bg="SlateGray3").pack()
Entry(root, textvariable=Name,width=40, font=(10)).pack()
Label(root, text='Number', font=("Times",20), bg= "SlateGray3").pack()
Entry(root, textvariable=Number  , width=40, font=(10)).pack()

Button(root, text='Add', font= "Bold",bg='#e8c1c7' , command=addcontact).pack()
Button(root, text="Update ", font="Bold", bg='#e8c1c7', command=update).pack()
Button(root, text='Delete',font ="Bold", bg='#e8c1c7', command=Delete_Entry).pack()
Button(root, text='View', font="Bold", bg='#e8c1c7', command=VIEW).pack()
Button(root,text='Reset', font="Bold", bg='#e8c1c7',command=EntryReset).pack()
Radiobutton(root,text='Reset', font="Bold", bg='#e8c1c7',command=EntryReset).pack()
Button(root, text='Exit', font="Bold", bg='#e8c1c7', command=EXIT).pack()
root.mainloop()




















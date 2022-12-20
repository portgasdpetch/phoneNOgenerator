from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import csv

root = Tk()
root.title("Phone NO Generator")

prefixNumber = Label(root,text="เลขนำหน้า :",font=20).place(x=10,y=10)
requiredNumber = Label(root,text="เลขที่ต้องการ(คั่นด้วย space) :",font=20).place(x=160,y=10)
quantity = Label(root,text="จำนวนเบอร์ที่ต้องการสร้าง :",font=20).place(x=160,y=110)
numberPerCSV = Label(root,text="จำนวนเบอร์ต่อไฟล์ CSV :",font=20).place(x=160,y=210)

requiredNumberTxt=StringVar(value="0")
quantityTxt=IntVar()
numberPerCSVTxt=IntVar()
prefixNumberTxt=StringVar(value="060")

combo= ttk.Combobox(textvariable=prefixNumberTxt)
combo.place(x=95,y=10,width=60)
combo["values"] = ("060","061","062","063","064","065","066","067","068","069",
"080","081","082","083","084","085","086","087","088","089",
"090","091","092","093","094","095","096","097","098","099")

def is_int(a,b,c):
    if (b==IntVar() and c==IntVar()):
        b = int(b)
        c = int(b)
        print("Valid")
        return True
    else:
        print("Not an integer")
        return False

def Prefix():
    global prefix
    prefix = prefixNumberTxt.get()
    if (prefix==None):
        return ""

def RequiredNumber():
    requiredNumber = requiredNumberTextBox.get()
    if (requiredNumber==None):
        return ""
    StrRn = str(requiredNumber)
    global splitedRn
    splitedRn = StrRn.split()
    return splitedRn

def NumberQuantity():
    global numberQuantity
    numberQuantity = quantityTextBox.get()
    return numberQuantity

def NumberPerCSV():
    global numberPerCSV
    numberPerCSV = numberPerCSVTextBox.get() 
    return numberPerCSV

def CsvDemo1():
    Prefix()
    RequiredNumber()
    NumberQuantity()
    NumberPerCSV()
    ShuffleNumber(prefix,splitedRn,numberQuantity)
    with open("generatedNumber.csv","w", newline="", encoding="utf8") as f:
        fw = csv.writer(f)
        fw.writerow(["First Name","Last Name","Prefix","Phone Number"])
        i = 0
        while i<(len(y)-2):
            fw.writerow([y[i],y[i+1],"",y[i+2]])
            i += 3

def ShuffleNumber(p,rn,nq):
    w = tuple(range(10000000))
    x = random.sample(w,len(w))
    y = []
    #for each X
    for i in x:
        #format number to at least 7 digits(in case of 0 leads)
        formattedList = format(i,"07d")
        #check to get only if required numbers are all in formattedList
        d = all(item in formattedList for item in rn)
        if(d):
            #add prefix and formatted + required numbers to make numbers
            y.append(p+formattedList)
        if(len(y)==nq):
            break
    generatedQuantity = len(y)
    return generatedQuantity

def MaxNumberQuantityButton():
    Prefix()
    RequiredNumber()
    generatedQuantity = ShuffleNumber(prefix,splitedRn,numberQuantity)
    quantityTxt.set(generatedQuantity)

def maxNumberPerCsvButton():
    Prefix()
    RequiredNumber()
    generatedQuantity = ShuffleNumber(prefix,splitedRn,numberQuantity)
    numberPerCSVTxt.set(generatedQuantity)

requiredNumberTextBox=Entry(root,textvariable=requiredNumberTxt,width=22).place(x=355,y=15)
quantityTextBox=Entry(root,textvariable=quantityTxt,width=17).place(x=335,y=115)
numberPerCSVTextBox=Entry(root,textvariable=numberPerCSVTxt,width=17).place(x=335,y=215)

maxQuantityButton = Button(root,text="MAX",width=5).place(x=450,y=110)
maxNumberPerCSVButton = Button(root,text="MAX",width=5).place(x=450,y=210)
exportButton = Button(root,text="Export to CSV",width=16,height=3,command=CsvDemo1).place(x=350,y=260)



root.geometry("500x350")
root.resizable(width=False,height=False)
def onClosed():
    confirm = tkinter.messagebox.askquestion("ยืนยันการปิดโปรแกรม","คุณต้องการปิดโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()
root.protocol("WM_DELETE_WINDOW",onClosed)
root.mainloop()



import random
u = ["41","59","60"]
v = "060"
w = tuple(range(10000000))
x = random.sample(w,len(w))
y = []
#for each X
for i in x:
    #format number to at least 7 digits(in case of 0 leads)
    formattedList = format(i,"07d")
    #check to get only if required numbers are all in formattedList
    d = all(item in formattedList for item in u)
    if(d):
        #add prefix and formatted + required numbers to make numbers
        y.append(v+formattedList)
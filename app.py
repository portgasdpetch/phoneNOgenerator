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

requiredNumberTxt=IntVar()
quantityTxt=IntVar()
numberPerCSVTxt=IntVar()
prefixNumberTxt=StringVar()

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

def exPort():
    global p 
    p = prefixNumberTxt.get()
    if (p==None):
        return ""
    else:
        pass

def csvDemo1(c):
    exPort()
    with open("generatedNumber.csv","w", newline="", encoding="utf8") as f:
        fw = csv.writer(f)
        fw.writerow(["First Name","Last Name","Prefix","Phone Number"])
        i = 0
        while i<(len(c)-2):
            fw.writerow([c[i],c[i+1],"",c[i+2]])
            i += 3

requiredNumberTextBox=Entry(root,textvariable=requiredNumberTxt,width=22).place(x=355,y=15)
quantityTextBox=Entry(root,textvariable=quantityTxt,width=17).place(x=335,y=115)
numberPerCSVTextBox=Entry(root,textvariable=numberPerCSVTxt,width=17).place(x=335,y=215)

maxQuantityButton = Button(root,text="MAX",width=5).place(x=450,y=110)
maxNumberPerCSVButton = Button(root,text="MAX",width=5).place(x=450,y=210)
exportButton = Button(root,text="Export to CSV",width=16,height=3,command=csvDemo1).place(x=350,y=260)



root.geometry("500x350")
root.resizable(width=False,height=False)
def onClosed():
    confirm = tkinter.messagebox.askquestion("ยืนยันการปิดโปรแกรม","คุณต้องการปิดโปรแกรมหรือไม่ ?")
    if confirm == "yes":
        root.destroy()
root.protocol("WM_DELETE_WINDOW",onClosed)
root.mainloop()



import random
t = "59"
u = ["41","59"]
v = "060"
w = list(range(10000000))
x = random.sample(w,len(w))
y = []
for i in x:
    formattedList = format(i,"07d")
    k=0
    while (k<len(u)):
        if u[k] in formattedList:
            if u[k] in formattedList:
                y.append(v+formattedList)
            else:
                pass
            k += 1
        else:
            pass
print(y)
print(len(y))
csvDemo1(y)


# a = range(0000000,10000000)
# for i in a:
#     # print("{:07d}".format(i))
#     print(format(i,"07d"))
    # csvDemo1(format(i,"07d"))

# from numpy import random
# import numpy as np
# a = np.arange(1000000)
# b = random.permutation(a)
# # d = np.array([])
# for c in b:
#     formattedList = format(c,"07d")
#     d = np.append(formattedList,formattedList)
# print(d)



# x = random.shuffle(list(w))
# print(x)

# for i in x:
#     print(format(i,"07d"))
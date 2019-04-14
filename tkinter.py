# !/usr/bin/python3

import tkinter 

from tkinter import Label,Button,Entry,Radiobutton,StringVar,messagebox


buttons=[]

def get_values():
     v1=1
     v2=1
     messagebox.showinfo("Check out OK")
     v1=r1.get()
     if(v1==''):
         v1=1
     v2=r2.get()
     if(v2==''):
         v2=1
     m1=r3.get()
     if(m1==''):
         m1=1
     m2=r4.get()
     if(m2==''):
         m2=1
     m3=r5.get()
     if(m3==''):
         m3=1
     m4=r6.get()
     if(m4==''):
         m4=1
     m5=r7.get()
     if(m5==''):
         m5=1
     m6=r8.get()
     if(m6==''):
         m6=1
     data=[[v1,v2,m1,m2,m3,m4,m5,m6]]
     print(data)
     
     
top=tkinter.Tk()
#scrollbar=Scrollbar(top)
#scrollbar.pack(side=RIGHT,fill=Y)



top.configure(background="Green")
top.geometry("1400x1000")
top.title('House Sale Price Prediciton')


L1 = Label(top,text = "USER NAME")
L1.place(x = 10,y = 80)
E1 = Entry(top,bd = 3)
E1.place(x = 300,y = 80)



#HouseStyle
r1=StringVar()
lbl=Label(text="Choose House Style:")
lbl.place(x=10,y=150)

R1=Radiobutton(top,text="2Story",variable=r1,value="2",tristatevalue="x")
R1.place(x=300,y=150)
buttons.append(R1)
R2=Radiobutton(top,text="1Story",variable=r1,value="1",tristatevalue="x")
R2.place(x=380,y=150)
buttons.append(R2)
R3=Radiobutton(top,text="1.5Fin",variable=r1,value="3",tristatevalue="x")
R3.place(x=460,y=150)
buttons.append(R3)
R4=Radiobutton(top,text="2.5Unf",variable=r1,value="4",tristatevalue="x")
R4.place(x=540,y=150)
buttons.append(R4)
R5=Radiobutton(top,text="SLvl",variable=r1,value="5",tristatevalue="x")
R5.place(x=620,y=150)
buttons.append(R5)
R6=Radiobutton(top,text="SFoyer",variable=r1,value="6",tristatevalue="x")
R6.place(x=700,y=150)
buttons.append(R6)
R7=Radiobutton(top,text="1.5Unf",variable=r1,value="7",tristatevalue="x")
R7.place(x=780,y=150)
buttons.append(R7)
R8=Radiobutton(top,text="2.5Fin",variable=r1,value="8",tristatevalue="x")
R8.place(x=860,y=150)
buttons.append(R8)


r2=StringVar()
lbl=Label(text="Select Utilities:")
lbl.place(x=10,y=200)

R9=Radiobutton(top,text="ALL Public",variable=r2,value="1",tristatevalue="x")
R9.place(x=300,y=200)
buttons.append(R9)
R10=Radiobutton(top,text="NoSeWa",variable=r2,value="2",tristatevalue="x")
R10.place(x=400,y=200)
buttons.append(R10)


r3=StringVar()
lbl=Label(text="Select Garage Type:")
lbl.place(x=10,y=250)

R11=Radiobutton(top,text="Attached",variable=r3,value="1",tristatevalue="x")
R11.place(x=300,y=250)
buttons.append(R11)
R12=Radiobutton(top,text="Dettached",variable=r3,value="2",tristatevalue="x")
R12.place(x=390,y=250)
buttons.append(R12)
R13=Radiobutton(top,text="Built_In",variable=r3,value="3",tristatevalue="x")
R13.place(x=480,y=250)
buttons.append(R13)
R14=Radiobutton(top,text="Basement",variable=r3,value="4",tristatevalue="x")
R14.place(x=580,y=250)
buttons.append(R14)
R15=Radiobutton(top,text="Carport",variable=r3,value="5",tristatevalue="x")
R15.place(x=680,y=250)
buttons.append(R15)
R16=Radiobutton(top,text="2types",variable=r3,value="6",tristatevalue="x")
R16.place(x=780,y=250)
buttons.append(R16)



r4=StringVar()
lbl=Label(text="Select Garage Quality:")
lbl.place(x=10,y=300)
R17=Radiobutton(top,text="TA",variable=r4,value="1",tristatevalue="x")
R17.place(x=300,y=300)
buttons.append(R17)
R18=Radiobutton(top,text="FA",variable=r4,value="2",tristatevalue="x")
R18.place(x=380,y=300)
buttons.append(R18)
R19=Radiobutton(top,text="GD",variable=r4,value="3",tristatevalue="x")
R19.place(x=460,y=300)
buttons.append(R19)
R20=Radiobutton(top,text="EX",variable=r4,value="5",tristatevalue="x")
R20.place(x=540,y=300)
buttons.append(R20)
R21=Radiobutton(top,text="PO",variable=r4,value="4",tristatevalue="x")
R21.place(x=620,y=300)
buttons.append(R21)




r5=StringVar()
lbl=Label(text="Select Heating Type:")
lbl.place(x=10,y=350)

R22=Radiobutton(top,text="GasA",variable=r5,value="1",tristatevalue="x")
R22.place(x=300,y=350)
buttons.append(R22)
R23=Radiobutton(top,text="GasW",variable=r5,value="2",tristatevalue="x")
R23.place(x=380,y=350)
buttons.append(R23)
R24=Radiobutton(top,text="Grav",variable=r5,value="3",tristatevalue="x")
R24.place(x=460,y=350)
buttons.append(R24)
R25=Radiobutton(top,text="Wall",variable=r5,value="4",tristatevalue="x")
R25.place(x=540,y=350)
buttons.append(R25)
R26=Radiobutton(top,text="other",variable=r5,value="5",tristatevalue="x")
R26.place(x=620,y=350)
buttons.append(R26)
R27=Radiobutton(top,text="Floor",variable=r5,value="6",tristatevalue="x")
R27.place(x=700,y=350)
buttons.append(R27)



r6=StringVar()
lbl=Label(text="Select Heating quality:")
lbl.place(x=10,y=400)

R28=Radiobutton(top,text="EX",variable=r6,value="1",tristatevalue="x")
R28.place(x=300,y=400)
buttons.append(R28)
R29=Radiobutton(top,text="Gd",variable=r6,value="3",tristatevalue="x")
R29.place(x=380,y=400)
buttons.append(R29)
R30=Radiobutton(top,text="TA",variable=r6,value="2",tristatevalue="x")
R30.place(x=460,y=400)
buttons.append(R30)
R31=Radiobutton(top,text="Fa",variable=r6,value="4",tristatevalue="x")
R31.place(x=540,y=400)
buttons.append(R31)
R32=Radiobutton(top,text="Po",variable=r6,value="5",tristatevalue="x")
R32.place(x=620,y=400)
buttons.append(R32)


r7=StringVar()
lbl=Label(text="Central Air Type:")
lbl.place(x=10,y=450)
R33=Radiobutton(top,text="Yes",variable=r7,value="1",tristatevalue="x")
R33.place(x=300,y=450)
buttons.append(R33)
R34=Radiobutton(top,text="No",variable=r7,value="2",tristatevalue="x")
R34.place(x=380,y=450)
buttons.append(R34)


r8=StringVar()
lbl=Label(text="Select Electric Quality:")
lbl.place(x=10,y=500)

R35=Radiobutton(top,text="SBrKr",variable=r8,value="1",tristatevalue="x")
R35.place(x=300,y=500)
buttons.append(R35)
R36=Radiobutton(top,text="FuseA",variable=r8,value="2",tristatevalue="x")
R36.place(x=380,y=500)
buttons.append(R36)
R37=Radiobutton(top,text="FuseF",variable=r8,value="3",tristatevalue="x")
R37.place(x=460,y=500)
buttons.append(R37)
R38=Radiobutton(top,text="FuseP",variable=r8,value="4",tristatevalue="x")
R38.place(x=540,y=500)
buttons.append(R38)
R39=Radiobutton(top,text="Mix",variable=r8,value="5",tristatevalue="x")
R39.place(x=620,y=500)
buttons.append(R39)


B1=Button(top,text="SUBMIT",command=get_values)
B1.place(x=500,y=650)


top.mainloop()



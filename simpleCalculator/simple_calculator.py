#simple calculator
import tkinter
class MYGUI:
    def __init__(self):
        self.window=tkinter.Tk()
        
        self.top_frame=tkinter.Frame()
        self.second_frame=tkinter.Frame()
        self.third_frame=tkinter.Frame()
        
        self.bottom_frame=tkinter.Frame()
        self.bottom_frame=tkinter.Frame()

        self.mid_frame=tkinter.Frame()
        
        self.L1=tkinter.Label(self.top_frame,text="Enter number1:")
        self.L1.pack(side='left')
        self.E=tkinter.Entry(self.top_frame, width=10)
        self.E.pack()

        self.L2=tkinter.Label(self.second_frame,text="Enter number2:")
        self.L2.pack(side='left')
        self.E2=tkinter.Entry(self.second_frame, width=10)
        self.E2.pack()
        
        self.L3=tkinter.Label(self.third_frame,text="Enter number3:")
        self.L3.pack(side='left')
        self.E3=tkinter.Entry(self.third_frame, width=10)
        self.E3.pack()

        self.B1=tkinter.Button(self.bottom_frame,text="ADD",width=5, height=2, bg="#D6EAF8" ,command=self.add)
        self.B1.pack(padx=5)
        self.B2=tkinter.Button(self.bottom_frame,text="SUB",width=5, height=2, bg="#D1F2EB" ,command=self.sub)
        self.B2.pack(padx=5)
        self.B3=tkinter.Button(self.bottom_frame,text="MUL",width=5, height=2, bg="#FCF3CF" ,command=self.mul)
        self.B3.pack(padx=5)
        self.B4=tkinter.Button(self.bottom_frame,text="DIV",width=5, height=2, bg="#FADBD8" ,command=self.div)
        self.B4.pack(padx=5)

        self.outputlable=tkinter.Label(self.mid_frame, text="Result: ")
        self.outputlable.pack()

        self.value= tkinter.StringVar()

        self.output=tkinter.Label(self.mid_frame,textvariable=self.value)
        self.output.pack()

        self.top_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.bottom_frame.pack()
        self.bottom_frame.pack()
        self.mid_frame.pack()

        self.window.mainloop()
    def add (self):
        n1=float(self.E.get())
        n2=float(self.E2.get())
        n3=float(self.E3.get())
        self.value.set(n1+n2+n3)
    def sub (self):
        n1=float(self.E.get())
        n2=float(self.E2.get())
        n3=float(self.E3.get())
        self.value.set(n1-n2-n3)
    def mul (self):
        n1=float(self.E.get())
        n2=float(self.E2.get())
        n3=float(self.E3.get())
        self.value.set(n1*n2*n3)  
    def div(self):
        n1=float(self.E.get())
        n2=float(self.E2.get())
        n3=float(self.E3.get())
        try:
            self.value.set(n1/n2/n3)
        except ZeroDivisionError:
            self.value.set("Error: divide by 0")             
GUI=MYGUI()        
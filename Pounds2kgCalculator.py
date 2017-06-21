#pounds to kg calculator
from tkinter import *
class pounds_to_kg(Frame):
     def __init__(self,master=None):
         Frame.__init__(self,master)
         self.master.title('Pounds to kg calculator')
         self.master.minsize(100,200)
         self.pack()
         
         self.pounds=StringVar()
         pounds2kg=Entry(self,width=50,textvariable =self.pounds).pack(side=LEFT)
         
         Label(self,text='lbs').pack(side=LEFT)
         
         Button(self,text='Calculate', command = self.calculate).pack(side=LEFT)
         
     def calculate(self):
         try:
            value=float(self.pounds.get())
            print(  str(value)+ ' lbs '  + ' is equivalent  to ' + str(0.453592 *value) + ' kg')
                       
         except ValueError: pass        

            
if __name__ == "__main__" :
    
   pounds_to_kg().mainloop()

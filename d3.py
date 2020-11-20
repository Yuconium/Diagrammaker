from tkinter import *
import pygal

class Diagrammprogramm:
    def __init__(self, window, bar):
        
        self.svg = ".svg"
        self.obertext = "Hello"
        self.barzeiger = ""
        self.zähler = 0
        self.Entrys()
        self.Labels()
        self.Buttons()

    def Entrys(self):
        self.title = Entry(window, bg = "#2ECCFA")
        self.title.grid(row = 4, column = 5)

        self.barname = Entry(window, bg = "#00BFFF")
        self.barname.grid(row = 5, column = 5)

        self.number = Entry(window, bg = "#01A9DB")
        self.number.grid(row = 6, column = 5)



    def Labels(self):
        self.lab = Label(window, text = self.obertext)
        self.lab.grid(row = 0, column = 5)
        #----#
        self.titlelab = Label(window, text = "Title:")
        self.titlelab.grid(row = 4, column = 4)
        #----#
        self.barnamelab = Label(window, text = "Barname:")
        self.barnamelab.grid(row = 5, column = 4)
        #----#
        self.numberlab = Label(window, text = "size:")
        self.numberlab.grid(row = 6, column = 4)
        #----#
        self.titlezeiger = Label(window)
        self.titlezeiger.grid(row = 7, column = 5)
        #----#
        self.zeiger = Label(window, text = self.barzeiger)
        self.zeiger.grid(row = 8, column = 5)
        #----#


    def Buttons(self):
        self.setter = Button(window, text = "Set!", command = self.set)
        self.setter.grid(row = 5, column = 6)
        self.titlesetter = Button(window, text = "Title", command = self.titleset)
        self.titlesetter.grid(row = 4, column = 6)
        self.renderbutton = Button(window, text = "Finish!", command = self.render)
        self.renderbutton.grid(row = 6, column = 6)


    def titleset(self):
        bar.title = self.title.get()
        self.titlezeiger.configure(text = bar.title)
        self.title2 = bar.title


    def set(self):
        self.name = self.barname.get()
        self.size = self.number.get()
        self.zähler += 1
        self.barzeiger += "Bar Nr.{}\nName:{}\nsize:{}\n".format(self.zähler, self.name, self.size)
        self.zeiger.configure(text = self.barzeiger)
        
        bar.add(self.name, int(self.size))


    def render(self):
        bar.render_to_file(self.title2 + self.svg)






bar = pygal.Bar()
window = Tk()
window.geometry("230x500")
window.title("Diagramm")
mygui = Diagrammprogramm(window, bar)
window.mainloop()
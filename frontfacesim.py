from tkinter import *
import time
import numpy as np

def rotate(steps):
    steps=steps
    x = 200 + (150 * np.cos(steps))
    y = 200 + (150 * np.sin(steps))
    return(x,y)
def rotateLunar(steps):
    steps=steps
    x = 200 + (75 * np.cos(steps))
    y = 200 + (75 * np.sin(steps))
    return(x,y)
class frontface(object):
     def __init__(self):
        legendtext = "Center: Lunar orbit \n Yellow: Sun \n Orange: Mercury \n Brown: Venus \n Red: Mars \n White: Jupiter \n Gray: Saturn"
        self.root = Tk()
        self.canvas = Canvas(self.root, width=400, height = 400)

        self.canvas.pack()
        colorval = "#%02x%02x%02x" % (205, 127, 50)
        self.face1 = self.canvas.create_oval(50, 50, 350, 350, outline='black',fill=colorval)
        self.sunpointer = self.canvas.create_line(200, 200, 200, 50, fill="black")
        self.sunindicator = self.canvas.create_oval(0, 0, 0, 0, fill="yellow")
        self.mercurypointer = self.canvas.create_line(200, 200, 200, 50, fill="black")
        self.mercuryindicator = self.canvas.create_oval(0, 0, 0, 0, fill="orange")
        self.venuspointer = self.canvas.create_line(200, 200, 200, 50, fill="black")
        self.venusindicator = self.canvas.create_oval(0, 0, 0, 0, fill="brown")
        self.marspointer = self.canvas.create_line(200, 200, 200, 50, fill="black")
        self.marsindicator = self.canvas.create_oval(0, 0, 0, 0, fill="red")
        self.jupiterpointer = self.canvas.create_line(200, 200, 200, 50, fill="black")
        self.jupiterindicator = self.canvas.create_oval(0, 0, 0, 0, fill="white")
        self.saturnpointer = self.canvas.create_line(200, 200, 200, 50, fill="black")
        self.saturnindicator = self.canvas.create_oval(0, 0, 0, 0, fill="gray")
        self.face2 =self.canvas.create_oval(125, 125, 275, 275, fill=colorval)
        self.lunarpointer = self.canvas.create_line(200, 200, 200, 125, fill="black")
        self.lunarindicator = self.canvas.create_oval(0, 0, 0, 0, fill="gray")

        self.canvas.create_text(50,360,fill="black",font="Times 8 bold",text=legendtext)
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

     def animation(self):
        suntrack=4.75
        mertrack=4.75
        ventrack=4.75
        martrack=4.75
        juptrack=4.75
        sattrack=4.75
        lunartrack=4.75
        while True:
            sunx,suny=rotate(suntrack)
            merx,mery=rotate(mertrack)
            venx,veny=rotate(ventrack)
            marx,mary=rotate(martrack)
            jupx,jupy=rotate(juptrack)
            satx,saty=rotate(sattrack)
            lunx,luny=rotateLunar(lunartrack)
            self.canvas.coords(self.sunpointer,200,200,sunx,suny)
            self.canvas.coords(self.sunindicator,sunx-5,suny-5,sunx+5,suny+5)
            self.canvas.coords(self.mercurypointer,200,200,merx,mery)
            self.canvas.coords(self.mercuryindicator,merx-5,mery-5,merx+5,mery+5)
            self.canvas.coords(self.venuspointer,200,200,venx,veny)
            self.canvas.coords(self.venusindicator,venx-5,veny-5,venx+5,veny+5)
            self.canvas.coords(self.marspointer,200,200,marx,mary)
            self.canvas.coords(self.marsindicator,marx-5,mary-5,marx+5,mary+5)
            self.canvas.coords(self.jupiterpointer,200,200,jupx,jupy)
            self.canvas.coords(self.jupiterindicator,jupx-5,jupy-5,jupx+5,jupy+5)
            self.canvas.coords(self.saturnpointer,200,200,satx,saty)
            self.canvas.coords(self.saturnindicator,satx-5,saty-5,satx+5,saty+5)
            self.canvas.coords(self.lunarpointer,200,200,lunx,luny)
            self.canvas.coords(self.lunarindicator,lunx-5,luny-5,lunx+5,luny+5)

            #time.sleep(0.00000)
            suntrack = (suntrack+(1/365))
            mertrack = (mertrack+(1/115.88))
            ventrack = (ventrack+(1/583.93))
            martrack = (martrack+(1/779.96))
            juptrack = (juptrack+(1/398.88))
            sattrack = (sattrack+(1/378.09))
            lunartrack = lunartrack+(1/27.321661)

            self.canvas.update()





frontface()

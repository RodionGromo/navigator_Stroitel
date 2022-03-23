from tkinter import *
import tkinter as tk


class marker:
    id = 0

    def __init__(self, posX, posY, textDesc, color, diameter, canvas, window, callback):
        self.id = marker.id
        marker.id += 1
        self.descpiptionFont = '"Times New Roman" 16'
        self.posX = posX
        self.posY = posY
        self.textDesc = textDesc
        self.canvas = canvas
        self.color = color
        self.diameter = diameter
        self.updated = True
        self.canvas.create_oval(posX, posY, posX + diameter, posY + diameter, fill=color, width=2)
        self.tip = None
        self.tips = []
        self.window = window
        self.callback = callback

    def motion(self, event):
        print(marker.id)

    def textSlicer(self):
        output = []
        buff = self.textDesc
        #self.canvas.update() #ошибка рекурсии!
        lb = Label(self.window, font=self.descpiptionFont, text=buff)
        if not lb.winfo_reqwidth() >= self.canvas.winfo_width() - self.posX:
            output.append(buff)
            return output
        while lb.winfo_reqwidth() > self.canvas.winfo_width() - self.posX + 5:
            cc = 0
            while lb.winfo_reqwidth() >= self.canvas.winfo_width() - self.posX + 5:
                lb = Label(self.window, font=self.descpiptionFont, text=buff[cc:])
                cc = cc + 1
            output.append(buff[:len(buff) - cc])
            buff = buff[len(buff) - cc:]
            lb = Label(self.window, font=self.descpiptionFont, text=buff)
        output.append(buff)
        return output

    def drawTip(self, create=True):
        right = self.posX + 140
        left = self.posX
        bottom = self.posY - 10
        text = self.textSlicer()
        widths = []
        top = self.posY - Label(self.window, font=self.descpiptionFont, text="111").winfo_reqheight() * (len(text) + 1)
        for a in text:
            widths.append(Label(self.window, font=self.descpiptionFont, text=a).winfo_reqwidth())
        if create:
            self.tip = self.canvas.create_rectangle(left, top, left + max(widths) + 1, bottom,
                                                    fill=self.color, tags="tip" + str(self.id))
            j = 0
            for i in range(top,
                           bottom - Label(self.window, font=self.descpiptionFont, text="111").winfo_reqheight(),
                           Label(self.window, font=self.descpiptionFont, text="111").winfo_reqheight()):
                self.tips.append(
                    Label(self.window, text=str(text[j]), font=self.descpiptionFont, background=self.color))
                self.tips[len(self.tips) - 1].place(x=left + 1, y=i + 1)
                if len(text) > j + 1:
                    j = j + 1
                else:
                    break
        else:
            self.canvas.delete("tip" + str(self.id))
            for obj in self.tips:
                obj.destroy()

    def info(self):
        print("X:", self.posX, " Y:", self.posY, " Text:", self.textDesc, sep="")

    def handle(self, event):
        if self.posX <= event.x <= (self.diameter + self.posX) and self.posY <= event.y <= (self.diameter + self.posY):
            self.drawTip()
        else:
            self.drawTip(False)

    def handleClick(self,event):
        if self.posX <= event.x <= (self.diameter + self.posX) and self.posY <= event.y <= (self.diameter + self.posY): #скобочки решают все проблемы :)
            self.callback()

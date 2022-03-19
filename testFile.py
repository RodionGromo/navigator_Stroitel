from tkinter import Tk,Label,font,Button,PhotoImage
import sys
import ctypes

settings = {
	"nav_window_size": "640x640"
}

def getCenter(windowsize):
	windowX,windowY = windowsize
	user32 = ctypes.windll.user32
	return f"{windowX}x{windowY}+{int((user32.GetSystemMetrics(0)/2) - (windowX/2))}+{int((user32.GetSystemMetrics(1)/2) - (windowY/2))}"

def createMainWindow():
	def nextStep():
		menuWindow.destroy()
		createNav()
	menuWindow = Tk()
	menuWindow.title("Навигатор_Строитель")
	menuWindow.geometry("640x170")
	menuWindow.resizable(0,0)
	lb1 = Label(master=menuWindow,text="Добро пожаловать в..")
	lb1.configure(font=font.Font(family="Times New Roman",size=14,weight="bold"))
	lb1.pack()
	lb2 = Label(master=menuWindow,text='Навигатор Строитель')
	lb2.configure(font=font.Font(family="Times New Roman",size=48,weight="normal"))
	lb2.pack()
	stAdvBtn = Button(master=menuWindow,text="Начать приключение",command=nextStep)
	stAdvBtn.pack()
	exitBtn = Button(master=menuWindow,text="Мама забери меня домой",command=sys.exit)
	exitBtn.pack()
	menuWindow.mainloop()

def createNav():
	def nextStep():
		navWindow.destroy()
		zoomInPloshad()
	navWindow = Tk()
	navWindow.title("Главная карта")
	img1data = PhotoImage(file='./assets/big_map1.png')
	img1 = Label(master=navWindow,image=img1data).pack()
	btn1 = Button(master=navWindow,text="я хочу в белгород",command=sys.exit)
	btn1.place(x=985,y=500)
	ploshadBtn = Button(master=navWindow,text="Главная площадь",command=nextStep)
	ploshadBtn.place(x=610,y=400)
	navWindow.geometry(getCenter((img1data.width(),img1data.height())))
	navWindow.mainloop()

def zoomInPloshad():
	ploshadWindow = Tk()
	ploshadWindow.title("Главная площадь")
	img1data = PhotoImage(file="./assets/ploshad_main.png")
	ploshadWindow.geometry(getCenter((img1data.width(),img1data.height())))
	img1 = Label(master=ploshadWindow,image=img1data).pack()
	ploshadWindow.mainloop()


createMainWindow()

from tkinter import Tk,Label,font,Button,PhotoImage,Canvas
import sys
import ctypes
import markers as mark
from PIL import Image,ImageTk

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
	markers = []

	def updMoveMarkers(event):
		for marki in markers:
			marki.handle(event=event)

	def clickMarkers(event):
		for marki in markers:
			marki.handleClick(event)

	def goToPloshad():
		navWindow.destroy()
		zoomInPloshad()

	navWindow = Tk()
	navWindow.geometry("1314x520")
	cnvs = Canvas(width=1314,height=520)
	cnvs.pack()
	img1data = PhotoImage(file='./assets/big_map1.png')
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(1015,500,"Выйти из приложения","yellow",10,cnvs,navWindow,sys.exit))
	markers.append(mark.marker(635,350,"Главная площадь","white",15,cnvs,navWindow,goToPloshad))
	navWindow.title("Главная карта")
	cnvs.bind("<Motion>",updMoveMarkers)
	cnvs.bind("<Button-1>",clickMarkers)
	navWindow.mainloop()

def zoomInMemorial():
	markers = []
	memorialWindow = Tk()
	memorialWindow.title("Мемориал")
	img1data = PhotoImage(file="./assets/cross1.png")
	cnvs = Canvas(width=img1data.width(),height=img1data.height())
	cnvs.pack()
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	memorialWindow.mainloop()



def zoomInPloshad():
	def updMoveMarkers(event):
		for marki in markers:
			marki.handle(event=event)

	def clickMarkers(event):
		for marki in markers:
			marki.handleClick(event)

	def gotoMemorial():
		cnvs.unbind("<Motion>",motBind)
		cnvs.unbind("<Button-1>",clickBind)
		ploshadWindow.destroy()
		zoomInMemorial()


	markers = []
	ploshadWindow = Tk()
	ploshadWindow.title("Главная площадь")
	img1data = PhotoImage(file="./assets/ploshad_main.png")
	ploshadWindow.geometry(getCenter((img1data.width(),img1data.height())))
	cnvs = Canvas(width=img1data.width(),height=img1data.height())
	cnvs.pack()
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(190,310,"Аллея героев","red",15,cnvs,ploshadWindow,None))
	markers.append(mark.marker(272,353,"Мемориал 'В честь 50-летия Победы в Курском сражении'","gold",15,cnvs,ploshadWindow,zoomInMemorial))
	motBind = cnvs.bind("<Motion>",updMoveMarkers)
	clickBind = cnvs.bind("<Button-1>",clickMarkers)
	ploshadWindow.mainloop()

if __name__ == '__main__':
	createMainWindow()

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
	menuWindow.geometry(getCenter((640,170)))
	menuWindow.resizable(0,0)
	lb1 = Label(master=menuWindow,text="Добро пожаловать в..")
	lb1.configure(font=font.Font(family="Times New Roman",size=14,weight="bold"))
	lb1.pack()
	lb2 = Label(master=menuWindow,text='Навигатор Строитель')
	lb2.configure(font=font.Font(family="Times New Roman",size=48,weight="normal"))
	lb2.pack()
	stAdvBtn = Button(master=menuWindow,text="Начать приключение",command=nextStep)
	stAdvBtn.pack()
	exitBtn = Button(master=menuWindow,text="Испугаться и выйти",command=sys.exit)
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

	def gotoParkRoz():
		navWindow.destroy()

	def safeExit():
		cnvs.unbind(moveBind)
		cnvs.unbind(clickBind)
		sys.exit()

	navWindow = Tk()
	navWindow.geometry(getCenter((1314,520)))
	cnvs = Canvas(width=1314,height=520)
	cnvs.pack()
	img1data = PhotoImage(file='./assets/big_map1.png')
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(1015,500,"Выйти из приложения","yellow",15,cnvs,navWindow,safeExit))
	markers.append(mark.marker(635,350,"Главная площадь","white",15,cnvs,navWindow,goToPloshad))
	markers.append(mark.marker(908,448,"Парк Роз","red",15,cnvs,navWindow,None))
	navWindow.title("Главная карта")
	moveBind = cnvs.bind("<Motion>",updMoveMarkers)
	clickBind = cnvs.bind("<Button-1>",clickMarkers)
	navWindow.mainloop()

def zoomInParkRoz():
	pass

def zoomInPloshad():
	def updMoveMarkers(event):
		for marki in markers:
			marki.handle(event=event)

	def clickMarkers(event):
		for marki in markers:
			marki.handleClick(event)

	def gotoMemorial():
		ploshadWindow.destroy()
		zoomInMemorial()

	def gotoChasovnya():
		ploshadWindow.destroy()
		zoomInChasovnya()

	def zoomOut():
		ploshadWindow.destroy()
		createNav()

	markers = []
	ploshadWindow = Tk()
	ploshadWindow.title("Главная площадь")
	img1data = PhotoImage(file="./assets/ploshad_main.png")
	ploshadWindow.geometry(getCenter((img1data.width(),img1data.height())))
	cnvs = Canvas(width=img1data.width(),height=img1data.height())
	cnvs.pack()
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(190,310,"Аллея героев","red",15,cnvs,ploshadWindow,None))
	markers.append(mark.marker(272,353,"Мемориал 'В честь 50-летия Победы в Курском сражении'","gold",15,cnvs,ploshadWindow,gotoMemorial))
	markers.append(mark.marker(322,368,"Часовня Георгия Победоносца + Памятник погибишим в Афганистане","gold",15,cnvs,ploshadWindow,gotoChasovnya))
	markers.append(mark.marker(360,444,"Назад","white",20,cnvs,ploshadWindow,zoomOut))
	motBind = cnvs.bind("<Motion>",updMoveMarkers)
	clickBind = cnvs.bind("<Button-1>",clickMarkers)
	ploshadWindow.mainloop()

def zoomInChasovnya():
	markers = []

	def updMoveMarkers(event):
		for marki in markers:
			marki.handle(event=event)

	def clickMarkers(event):
		for marki in markers:
			marki.handleClick(event)

	def zoomIn():
		chasWindow.destroy()
		zoomInZvonSign()
	chasWindow = Tk()
	chasWindow.title("Часовня Георгия Победоносца")
	img1 = Image.open("./assets/zvonnitsa1.JPG")
	img1data = ImageTk.PhotoImage(img1.resize((img1.width//2,img1.height//2)))
	chasWindow.geometry(getCenter((img1data.width(),img1data.height())))
	cnvs = Canvas(width=img1data.width(),height=img1data.height())
	cnvs.pack()
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(472,500,"Пройти дальше","blue",25,cnvs,chasWindow,zoomIn))
	motBind = cnvs.bind("<Motion>",updMoveMarkers)
	clickBind = cnvs.bind("<Button-1>",clickMarkers)
	chasWindow.mainloop()

def zoomInZvonSign():
	markers = []

	def updMoveMarkers(event):
		for marki in markers:
			marki.handle(event=event)

	def clickMarkers(event):
		for marki in markers:
			marki.handleClick(event)

	def zoomOut():
		zoominWindow.destroy()
		zoomInChasovnya()

	zoominWindow = Tk()
	zoominWindow.title("Часовня Георгия Победоносца + Памятник погибишим в Афганистане")
	img1 = Image.open("./assets/zvonnitsa2.JPG")
	img1data = ImageTk.PhotoImage(img1.resize((img1.width//2,img1.height//2)))
	zoominWindow.geometry(getCenter((img1data.width(),img1data.height())))
	cnvs = Canvas(width=img1data.width(),height=img1data.height())
	cnvs.pack()
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(472,470,"Назад","white",25,cnvs,zoominWindow,zoomOut))
	motBind = cnvs.bind("<Motion>",updMoveMarkers)
	clickBind = cnvs.bind("<Button-1>",clickMarkers)
	zoominWindow.mainloop()

def zoomInMemorial():

	def updMoveMarkers(event):
		for marki in markers:
			marki.handle(event=event)

	def clickMarkers(event):
		for marki in markers:
			marki.handleClick(event)

	def zoomInSign():
		memorialWindow.destroy()
		zoomInMemorialSign()

	def zoomOut():
		memorialWindow.destroy()
		zoomInPloshad()

	markers = []
	memorialWindow = Tk()
	memorialWindow.title("Мемориал")
	img1 = Image.open("./assets/cross1.png")
	img1data = ImageTk.PhotoImage(img1.resize((img1.width//2,img1.height//2)))
	memorialWindow.geometry(getCenter((img1data.width(),img1data.height())))
	cnvs = Canvas(width=img1data.width(),height=img1data.height())
	cnvs.pack()
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(563,519,"Приблизить табличку","gray",15,cnvs,memorialWindow,zoomInSign))
	markers.append(mark.marker(850,516,"Назад","white",15,cnvs,memorialWindow,zoomOut))
	motBind = cnvs.bind("<Motion>",updMoveMarkers)
	clickBind = cnvs.bind("<Button-1>",clickMarkers)
	memorialWindow.mainloop()

def zoomInMemorialSign():

	def updMoveMarkers(event):
		for marki in markers:
			marki.handle(event=event)

	def clickMarkers(event):
		for marki in markers:
			marki.handleClick(event)

	def zoomOut():
		memorialSignWindow.destroy()
		zoomInMemorial()

	markers = []
	memorialSignWindow = Tk()
	memorialSignWindow.title("Табличка на мемориале")
	img1 = Image.open("./assets/cross2.JPG")
	img1data = ImageTk.PhotoImage(img1.resize((img1.width//2,img1.height//2)))
	memorialSignWindow.geometry(getCenter((img1data.width(),img1data.height())))
	cnvs = Canvas(width=img1data.width(),height=img1data.height())
	cnvs.pack()
	cnvs.create_image(0,0,image=img1data,anchor="nw")
	markers.append(mark.marker(587,470,"Назад","white",20,cnvs,memorialSignWindow,zoomOut))
	motBind = cnvs.bind("<Motion>",updMoveMarkers)
	clickBind = cnvs.bind("<Button-1>",clickMarkers)
	memorialSignWindow.mainloop()

if __name__ == '__main__':
	createMainWindow()

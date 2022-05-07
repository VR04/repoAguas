from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from numpy import mat
import pandas as pd
from math import pi,sin,cos,tan,sqrt,log10
from functools import partial

class HoverButton(Button):
		def __init__(self, master, **kw):
			Button.__init__(self,master=master,**kw)
			self.defaultBackground = self["background"]
			self.bind("<Enter>", self.on_enter)
			self.bind("<Leave>", self.on_leave)

		def on_enter(self, e):
			self["background"] = self["activebackground"]

		def on_leave(self, e):
			self["background"] = self.defaultBackground  
def getSuper(x): 
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s)) 
    return x.translate(res) 
  
def getSub(x): 
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s)) 
    return x.translate(res) 


def returnMainWindow(window):
	window.withdraw()
	mainWindow.deiconify()

def destroyMainWindow():
	mainWindow.destroy()

def on_closing():
	if messagebox.askokcancel("Salir","¿Desea salir?"):
		mainWindow.destroy()





contador=0
contadorFiltro=0
contador2 = 0
contadorFloculador=0


def openSedWindow():
	#Style
	style = ttk.Style()
	#Pick a theme
	style.theme_use("clam")

	#Configure colors

	style.configure("Treeview",background="#9DC4AA", foreground="black", rowheight=40,fieldbackground="#9DC4AA")
	style.configure("Treeview.Heading", foreground="black", font =("Courier",12))
	#Change selected color
	style.map("Treeview", background=[("selected", "#09C5CE")])	 

	def calcularSed(lista_ent):
		lista_entry=[0]*20
		
		for entryID in range(0,len(lista_ent)):
			try:
				if entryID == 4:				
					
					lista_entry[entryID]= lista_ent[entryID].get()
					
				else: 
										
					lista_entry[entryID]=(float(lista_ent[entryID].get()))
				
			except:
				messagebox.showwarning(message="El ingreso de datos es erróneo, vuelva a intentarlo", title= "¡Cuidado!")
				return None
			


		if lista_entry[10]>60.0 or lista_entry[10]<45:
			messagebox.showwarning(message="El valor del ángulo de inclinación de la placa debe estar entre 45° y 60°", title= "¡Cuidado!")
			return None

			
	def formulaN(archivo):
		forWindow= tk.Toplevel()
		forWindow.iconbitmap(bitmap='icons\\agua.ico')
		forWindow.geometry("800x600") 
		forWindow.resizable(0,0)
		forWindow.configure(background="#9DC4AA")
		framefor=Frame(forWindow)
		framefor.pack(side=TOP, fill=BOTH, expand=True)
		ima= PhotoImage(file=archivo)
		l=Label(framefor, image=ima)
		l.pack()
		forWindow.mainloop()


	def newDataTreeview(tree,listaS):
		global contador
		
		if contador%2 ==0:
			
			tree.insert("",END,text= f"{contador+1}", values=listaS,
			iid=contador, tags=("evenrow"))	
		else:	
			tree.insert("",END,text= f"{contador+1}", values=listaS,
				iid=contador, tags=("oddrow"))
		contador=contador+1
		
		
	def newEntrySed(lista,optionValue):
		for elemento in lista:
			if elemento != optionValue:
				elemento.delete(0, END)
			else:
				optionValue.set("Seleccione")	
		

	def deleteSedTable(arbol):
		global contador
		m= arbol.get_children()	
		for j in m:
			arbol.delete(j)
		contador=0
		
	
	def parametrosDeDiseñoSedimentadorAltaTasa():
		
		parametrosDeDiseñoSedimentadorAltaTasaWindow = tk.Toplevel()
		parametrosDeDiseñoSedimentadorAltaTasaWindow.iconbitmap(bitmap='icons\\agua.ico')
		parametrosDeDiseñoSedimentadorAltaTasaWindow.geometry("700x600") 
		parametrosDeDiseñoSedimentadorAltaTasaWindow.resizable(0,0)	
		parametrosDeDiseñoSedimentadorAltaTasaWindow.configure(background="#9DC4AA")

		parametrosDeDiseñoSedimentadorAltaTasaFrame=LabelFrame(parametrosDeDiseñoSedimentadorAltaTasaWindow, text="Parámetros de diseño de sedimentador de alta tasa", font=("Yu Gothic bold", 11))
		parametrosDeDiseñoSedimentadorAltaTasaFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolparametrosDeDiseñoSedimentadorAltaTasa_frame = Frame(parametrosDeDiseñoSedimentadorAltaTasaFrame)
		arbolparametrosDeDiseñoSedimentadorAltaTasa_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolparametrosDeDiseñoSedimentadorAltaTasa_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolparametrosDeDiseñoSedimentadorAltaTasa_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolparametrosDeDiseñoSedimentadorAltaTasa= ttk.Treeview(arbolparametrosDeDiseñoSedimentadorAltaTasa_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolparametrosDeDiseñoSedimentadorAltaTasa.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolparametrosDeDiseñoSedimentadorAltaTasa.xview)
		sedScrollY.configure(command=arbolparametrosDeDiseñoSedimentadorAltaTasa.yview)
		#Define columnas.
		arbolparametrosDeDiseñoSedimentadorAltaTasa["columns"]= (
		"1","2","3")

		#Headings
		arbolparametrosDeDiseñoSedimentadorAltaTasa.heading("#0",text="ID", anchor=CENTER)


		def formulaN(archivo):
			forWindow= tk.Toplevel()
			forWindow.iconbitmap(bitmap='icons\\agua.ico')
			forWindow.geometry("1000x350") 
			forWindow.resizable(0,0)
			forWindow.configure(background="#9DC4AA")
			framefor=Frame(forWindow)
			framefor.pack(side=TOP, fill=BOTH, expand=True)
			ima= PhotoImage(file=archivo)
			l=Label(framefor, image=ima)
			l.pack()
			forWindow.mainloop()

		for col in arbolparametrosDeDiseñoSedimentadorAltaTasa["columns"]:
			arbolparametrosDeDiseñoSedimentadorAltaTasa.heading(col, text=col,anchor=CENTER, command=lambda: formulaN("images\\Predimensionamiento.png") )	

		
		arbolparametrosDeDiseñoSedimentadorAltaTasa.column("#0",width=0, stretch=False)
		arbolparametrosDeDiseñoSedimentadorAltaTasa.column("#1",width=450, stretch=False)	
		arbolparametrosDeDiseñoSedimentadorAltaTasa.column("#2",width=100, stretch=False)	
		arbolparametrosDeDiseñoSedimentadorAltaTasa.column("#3",width=150, stretch=False)	
		#Striped row tags
		arbolparametrosDeDiseñoSedimentadorAltaTasa.tag_configure("evenrow", background= "#1FCCDB")
		arbolparametrosDeDiseñoSedimentadorAltaTasa.tag_configure("oddrow", background= "#9DC4AA")






		encabezadosLista=["Carga superficial en placas angostas",
		"Carga superficial en placas profundas",
		"Velocidad de sedimentación crítica para floc de alumbre",
		"Velocidad de sedimentación crítica para floc de alumbre y polielectrolitos",
		"Tiempo de retención en placas",
		"Tiempo de retención en tubos",
		"Inclinación de placas",
		"Número de Reynolds",
		"Tasa de rebose",
		"Distancia entre placas",
		"Profundidad",
		"Fracción del tanque a tasa acelerada"]

		listaparametrosDeDiseñoSedimentadorAltaTasa =[ "120 - 185",
		"200 - 300",
		"12 - 23",
		"16 - 29",
		"10 - 15",
		"6 - 10",
		"60",
		"100 - 250",
		"1,7 - 3,3",
		"5 - 6",
		"3 - 5",
		"< 75"]

		unidadesLista = [	
		"m^3/m^2/d",
		"m^3/m^2/d",
		"m/d",
		"m/d",
		"min",
		"min",
		"°",
		"",
		"L/s.m",
		"cm",
		"m",
		"%"
		]


		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listaparametrosDeDiseñoSedimentadorAltaTasa[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolparametrosDeDiseñoSedimentadorAltaTasa,listaTemp)

	def determinacionParametrosBasicosDiseno():
		determinacionParametrosBasicosDisenoWindow = tk.Toplevel()
		determinacionParametrosBasicosDisenoWindow.iconbitmap(bitmap='icons\\agua.ico')
		determinacionParametrosBasicosDisenoWindow.geometry("600x400") 
		determinacionParametrosBasicosDisenoWindow.resizable(0,0)	
		determinacionParametrosBasicosDisenoWindow.configure(background="#9DC4AA")

		determinacionParametrosBasicosDisenoFrame=LabelFrame(determinacionParametrosBasicosDisenoWindow, text="Determinación de parámetro básicos de diseño", font=("Yu Gothic bold", 11))
		determinacionParametrosBasicosDisenoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboldeterminacionParametrosBasicosDiseno_frame = Frame(determinacionParametrosBasicosDisenoFrame)
		arboldeterminacionParametrosBasicosDiseno_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arboldeterminacionParametrosBasicosDiseno_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldeterminacionParametrosBasicosDiseno_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldeterminacionParametrosBasicosDiseno= ttk.Treeview(arboldeterminacionParametrosBasicosDiseno_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arboldeterminacionParametrosBasicosDiseno.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arboldeterminacionParametrosBasicosDiseno.xview)
		sedScrollY.configure(command=arboldeterminacionParametrosBasicosDiseno.yview)
		#Define columnas.
		arboldeterminacionParametrosBasicosDiseno["columns"]= (
		"1","2","3")

		#Headings
		arboldeterminacionParametrosBasicosDiseno.heading("#0",text="ID", anchor=CENTER)


		def formulaN(archivo):
			forWindow= tk.Toplevel()
			forWindow.iconbitmap(bitmap='icons\\agua.ico')
			forWindow.geometry("1000x350") 
			forWindow.resizable(0,0)
			forWindow.configure(background="#9DC4AA")
			framefor=Frame(forWindow)
			framefor.pack(side=TOP, fill=BOTH, expand=True)
			ima= PhotoImage(file=archivo)
			l=Label(framefor, image=ima)
			l.pack()
			forWindow.mainloop()

		for col in arboldeterminacionParametrosBasicosDiseno["columns"]:
			arboldeterminacionParametrosBasicosDiseno.heading(col, text=col,anchor=CENTER, command=lambda: formulaN("images\\Predimensionamiento.png") )	

		for i in range(0,len(arboldeterminacionParametrosBasicosDiseno["columns"])+1) :
				arboldeterminacionParametrosBasicosDiseno.column(f"#{i}",width=700, stretch=False)	
		arboldeterminacionParametrosBasicosDiseno.column("#0",width=0, stretch=False)

		#Striped row tags
		arboldeterminacionParametrosBasicosDiseno.tag_configure("evenrow", background= "#1FCCDB")
		arboldeterminacionParametrosBasicosDiseno.tag_configure("oddrow", background= "#9DC4AA")




		listadeterminacionParametrosBasicosDiseno=list()


		encabezadosLista=[]

		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listadeterminacionParametrosBasicosDiseno[i])
			newDataTreeview(arboldeterminacionParametrosBasicosDiseno,listaTemp)

		determinacionParametrosBasicosDisenoWindow.mainloop()
		

	def canaletasRecoleccionAgua():
		canaletasRecoleccionAguaWindow = tk.Toplevel()
		canaletasRecoleccionAguaWindow.iconbitmap(bitmap='icons\\agua.ico')
		canaletasRecoleccionAguaWindow.geometry("600x400") 
		canaletasRecoleccionAguaWindow.resizable(0,0)	
		canaletasRecoleccionAguaWindow.configure(background="#9DC4AA")

		canaletasRecoleccionAguaFrame=LabelFrame(canaletasRecoleccionAguaWindow, text="Canaletas de recolección de agua clarificada", font=("Yu Gothic bold", 11))
		canaletasRecoleccionAguaFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolcanaletasRecoleccionAgua_frame = Frame(canaletasRecoleccionAguaFrame)
		arbolcanaletasRecoleccionAgua_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolcanaletasRecoleccionAgua_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolcanaletasRecoleccionAgua_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolcanaletasRecoleccionAgua= ttk.Treeview(arbolcanaletasRecoleccionAgua_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolcanaletasRecoleccionAgua.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolcanaletasRecoleccionAgua.xview)
		sedScrollY.configure(command=arbolcanaletasRecoleccionAgua.yview)
		#Define columnas.
		arbolcanaletasRecoleccionAgua["columns"]= (
		"1","2","3")

		#Headings
		arbolcanaletasRecoleccionAgua.heading("#0",text="ID", anchor=CENTER)


		def formulaN(archivo):
			forWindow= tk.Toplevel()
			forWindow.iconbitmap(bitmap='icons\\agua.ico')
			forWindow.geometry("1000x350") 
			forWindow.resizable(0,0)
			forWindow.configure(background="#9DC4AA")
			framefor=Frame(forWindow)
			framefor.pack(side=TOP, fill=BOTH, expand=True)
			ima= PhotoImage(file=archivo)
			l=Label(framefor, image=ima)
			l.pack()
			forWindow.mainloop()

		for col in arbolcanaletasRecoleccionAgua["columns"]:
			arbolcanaletasRecoleccionAgua.heading(col, text=col,anchor=CENTER, command=lambda: formulaN("images\\Predimensionamiento.png") )	

		for i in range(0,len(arbolcanaletasRecoleccionAgua["columns"])+1) :
				arbolcanaletasRecoleccionAgua.column(f"#{i}",width=700, stretch=False)	
		arbolcanaletasRecoleccionAgua.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolcanaletasRecoleccionAgua.tag_configure("evenrow", background= "#1FCCDB")
		arbolcanaletasRecoleccionAgua.tag_configure("oddrow", background= "#9DC4AA")




		listacanaletasRecoleccionAgua=list()


		encabezadosLista=[]

		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listacanaletasRecoleccionAgua[i])
			newDataTreeview(arbolcanaletasRecoleccionAgua,listaTemp)

		canaletasRecoleccionAguaWindow.mainloop()


	def tiempoRetencionTotalTanque():
		tiempoRetencionTotalTanqueWindow = tk.Toplevel()
		tiempoRetencionTotalTanqueWindow.iconbitmap(bitmap='icons\\agua.ico')
		tiempoRetencionTotalTanqueWindow.geometry("600x400") 
		tiempoRetencionTotalTanqueWindow.resizable(0,0)	
		tiempoRetencionTotalTanqueWindow.configure(background="#9DC4AA")

		tiempoRetencionTotalTanqueFrame=LabelFrame(tiempoRetencionTotalTanqueWindow, text="Tiempo de retención total en el tanque", font=("Yu Gothic bold", 11))
		tiempoRetencionTotalTanqueFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboltiempoRetencionTotalTanque_frame = Frame(tiempoRetencionTotalTanqueFrame)
		arboltiempoRetencionTotalTanque_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arboltiempoRetencionTotalTanque_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboltiempoRetencionTotalTanque_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboltiempoRetencionTotalTanque= ttk.Treeview(arboltiempoRetencionTotalTanque_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arboltiempoRetencionTotalTanque.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arboltiempoRetencionTotalTanque.xview)
		sedScrollY.configure(command=arboltiempoRetencionTotalTanque.yview)
		#Define columnas.
		arboltiempoRetencionTotalTanque["columns"]= (
		"1","2","3")

		#Headings
		arboltiempoRetencionTotalTanque.heading("#0",text="ID", anchor=CENTER)


		def formulaN(archivo):
			forWindow= tk.Toplevel()
			forWindow.iconbitmap(bitmap='icons\\agua.ico')
			forWindow.geometry("1000x350") 
			forWindow.resizable(0,0)
			forWindow.configure(background="#9DC4AA")
			framefor=Frame(forWindow)
			framefor.pack(side=TOP, fill=BOTH, expand=True)
			ima= PhotoImage(file=archivo)
			l=Label(framefor, image=ima)
			l.pack()
			forWindow.mainloop()

		for col in arboltiempoRetencionTotalTanque["columns"]:
			arboltiempoRetencionTotalTanque.heading(col, text=col,anchor=CENTER, command=lambda: formulaN("images\\Predimensionamiento.png") )	

		for i in range(0,len(arboltiempoRetencionTotalTanque["columns"])+1) :
				arboltiempoRetencionTotalTanque.column(f"#{i}",width=700, stretch=False)	
		arboltiempoRetencionTotalTanque.column("#0",width=0, stretch=False)

		#Striped row tags
		arboltiempoRetencionTotalTanque.tag_configure("evenrow", background= "#1FCCDB")
		arboltiempoRetencionTotalTanque.tag_configure("oddrow", background= "#9DC4AA")




		listatiempoRetencionTotalTanque=list()


		encabezadosLista=[]

		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listatiempoRetencionTotalTanque[i])
			newDataTreeview(arboltiempoRetencionTotalTanque,listaTemp)

		tiempoRetencionTotalTanqueWindow.mainloop()

	def dimensionesDelSedimentador():
		dimensionesDelSedimentadorWindow = tk.Toplevel()
		dimensionesDelSedimentadorWindow.iconbitmap(bitmap='icons\\agua.ico')
		dimensionesDelSedimentadorWindow.geometry("600x400") 
		dimensionesDelSedimentadorWindow.resizable(0,0)	
		dimensionesDelSedimentadorWindow.configure(background="#9DC4AA")

		dimensionesDelSedimentadorFrame=LabelFrame(dimensionesDelSedimentadorWindow, text="Dimensiones del sedimentador", font=("Yu Gothic bold", 11))
		dimensionesDelSedimentadorFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboldimensionesDelSedimentador_frame = Frame(dimensionesDelSedimentadorFrame)
		arboldimensionesDelSedimentador_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arboldimensionesDelSedimentador_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldimensionesDelSedimentador_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldimensionesDelSedimentador= ttk.Treeview(arboldimensionesDelSedimentador_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arboldimensionesDelSedimentador.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arboldimensionesDelSedimentador.xview)
		sedScrollY.configure(command=arboldimensionesDelSedimentador.yview)
		#Define columnas.
		arboldimensionesDelSedimentador["columns"]= (
		"1","2","3")

		#Headings
		arboldimensionesDelSedimentador.heading("#0",text="ID", anchor=CENTER)


		def formulaN(archivo):
			forWindow= tk.Toplevel()
			forWindow.iconbitmap(bitmap='icons\\agua.ico')
			forWindow.geometry("1000x350") 
			forWindow.resizable(0,0)
			forWindow.configure(background="#9DC4AA")
			framefor=Frame(forWindow)
			framefor.pack(side=TOP, fill=BOTH, expand=True)
			ima= PhotoImage(file=archivo)
			l=Label(framefor, image=ima)
			l.pack()
			forWindow.mainloop()

		for col in arboldimensionesDelSedimentador["columns"]:
			arboldimensionesDelSedimentador.heading(col, text=col,anchor=CENTER, command=lambda: formulaN("images\\Predimensionamiento.png") )	

		for i in range(0,len(arboldimensionesDelSedimentador["columns"])+1) :
				arboldimensionesDelSedimentador.column(f"#{i}",width=700, stretch=False)	
		arboldimensionesDelSedimentador.column("#0",width=0, stretch=False)

		#Striped row tags
		arboldimensionesDelSedimentador.tag_configure("evenrow", background= "#1FCCDB")
		arboldimensionesDelSedimentador.tag_configure("oddrow", background= "#9DC4AA")




		listadimensionesDelSedimentador=list()


		encabezadosLista=[]

		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listadimensionesDelSedimentador[i])
			newDataTreeview(arboldimensionesDelSedimentador,listaTemp)

		dimensionesDelSedimentadorWindow.mainloop()

	def disenoSistemaEvacuacionLodos():
		disenoSistemaEvacuacionLodosWindow = tk.Toplevel()
		disenoSistemaEvacuacionLodosWindow.iconbitmap(bitmap='icons\\agua.ico')
		disenoSistemaEvacuacionLodosWindow.geometry("600x400") 
		disenoSistemaEvacuacionLodosWindow.resizable(0,0)	
		disenoSistemaEvacuacionLodosWindow.configure(background="#9DC4AA")

		disenoSistemaEvacuacionLodosFrame=LabelFrame(disenoSistemaEvacuacionLodosWindow, text="Diseño del sistema de evacuación de lodos", font=("Yu Gothic bold", 11))
		disenoSistemaEvacuacionLodosFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboldisenoSistemaEvacuacionLodos_frame = Frame(disenoSistemaEvacuacionLodosFrame)
		arboldisenoSistemaEvacuacionLodos_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arboldisenoSistemaEvacuacionLodos_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldisenoSistemaEvacuacionLodos_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldisenoSistemaEvacuacionLodos= ttk.Treeview(arboldisenoSistemaEvacuacionLodos_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arboldisenoSistemaEvacuacionLodos.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arboldisenoSistemaEvacuacionLodos.xview)
		sedScrollY.configure(command=arboldisenoSistemaEvacuacionLodos.yview)
		#Define columnas.
		arboldisenoSistemaEvacuacionLodos["columns"]= (
		"1","2","3")

		#Headings
		arboldisenoSistemaEvacuacionLodos.heading("#0",text="ID", anchor=CENTER)


		def formulaN(archivo):
			forWindow= tk.Toplevel()
			forWindow.iconbitmap(bitmap='icons\\agua.ico')
			forWindow.geometry("1000x350") 
			forWindow.resizable(0,0)
			forWindow.configure(background="#9DC4AA")
			framefor=Frame(forWindow)
			framefor.pack(side=TOP, fill=BOTH, expand=True)
			ima= PhotoImage(file=archivo)
			l=Label(framefor, image=ima)
			l.pack()
			forWindow.mainloop()

		for col in arboldisenoSistemaEvacuacionLodos["columns"]:
			arboldisenoSistemaEvacuacionLodos.heading(col, text=col,anchor=CENTER, command=lambda: formulaN("images\\Predimensionamiento.png") )	

		for i in range(0,len(arboldisenoSistemaEvacuacionLodos["columns"])+1) :
				arboldisenoSistemaEvacuacionLodos.column(f"#{i}",width=700, stretch=False)	
		arboldisenoSistemaEvacuacionLodos.column("#0",width=0, stretch=False)

		#Striped row tags
		arboldisenoSistemaEvacuacionLodos.tag_configure("evenrow", background= "#1FCCDB")
		arboldisenoSistemaEvacuacionLodos.tag_configure("oddrow", background= "#9DC4AA")




		listadisenoSistemaEvacuacionLodos=list()


		encabezadosLista=[]

		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listadisenoSistemaEvacuacionLodos[i])
			newDataTreeview(arboldisenoSistemaEvacuacionLodos,listaTemp)

		disenoSistemaEvacuacionLodosWindow.mainloop()
		
		
		


	mainWindow.withdraw()
	sedWindow= tk.Toplevel()
	sedWindow.protocol("WM_DELETE_WINDOW", on_closing)
	sedWindow.iconbitmap(bitmap='icons\\agua.ico')
	sedWindow.geometry("1240x600") 
	#sedWindow.geometry("1366x680") 
	#sedWindow.resizable(1366,763)
	sedWindow.resizable(0,0)
	sedWindow.configure(background="#9DC4AA")

	##Panel:
	panel = ttk.Notebook(sedWindow)
	panel.pack(fill=BOTH, expand=TRUE)

	frameSed= LabelFrame(panel, text="Sedimentador de alta tasa")
	frameSed.pack(side=TOP,fill=BOTH,expand=True)
	panel.add(frameSed, text="Cálculos")
	

	
	factorMayoracionCaudalMD = Entry(frameSed)
	factorMayoracionCaudalMD.focus()
	factorMayoracionCaudalMH = Entry(frameSed)
	caudalMedioEntry = Entry(frameSed)
	
	listaValoresTemp=list()
	for i in range(0,36):
		listaValoresTemp.append(f"{i}")
	
	temperaturaEntry = ttk.Combobox(frameSed, width="30", state="readonly",values=listaValoresTemp)
	temperaturaEntry.set("Seleccione la temperatura")
	
	
	
	


	oP1=["Floc de alumbre", "Floc con alumbre y polielectrolitos"]
	tipoFloc = ttk.Combobox(frameSed, width="40", state="readonly", values=oP1)
	tipoFloc.set("Seleccion el tipo de floc")
	oP2 = {
	"Placas planas paralelas": ("Acero inoxidable AISI 316","Polietileno alta densidad (HDPE)","Poliestireno de alto impacto(HIPS)") , 
	"Placas onduladas paralelas":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)"),
	"Conductos cuadrados":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)")}
	
	
	
	def onComboboxSelect1(event):
		dimensionesTipoCeldaMaterial.set("Seleccione las dimensiones del tipo de celda")
		materialTipoCelda.set("Seleccione el material del tipo de celda")
		materialTipoCelda.config(values=oP2[tipoCelda.get()])

	def onComboboxSelect2(event):
		dimensionesTipoCeldaMaterial.set("Seleccione las dimensiones del tipo de celda")
		oP2 = {
			"Placas planas paralelas": ("Acero inoxidable AISI 316","Polietileno alta densidad (HDPE)","Poliestireno de alto impacto(HIPS)") , 
			"Placas onduladas paralelas":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)"),
			"Conductos cuadrados":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)")}
		combinacionesTipoCeldaMaterial = list()
		for elemento in tuple(oP2.keys()):
			for ele2 in oP2[elemento]:
				combinacionesTipoCeldaMaterial.append((elemento, ele2))
		dimensiones= [	
		('1219 x 1219', '1219 x 2438', '1524 x 1524', '1524 x 3048'), 
		('1200 x 1200', '1200 x 1400', '1200 x 1600', '1200 x 1800', '1200 x 2000', '1200 x 2200', '1200 x 2400', '1200 x 2600', '1200 x 2800', '1200 x 3000'), 
		('1200 x 1200', '1200 x 1500', '1200 x 2400', '1200 x 3000'), 
		('1200 x 1200', '1200 x 1400', '1200 x 1600', '1200 x 1800', '1200 x 2000', '1200 x 2200', '1200 x 2400', '1200 x 2600', '1200 x 2800', '1200 x 3000'), 
		('1200 x 1200', '1200 x 1400', '1200 x 1600', '1200 x 1800', '1200 x 2000', '1200 x 2200', '1200 x 2400', '1200 x 2600', '1200 x 2800', '1200 x 3000'), 
		('1200 x 1500', '1200 x 2000', '1200 x 2500', '1200 x 3000'), 
		('1200 x 1500', '1200 x 2000', '1200 x 2500', '1200 x 3000')]

		if ((tipoCelda.get(),materialTipoCelda.get())==("Seleccione el material del tipo de celda","Seleccione las dimensiones del tipo de celda")):
			dimensionesTipoCeldaMaterial.set("Seleccione las dimensiones del tipo de celda")
		for i in range(0,len(combinacionesTipoCeldaMaterial)):
			if ((tipoCelda.get(),materialTipoCelda.get())== combinacionesTipoCeldaMaterial[i]):
				dimensionesTipoCeldaMaterial.config(values=dimensiones[i])
		

		

	tipoCelda = ttk.Combobox(frameSed, width="40", state="readonly",values=tuple(oP2.keys()))
	tipoCelda.bind("<<ComboboxSelected>>", onComboboxSelect1)
	tipoCelda.set("Seleccione el tipo de celda")
	

	materialTipoCelda = ttk.Combobox(frameSed, width="40", state="readonly")
	materialTipoCelda.bind("<<ComboboxSelected>>", onComboboxSelect2)
	materialTipoCelda.set("Seleccione el material del tipo de celda")
	
	dimensionesTipoCeldaMaterial = ttk.Combobox(frameSed, width="40", state="readonly")
	dimensionesTipoCeldaMaterial.set("Seleccione las dimensiones del tipo de celda")
	

	
	
	anguloInclinacion = Entry(frameSed)
	numeroUnidades = ttk.Combobox(frameSed, width="40", state="readonly",values=["2","3","4","5","6","7","8"])
	numeroUnidades.set("Seleccione el número de unidades")
	distanciaPlacas = Entry(frameSed)
	longitudPlacas = Entry(frameSed)
	distanciaCanaletasRecoleccion = Entry(frameSed)
	distanciaVerticalDistribucionPlacas = Entry(frameSed)
	bordeLibre = Entry(frameSed)
	espesorMuros = Entry(frameSed)
	pendienteTransversalTolva = Entry(frameSed)
	anchoBasePlanaTolva = Entry(frameSed)
	velocidadMinimaArrastre = Entry(frameSed)

	diametroNominalLista= ['1/2 (RDE 9)',
		'3/4 (RDE 11)',
		'3/4 (RDE 21)',
		'1 (RDE 13,5)',
		'1 (RDE 21)',
		'1 1/4 (RDE 21)',
		'1 1/2 (RDE 21)',
		'2 (RDE 21)']
	
	diametroNominalOrificionesMultipleDescarga = ttk.Combobox(frameSed, width="65", state="readonly",values= diametroNominalLista)
	diametroNominalOrificionesMultipleDescarga.set("Seleccione el diámetro nominal de los orificios del múltiple de descarga")
	

	lista_entradas=[factorMayoracionCaudalMD,
	factorMayoracionCaudalMH,caudalMedioEntry,
	temperaturaEntry, tipoFloc,tipoCelda,
	materialTipoCelda,
	dimensionesTipoCeldaMaterial,
	anguloInclinacion, 
	numeroUnidades,
	distanciaPlacas,
	longitudPlacas, 
	distanciaCanaletasRecoleccion,
	distanciaVerticalDistribucionPlacas,
	bordeLibre,
	espesorMuros,
	pendienteTransversalTolva,
	anchoBasePlanaTolva,
	velocidadMinimaArrastre,
	diametroNominalOrificionesMultipleDescarga
	]
	
	
	labelIntroduccion = Label(frameSed, text="Datos de entrada para parámetros básicos: ",font=("Yu Gothic bold",10))
	caudalDiseñoLabel = Label(frameSed, text="Caudales de diseño", font =("Yu Gothic bold",10))
	factorMayoracionCaudalMDLabel = Label(frameSed, text="Factor de mayoración del caudal máximo diario:", font =("Yu Gothic",9))
	factorMayoracionCaudalMHLabel = Label(frameSed, text="Factor de mayoración del caudal máximo horario:", font =("Yu Gothic",9))
	caudalEntryLabel = Label(frameSed, text="Caudal de diseño [m^3/s]: ", font =("Yu Gothic",9))
	propiedadesFisicasAguaLabel = Label(frameSed, text="Propiedades físicas del agua a tratar.", font =("Yu Gothic bold",10))
	datosEntradaParametrosBasicosLabel = Label(frameSed, text="Datos de entrada para parámetros básicos.", font =("Yu Gothic bold",10))
	anguloInclinacionLabel = Label(frameSed, text="Ángulo de inclinación:", font =("Yu Gothic",9))
	distanciaPlacasLabel = Label(frameSed, text="Distancia entre placas:", font =("Yu Gothic",9))
	longitudPlacasLabel = Label(frameSed, text="Longitud ocupada por las placas:", font =("Yu Gothic",9))
	distanciaCanaletasRecoleccionLabel = Label(frameSed, text="Distancia entre las canaletas de recolección: ", font =("Yu Gothic",9))
	distanciaVerticalDistribucionPlacasLabel = Label(frameSed, text="Distancia vertical de orificios de distribución", font =("Yu Gothic",9))	
	bordeLibreLabel= Label(frameSed, text="Borde libre", font =("Yu Gothic",9))	
	espesorMurosLabel = Label(frameSed, text="Espesor de muros de concreto", font =("Yu Gothic",9))	
	pendienteTransversalTolvaLabel = Label(frameSed, text="Pendiente transversal de la tolva de lodos", font =("Yu Gothic",9))	
	anchoBasePlanaTolvaLabel = Label(frameSed, text="Ancho de la base plana de la tolva de lodos", font =("Yu Gothic",9))	
	velocidadMinimaArrastreLabel = Label(frameSed, text="Velocidad mínima de arrastre asignada", font =("Yu Gothic",9))	

	
	listaLabels=[labelIntroduccion,
	caudalDiseñoLabel,
	factorMayoracionCaudalMDLabel,
	factorMayoracionCaudalMHLabel,
	caudalEntryLabel,
	propiedadesFisicasAguaLabel,
	temperaturaEntry,
	datosEntradaParametrosBasicosLabel,
	tipoFloc,
	tipoCelda,
	materialTipoCelda,
	dimensionesTipoCeldaMaterial,
	anguloInclinacionLabel,
	numeroUnidades,
	distanciaPlacasLabel,
	longitudPlacasLabel,
	distanciaCanaletasRecoleccionLabel,
	distanciaVerticalDistribucionPlacasLabel,
	bordeLibreLabel,
	espesorMurosLabel,
	pendienteTransversalTolvaLabel,
	anchoBasePlanaTolvaLabel,
	velocidadMinimaArrastreLabel,
	diametroNominalOrificionesMultipleDescarga
	]
	

	imageAtras= PhotoImage(file="images\\atras.png")
	#BotonesSed.
	botonAtras= HoverButton(frameSed, image=imageAtras, width=100, height=40, bg= None, command=lambda: returnMainWindow(sedWindow))
	botonAtras.place(x=0,y=10)
	

	botonParametrosDeDiseñoSedimentadorAltaTasa = HoverButton(frameSed, text="Parámetros de diseño de sedimentadores de alta tasa", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: parametrosDeDiseñoSedimentadorAltaTasa())
	botonDeterminacionParametrosBasicosDiseno = HoverButton(frameSed, text="Determinación de parámetros básicos de diseño", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: determinacionParametrosBasicosDiseno())
	botonCanaletasRecoleccionAgua = HoverButton(frameSed, text="Canaletas de recolección de agua clarificada", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: canaletasRecoleccionAgua())
	botonTiempoRetencionTotalTanque = HoverButton(frameSed, text="Tiempo de retención total en el tanque", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: tiempoRetencionTotalTanque())
	botonDimensionesDelSedimentador = HoverButton(frameSed, text="Dimensiones del sedimentador", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: dimensionesDelSedimentador())
	botonDisenoSistemaEvacuacionLodos = HoverButton(frameSed, text="Diseño del sistema de evacuación de lodos", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: disenoSistemaEvacuacionLodos())
	botonLimpiarEntradas = HoverButton(frameSed, text="Limpiar entradas", activebackground="#9DC4AA", width=40, height=2, bg= "#09C5CE", font =("Courier",8),command= lambda: newEntrySed(lista_entradas))

	listaBotones=[botonParametrosDeDiseñoSedimentadorAltaTasa,
	botonDeterminacionParametrosBasicosDiseno,
	botonCanaletasRecoleccionAgua,
	botonTiempoRetencionTotalTanque, 
	botonDimensionesDelSedimentador,
	botonDisenoSistemaEvacuacionLodos, 
	botonLimpiarEntradas]

	
	#UbicacionElementos


	yInicial= 60
	yInicial2=50
	yInicial3=50
	#0,1,5,7
	j=0
	for i in range(0, len(listaLabels)):
		if i<7:

			if i==0 or i==1 or i==5:
				listaLabels[i].place(x=0, y=yInicial)
				yInicial=yInicial + 40
			else:
				lista_entradas[j].place(x=300, y=yInicial)
				listaLabels[i].place(x=0, y=yInicial)
				yInicial=yInicial + 40
				j=j+1
		
		elif 7<=i<16 :
			if i==7:
				listaLabels[i].place(x=450, y=yInicial2)
				yInicial2=yInicial2 + 30
			else:
				lista_entradas[j].place(x=650, y=yInicial2)
				listaLabels[i].place(x=450, y=yInicial2)
				yInicial2=yInicial2 + 30
				j=j+1
		else:

				lista_entradas[j].place(x=1100, y=yInicial3)
				listaLabels[i].place(x=800, y=yInicial3)
				yInicial3=yInicial3 + 30
				
				j=j+1
		i=i+1


		varX= [0, 450, 800]
		yBotones=yInicial

		for i in range(0,3):
			
			listaBotones[i].place(x=varX[0],y=yBotones)
			listaBotones[i+3].place(x=varX[2], y=yBotones)
			listaBotones[6].place(x=470,y=yBotones-50)
			
			yBotones=yBotones+50
	
	##CalculosAdicionalesDatosEntradaBásicos


	espesorPlacas = 8




	sedWindow.mainloop()



def openFiltroWindow():
	global contadorFiltro
	#Style
	style = ttk.Style()
	#Pick a theme
	style.theme_use("clam")

	#Configure colors
	
	style.configure("Treeview",background="#9DC4AA", foreground="black", rowheight=40,fieldbackground="#9DC4AA")
	style.configure("Treeview.Heading", foreground="black", font =("Courier",12))
	#Change selected color
	style.map("Treeview", background=[("selected", "#09C5CE")])	 

	def newEntryFiltro(lista, optValue,lista2): 
		for elemento in lista:
				elemento.delete(0, END)

		optValue.set("Seleccione la temperatura")
		lista2[0].delete(0,END)

	def newDataTreeview(tree,listaS):
		global contadorFiltro

		if contadorFiltro%2 ==0:
			tree.insert("",END,text= f"{contadorFiltro+1}", values=tuple(listaS),
			iid=contadorFiltro, tags=("evenrow",))	
		else:	
			tree.insert("",END,text= f"{contadorFiltro+1}", values=tuple(listaS),
				iid=contadorFiltro, tags=("oddrow",))
		contadorFiltro=contadorFiltro+1

	def principalesCaracFiltro():
		
		caracFiltroWindow = tk.Toplevel()
		caracFiltroWindow.iconbitmap(bitmap='icons\\agua.ico')
		caracFiltroWindow.geometry("1000x500") 
		caracFiltroWindow.resizable(0,0)	
		caracFiltroWindow.configure(background="#9DC4AA")
		
		#Frame Treeview
		arbolCaracFiltro_frame = LabelFrame(caracFiltroWindow, text="Principales caracterísiticas del filtro", font=("Yu Gothic bold", 11))
		arbolCaracFiltro_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolCaracFiltro_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolCaracFiltro_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCaracFiltro= ttk.Treeview(arbolCaracFiltro_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolCaracFiltro.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolCaracFiltro.xview)
		sedScrollY.configure(command=arbolCaracFiltro.yview)
		#Define columnas.
		arbolCaracFiltro["columns"]= (
		"Característica",""
		)

		#Headings
		arbolCaracFiltro.heading("#0",text="ID", anchor=CENTER)
		
		for col in arbolCaracFiltro["columns"]:
			arbolCaracFiltro.heading(col, text=col,anchor=CENTER)

		for i in range(0,len(arbolCaracFiltro["columns"])) :
				arbolCaracFiltro.column(f"#{i}",width=300, stretch=False)	
	
		arbolCaracFiltro.column("#2",width=300, stretch=True)
		arbolCaracFiltro.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolCaracFiltro.tag_configure("oddrow", background= "#1FCCDB")
		arbolCaracFiltro.tag_configure("evenrow", background= "#9DC4AA")

		col1=["Tipo de filtro","Medio filtrante","Distribución del medio","Tasa media de filtración","Tasa máxima de filtración","Duración de carrera","Pérdida de carga inicial","Pérdida de carga final","Uso de agua tratada en lavado","Profundida del medio","Profundidad de grava","Drenaje"]
		col2=["Filtro rápido de arena","Arena","Estratigicado de fino a grueso","120 m/d","150 m/d","12 - 36 horas", "0,3 m","2,4 - 3,0 m","2-4%","0,60-0,75 m","0,30-0,45 m","Tubería Perforada"]

		count=0
		for m in range(0,12):
			if count%2 ==0:
				arbolCaracFiltro.insert("",END,text=f"{count+1}", values=(col1[count],col2[count]),
					iid=count, tags=("evenrow",))	
				count=count+1
			else:
				arbolCaracFiltro.insert("",END,text= f"{count+1}", values=(col1[count],col2[count]),
					iid=count, tags=("oddrow",))
				count=count+1

		caracFiltroWindow.mainloop()

	def granulometria(lista1,lista2):
		
		def buscarEnTabla(NumTamiz,tablaDic):
			return tablaDic[NumTamiz]

		listaNTamizTemp=lista1.copy()
		listaARetenidaTemp=lista2.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de los números de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de la arena retenida.")
			return None

		for ind in range(0, len(listaNTamizTemp)):
			if listaNTamizTemp[ind].get() == "" and ind%2==0:
				break
			elif listaNTamizTemp[ind].get() == "" and ind%2 != 0:
				messagebox.showwarning(title="Error", message="Hace falta el rango de la derecha de alguna entrada.")
				return None
			else:
				try:
					CountControl=0
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m: 
							CountControl=CountControl+1
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m and CountControl==18:
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores estándar para número de tamiz. Pulse el botón para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de número de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None

		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de número de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento

			
		

		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None
	


	

		granulometriaWindow = tk.Toplevel()
		granulometriaWindow.iconbitmap(bitmap='icons\\agua.ico')
		granulometriaWindow.geometry("1000x500") 
		granulometriaWindow.resizable(0,0)	
		granulometriaWindow.configure(background="#9DC4AA")
		
		#Frame principal
		granulometriaFrame=LabelFrame(granulometriaWindow, text="Granulometría del medio filtrante de arena", font=("Yu Gothic bold", 11))
		granulometriaFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolgranulometria_frame = LabelFrame(granulometriaFrame, text="Principales caracterísiticas del filtro", font=("Yu Gothic bold", 11))
		arbolgranulometria_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolgranulometria_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolgranulometria_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolGranulometria= ttk.Treeview(arbolgranulometria_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolGranulometria.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolGranulometria.xview)
		sedScrollY.configure(command=arbolGranulometria.yview)
		#Define columnas.
		arbolGranulometria["columns"]= (
		"Número de tamiz",
		"Arena retenida [%]", 
		"Número de tamiz que retiene", 
		"Tamaño de abertura del tamiz [mm] (OD)", 
		"Acumulado de arena que pasa [%] (OD)", 
		"Tamaño de abertura del tamiz [mm] (OA)", 
		"Acumulado de arena que pasa [%](OA)" 
		)

		#Headings
		arbolGranulometria.heading("#0",text="ID", anchor=CENTER)
		
		for col in arbolGranulometria["columns"]:
			arbolGranulometria.heading(col, text=col,anchor=CENTER)

		for i in range(0,4) :
				arbolGranulometria.column(f"#{i}",width=300, stretch=False)	
		
		for i in range(4,len(arbolGranulometria["columns"])+1) :
				arbolGranulometria.column(f"#{i}",width=500, stretch=False)	
		
	
		arbolGranulometria.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolGranulometria.tag_configure("oddrow", background= "#1FCCDB")
		arbolGranulometria.tag_configure("evenrow", background= "#9DC4AA")


		#Insersión datos.
		global contadorFiltro
		contadorFiltro = 0

		listaEntradaTemp=list()
		datosSalida=list()
		
		
		
		
		#Tabla Tamaño Abertura Tamiz
		TamañoTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
		TamañoAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
		tablaTamañoAberturaTamiz=dict()
		for ind in range(0, len(TamañoTamiz)):
			tablaTamañoAberturaTamiz[TamañoTamiz[ind]] = TamañoAbertura[ind]

		#Acumulado arena que pasa.
		def acumuladoArenaQuePasa(indice):
			suma=0
			for elemento in range(0,indice+1):
				suma= suma+listaARetenida[elemento]
			return 100-suma
		#Calculando acumulado:
		listaAcumuladoArenaDescendente=list()
		for ind in range(0, len(listaARetenida)):
			listaAcumuladoArenaDescendente.append(acumuladoArenaQuePasa(ind))

		listaAcumuladoArenaAscendente = listaAcumuladoArenaDescendente.copy()
		listaAcumuladoArenaAscendente.reverse()

		#OrganizandoListaNTamiz
		listaNTamizExtremo=list()
		listaNTamizSinRepeticion=list()
		for num in range(0,len(listaNTamiz)):
			if num%2==0:
				pass	
			else:
				listaNTamizExtremo.append(listaNTamiz[num])
		guardado=listaNTamiz[0]
		listaNTamizSinRepeticion.append(guardado)
		for elemento in listaNTamiz:
			if elemento != guardado:
				listaNTamizSinRepeticion.append(elemento)
				guardado=elemento
	
				

		longListaARetenida=len(listaARetenida)-1
		for ind in range(0, len(listaARetenida)):
			listaEntradaTemp.clear()
			
			listaEntradaTemp.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
			extremoDerecho=listaNTamizExtremo[ind]
			listaEntradaTemp.append(listaARetenida[ind])
			listaEntradaTemp.append(extremoDerecho)
			listaEntradaTemp.append(tablaTamañoAberturaTamiz[extremoDerecho])
			listaEntradaTemp.append(listaAcumuladoArenaDescendente[ind])
			listaEntradaTemp.append(tablaTamañoAberturaTamiz[listaNTamizExtremo[longListaARetenida-ind]])
			listaEntradaTemp.append(listaAcumuladoArenaAscendente[ind])
			listaIntermedia = listaEntradaTemp.copy()
			datosSalida.append(listaIntermedia)
			newDataTreeview(arbolGranulometria, listaEntradaTemp)
		
		


		

		
		granulometriaWindow.mainloop()

	def coeficienteDeUniformidad(lista1,lista2):

		def buscarEnTabla(NumTamiz,tablaDic):
			return tablaDic[NumTamiz]

		listaNTamizTemp=lista1.copy()
		listaARetenidaTemp=lista2.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de los números de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de la arena retenida.")
			return None

		for ind in range(0, len(listaNTamizTemp)):
			if listaNTamizTemp[ind].get() == "" and ind%2==0:
				break
			elif listaNTamizTemp[ind].get() == "" and ind%2 != 0:
				messagebox.showwarning(title="Error", message="Hace falta el rango de la derecha de alguna entrada.")
				return None
			else:
				try:
					CountControl=0
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m: 
							CountControl=CountControl+1
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m and CountControl==18:
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores estándar para número de tamiz. Pulse el botón para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de número de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de número de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento
		
		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None
	

		coeficienteDUWindow = tk.Toplevel()
		coeficienteDUWindow.iconbitmap(bitmap='icons\\agua.ico')
		coeficienteDUWindow.geometry("1000x200") 
		coeficienteDUWindow.resizable(0,0)	
		coeficienteDUWindow.configure(background="#9DC4AA")
		
		#Frame principal
		coeficienteDUFrame=LabelFrame(coeficienteDUWindow, text="Coeficiente de uniformidad CU", font=("Yu Gothic bold", 11))
		coeficienteDUFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolCoeficienteDU_frame = Frame(coeficienteDUFrame)
		arbolCoeficienteDU_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolCoeficienteDU_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolCoeficienteDU_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCoeficienteDU= ttk.Treeview(arbolCoeficienteDU_frame,selectmode=BROWSE, height=2,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolCoeficienteDU.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolCoeficienteDU.xview)
		sedScrollY.configure(command=arbolCoeficienteDU.yview)
		#Define columnas.
		arbolCoeficienteDU["columns"]= (
		"Tamaño Efectivo d{} [mm]".format(getSub("10")),
        "Tamaño Efectivo d{} [mm]".format(getSub("60")),
        "Coeficiente de uniformidad. CU= d{}/d{}".format(getSub("60"),getSub("10"))
		)
		

		

		#Headings
		arbolCoeficienteDU.heading("#0",text="ID", anchor=CENTER)
		
		arbolCoeficienteDU.heading("#1", text="Tamaño Efectivo d{} [mm]".format(getSub("10")), anchor=CENTER, command= lambda: tamañod(x1,y1,x2,y2,10))
		arbolCoeficienteDU.heading("#2", text="Tamaño Efectivo d{} [mm]".format(getSub("60")), anchor=CENTER, command= lambda: tamañod(X1,Y1,X2,Y2,60))
		arbolCoeficienteDU.heading("#3", text="Coeficiente de uniformidad. CU= d{}/d{}".format(getSub("60"),getSub("10")), anchor=CENTER)

		"""for col in arbolCoeficienteDU["columns"]:
			arbolCoeficienteDU.heading(col, text=col,anchor=CENTER)"""
		


		
		for i in range(0,len(arbolCoeficienteDU["columns"])) :
				arbolCoeficienteDU.column(f"#{i}",width=300, stretch=False)	
		arbolCoeficienteDU.column("#3",width=600, stretch=True)	
		arbolCoeficienteDU.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolCoeficienteDU.tag_configure("oddrow", background= "#1FCCDB")
		arbolCoeficienteDU.tag_configure("evenrow", background= "#9DC4AA")


		#Insersión datos.
		global contadorFiltro
		contadorFiltro = 0

		listaEntradaTemp=list()
		datosSalida=list()
		

		
		
		#Tabla Tamaño Abertura Tamiz
		TamañoTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
		TamañoAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
		tablaTamañoAberturaTamiz=dict()
		for ind in range(0, len(TamañoTamiz)):
			tablaTamañoAberturaTamiz[TamañoTamiz[ind]] = TamañoAbertura[ind]

		#Acumulado arena que pasa.
		def acumuladoArenaQuePasa(indice):
			suma=0
			for elemento in range(0,indice+1):
				suma= suma+listaARetenida[elemento]

			return 100.0-suma
		#Calculando acumulado:
		listaAcumuladoArenaDescendente=list()
		for ind in range(0, len(listaARetenida)):
			if ind != len(listaARetenida)-1:
				listaAcumuladoArenaDescendente.append(acumuladoArenaQuePasa(ind))
			else:
				listaAcumuladoArenaDescendente.append(0)
		listaAcumuladoArenaAscendente = listaAcumuladoArenaDescendente.copy()
		listaAcumuladoArenaAscendente.reverse()

		
		#OrganizandoListaNTamiz
		listaNTamizExtremo=list()
		listaNTamizSinRepeticion=list()
		for num in range(0,len(listaNTamiz)):
			if num%2==0:
				pass	
			else:
				listaNTamizExtremo.append(listaNTamiz[num])
		guardado=listaNTamiz[0]
		listaNTamizSinRepeticion.append(guardado)
		for elemento in listaNTamiz:
			if elemento != guardado:
				listaNTamizSinRepeticion.append(elemento)
				guardado=elemento
	
				

		longListaARetenida=len(listaARetenida)-1
		for ind in range(0, len(listaARetenida)):
			listaEntradaTemp.clear()
			
			listaEntradaTemp.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
			extremoDerecho=listaNTamizExtremo[ind]
			listaEntradaTemp.append(listaARetenida[ind])
			listaEntradaTemp.append(extremoDerecho)
			listaEntradaTemp.append(tablaTamañoAberturaTamiz[extremoDerecho])
			listaEntradaTemp.append(listaAcumuladoArenaDescendente[ind])
			listaEntradaTemp.append(tablaTamañoAberturaTamiz[listaNTamizExtremo[longListaARetenida-ind]])
			listaEntradaTemp.append(listaAcumuladoArenaAscendente[ind])
			listaIntermedia = listaEntradaTemp.copy()
			datosSalida.append(listaIntermedia)
		
		abAcDic= dict()
		for ind in range(0,len(datosSalida)):
			abAcDic[datosSalida[ind][6]]=datosSalida[ind][5]
		
		

		def tamañoEfectivod1(numero,dic):
			elementoAnterior=dic[0]
			for elemento in dic:
				if elemento <= numero and elemento>=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda

		def tamañoEfectivod2(numero,dic):
			elementoAnterior=100
			for elemento in dic:
				if elemento >= numero and elemento<=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda
		def tamañoEfectivod(numero,dic):
			return[tamañoEfectivod1(numero,dic), tamañoEfectivod2(numero,dic)]

		def calculo1CU(numero,x1,y1,x2,y2):
			return(log10(x1)+(((numero-y1)/(y2-y1))*log10(x2/x1)))
		def calculo2CU(numero,x1,y1,x2,y2):
			return (10**(calculo1CU(numero,x1,y1,x2,y2)))
		
		#Calculo Tamaño Efectivo d10:
		listaAcumuladoCU10=tamañoEfectivod(10,abAcDic)
		y1=listaAcumuladoCU10[0]
		y2=listaAcumuladoCU10[1]
		x1=abAcDic[y1]
		x2=abAcDic[y2]
		d10= calculo2CU(10,x1,y1,x2,y2)
		listaAcumuladoCU60=tamañoEfectivod(60,abAcDic)
		Y1= listaAcumuladoCU60[0]
		Y2= listaAcumuladoCU60[1]
		X1= abAcDic[Y1]
		X2=	abAcDic[Y2]
		d60= calculo2CU(60,X1,Y1,X2,Y2)
		CU=d60/d10
		listaIngreso=[d10,d60,CU]
		newDataTreeview(arbolCoeficienteDU,listaIngreso)

		def tamañod(x1,y1,x2,y2,numero):
			tamañoD10Window = tk.Toplevel()
			tamañoD10Window.iconbitmap(bitmap='icons\\agua.ico')
			tamañoD10Window.geometry("1000x200") 
			tamañoD10Window.resizable(0,0)	
			tamañoD10Window.configure(background="#9DC4AA")
			coeficienteDUFrame10=LabelFrame(tamañoD10Window, text="Tamaño Efectio d{} del medio filtrante".format(getSub(f"{numero}")), font=("Yu Gothic bold", 11))
			coeficienteDUFrame10.pack(side=TOP, fill=BOTH,expand=True)
			
			#Frame Treeview
			coeficienteDUFrame10 = Frame(coeficienteDUFrame10)
			coeficienteDUFrame10.pack(side=LEFT,fill=BOTH,expand=TRUE)

			#Scrollbar
			sedScrollX=Scrollbar(coeficienteDUFrame10,orient=HORIZONTAL)
			sedScrollX.pack(side=BOTTOM, fill=X)
			sedScrollY=Scrollbar(coeficienteDUFrame10,orient=VERTICAL)
			sedScrollY.pack(side=LEFT, fill=Y)

			#Treeview
			arbolCoeficienteDU10= ttk.Treeview(coeficienteDUFrame10,selectmode=BROWSE, height=2,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
			arbolCoeficienteDU10.pack(side=TOP, fill=BOTH, expand=TRUE)

			sedScrollX.configure(command=arbolCoeficienteDU10.xview)
			sedScrollY.configure(command=arbolCoeficienteDU10.yview)
			#Define columnas.
			arbolCoeficienteDU10["columns"]= (
			"Valores para referencia",
			"Tamaño de abertura del tamiz [mm]",
			"Acumulado de arena que pasa [%]",
			"Tamaño d{} [mm]".format(getSub(f"{numero}"))
			)

			#Headings
			arbolCoeficienteDU10.heading("#0",text="ID", anchor=CENTER)
			for col in arbolCoeficienteDU10["columns"]:
				arbolCoeficienteDU10.heading(col, text=col,anchor=CENTER)
		
			
			for i in range(0,len(arbolCoeficienteDU10["columns"])) :
					arbolCoeficienteDU10.column(f"#{i}",width=500, stretch=False)	
			arbolCoeficienteDU10.column("#4",width=600, stretch=True)	
			arbolCoeficienteDU10.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolCoeficienteDU10.tag_configure("oddrow", background= "#1FCCDB")
			arbolCoeficienteDU10.tag_configure("evenrow", background= "#9DC4AA")

			lista1=list()
			lista2=list()
			lista1.append("(x1,y1)")
			lista1.append(x1)
			lista1.append(y1)
			lista1.append(calculo2CU(numero,x1,y1,x2,y2))
			lista2.append("(x2,y2)")
			lista2.append(x2)
			lista2.append(y2)
			lista2.append(calculo2CU(numero,x1,y1,x2,y2))
			listaInsertar=[lista1,lista2]
			
			for elemento in listaInsertar:
				newDataTreeview(arbolCoeficienteDU10,elemento)



		coeficienteDUWindow.mainloop()

	def calcularPEArena(listaNTamiz,listaARetenida,listaE,valorTemperatura):
		listaEU=list()

		
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==5:
					if elemento.get() == "Seleccione el tipo de grano de arena":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de grano de arena")
						return None
					elif elemento.get() == "Seleccione la tasa para calcular":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar la tasa")
						return None
					else:
						
						if i==0:
							listaEU.append(elemento.get())
						else:
							TasaCopy = elemento.get()
							
						i=i+1
				else:
					i=i+1
					listaEU.append(float(elemento.get()))
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None
			
		listaEU.append(float(valorTemperatura))
		

		

		estimacionPerdidaArenaCalculoWindow = tk.Toplevel()
		estimacionPerdidaArenaCalculoWindow.iconbitmap(bitmap='icons\\agua.ico')
		estimacionPerdidaArenaCalculoWindow.geometry("1000x500") 
		estimacionPerdidaArenaCalculoWindow.resizable(0,0)	
		estimacionPerdidaArenaCalculoWindow.configure(background="#9DC4AA")
		global contadorFiltro

		if listaEU[0] != "Afilada":

			##Panel:
			panelFiltro = ttk.Notebook(estimacionPerdidaArenaCalculoWindow)
			panelFiltro.pack(fill=BOTH, expand=TRUE)
			###########Frame Principal1
			estimacionPerdidaArenaFHFrame=LabelFrame(panelFiltro, text=f"Estimación de la pérdida de energía en le lecho filtrante de arena limpio a {TasaCopy.lower()}.", font=("Yu Gothic bold", 11))
			estimacionPerdidaArenaFHFrame.pack(side=TOP, fill=BOTH,expand=True)
			panelFiltro.add(estimacionPerdidaArenaFHFrame,text="Fair Hatch")
			#Frame Treeview
			arbolEstimacionPerdidaArenaFH_frame = LabelFrame(estimacionPerdidaArenaFHFrame, text="Fair Hatch", font=("Yu Gothic bold", 11))
			arbolEstimacionPerdidaArenaFH_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

			#Scrollbar
			sedScrollX=Scrollbar(arbolEstimacionPerdidaArenaFH_frame,orient=HORIZONTAL)
			sedScrollX.pack(side=BOTTOM, fill=X)
			sedScrollY=Scrollbar(arbolEstimacionPerdidaArenaFH_frame,orient=VERTICAL)
			sedScrollY.pack(side=LEFT, fill=Y)

			#Treeview
			arbolEstimacionPerdidaArenaFH= ttk.Treeview(arbolEstimacionPerdidaArenaFH_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
			arbolEstimacionPerdidaArenaFH.pack(side=TOP, fill=BOTH, expand=TRUE)

			sedScrollX.configure(command=arbolEstimacionPerdidaArenaFH.xview)
			sedScrollY.configure(command=arbolEstimacionPerdidaArenaFH.yview)
			#Define columnas.
			arbolEstimacionPerdidaArenaFH["columns"]= (
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"arena retenida/tamaño promedio geométrico [1/(m^2)]",
			"Fair-Hatch"
			)

			#Headings
			arbolEstimacionPerdidaArenaFH.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaFH["columns"]:
				arbolEstimacionPerdidaArenaFH.heading(col, text=col,anchor=CENTER)	

			for i in range(0,len(arbolEstimacionPerdidaArenaFH["columns"])+1) :
					arbolEstimacionPerdidaArenaFH.column(f"#{i}",width=500, stretch=False)	
			arbolEstimacionPerdidaArenaFH.column("#6",width=600, stretch=False)
			arbolEstimacionPerdidaArenaFH.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolEstimacionPerdidaArenaFH.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaFH.tag_configure("evenrow", background= "#9DC4AA")
			
			################Frame principal2
			estimacionPerdidaArenaCKFrame=LabelFrame(panelFiltro, text="Estimación de la pérdida de energía en le lecho filtrante de arena limpio.", font=("Yu Gothic bold", 11))
			estimacionPerdidaArenaCKFrame.pack(side=TOP, fill=BOTH,expand=True)
			panelFiltro.add(estimacionPerdidaArenaCKFrame,text="Carmen-Kozeny")
			#Frame Treeview
			arbolEstimacionPerdidaArenaCK_frame = LabelFrame(estimacionPerdidaArenaCKFrame, text="Carmen-Kozeny", font=("Yu Gothic bold", 11))
			arbolEstimacionPerdidaArenaCK_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

			#Scrollbar
			sedScrollX=Scrollbar(arbolEstimacionPerdidaArenaCK_frame,orient=HORIZONTAL)
			sedScrollX.pack(side=BOTTOM, fill=X)
			sedScrollY=Scrollbar(arbolEstimacionPerdidaArenaCK_frame,orient=VERTICAL)
			sedScrollY.pack(side=LEFT, fill=Y)

			#Treeview
			arbolEstimacionPerdidaArenaCK= ttk.Treeview(arbolEstimacionPerdidaArenaCK_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
			arbolEstimacionPerdidaArenaCK.pack(side=TOP, fill=BOTH, expand=TRUE)

			sedScrollX.configure(command=arbolEstimacionPerdidaArenaCK.xview)
			sedScrollY.configure(command=arbolEstimacionPerdidaArenaCK.yview)
			#Define columnas.
			arbolEstimacionPerdidaArenaCK["columns"]= (
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"Número de Reynolds", 
			"Factor de fricción",
			#Pendiente
			"NOMBREPREG",
			"Pérdida de cabeza hidráulica total",
			"NombrePREG",
			"Coeficiente de permeabilidad",
			)

			#Headings
			arbolEstimacionPerdidaArenaCK.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaCK["columns"]:
				arbolEstimacionPerdidaArenaCK.heading(col, text=col,anchor=CENTER)	

			for i in range(0,len(arbolEstimacionPerdidaArenaCK["columns"])+1) :
					arbolEstimacionPerdidaArenaCK.column(f"#{i}",width=500, stretch=False)	
			arbolEstimacionPerdidaArenaCK.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolEstimacionPerdidaArenaCK.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaCK.tag_configure("evenrow", background= "#9DC4AA")

			##########Frame principal3
			estimacionPerdidaArenaRFrame=LabelFrame(panelFiltro, text="Estimación de la pérdida de energía en le lecho filtrante de arena limpio.", font=("Yu Gothic bold", 11))
			estimacionPerdidaArenaRFrame.pack(side=TOP, fill=BOTH,expand=True)
			panelFiltro.add(estimacionPerdidaArenaRFrame,text="Rose")
			#Frame Treeview
			arbolEstimacionPerdidaArenaR_frame = LabelFrame(estimacionPerdidaArenaRFrame, text="Rose.", font=("Yu Gothic bold", 11))
			arbolEstimacionPerdidaArenaR_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

			#Scrollbar
			sedScrollX=Scrollbar(arbolEstimacionPerdidaArenaR_frame,orient=HORIZONTAL)
			sedScrollX.pack(side=BOTTOM, fill=X)
			sedScrollY=Scrollbar(arbolEstimacionPerdidaArenaR_frame,orient=VERTICAL)
			sedScrollY.pack(side=LEFT, fill=Y)

			#Treeview
			arbolEstimacionPerdidaArenaR= ttk.Treeview(arbolEstimacionPerdidaArenaR_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
			arbolEstimacionPerdidaArenaR.pack(side=TOP, fill=BOTH, expand=TRUE)

			sedScrollX.configure(command=arbolEstimacionPerdidaArenaR.xview)
			sedScrollY.configure(command=arbolEstimacionPerdidaArenaR.yview)
			#Define columnas.
			arbolEstimacionPerdidaArenaR["columns"]= (
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"Número de Reynolds",
			"PREGUNTAR",
			"PREGUNTAR",
			"PREGUNTAR"
			)

			#Headings
			arbolEstimacionPerdidaArenaR.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaR["columns"]:
				arbolEstimacionPerdidaArenaR.heading(col, text=col,anchor=CENTER)	

			for i in range(0,len(arbolEstimacionPerdidaArenaR["columns"])+1) :
					arbolEstimacionPerdidaArenaR.column(f"#{i}",width=500, stretch=False)	
			arbolEstimacionPerdidaArenaR.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolEstimacionPerdidaArenaR.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaR.tag_configure("evenrow", background= "#9DC4AA")

			

			############Insersión datos.

			
			contadorFiltro = 0
			
			listaEntradaTemp1=list()
			listaEntradaTemp2=list()
			listaEntradaTemp3=list()
			datosSalida=list()
			
					
			

			if listaEU[0] == "Angular":
				listaEU.append(0.73)
				listaEU.append(0.81)
				listaEU.append(7.7)
				listaEU.append(6.9)

			elif listaEU[0] == "Afilada":
				listaEU.append(0)
				listaEU.append(0.85)
				listaEU.append(0)
				listaEU.append(6.2)

			elif listaEU[0] == "Erosionada":
				listaEU.append(0.75)
				listaEU.append(0.89)
				listaEU.append(6.4)
				listaEU.append(5.7)

			elif listaEU[0] == "Redondeada":
				listaEU.append(0.82)
				listaEU.append(0.91)
				listaEU.append(6.1)
				listaEU.append(5.5)

			elif listaEU[0] == "Esférica":
				listaEU.append(1)
				listaEU.append(1)
				listaEU.append(6)
				listaEU.append(6)

			
			
				

			#Tabla Tamaño Abertura Tamiz
			TamañoTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
			TamañoAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
			tablaTamañoAberturaTamiz=dict()
			for ind in range(0, len(TamañoTamiz)):
				tablaTamañoAberturaTamiz[TamañoTamiz[ind]] = TamañoAbertura[ind]

			#Tabla Temperatura Viscocidad
			valorTemperaturas=list()
			tablaTemperaturaViscocidad=dict()
			tablaTemperaturaDensidad= dict()
			tablaTemperaturaViscosidadDinamica = dict()
			for i in range(0,36):
				valorTemperaturas.append(i)
			
			valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
			,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
			1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

			valorDensidad= [999.82, 999.89, 999.94, 999.98, 1000.0, 1000.0, 999.99, 999.96, 999.91, 999.85, 999.77, 999.68, 999.58, 999.46, 999.33, 999.19, 999.03, 998.86, 998.68, 998.49, 998.29, 998.08, 997.86, 997.62, 997.38, 997.13, 
			996.86, 996.59, 996.31, 996.02, 995.71, 995.41, 995.09, 994.76, 994.43, 994.08]
			
			valorViscosidadDinamica = [0.001792, 0.001731, 0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 0.001083, 0.001056, 0.00103
			, 0.001005, 0.000981, 0.000958, 0.000936, 0.000914, 0.000894, 0.000874, 0.000855, 0.000836, 0.000818, 0.000801, 0.000784, 0.000768, 0.000752, 0.000737, 0.000723]  

			for ind in range(0,len(valorTemperaturas)):
				tablaTemperaturaViscocidad[valorTemperaturas[ind]]=valorViscocidad[ind]
				tablaTemperaturaDensidad[valorTemperaturas[ind]]= valorDensidad[ind]
				tablaTemperaturaViscosidadDinamica[valorTemperaturas[ind]] = valorViscosidadDinamica[ind]

			listaEU[5]=tablaTemperaturaViscocidad[listaEU[5]]
			
			
			listaEU.append(TasaCopy)

			if listaEU[10] == "Tasa media":
				listaEU[10]=120
			elif listaEU[10] == "Tasa máxima":
				listaEU[10]=150
			
			
			#OrganizandoListaNTamiz: Extremos 
			listaNTamizExtremoD=list()
			listaNTamizExtremoI=list()
			listaNTamizSinRepeticion=list()
			for num in range(0,len(listaNTamiz)):
				if num%2==0:
					listaNTamizExtremoI.append(listaNTamiz[num])	
				else:
					listaNTamizExtremoD.append(listaNTamiz[num])
			#Lista sin repetición.
			guardado=listaNTamiz[0]
			listaNTamizSinRepeticion.append(guardado)
			for elemento in listaNTamiz:
				if elemento != guardado:
					listaNTamizSinRepeticion.append(elemento)
					guardado=elemento


			
			def tamañoPromedioGeometrico(d1,d2):
				return sqrt(d1*d2)

			

			"""	 
			#ListaOrden
			listaEU=[0 = TipoGranoArena, 1 = profundidadLechoFijoArena, 2 = densidadRelativaArena,
			3 = porosidadLechoFijo,4 = constanteFiltracionFH, 5 = temperatura, 6 = Coeficiente de filtración,
			7 = Factor de esfericidad (FH - CK), 8 = Factor de forma (FH), 9 = Factor de forma (Rose)]

			"""

			#############DATOS

			#DatosPara1

			'''(
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"arena retenida/tamaño promedio geométrico [1/(m^2)]",
			"Fair-Hatch"
			)
			'''
			sumaFH=0
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp1.clear()
				
				arenaRenetinda=listaARetenida[ind]
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				valorEnSuma= (arenaRenetinda/100)/((tamañoPromedioGeo/1000)**2)
				sumaFH=sumaFH+valorEnSuma
			
			

			contadorFiltro=0

			valorFH= (listaEU[4]*listaEU[5])*((1-listaEU[3])**2)*listaEU[1]*(listaEU[10]/86400.0)*((6/listaEU[6])**2)*(1/9.806)*((1/listaEU[3])**3)*sumaFH
			

			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp1.clear()
				listaEntradaTemp1.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp1.append(arenaRenetinda)
				

				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				listaEntradaTemp1.append(tamañoSuperior)
				listaEntradaTemp1.append(tamañoInferior)
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				listaEntradaTemp1.append(tamañoPromedioGeo)
				valorEnSuma= (arenaRenetinda/100)/((tamañoPromedioGeo/1000)**2)
				listaEntradaTemp1.append(valorEnSuma)
				
				listaEntradaTemp1.append(valorFH)
				newDataTreeview(arbolEstimacionPerdidaArenaFH, listaEntradaTemp1)
		
				
			
			#DatosPara2
			'''(
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"Número de Reynolds", 
			"Factor de fricción",
			#Pendiente
			"NOMBREPREG",
			"Pérdida de cabeza hidráulica total",
			"NombrePREG",
			"Coeficiente de permeabilidad",
			)
			'''

			
			

			contadorFiltro=0
			sumaCK=0
			
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp2.clear()
				arenaRenetinda=listaARetenida[ind]
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				Reynolds2=listaEU[6]*(tamañoPromedioGeo/1000)*(listaEU[10]/86400)*(1/listaEU[5])
				friccion2=150*((1-listaEU[3])/Reynolds2)+1.75
				valorSuma2A= friccion2*(arenaRenetinda/100)*(1/(tamañoPromedioGeo/1000))
				sumaCK=sumaCK+valorSuma2A
			
			valorCK=(1/listaEU[6])*(1-listaEU[3])*((1/listaEU[3])**3)*listaEU[1]*((listaEU[10]/86400)**2)*(1/9.806)*sumaCK
		
			
			sumaCKsinF=0
			
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp2.clear()
				arenaRenetinda=listaARetenida[ind]
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				Reynolds2_2=listaEU[6]*(tamañoPromedioGeo/1000)*(listaEU[10]/86400)*(1/listaEU[5])
				valorSuma2_2= (arenaRenetinda/100)*(1/(tamañoPromedioGeo/1000))
				sumaCKsinF=sumaCKsinF+valorSuma2_2
			
			
			
			valorCoefPermeabilidad = (tablaTemperaturaDensidad[valorTemperatura]*9.806)*(1/tablaTemperaturaViscosidadDinamica[valorTemperatura])*(1/listaEU[4])*((1/listaEU[8])**2)*(listaEU[3]**3)*(1/(1-listaEU[3]))*(sumaCKsinF**(-2))


			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp2.clear()
				listaEntradaTemp2.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp2.append(arenaRenetinda)
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				listaEntradaTemp2.append(tamañoSuperior)
				listaEntradaTemp2.append(tamañoInferior)
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				listaEntradaTemp2.append(tamañoPromedioGeo)
				Reynolds2=listaEU[6]*(tamañoPromedioGeo/1000)*(listaEU[10]/86400)*(1/listaEU[5])
				listaEntradaTemp2.append(Reynolds2)
				friccion2=150*((1-listaEU[3])/Reynolds2)+1.75
				listaEntradaTemp2.append(friccion2)
				valorSuma2= friccion2*(arenaRenetinda/100)*(1/(tamañoPromedioGeo/1000))
				listaEntradaTemp2.append(valorSuma2)
				listaEntradaTemp2.append(valorCK)
				valorSuma2_2= (arenaRenetinda/100)*(1/(tamañoPromedioGeo/1000))
				listaEntradaTemp2.append(valorSuma2_2)
				listaEntradaTemp2.append(valorCoefPermeabilidad)


				newDataTreeview(arbolEstimacionPerdidaArenaCK, listaEntradaTemp2)
				
			#DatosPara3

			'''(
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"Número de Reynolds",
			"PREGUNTAR",
			"PREGUNTAR",
			"PREGUNTAR"
			)
			'''

			"""	 
			#ListaOrden
			listaEU=[0 = TipoGranoArena, 1 = profundidadLechoFijoArena, 2 = densidadRelativaArena,
			3 = porosidadLechoFijo,4 = constanteFiltracionFH, 5 = temperatura, 6 = Factor de esfericidad (FH - CK),
			7 = Factor de esfericidad (Rose), 8 = Factor de forma (FH), 9 = Factor de forma (Rose), 10=Vel]

			"""

			contadorFiltro=0
			sumaR=0

			for ind in range(0, len(listaARetenida)):
				arenaRenetinda=listaARetenida[ind]
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				Reynolds3= (tamañoPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				Suma3=Cd*(arenaRenetinda/100)*(1000/tamañoPromedioGeo)
				sumaR= sumaR + Suma3
			

			valorR= 1.067*((listaEU[10]/86400.0)**2)*listaEU[1]*(1/9.806)*((1/listaEU[3])**4)*(1/listaEU[7])*sumaR

			
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp3.clear()
				listaEntradaTemp3.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp3.append(arenaRenetinda)
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				listaEntradaTemp3.append(tamañoSuperior)
				listaEntradaTemp3.append(tamañoInferior)
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				listaEntradaTemp3.append(tamañoPromedioGeo)
				Reynolds3= (tamañoPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				listaEntradaTemp3.append(Reynolds3)
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				listaEntradaTemp3.append(Cd)
				Suma3=Cd*(arenaRenetinda/100)*(1000/tamañoPromedioGeo)
				listaEntradaTemp3.append(Suma3)
				listaEntradaTemp3.append(valorR)
				newDataTreeview(arbolEstimacionPerdidaArenaR, listaEntradaTemp3)

			estimacionPerdidaArenaCalculoWindow.mainloop()
			
		else: #Inicio
			
			
			
			
			##Panel:
			panelFiltro = ttk.Notebook(estimacionPerdidaArenaCalculoWindow)
			panelFiltro.pack(fill=BOTH, expand=TRUE)
			
			##########Frame principal3
			estimacionPerdidaArenaRFrame=LabelFrame(panelFiltro, text="Estimación de la pérdida de energía en le lecho filtrante de arena limpio.", font=("Yu Gothic bold", 11))
			estimacionPerdidaArenaRFrame.pack(side=TOP, fill=BOTH,expand=True)
			panelFiltro.add(estimacionPerdidaArenaRFrame,text="Rose")
			#Frame Treeview
			arbolEstimacionPerdidaArenaR_frame = LabelFrame(estimacionPerdidaArenaRFrame, text="Rose.", font=("Yu Gothic bold", 11))
			arbolEstimacionPerdidaArenaR_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

			#Scrollbar
			sedScrollX=Scrollbar(arbolEstimacionPerdidaArenaR_frame,orient=HORIZONTAL)
			sedScrollX.pack(side=BOTTOM, fill=X)
			sedScrollY=Scrollbar(arbolEstimacionPerdidaArenaR_frame,orient=VERTICAL)
			sedScrollY.pack(side=LEFT, fill=Y)

			#Treeview
			arbolEstimacionPerdidaArenaR= ttk.Treeview(arbolEstimacionPerdidaArenaR_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
			arbolEstimacionPerdidaArenaR.pack(side=TOP, fill=BOTH, expand=TRUE)

			sedScrollX.configure(command=arbolEstimacionPerdidaArenaR.xview)
			sedScrollY.configure(command=arbolEstimacionPerdidaArenaR.yview)
			#Define columnas.
			arbolEstimacionPerdidaArenaR["columns"]= (
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"Número de Reynolds",
			"PREGUNTAR",
			"PREGUNTAR",
			"PREGUNTAR"
			)

			#Headings
			arbolEstimacionPerdidaArenaR.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaR["columns"]:
				arbolEstimacionPerdidaArenaR.heading(col, text=col,anchor=CENTER)	

			for i in range(0,len(arbolEstimacionPerdidaArenaR["columns"])+1) :
					arbolEstimacionPerdidaArenaR.column(f"#{i}",width=500, stretch=False)	
			arbolEstimacionPerdidaArenaR.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolEstimacionPerdidaArenaR.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaR.tag_configure("evenrow", background= "#9DC4AA")

			

			############Insersión datos.

			
			contadorFiltro = 0
			
			
			listaEntradaTemp3=list()
			datosSalida=list()
			
					
			


			if listaEU[0] == "Afilada":
				listaEU.append(0)
				listaEU.append(0.85)
				listaEU.append(0)
				listaEU.append(6.2)
			
			
				

			#Tabla Tamaño Abertura Tamiz
			TamañoTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
			TamañoAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
			tablaTamañoAberturaTamiz=dict()
			for ind in range(0, len(TamañoTamiz)):
				tablaTamañoAberturaTamiz[TamañoTamiz[ind]] = TamañoAbertura[ind]

			#Tabla Temperatura Viscocidad
			valorTemperaturas=list()
			tablaTemperaturaViscocidad=dict()
			tablaTemperaturaDensidad= dict()
			tablaTemperaturaViscosidadDinamica = dict()
			for i in range(0,36):
				valorTemperaturas.append(i)
			
			valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
			,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
			1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

			valorDensidad= [999.82, 999.89, 999.94, 999.98, 1000.0, 1000.0, 999.99, 999.96, 999.91, 999.85, 999.77, 999.68, 999.58, 999.46, 999.33, 999.19, 999.03, 998.86, 998.68, 998.49, 998.29, 998.08, 997.86, 997.62, 997.38, 997.13, 
			996.86, 996.59, 996.31, 996.02, 995.71, 995.41, 995.09, 994.76, 994.43, 994.08]
			
			valorViscosidadDinamica = [0.001792, 0.001731, 0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 0.001083, 0.001056, 0.00103
			, 0.001005, 0.000981, 0.000958, 0.000936, 0.000914, 0.000894, 0.000874, 0.000855, 0.000836, 0.000818, 0.000801, 0.000784, 0.000768, 0.000752, 0.000737, 0.000723]  

			for ind in range(0,len(valorTemperaturas)):
				tablaTemperaturaViscocidad[valorTemperaturas[ind]]=valorViscocidad[ind]
				tablaTemperaturaDensidad[valorTemperaturas[ind]]= valorDensidad[ind]
				tablaTemperaturaViscosidadDinamica[valorTemperaturas[ind]] = valorViscosidadDinamica[ind]

			listaEU[5]=tablaTemperaturaViscocidad[listaEU[5]]
			
			
			listaEU.append(TasaCopy)

			

			if listaEU[10] == "Tasa media":
				listaEU[10]=120
			elif listaEU[10] == "Tasa máxima":
				listaEU[10]=150
			
			
			#OrganizandoListaNTamiz: Extremos 
			listaNTamizExtremoD=list()
			listaNTamizExtremoI=list()
			listaNTamizSinRepeticion=list()
			for num in range(0,len(listaNTamiz)):
				if num%2==0:
					listaNTamizExtremoI.append(listaNTamiz[num])	
				else:
					listaNTamizExtremoD.append(listaNTamiz[num])
			#Lista sin repetición.
			guardado=listaNTamiz[0]
			listaNTamizSinRepeticion.append(guardado)
			for elemento in listaNTamiz:
				if elemento != guardado:
					listaNTamizSinRepeticion.append(elemento)
					guardado=elemento


			
			def tamañoPromedioGeometrico(d1,d2):
				return sqrt(d1*d2)

	
				
			#DatosPara3

			'''(
			"Número de tamiz",
			"Arena retenida [%]", 
			"Tamaño de abertura del tamiz superior [mm]", 
			"Tamaño de abertura del tamiz inferior [mm]",
			"Tamaño promedio geométrico [mm]",
			"Número de Reynolds",
			"PREGUNTAR",
			"PREGUNTAR",
			"PREGUNTAR"
			)
			'''

			"""	 
			#ListaOrden
			listaEU=[0 = TipoGranoArena, 1 = profundidadLechoFijoArena, 2 = densidadRelativaArena,
			3 = porosidadLechoFijo,4 = constanteFiltracionFH, 5 = temperatura, 6 = Factor de esfericidad (FH - CK),
			7 = Factor de esfericidad (Rose), 8 = Factor de forma (FH), 9 = Factor de forma (Rose), 10=Vel]

			"""

			contadorFiltro=0
			sumaR=0

			for ind in range(0, len(listaARetenida)):
				arenaRenetinda=listaARetenida[ind]
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				Reynolds3= (tamañoPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				Suma3=Cd*(arenaRenetinda/100)*(1000/tamañoPromedioGeo)
				sumaR= sumaR + Suma3
			
			
			
			valorR= 1.067*((listaEU[10]/86400.0)**2)*listaEU[1]*(1/9.806)*(1/((listaEU[3])**4))*(1/listaEU[7])*sumaR

			
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp3.clear()
				listaEntradaTemp3.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp3.append(arenaRenetinda)
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tamañoSuperior= tablaTamañoAberturaTamiz[extremoIzquierdo]
				tamañoInferior= tablaTamañoAberturaTamiz[extremoDerecho]
				listaEntradaTemp3.append(tamañoSuperior)
				listaEntradaTemp3.append(tamañoInferior)
				tamañoPromedioGeo = tamañoPromedioGeometrico(tamañoSuperior,tamañoInferior)
				listaEntradaTemp3.append(tamañoPromedioGeo)
				Reynolds3= (tamañoPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				listaEntradaTemp3.append(Reynolds3)
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				listaEntradaTemp3.append(Cd)
				Suma3=Cd*(arenaRenetinda/100)*(1000/tamañoPromedioGeo)
				listaEntradaTemp3.append(Suma3)
				listaEntradaTemp3.append(valorR)
				newDataTreeview(arbolEstimacionPerdidaArenaR, listaEntradaTemp3)

			estimacionPerdidaArenaCalculoWindow.mainloop()

				
			







	def estimacionPerdidaEnergiaArena(lista1,lista2,optnValue):
		listaNTamizTemp=lista1.copy()
		listaARetenidaTemp=lista2.copy()
		listaNTamiz=list()
		listaARetenida=list()
		
		
		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de los números de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de la arena retenida.")
			return None
		if optnValue.get() == "Seleccione la temperatura":
			messagebox.showwarning(title="Error", message="Hace falta elegir el valor de la temperatura del agua a tratar.")
			return None
		else:
			valorTemperatura= int(optnValue.get())

		for ind in range(0, len(listaNTamizTemp)):
			if listaNTamizTemp[ind].get() == "" and ind%2==0:
				break
			elif listaNTamizTemp[ind].get() == "" and ind%2 != 0:
				messagebox.showwarning(title="Error", message="Hace falta el rango de la derecha de alguna entrada.")
				return None
			else:
				try:
					CountControl=0
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m: 
							CountControl=CountControl+1
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m and CountControl==18:
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores estándar para número de tamiz. Pulse el botón para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de número de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None


		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de número de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None


		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento


		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None

		estimacionPerdidaArenaWindow = tk.Toplevel()
		estimacionPerdidaArenaWindow.iconbitmap(bitmap='icons\\agua.ico')
		estimacionPerdidaArenaWindow.geometry("800x600") 
		estimacionPerdidaArenaWindow.resizable(0,0)	
		estimacionPerdidaArenaWindow.configure(background="#9DC4AA")

		frameEstimacionPerdidaArena= LabelFrame(estimacionPerdidaArenaWindow, text="Estimación de la pérdida de energía en el lecho filtrante de arena limpio",font=("Yu Gothic bold", 11))
		frameEstimacionPerdidaArena.pack(side=TOP,fill=BOTH,expand=True)
		
		def newEntryFiltroP(lista):
			for elemento in lista:
				if elemento == TipoGranoArena:
					TipoGranoArena.set("Seleccione el tipo de grano de arena")
				elif elemento ==Tasa:
					Tasa.set("Seleccione la tasa para calcular")
				else:
					elemento.delete(0, END)
		
		
		#Input
		lista_inputs=["Tasa máxima de filtración [m/d]",
		"Profundidad del lecho fijo de arena",
		"Densidad relativa de la arena",
		"Porosidad del lecho fijo",
		"Constante de filtración (Fair-Hatch)",
		"Factor de forma (Fair-Hatch)",
		"Factor de forma (Carmen -Kozeny)",
		"Factor de forma (Rose)"
					]
	
		inicialLabel=Label(frameEstimacionPerdidaArena, text="Características del lecho filtrante de arena: ",font=("Yu Gothic bold",10))

		
		
		
		TipoGranoArena = StringVar()
		TipoGranoArena.set("Seleccione el tipo de grano de arena")
		listaValoresTemp=["Angular", "Afilada", "Erosionada", "Redondeada", "Esférica"]
		TipoGranoArenaName = OptionMenu(frameEstimacionPerdidaArena, TipoGranoArena, *listaValoresTemp)

		Tasa = StringVar()
		Tasa.set("Seleccione la tasa para calcular")
		listaValoresTemp1=["Tasa media", "Tasa máxima"]
		TasaName = OptionMenu(frameEstimacionPerdidaArena, Tasa, *listaValoresTemp1)
		


		profundidadLechoFijoArenaLabel = Label(frameEstimacionPerdidaArena, text="L = Profundidad del lecho fijo de arena [m]:", font =("Yu Gothic",9))
		
		densidadRelativaArenaLabel = Label(frameEstimacionPerdidaArena, text="S{} = Densidad relativa de la arena:".format(getSub("s")), font =("Yu Gothic",9))
		porosidadLechoFijoLabel = Label(frameEstimacionPerdidaArena, text=u"\u03B5 ,e = Porosidad del lecho fijo:", font =("Yu Gothic",9))
		constanteFiltracionFHLabel = Label(frameEstimacionPerdidaArena, text=u"\u03BA = Constante de Filtración (Fair-Hatch):", font =("Yu Gothic",9))
		
		
		

		profundidadLechoFijoArena = Entry(frameEstimacionPerdidaArena)
		densidadRelativaArena = Entry(frameEstimacionPerdidaArena)
		porosidadLechoFijo = Entry(frameEstimacionPerdidaArena)
		constanteFiltracionFH = Entry(frameEstimacionPerdidaArena)
		
		#Borrar

		profundidadLechoFijoArena.insert(0,"0.64")
		densidadRelativaArena.insert(0,"2.65")
		porosidadLechoFijo.insert(0,"0.45")
		constanteFiltracionFH.insert(0,"5")
		TipoGranoArena.set("Erosionada")
		Tasa.set("Tasa media")
	

		listaEntradas=[TipoGranoArena, profundidadLechoFijoArena, densidadRelativaArena,
		porosidadLechoFijo,constanteFiltracionFH,Tasa]

		listaLabel=[inicialLabel, TipoGranoArenaName, profundidadLechoFijoArenaLabel, densidadRelativaArenaLabel,
		porosidadLechoFijoLabel,constanteFiltracionFHLabel, TasaName]
		
		alturaInicialLabel=20
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=47
		
		alturaInicialEntradas=67
		i=0
		for elemento in listaEntradas:
				if i == 0 or i==5:
					i=i+1
					alturaInicialEntradas+=47
				else: 
					i=i+1
					elemento.place(x=400,y=alturaInicialEntradas)
					alturaInicialEntradas+=47
		
		#Botones.
		botonCalcular = HoverButton(frameEstimacionPerdidaArena, text="Calcular la estimación de la pérdida de energía en el lecho filtrante de arena limpio.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularPEArena(listaNTamiz,listaARetenida,listaEntradas,valorTemperatura) )
		botonNewEntry = HoverButton(frameEstimacionPerdidaArena, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50
		estimacionPerdidaArenaWindow.mainloop()

	def valorCoeficienteDeUniformidad(lista1,lista2):
		
		def buscarEnTabla(NumTamiz,tablaDic):
			return tablaDic[NumTamiz]
		
		listaNTamizTemp=lista1.copy()
		listaARetenidaTemp=lista2.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de los números de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de la arena retenida.")
			return None

		for ind in range(0, len(listaNTamizTemp)):
			if listaNTamizTemp[ind].get() == "" and ind%2==0:
				break
			elif listaNTamizTemp[ind].get() == "" and ind%2 != 0:
				messagebox.showwarning(title="Error", message="Hace falta el rango de la derecha de alguna entrada.")
				return None
			else:
				try:
					CountControl=0
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m: 
							CountControl=CountControl+1
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m and CountControl==18:
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores estándar para número de tamiz. Pulse el botón para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de número de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de número de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento
		
		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None

		listaEntradaTemp=list()
		datosSalida=list()
		
		
		
		#Tabla Tamaño Abertura Tamiz
		TamañoTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
		TamañoAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
		tablaTamañoAberturaTamiz=dict()
		for ind in range(0, len(TamañoTamiz)):
			tablaTamañoAberturaTamiz[TamañoTamiz[ind]] = TamañoAbertura[ind]

		#Acumulado arena que pasa.
		def acumuladoArenaQuePasa(indice):
			suma=0
			for elemento in range(0,indice+1):
				suma= suma+listaARetenida[elemento]
			return 100.0-suma
		#Calculando acumulado:
		listaAcumuladoArenaDescendente=list()
		for ind in range(0, len(listaARetenida)):
			if ind != len(listaARetenida)-1:
				listaAcumuladoArenaDescendente.append(acumuladoArenaQuePasa(ind))
			else:
				listaAcumuladoArenaDescendente.append(0)

		listaAcumuladoArenaAscendente = listaAcumuladoArenaDescendente.copy()
		listaAcumuladoArenaAscendente.reverse()

		#OrganizandoListaNTamiz
		listaNTamizExtremo=list()
		listaNTamizSinRepeticion=list()
		for num in range(0,len(listaNTamiz)):
			if num%2==0:
				pass	
			else:
				listaNTamizExtremo.append(listaNTamiz[num])
		guardado=listaNTamiz[0]
		listaNTamizSinRepeticion.append(guardado)
		for elemento in listaNTamiz:
			if elemento != guardado:
				listaNTamizSinRepeticion.append(elemento)
				guardado=elemento
	
				

		longListaARetenida=len(listaARetenida)-1
		for ind in range(0, len(listaARetenida)):
			listaEntradaTemp.clear()
			
			listaEntradaTemp.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
			extremoDerecho=listaNTamizExtremo[ind]
			listaEntradaTemp.append(listaARetenida[ind])
			listaEntradaTemp.append(extremoDerecho)
			listaEntradaTemp.append(tablaTamañoAberturaTamiz[extremoDerecho])
			listaEntradaTemp.append(listaAcumuladoArenaDescendente[ind])
			listaEntradaTemp.append(tablaTamañoAberturaTamiz[listaNTamizExtremo[longListaARetenida-ind]])
			listaEntradaTemp.append(listaAcumuladoArenaAscendente[ind])
			listaIntermedia = listaEntradaTemp.copy()
			datosSalida.append(listaIntermedia)
		
		abAcDic= dict()
		for ind in range(0,len(datosSalida)):
			abAcDic[datosSalida[ind][6]]=datosSalida[ind][5]
		
	
		def tamañoEfectivod1(numero,dic):
			elementoAnterior=dic[0]
			for elemento in dic:
				if elemento <= numero and elemento>=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda

		def tamañoEfectivod2(numero,dic):
			elementoAnterior=100
			for elemento in dic:
				if elemento >= numero and elemento<=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda
		def tamañoEfectivod(numero,dic):
			return[tamañoEfectivod1(numero,dic), tamañoEfectivod2(numero,dic)]

		def calculo1CU(numero,x1,y1,x2,y2):
			return(log10(x1)+(((numero-y1)/(y2-y1))*log10(x2/x1)))
		def calculo2CU(numero,x1,y1,x2,y2):
			return (10**(calculo1CU(numero,x1,y1,x2,y2)))
		
		#Calculo Tamaño Efectivo d10:
		listaAcumuladoCU10=tamañoEfectivod(10,abAcDic)
		y1=listaAcumuladoCU10[0]
		y2=listaAcumuladoCU10[1]
		x1=abAcDic[y1]
		x2=abAcDic[y2]
		d10= calculo2CU(10,x1,y1,x2,y2)
		listaAcumuladoCU60=tamañoEfectivod(60,abAcDic)
		Y1= listaAcumuladoCU60[0]
		Y2= listaAcumuladoCU60[1]
		X1= abAcDic[Y1]
		X2=	abAcDic[Y2]
		d60= calculo2CU(60,X1,Y1,X2,Y2)
		CU=d60/d10

		return [d10,CU]

	def calcularPEGravaYPredimensionamiento(listaEntradas,lista1, lista2,temp):
		listaE=list()
		for elemento in listaEntradas:
			try:
				listaE.append(float(elemento.get()))
			except:
				messagebox.showwarning(title="Error", message="Todos los valores ingresados deben ser números.")
				return None
	
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow = tk.Toplevel()
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.iconbitmap(bitmap='icons\\agua.ico')
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.geometry("1000x200") 
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.resizable(0,0)	
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.configure(background="#9DC4AA")

		##Panel:
		panelGravaDimension = ttk.Notebook(estimacionPerdidaGravaYPredimensionamientoCalculoWindow)
		panelGravaDimension.pack(fill=BOTH, expand=TRUE)
		###########Frame Principal1
		estimacionPerdidaGravaFrame=LabelFrame(panelGravaDimension, text="Estimación de la pérdida de energía en le lecho de grava.", font=("Yu Gothic bold", 11))
		estimacionPerdidaGravaFrame.pack(side=TOP, fill=BOTH,expand=True)
		panelGravaDimension.add(estimacionPerdidaGravaFrame,text="Pérdida energía en el lecho de grava")
		#Frame Treeview
		arbolEstimacionPerdidaGrava_frame = Frame(estimacionPerdidaGravaFrame)
		arbolEstimacionPerdidaGrava_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolEstimacionPerdidaGrava_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolEstimacionPerdidaGrava_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolEstimacionPerdidaGrava= ttk.Treeview(arbolEstimacionPerdidaGrava_frame,selectmode=BROWSE, height=3,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolEstimacionPerdidaGrava.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolEstimacionPerdidaGrava.xview)
		sedScrollY.configure(command=arbolEstimacionPerdidaGrava.yview)
		#Define columnas.
		arbolEstimacionPerdidaGrava["columns"]= (
		"V{} = Tasa de filtración [m/d]".format(getSub("f")),
		"L{} = Profundidad del lecho de grava [m]".format(getSub("g")),
		"h{} = Pérdida de energía en lecho de grava durante la filtración [m]".format(getSub("g"))
		)

		#Headings
		arbolEstimacionPerdidaGrava.heading("#0",text="ID", anchor=CENTER)

		for col in arbolEstimacionPerdidaGrava["columns"]:
			arbolEstimacionPerdidaGrava.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolEstimacionPerdidaGrava["columns"])+1) :
				arbolEstimacionPerdidaGrava.column(f"#{i}",width=500, stretch=False)	
		arbolEstimacionPerdidaGrava.column("#3",width=600, stretch=True)
		arbolEstimacionPerdidaGrava.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolEstimacionPerdidaGrava.tag_configure("evenrow", background= "#1FCCDB")
		arbolEstimacionPerdidaGrava.tag_configure("oddrow", background= "#9DC4AA")
		
		################Frame principal2
		PerdidaCargaGravaFrame=LabelFrame(panelGravaDimension, text="Pérdida de carga a través del lecho de grava", font=("Yu Gothic bold", 11))
		PerdidaCargaGravaFrame.pack(side=TOP, fill=BOTH,expand=True)
		panelGravaDimension.add(PerdidaCargaGravaFrame,text="Pérdida de carga a través del lecho de grava")
		#Frame Treeview
		arbolPerdidaCargaGrava_frame = Frame(PerdidaCargaGravaFrame)
		arbolPerdidaCargaGrava_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolPerdidaCargaGrava_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPerdidaCargaGrava_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaCargaGrava= ttk.Treeview(arbolPerdidaCargaGrava_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolPerdidaCargaGrava.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolPerdidaCargaGrava.xview)
		sedScrollY.configure(command=arbolPerdidaCargaGrava.yview)
		#Define columnas.
		arbolPerdidaCargaGrava["columns"]= (
		"V{} = Velocidad de lavado [m/min]".format(getSub("b")),
		"L{} = Profundidad del lecho de grava [m]".format(getSub("g")),
		"h{} = Pérdida de energía en el lecho de grava durante el lavado [m]".format(getSub("2"))
		)

		#Headings
		arbolPerdidaCargaGrava.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaCargaGrava["columns"]:
			arbolPerdidaCargaGrava.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolPerdidaCargaGrava["columns"])+1) :
				arbolPerdidaCargaGrava.column(f"#{i}",width=500, stretch=False)	
		arbolPerdidaCargaGrava.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPerdidaCargaGrava.tag_configure("evenrow", background= "#1FCCDB")
		arbolPerdidaCargaGrava.tag_configure("oddrow", background= "#9DC4AA")

		############Insersión datos.
		##ListaE Provisional"
		listaE=[1,3/4,1/2,1/4,1/8,3/4,1/2,1/4,1/8,1/16,0.100,0.075,0.075,0.100,0.100]
		
		global contadorFiltro
		contadorFiltro = 0
		
		listaEntradaTemp1=list()
		listaEntradaTemp3=list()
		
		listaEntradaTemp1.append(150)
		suma=0
		for ind in range(10,15):
			suma=suma+listaE[ind]
		listaEntradaTemp1.append(suma)
		PenergiaLechoGravaFiltracion=(150/(24*60))*suma*(1/3)
		listaEntradaTemp1.append(PenergiaLechoGravaFiltracion)

		newDataTreeview(arbolEstimacionPerdidaGrava,listaEntradaTemp1)
		
		
		contadorFiltro = 0
	
		#Tabla Temperatura Viscocidad
		valorTemperaturas=list()
		tablaTemperaturaViscocidad=dict()
		for i in range(0,36):
			valorTemperaturas.append(i)
			valorViscocidad=[0.001792, 0.001731, 0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 0.001083, 0.001056, 0.00103, 0.001005, 0.000981, 0.000958, 0.000936, 0.000914, 0.000894, 0.000874, 0.000855, 0.000836, 0.000818, 0.000801, 0.000784, 0.000768, 0.000752, 0.000737, 0.000723]

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaViscocidad[valorTemperaturas[ind]]=valorViscocidad[ind]
		
		listatemporal = valorCoeficienteDeUniformidad(lista1,lista2)
		percentil60AnalisisGranulometrico = listatemporal[0]*listatemporal[1] 
		
		

		velocidadArrasteMedioA20= percentil60AnalisisGranulometrico*10
		

		viscocidadDinamicaAgua= (tablaTemperaturaViscocidad[temp])*1000

		

		if temp == 20:
			velocidadArrastreMedioFiltrante = velocidadArrasteMedioA20
		else:
			velocidadArrastreMedioFiltrante= velocidadArrasteMedioA20*((viscocidadDinamicaAgua)**((-1/3)))
		
		

		velocidadLavado=0.1*velocidadArrastreMedioFiltrante
		
		listaEntradaTemp3.append(velocidadLavado)
		listaEntradaTemp3.append(suma)
		perdidaEnergiaLechoGravaDuranteLavado= suma*velocidadLavado*(1/3)
		listaEntradaTemp3.append(perdidaEnergiaLechoGravaDuranteLavado)
		newDataTreeview(arbolPerdidaCargaGrava,listaEntradaTemp3)

		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.mainloop()

	def estPerdidaLechoGravaYPredimensionamientoFiltros(lista1, lista2,optnValue):
		
		if optnValue.get() == "Seleccione la temperatura":
			messagebox.showwarning(title="Error", message="Hace falta elegir el valor de la temperatura del agua a tratar.")
			return None
		else:
			temp = int(optnValue.get())

		estimacionPerdidaGravaYPredimensionamientoWindow = tk.Toplevel()
		estimacionPerdidaGravaYPredimensionamientoWindow.iconbitmap(bitmap='icons\\agua.ico')
		estimacionPerdidaGravaYPredimensionamientoWindow.geometry("800x600") 
		estimacionPerdidaGravaYPredimensionamientoWindow.resizable(0,0)	
		estimacionPerdidaGravaYPredimensionamientoWindow.configure(background="#9DC4AA")
		frameEstimacionPerdidaGravaYPredimensionamiento= LabelFrame(estimacionPerdidaGravaYPredimensionamientoWindow, text="Estimación de la pérdida de energía en el lecho de grava y predimensionamiento de los filtros",font=("Yu Gothic bold", 11))
		frameEstimacionPerdidaGravaYPredimensionamiento.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				elemento.delete(0, END)


		#Input
		lista_inputs=[]

		inicialLabel=Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Características del lecho de grava para drenaje por tuberías: ",font=("Yu Gothic bold",10))
		segundoLabel= Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Caudales de diseño",font=("Yu Gothic bold",10))

		NumeroCapaLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Número de capa",font=("Yu Gothic bold",10))
		tamañoAberturaMallaPasandoLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Tamaño de abertura\nde malla pasando [pulg]",font=("Yu Gothic bold",10))
		tamañoAberturaMallaRetenidaLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Tamaño de abertura\nde malla retenida [pulg]",font=("Yu Gothic bold",10))
		profundidadCapaLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Profundidad de la capa [m]",font=("Yu Gothic bold",10))
		NumeroCapaLabel1Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="1",font=("Yu Gothic bold",10))
		NumeroCapaLabel2Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="2",font=("Yu Gothic bold",10))
		NumeroCapaLabel3Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="3",font=("Yu Gothic bold",10))
		NumeroCapaLabel4Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="4",font=("Yu Gothic bold",10))
		NumeroCapaLabel5Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="5",font=("Yu Gothic bold",10))

		

		tamañoAberturaMallaPasando1 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaPasando1.focus()
		tamañoAberturaMallaPasando2 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaPasando3 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaPasando4 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaPasando5 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)

		tamañoAberturaMallaRetenida1 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaRetenida2 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaRetenida3 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaRetenida4 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tamañoAberturaMallaRetenida5 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)

		profundidadCapa1 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa2 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa3 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa4 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa5 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)

		

		listaTitulosTabla=[NumeroCapaLabel,tamañoAberturaMallaPasandoLabel, tamañoAberturaMallaRetenidaLabel, profundidadCapaLabel]

		listaColumna1=[NumeroCapaLabel1Label,NumeroCapaLabel2Label,NumeroCapaLabel3Label,NumeroCapaLabel4Label,NumeroCapaLabel5Label]
		listaColumna2=[tamañoAberturaMallaPasando1,tamañoAberturaMallaPasando2,tamañoAberturaMallaPasando3,tamañoAberturaMallaPasando4,tamañoAberturaMallaPasando5]
		listaColumna3=[tamañoAberturaMallaRetenida1,tamañoAberturaMallaRetenida2,tamañoAberturaMallaRetenida3,tamañoAberturaMallaRetenida4,tamañoAberturaMallaRetenida5]
		listaColumna4=[profundidadCapa1,profundidadCapa2,profundidadCapa3,profundidadCapa4,profundidadCapa5]
		
		listaEntradas = [tamañoAberturaMallaPasando1,tamañoAberturaMallaPasando2,tamañoAberturaMallaPasando3,tamañoAberturaMallaPasando4,tamañoAberturaMallaPasando5,
		tamañoAberturaMallaRetenida1,tamañoAberturaMallaRetenida2,tamañoAberturaMallaRetenida3,tamañoAberturaMallaRetenida4,tamañoAberturaMallaRetenida5,
		profundidadCapa1,profundidadCapa2,profundidadCapa3,profundidadCapa4,profundidadCapa5]
		
		#Organización tabla.
		xInicial=20
		for elemento in listaTitulosTabla:
			elemento.place(x=xInicial,y=63)
			xInicial=xInicial+180

		alturaInicialCol1=106
		inicialLabel.place(x=20,y=20)
		for elemento in listaColumna1:
			elemento.place(x=60,y=alturaInicialCol1)
			alturaInicialCol1+=43
		alturaInicialCol1=106
		
		for elemento in listaColumna2:
			elemento.place(x=200,y=alturaInicialCol1)
			alturaInicialCol1+=43
		alturaInicialCol1=106
		
		for elemento in listaColumna3:
			elemento.place(x=380,y=alturaInicialCol1)
			alturaInicialCol1+=43
		
		alturaInicialCol1=106
		
		for elemento in listaColumna4:
			elemento.place(x=560,y=alturaInicialCol1)
			alturaInicialCol1+=43

		segundoLabel.place(x=20,y=alturaInicialCol1)
		

		#Botones.
		botonCalcular = HoverButton(frameEstimacionPerdidaGravaYPredimensionamiento, text="Calcular la estimación de la pérdida de energía en el lecho de grava.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularPEGravaYPredimensionamiento(listaEntradas,lista1, lista2,temp) )
		botonNewEntry = HoverButton(frameEstimacionPerdidaGravaYPredimensionamiento, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50
			
		estimacionPerdidaGravaYPredimensionamientoWindow.mainloop()
	
	def calcularPerdidadLechoExpandido(listaEntradas):
		listaE=list()
		for elemento in listaEntradas:
			try:
				listaE.append(float(elemento.get()))
			except:
				messagebox.showwarning(title="Error",message="Uno o varios de los valores ingresados no son números.")
				return None
		perdidaLechoExpandidoCWindow = tk.Toplevel()
		perdidaLechoExpandidoCWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaLechoExpandidoCWindow.geometry("1000x500") 
		perdidaLechoExpandidoCWindow.resizable(0,0)	
		perdidaLechoExpandidoCWindow.configure(background="#9DC4AA")

		#Frame principal
		perdidaLechoExpandidoCFrame=LabelFrame(perdidaLechoExpandidoCWindow, text="Pérdida de carga a través del lecho expandido", font=("Yu Gothic bold", 11))
		perdidaLechoExpandidoCFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolPerdidaLechoExpandidoC_frame = Frame(perdidaLechoExpandidoCFrame)
		arbolPerdidaLechoExpandidoC_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolPerdidaLechoExpandidoC_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPerdidaLechoExpandidoC_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaLechoExpandidoC= ttk.Treeview(arbolPerdidaLechoExpandidoC_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolPerdidaLechoExpandidoC.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolPerdidaLechoExpandidoC.xview)
		sedScrollY.configure(command=arbolPerdidaLechoExpandidoC.yview)
		#Define columnas.
		arbolPerdidaLechoExpandidoC["columns"]= (
		"L = Profundidad del lecho fijo [m]",
		"e = Porosidad del lecho fijo",
		"S{} = Densidad relativa de la arena".format(getSub("s")),
		"h{} = Pérdida de carga a través del lecho expandido [m]".format(getSub("1"))
		)

		#Headings
		arbolPerdidaLechoExpandidoC.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaLechoExpandidoC["columns"]:
			arbolPerdidaLechoExpandidoC.heading(col, text=col,anchor=CENTER)


		for i in range(0,len(arbolPerdidaLechoExpandidoC["columns"])+1) :
				arbolPerdidaLechoExpandidoC.column(f"#{i}",width=500, stretch=False)	


		arbolPerdidaLechoExpandidoC.column("#0",width=0, stretch=False)
		arbolPerdidaLechoExpandidoC.column("#4",width=700, stretch=True)
		#Striped row tags
		arbolPerdidaLechoExpandidoC.tag_configure("evenrow", background= "#1FCCDB")
		arbolPerdidaLechoExpandidoC.tag_configure("oddrow", background= "#9DC4AA")


		#Insersión datos.
		global contadorFiltro
		contadorFiltro = 0

		listaEnt=list()
		for j in range(0,3):
			listaEnt.append(listaE[j])

		perdidaCargaLechoExpandidoVal= listaE[0]*(1-listaE[1])*(listaE[2]-1)
		listaEnt.append(perdidaCargaLechoExpandidoVal)
		newDataTreeview(arbolPerdidaLechoExpandidoC,listaEnt)

		'''
		def perdidaCargaLechoExpandido():
		perdidaCargaLechoExpandidoWindow = tk.Toplevel()
		perdidaCargaLechoExpandidoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaLechoExpandidoWindow.geometry("600x400") 
		perdidaCargaLechoExpandidoWindow.resizable(0,0)	
		perdidaCargaLechoExpandidoWindow.configure(background="#9DC4AA")

		framePerdidaCargaLechoExpandido= LabelFrame(perdidaCargaLechoExpandidoWindow, text="Pérdida de carga a través del lecho expandido",font=("Yu Gothic bold", 11))
		framePerdidaCargaLechoExpandido.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				elemento.delete(0, END)


		#Input
		lista_inputs=[]

		inicialLabel=Label(framePerdidaCargaLechoExpandido, text="Características del lecho filtrante de arena: ",font=("Yu Gothic bold",10))



		profundidadLechoFijoArenaLabel = Label(framePerdidaCargaLechoExpandido, text="L = Profundidad del lecho fijo de arena [m]:", font =("Yu Gothic",9))
		porosidadLechoFijoLabel = Label(framePerdidaCargaLechoExpandido, text=u"\u03B5 ,e = Porosidad del lecho fijo:", font =("Yu Gothic",9))
		densidadRelativaArenaLabel = Label(framePerdidaCargaLechoExpandido, text="S{} = Densidad relativa de la arena:".format(getSub("s")), font =("Yu Gothic",9))

		profundidadLechoFijoArena = Entry(framePerdidaCargaLechoExpandido)
		profundidadLechoFijoArena.focus()
		porosidadLechoFijo = Entry(framePerdidaCargaLechoExpandido)
		densidadRelativaArena = Entry(framePerdidaCargaLechoExpandido)



		listaEntradas=[profundidadLechoFijoArena,
		porosidadLechoFijo, densidadRelativaArena]

		listaLabel=[inicialLabel, profundidadLechoFijoArenaLabel,
		porosidadLechoFijoLabel, densidadRelativaArenaLabel]

		alturaInicialLabel=20
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=47

		alturaInicialEntradas=67

		for elemento in listaEntradas:
				elemento.place(x=400,y=alturaInicialEntradas)
				alturaInicialEntradas+=47

		#Botones.
		botonCalcular = HoverButton(framePerdidaCargaLechoExpandido, text="Calcular la pérdida de carga a través del lecho expandido.", activebackground="#9DC4AA", width=70, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularPerdidadLechoExpandido(listaEntradas) )
		botonNewEntry = HoverButton(framePerdidaCargaLechoExpandido, text="Limpiar entradas.", activebackground="#9DC4AA", width=70, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=220
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50
		
		perdidaCargaLechoExpandidoWindow.mainloop()'''

	def predimensionamientoFiltros(listaET):
	
			
		try: 
			caudalMedio=float(listaET[0].get())
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un número.")
			return None
		
		predimensionamientoFiltrosWindow = tk.Toplevel()
		predimensionamientoFiltrosWindow.iconbitmap(bitmap='icons\\agua.ico')
		predimensionamientoFiltrosWindow.geometry("600x400") 
		predimensionamientoFiltrosWindow.resizable(0,0)	
		predimensionamientoFiltrosWindow.configure(background="#9DC4AA")

		PredimensionamientoFiltrosFrame=LabelFrame(predimensionamientoFiltrosWindow, text="Predimensionamiento de los filtros", font=("Yu Gothic bold", 11))
		PredimensionamientoFiltrosFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolPredimensionamientoFiltros_frame = Frame(PredimensionamientoFiltrosFrame)
		arbolPredimensionamientoFiltros_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolPredimensionamientoFiltros_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPredimensionamientoFiltros_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPredimensionamientoFiltros= ttk.Treeview(arbolPredimensionamientoFiltros_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolPredimensionamientoFiltros.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolPredimensionamientoFiltros.xview)
		sedScrollY.configure(command=arbolPredimensionamientoFiltros.yview)
		#Define columnas.
		arbolPredimensionamientoFiltros["columns"]= (
		"1","2")
		
		'''
		"Q = Caudal de diseño (QMD)  [(m^3)/s]",
		"V{} = Tasa de filtración en operación normal [m/día]".format(getSub("f")),
		"V{} = Tasa de filtración con un filtro fuera de servicio por lavado".format(getSub("max")),
		"A{} = Área de filtración en operación normal".format(getSub("T")),
		"A{} = Área de filtración con un filtros fuera de servicio por lavado".format(getSub("t")),
		"Área de filtración fuera de servicio por lavado de filtros",
		"N{} = Número mínimo de filtros [und]".format(getSub("f")),
		"N{} = Número de filtros [und]".format(getSub("f")),
		"A{} = Área de cada filtro".format(getSub("f")),
		"L{} = Lado de cada filtro".format(getSub("f"))'''
		

		#Headings
		arbolPredimensionamientoFiltros.heading("#0",text="ID", anchor=CENTER)


		def formulaN(archivo):
			forWindow= tk.Toplevel()
			forWindow.iconbitmap(bitmap='icons\\agua.ico')
			forWindow.geometry("1000x350") 
			forWindow.resizable(0,0)
			forWindow.configure(background="#9DC4AA")
			framefor=Frame(forWindow)
			framefor.pack(side=TOP, fill=BOTH, expand=True)
			ima= PhotoImage(file=archivo)
			l=Label(framefor, image=ima)
			l.pack()
			forWindow.mainloop()

		for col in arbolPredimensionamientoFiltros["columns"]:
			arbolPredimensionamientoFiltros.heading(col, text=col,anchor=CENTER, command=lambda: formulaN("images\\Predimensionamiento.png") )	

		for i in range(0,len(arbolPredimensionamientoFiltros["columns"])+1) :
				arbolPredimensionamientoFiltros.column(f"#{i}",width=700, stretch=False)	
		arbolPredimensionamientoFiltros.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPredimensionamientoFiltros.tag_configure("evenrow", background= "#1FCCDB")
		arbolPredimensionamientoFiltros.tag_configure("oddrow", background= "#9DC4AA")

		
		contadorFiltro = 0

		listaArbolCaudal=list()
		caudal=caudalMedio*(1.30)
		listaArbolCaudal.append(caudal)
		Vf=120
		Vmax=150
		listaArbolCaudal.append(Vf)
		listaArbolCaudal.append(Vmax)
		arenaFilOpNormal=caudal*86400*(1/Vf)
		listaArbolCaudal.append(arenaFilOpNormal)
		arenaFilFueraServ=caudal*86400*(1/Vmax)
		listaArbolCaudal.append(arenaFilFueraServ)
		arenaFilFueraServ2 = arenaFilOpNormal - arenaFilFueraServ
		listaArbolCaudal.append(arenaFilFueraServ2)

		if arenaFilOpNormal/arenaFilFueraServ2 < 3.0:
			numMinFiltros=3
		else:
			numMinFiltros= round(arenaFilOpNormal/arenaFilFueraServ2 ,0)
		listaArbolCaudal.append(numMinFiltros)

		

		if 0.044*sqrt(caudal*86400)<numMinFiltros:
			numFiltros=numMinFiltros
		else:
			numFiltros = int(0.044*sqrt(caudal*86400))+1
		listaArbolCaudal.append(numFiltros)

		areaFiltro = arenaFilOpNormal/numFiltros
		listaArbolCaudal.append(areaFiltro)

		ladoFiltro= sqrt(areaFiltro)
		listaArbolCaudal.append(ladoFiltro)
		
		encabezadosLista=["Q = Caudal de diseño (QMD)  [(m^3)/s]",
		"V{} = Tasa de filtración en operación normal [m/día]".format(getSub("f")),
		"V{} = Tasa de filtración con un filtro fuera de servicio por lavado".format(getSub("max")),
		"A{} = Área de filtración en operación normal".format(getSub("T")),
		"A{} = Área de filtración con un filtros fuera de servicio por lavado".format(getSub("t")),
		"Área de filtración fuera de servicio por lavado de filtros",
		"N{} = Número mínimo de filtros [und]".format(getSub("f")),
		"N{} = Número de filtros [und]".format(getSub("f")),
		"A{} = Área de cada filtro".format(getSub("f")),
		"L{} = Lado de cada filtro".format(getSub("f"))]

		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listaArbolCaudal[i])
			newDataTreeview(arbolPredimensionamientoFiltros,listaTemp)
		#newDataTreeview(arbolPredimensionamientoFiltros,listaArbolCaudal)
		
		
		
		

		predimensionamientoFiltrosWindow.mainloop()
	
	def ValuepredimensionamientoFiltros(listaET):
	
			
		try: 
			caudalMedio=float(listaET[0].get())
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un número.")
			return None

		

		contadorFiltro = 0

		listaArbolCaudal=list()
		caudal=caudalMedio*(1.30)
		listaArbolCaudal.append(caudal)
		Vf=120
		Vmax=150
		listaArbolCaudal.append(Vf)
		listaArbolCaudal.append(Vmax)
		arenaFilOpNormal=caudal*86400*(1/Vf)
		listaArbolCaudal.append(arenaFilOpNormal)
		arenaFilFueraServ=caudal*86400*(1/Vmax)
		listaArbolCaudal.append(arenaFilFueraServ)
		arenaFilFueraServ2 = arenaFilOpNormal - arenaFilFueraServ
		listaArbolCaudal.append(arenaFilFueraServ2)

		if arenaFilOpNormal/arenaFilFueraServ2 < 3.0:
			numMinFiltros=3
		else:
			numMinFiltros= round(arenaFilOpNormal/arenaFilFueraServ2 ,0)
		listaArbolCaudal.append(numMinFiltros)

		

		if 0.044*sqrt(caudal*86400)<numMinFiltros:
			numFiltros=numMinFiltros
		else:
			numFiltros = int(0.044*sqrt(caudal*86400))+1
		listaArbolCaudal.append(numFiltros)

		areaFiltro = arenaFilOpNormal/numFiltros
		listaArbolCaudal.append(areaFiltro)

		ladoFiltro= sqrt(areaFiltro)
		listaArbolCaudal.append(ladoFiltro)
		
		
		return listaArbolCaudal

	def drenajeFiltro2(caudal,listaEntradaDrenaje):
			
		
		'''
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]

		'''

		
		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())
		
		
		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()
		
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())
	

		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()
		
		
	
			
		drenajeFiltrosWindow = tk.Toplevel()
		drenajeFiltrosWindow.iconbitmap(bitmap='icons\\agua.ico')
		drenajeFiltrosWindow.geometry("600x400") 
		drenajeFiltrosWindow.resizable(0,0)	
		drenajeFiltrosWindow.configure(background="#9DC4AA")

		drenajeFiltrosFrame=LabelFrame(drenajeFiltrosWindow, text="Drenaje calculo", font=("Yu Gothic bold", 11))
		drenajeFiltrosFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolDrenajeFiltros_frame = Frame(drenajeFiltrosFrame)
		arbolDrenajeFiltros_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolDrenajeFiltros_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolDrenajeFiltros_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolDrenajeFiltros= ttk.Treeview(arbolDrenajeFiltros_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolDrenajeFiltros.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolDrenajeFiltros.xview)
		sedScrollY.configure(command=arbolDrenajeFiltros.yview)
		#Define columnas.
		arbolDrenajeFiltros["columns"]= (
		
		"B{} = Ancho del múltiple".format(getSub("mul")),
		"L{} = Longitud de los laterales".format(getSub("lat")),
		"N{} = Número de laterales por unidad de filtración".format(getSub("lat")),
		" = Número de orificios por lateral",
		"N{} = Número de orificios por unidad de filtración".format(getSub("ori")),
		"Área total de orificios/ área filtrante",
		"Área transversal del lateral / área de orificios del lateral",
		"Área transversal del múltiple / área transversal de laterales",
		"Longitud de lateral / diámetro de lateral",
		)

		#Headings
		arbolDrenajeFiltros.heading("#0",text="ID", anchor=CENTER)

		for col in arbolDrenajeFiltros["columns"]:
			arbolDrenajeFiltros.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolDrenajeFiltros["columns"])+1) :
				arbolDrenajeFiltros.column(f"#{i}",width=700, stretch=False)	
		arbolDrenajeFiltros.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolDrenajeFiltros.tag_configure("evenrow", background= "#1FCCDB")
		arbolDrenajeFiltros.tag_configure("oddrow", background= "#9DC4AA")


		#Tablas


		listaSeccionTuberia=['6 X 6', '8 X 8', '10 X 10', '12 X 12', '14 X 14', '16 X 16', '18 X 18','20 X 20']
		listaAnchoSeccion=list()
		listaAnchoSeccion2=list()
		ind=0
		
		for elemento in listaSeccionTuberia:
			if elemento == '10 X 10':
				ind=ind+1
			if ind==0:
				listaAnchoSeccion.append((float(elemento[0])*0.0254))
			else:
				listaAnchoSeccion.append(float(elemento[0:2])*0.0254)
		
		ind=0

		for elemento in listaSeccionTuberia:
			if elemento == '10 X 10':
				ind=ind+1
			if ind==0:
				listaAnchoSeccion2.append((float(elemento[0])*0.0254)**2)
			else:
				listaAnchoSeccion2.append((float(elemento[0:2])*0.0254)**2)


		anchoSeccion=dict()
		anchoSeccion2=dict()

		for j in range(0,len(listaSeccionTuberia)):
			anchoSeccion[listaSeccionTuberia[j]]=listaAnchoSeccion[j]

		for j in range(0,len(listaSeccionTuberia)):
			anchoSeccion2[listaSeccionTuberia[j]]=listaAnchoSeccion2[j]

		#Obtención de Lf
		
		caudal=caudal*(1.30)
		
		


		Vf=120
		Vmax=150

		arenaFilOpNormal=caudal*86400*(1/Vf)
		arenaFilFueraServ=caudal*86400*(1/Vmax)
		arenaFilFueraServ2 = arenaFilOpNormal - arenaFilFueraServ

		if arenaFilOpNormal/arenaFilFueraServ2 < 3.0:
			numMinFiltros=3
		else:
			numMinFiltros= round(arenaFilOpNormal/arenaFilFueraServ2 ,0)
		if 0.044*sqrt(caudal*86400)<numMinFiltros:
			numFiltros=numMinFiltros
		else:
			numFiltros = int(0.044*sqrt(caudal*86400))+1
	


		areaFiltro = arenaFilOpNormal/numFiltros
		ladoFiltro= sqrt(areaFiltro)
		



		listaDiametroOrificios= [1/4,3/8,1/2,5/8]

		listaAreasOrificios= [0.00003166921744359,0.00007125573924809,0.00012667686977437,0.00019793260902246]

		
		

		
		areaOrificiosDic = dict()

		for i in range(0,len(listaDiametroOrificios)):
			areaOrificiosDic[listaDiametroOrificios[i]]=listaAreasOrificios[i]


		listaDiametroLaterales= ("1 1/2", "2", "2 1/2", "3")
		listaAreasLaterales=[0.0011401,0.0020268,0.0031669,0.0045604]
		areaLateralesDic=dict()

		for i in range(0, len(listaDiametroLaterales)):
			areaLateralesDic[listaDiametroLaterales[i]]=listaAreasLaterales[i]

		'''
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]

		'''


		
		
		


		listaArbolDreanejFiltros=list()
		
		anchoMultiple= anchoSeccion[seccionTransvMultiple]
		listaArbolDreanejFiltros.append(anchoMultiple)


		longitudLaterales= (ladoFiltro/2) - (anchoMultiple/2) -0.05
		listaArbolDreanejFiltros.append(longitudLaterales)
		
		
		numLatPUDF= 2*round((ladoFiltro/distanciaLaterales),0)
		listaArbolDreanejFiltros.append(numLatPUDF)

		numOrif= 2*(int(longitudLaterales/distanciaOrificios)+1)
		listaArbolDreanejFiltros.append(numOrif)

		

		numOrifPUDF=numLatPUDF*numOrif
		listaArbolDreanejFiltros.append(numOrifPUDF)

		print(numOrifPUDF, areaOrificiosDic[diametroOrificios],areaFiltro)


		areaTotalOrificios= float(numOrifPUDF)*areaOrificiosDic[diametroOrificios]*(1.0/areaFiltro)
		listaArbolDreanejFiltros.append(areaTotalOrificios)



		areaTransversalDelLateral= areaLateralesDic[diametroLaterales]/(areaOrificiosDic[diametroOrificios]*numOrif)
		listaArbolDreanejFiltros.append(areaTransversalDelLateral)


		areaTransversalDelMultiple=	anchoSeccion2[seccionTransvMultiple]/(numLatPUDF*areaLateralesDic[diametroLaterales])
		listaArbolDreanejFiltros.append(areaTransversalDelMultiple)
			

		#diametroLateralesA número:

		if diametroLaterales=="1 1/2":
			diametroLaterales= 1.0 + (1/2)
		elif diametroLaterales=="2 1/2":
			diametroLaterales=2.0 + (1/2)
		else:
			diametroLaterales=float(diametroLaterales)

		longitudLateral= longitudLaterales/(diametroLaterales*0.0254)
		listaArbolDreanejFiltros.append(longitudLateral)

		newDataTreeview(arbolDrenajeFiltros,listaArbolDreanejFiltros)
		
		drenajeFiltrosWindow.mainloop()
	
	def ValueDrenajeFiltro2(caudal,listaEntradaDrenaje):
			
		
		'''
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]

		'''

		
		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())
		
		
		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()
		
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())
	

		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()
		
			
		#Tablas


		listaSeccionTuberia=['6 X 6', '8 X 8', '10 X 10', '12 X 12', '14 X 14', '16 X 16', '18 X 18','20 X 20']
		listaAnchoSeccion=list()
		listaAnchoSeccion2=list()
		ind=0

		for elemento in listaSeccionTuberia:
			if elemento == '10 X 10':
				ind=ind+1
			if ind==0:
				listaAnchoSeccion.append((float(elemento[0])*0.0254))
			else:
				listaAnchoSeccion.append(float(elemento[0:2])*0.0254)
		
		ind=0

		for elemento in listaSeccionTuberia:
			if elemento == '10 X 10':
				ind=ind+1
			if ind==0:
				listaAnchoSeccion2.append((float(elemento[0])*0.0254)**2)
			else:
				listaAnchoSeccion2.append((float(elemento[0:2])*0.0254)**2)


		anchoSeccion=dict()
		anchoSeccion2=dict()

		for j in range(0,len(listaSeccionTuberia)):
			anchoSeccion[listaSeccionTuberia[j]]=listaAnchoSeccion[j]

		for j in range(0,len(listaSeccionTuberia)):
			anchoSeccion2[listaSeccionTuberia[j]]=listaAnchoSeccion2[j]

		#Obtención de Lf
		
		caudal=caudal*(1.30)
		
		


		Vf=120
		Vmax=150
		arenaFilOpNormal=caudal*86400*(1/Vf)
		arenaFilFueraServ=caudal*86400*(1/Vmax)
		arenaFilFueraServ2 = arenaFilOpNormal - arenaFilFueraServ
		if arenaFilOpNormal/arenaFilFueraServ2 < 3.0:
			numMinFiltros=3
		else:
			numMinFiltros= round(arenaFilOpNormal/arenaFilFueraServ2 ,0)
		if 0.044*sqrt(caudal*86400)<numMinFiltros:
			numFiltros=numMinFiltros
		else:
			numFiltros = int(0.044*sqrt(caudal*86400))+1
	

		areaFiltro = arenaFilOpNormal/numFiltros
		ladoFiltro= sqrt(areaFiltro)
		



		listaDiametroOrificios= [1/4,3/8,1/2,5/8]

		listaAreasOrificios= [0.00003166921744359,0.00007125573924809,0.00012667686977437,0.00019793260902246]

		areaOrificiosDic = dict()

		for i in range(0,len(listaDiametroOrificios)):
			areaOrificiosDic[listaDiametroOrificios[i]]=listaAreasOrificios[i]


		listaDiametroLaterales= ("1 1/2", "2", "2 1/2", "3")
		listaAreasLaterales=[0.0011401,0.0020268,0.0031669,0.0045604]
		areaLateralesDic=dict()

		for i in range(0, len(listaDiametroLaterales)):
			areaLateralesDic[listaDiametroLaterales[i]]=listaAreasLaterales[i]

		'''
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]

		'''	
	
		listaArbolDreanejFiltros=list()
		
		anchoMultiple= anchoSeccion[seccionTransvMultiple]
		listaArbolDreanejFiltros.append(anchoMultiple)


		longitudLaterales= (ladoFiltro/2) - (anchoMultiple/2) -0.05
		listaArbolDreanejFiltros.append(longitudLaterales)

		numLatPUDF= 2*round((ladoFiltro/distanciaLaterales),0)
		listaArbolDreanejFiltros.append(numLatPUDF)

		numOrif= 2*(int(longitudLaterales/distanciaOrificios)+1)
		listaArbolDreanejFiltros.append(numOrif)

		

		numOrifPUDF=numLatPUDF*numOrif
		listaArbolDreanejFiltros.append(numOrifPUDF)

		areaTotalOrificios= numOrifPUDF*areaOrificiosDic[diametroOrificios]*(1/areaFiltro)
		listaArbolDreanejFiltros.append(areaTotalOrificios)



		areaTransversalDelLateral= areaLateralesDic[diametroLaterales]/(areaOrificiosDic[diametroOrificios]*numOrif)
		listaArbolDreanejFiltros.append(areaTransversalDelLateral)


		areaTransversalDelMultiple=	anchoSeccion2[seccionTransvMultiple]/(numLatPUDF*areaLateralesDic[diametroLaterales])
		listaArbolDreanejFiltros.append(areaTransversalDelMultiple)
			

		#diametroLateralesA número:

		if diametroLaterales=="1 1/2":
			diametroLaterales= 1.0 + (1/2)
		elif diametroLaterales=="2 1/2":
			diametroLaterales=2.0 + (1/2)
		else:
			diametroLaterales=float(diametroLaterales)

		longitudLateral= longitudLaterales/(diametroLaterales*0.0254)
		listaArbolDreanejFiltros.append(longitudLateral)

		return listaArbolDreanejFiltros
		
		
	
	def drenajeFiltro(listaET):
		
		try: 
			caudalMedio=float(listaET[0].get())
			
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un número.")
			return None

		
		drenajeFiltrosMainWindow = tk.Toplevel()
		drenajeFiltrosMainWindow.iconbitmap(bitmap='icons\\agua.ico')
		drenajeFiltrosMainWindow.geometry("600x600") 
		drenajeFiltrosMainWindow.resizable(0,0)	
		drenajeFiltrosMainWindow.configure(background="#9DC4AA")

		drenajeFiltrosMainFrame=LabelFrame(drenajeFiltrosMainWindow, text="Datos adicionales para drenaje del filtro:", font=("Yu Gothic bold", 11))
		drenajeFiltrosMainFrame.pack(side=TOP, fill=BOTH,expand=True)

		
		
		diametroOrificios = StringVar()
		diametroOrificios.set("Diametro de los orificios")
		listaValoresTempDiametroOrificios=list()
		listaValoresTempDiametroOrificios.append("1/4")
		listaValoresTempDiametroOrificios.append("3/8")
		listaValoresTempDiametroOrificios.append("1/2")
		listaValoresTempDiametroOrificios.append("5/8")
		diametroOrificiosName = OptionMenu(drenajeFiltrosMainFrame, diametroOrificios, *listaValoresTempDiametroOrificios)
		diametroOrificiosLabel= Label(drenajeFiltrosMainWindow, text="Seleccione el diámetro de los orificios:", font=("Yu Gothic bold", 11))
		

		
		distanciaOrificios = StringVar()
		distanciaOrificios.set("Distancia entre los orificios")
		listaValoresTempDistanciaOrificios=list()
		listaValoresTempDistanciaOrificios.append("0.750")
		listaValoresTempDistanciaOrificios.append("0.100")
		listaValoresTempDistanciaOrificios.append("0.125")
		listaValoresTempDistanciaOrificios.append("0.150")
		distanciaOrificiosName = OptionMenu(drenajeFiltrosMainFrame, distanciaOrificios, *listaValoresTempDistanciaOrificios)
		distanciaOrificiosLabel= Label(drenajeFiltrosMainWindow, text="Seleccione la distancia entre orificios", font=("Yu Gothic bold", 11))


		seccionTransversal = StringVar()
		seccionTransversal.set("Sección transversal")
		listaValoresTempSeccionTransversal=list()
		listaValoresTempSeccionTransversal.append("6 X 6")
		listaValoresTempSeccionTransversal.append("8 X 8")
		listaValoresTempSeccionTransversal.append("10 X 10")
		listaValoresTempSeccionTransversal.append("12 X 12")
		listaValoresTempSeccionTransversal.append("14 X 14")
		listaValoresTempSeccionTransversal.append("16 X 16")
		listaValoresTempSeccionTransversal.append("18 X 18")
		listaValoresTempSeccionTransversal.append("20 X 20")
		seccionTransversalName = OptionMenu(drenajeFiltrosMainFrame, seccionTransversal, *listaValoresTempSeccionTransversal)
		seccionTransversalLabel= Label(drenajeFiltrosMainWindow, text="Seleccione la sección transversal comercial del múltiple", font=("Yu Gothic bold", 11))


		distanciaLaterales = StringVar()
		distanciaLaterales.set("Distancia entre laterales")
		listaValoresTempDistanciaLaterales=list()
		listaValoresTempDistanciaLaterales.append("0.20")
		listaValoresTempDistanciaLaterales.append("0.25")
		listaValoresTempDistanciaLaterales.append("0.30")
		distanciaLateralesName = OptionMenu(drenajeFiltrosMainFrame, distanciaLaterales, *listaValoresTempDistanciaLaterales)
		distanciaLateralesLabel= Label(drenajeFiltrosMainWindow, text="Seleccione la distancia entre laterales", font=("Yu Gothic bold", 11))
		

		
		diametroEntreLaterales = StringVar()
		diametroEntreLaterales.set("Diámetro de los laterales")
		listaValoresTempDiametroEntreLaterales=list()
		listaValoresTempDiametroEntreLaterales.append("1 1/2")
		listaValoresTempDiametroEntreLaterales.append("2")
		listaValoresTempDiametroEntreLaterales.append("2 1/2")
		listaValoresTempDiametroEntreLaterales.append("3")
		diametroEntreLateralesName = OptionMenu(drenajeFiltrosMainFrame, diametroEntreLaterales, *listaValoresTempDiametroEntreLaterales)
		diametroEntreLateralesLabel= Label(drenajeFiltrosMainWindow, text="Seleccione el diámetro de los laterales", font=("Yu Gothic bold", 11))


		
		listaEntradaDrenaje2=[diametroOrificiosName,distanciaOrificiosName,seccionTransversalName,distanciaLateralesName, diametroEntreLateralesName]
		listaLabel= [diametroOrificiosLabel,distanciaOrificiosLabel, seccionTransversalLabel, distanciaLateralesLabel, diametroEntreLateralesLabel]
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]
		
		#Borrar

		diametroOrificios.set("1/4")
		distanciaOrificios.set("0.100")
		seccionTransversal.set("14 X 14")
		distanciaLaterales.set("0.25")
		diametroEntreLaterales.set("1 1/2")


		
	
		altIn= 30
		for ind in range(0,len(listaLabel)):
			listaLabel[ind].place(x=0,y=altIn)
			listaEntradaDrenaje2[ind].place(x=0, y= altIn+20)
			altIn=altIn+80
		
		botonCalculoDrenaje = HoverButton(drenajeFiltrosMainFrame, text="Cálculos para el drenaje del filtro", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: drenajeFiltro2(caudalMedio,listaEntradaDrenaje))
		botonCalculoDrenaje.place(x=0, y=altIn)
		
		
		def newEntryFiltroDrenaje(lista): 
			lista2= [
						"Diametro de los orificios",
						"Distancia entre los orificios",
						"Sección transversal",
						"Distancia entre laterales",
						"Diámetro de los laterales"]

			for i in range(0, len(lista)):
					lista[i].set(lista2[i])



		botonLimpiarEntradasDrenaje = HoverButton(drenajeFiltrosMainFrame, text="Limpiar entradas", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: newEntryFiltroDrenaje(listaEntradaDrenaje))
		botonLimpiarEntradasDrenaje.place(x=0, y=altIn+80)		
		#Pendiente: Botón Limpiar Entradas
	
		
		
		drenajeFiltrosMainWindow.mainloop()
	
	def velocidadLavadoExpansionLechoFiltrante(tempValue,d60):
		
		


		velocidadLavadoExpansionLechoFiltranteWindow = tk.Toplevel()
		velocidadLavadoExpansionLechoFiltranteWindow.iconbitmap(bitmap='icons\\agua.ico')
		velocidadLavadoExpansionLechoFiltranteWindow.geometry("600x400") 
		velocidadLavadoExpansionLechoFiltranteWindow.resizable(0,0)	
		velocidadLavadoExpansionLechoFiltranteWindow.configure(background="#9DC4AA")

		velocidadLavadoExpansionLechoFiltranteFrame=LabelFrame(velocidadLavadoExpansionLechoFiltranteWindow, text="Cálculos para la velocidad de expansión del lecho filtrante", font=("Yu Gothic bold", 11))
		velocidadLavadoExpansionLechoFiltranteFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolvelocidadLavadoExpansionLechoFiltrante_frame = Frame(velocidadLavadoExpansionLechoFiltranteFrame)
		arbolvelocidadLavadoExpansionLechoFiltrante_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolvelocidadLavadoExpansionLechoFiltrante_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolvelocidadLavadoExpansionLechoFiltrante_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolvelocidadLavadoExpansionLechoFiltrante= ttk.Treeview(arbolvelocidadLavadoExpansionLechoFiltrante_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolvelocidadLavadoExpansionLechoFiltrante.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolvelocidadLavadoExpansionLechoFiltrante.xview)
		sedScrollY.configure(command=arbolvelocidadLavadoExpansionLechoFiltrante.yview)
		#Define columnas.
		arbolvelocidadLavadoExpansionLechoFiltrante["columns"]= (
		"Porosidad del lecho fijo", "Viscosidad dinámica del agua",
		"Percentil 60 del análisis granulométrico", "Velocidad de asentamiento del medio filtrante a 20 °C",
		f"Velocidad de asentamiento del medio filtrante a {tempValue} °C",
		f"Velocidad de fluidización del medio filtrante a {tempValue} °C",
		f"Velocidad óptima de lavado a {tempValue} °C",
		"Porosidad del lecho expandido",
		"Profundidad del lecho fijo",
		"Profundidad del lecho expandido",
		"Relación de expansión",
		)

		#Headings
		arbolvelocidadLavadoExpansionLechoFiltrante.heading("#0",text="ID", anchor=CENTER)

		for col in arbolvelocidadLavadoExpansionLechoFiltrante["columns"]:
			arbolvelocidadLavadoExpansionLechoFiltrante.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolvelocidadLavadoExpansionLechoFiltrante["columns"])+1) :
				arbolvelocidadLavadoExpansionLechoFiltrante.column(f"#{i}",width=700, stretch=False)	
		arbolvelocidadLavadoExpansionLechoFiltrante.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolvelocidadLavadoExpansionLechoFiltrante.tag_configure("evenrow", background= "#1FCCDB")
		arbolvelocidadLavadoExpansionLechoFiltrante.tag_configure("oddrow", background= "#9DC4AA")    

		listavelocidadLavadoExpansionLechoFiltrante=list()
	
		porosidad= 0.45
		listavelocidadLavadoExpansionLechoFiltrante.append(porosidad)


		tablaTemperaturaViscosidadDinamica=dict()
		valorTemperaturas=list()
		
		for i in range(0,36):
			valorTemperaturas.append(i)

		valorViscosidadDinamica = [0.001792, 0.001731, 0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 0.001083, 0.001056, 0.00103
					, 0.001005, 0.000981, 0.000958, 0.000936, 0.000914, 0.000894, 0.000874, 0.000855, 0.000836, 0.000818, 0.000801, 0.000784, 0.000768, 0.000752, 0.000737, 0.000723]  

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaViscosidadDinamica[valorTemperaturas[ind]] = valorViscosidadDinamica[ind]

		viscosidadDinamica= tablaTemperaturaViscosidadDinamica[tempValue] * 1000.0
		
		listavelocidadLavadoExpansionLechoFiltrante.append(viscosidadDinamica)

		D60=d60

		listavelocidadLavadoExpansionLechoFiltrante.append(D60)

		velocidadAsentamientoMedioFiltrante20 = D60*10
		
		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadAsentamientoMedioFiltrante20)

		velocidadAsentamientoMedioFiltrante3= velocidadAsentamientoMedioFiltrante20*(viscosidadDinamica**(-1/3))

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadAsentamientoMedioFiltrante3)

		velocidadFluidizacion3 = velocidadAsentamientoMedioFiltrante3*(porosidad**(4.5))

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadFluidizacion3)

		velocidadOptimaLavado3= velocidadAsentamientoMedioFiltrante3*0.1

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadOptimaLavado3)

		porosidadLechoExpandido = (velocidadOptimaLavado3/velocidadAsentamientoMedioFiltrante3)**(0.22)

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadOptimaLavado3)

		profundidadLechoFijo = 0.640

		listavelocidadLavadoExpansionLechoFiltrante.append(profundidadLechoFijo)

		profundidadLechoExpandido= profundidadLechoFijo*((1-porosidad)/(1- porosidadLechoExpandido))

		listavelocidadLavadoExpansionLechoFiltrante.append(profundidadLechoExpandido)

		relacionExpansion = ((porosidadLechoExpandido-porosidad)/(1-porosidadLechoExpandido))*100

		listavelocidadLavadoExpansionLechoFiltrante.append(relacionExpansion)


		newDataTreeview(arbolvelocidadLavadoExpansionLechoFiltrante,listavelocidadLavadoExpansionLechoFiltrante)
		
		velocidadLavadoExpansionLechoFiltranteWindow.mainloop()
	
	def ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60):
		

		listavelocidadLavadoExpansionLechoFiltrante=list()
	
		porosidad= 0.45
		listavelocidadLavadoExpansionLechoFiltrante.append(porosidad)


		tablaTemperaturaViscosidadDinamica=dict()
		valorTemperaturas=list()
		
		for i in range(0,36):
			valorTemperaturas.append(i)

		valorViscosidadDinamica = [0.001792, 0.001731, 0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 0.001083, 0.001056, 0.00103
					, 0.001005, 0.000981, 0.000958, 0.000936, 0.000914, 0.000894, 0.000874, 0.000855, 0.000836, 0.000818, 0.000801, 0.000784, 0.000768, 0.000752, 0.000737, 0.000723]  

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaViscosidadDinamica[valorTemperaturas[ind]] = valorViscosidadDinamica[ind]

		viscosidadDinamica= tablaTemperaturaViscosidadDinamica[tempValue] * 1000.0
		
		listavelocidadLavadoExpansionLechoFiltrante.append(viscosidadDinamica)

		D60=d60

		listavelocidadLavadoExpansionLechoFiltrante.append(D60)

		velocidadAsentamientoMedioFiltrante20 = D60*10
		
		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadAsentamientoMedioFiltrante20)

		velocidadAsentamientoMedioFiltrante3= velocidadAsentamientoMedioFiltrante20*(viscosidadDinamica**(-1/3))

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadAsentamientoMedioFiltrante3)

		velocidadFluidizacion3 = velocidadAsentamientoMedioFiltrante3*(porosidad**(4.5))

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadFluidizacion3)

		velocidadOptimaLavado3= velocidadAsentamientoMedioFiltrante3*0.1

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadOptimaLavado3)

		porosidadLechoExpandido = (velocidadOptimaLavado3/velocidadAsentamientoMedioFiltrante3)**(0.22)

		listavelocidadLavadoExpansionLechoFiltrante.append(velocidadOptimaLavado3)

		profundidadLechoFijo = 0.640

		listavelocidadLavadoExpansionLechoFiltrante.append(profundidadLechoFijo)

		profundidadLechoExpandido= profundidadLechoFijo*((1-porosidad)/(1- porosidadLechoExpandido))

		listavelocidadLavadoExpansionLechoFiltrante.append(profundidadLechoExpandido)

		relacionExpansion = ((porosidadLechoExpandido-porosidad)/(1-porosidadLechoExpandido))*100

		listavelocidadLavadoExpansionLechoFiltrante.append(relacionExpansion)
		
		return(listavelocidadLavadoExpansionLechoFiltrante)
		


	def ValueConsumoAguaLavado(listaE,tempValue,d60,caudalLista):
		

	
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		else:
			tiempoRetrolavado = float(listaE[0].get())

		listaconsumoAguaLavado2=list()

		listaVelocidadVelocidadLavadoExpansion = ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60)

		listaconsumoAguaLavado2.append(tiempoRetrolavado)

		carreraFiltracionNormal=36.0

		listaconsumoAguaLavado2.append(carreraFiltracionNormal)

		velocidadDeLavado= round(listaVelocidadVelocidadLavadoExpansion[6],4)
		
		listaconsumoAguaLavado2.append(velocidadDeLavado)

		tasaFiltracionOpNormal=120

		listaconsumoAguaLavado2.append(tasaFiltracionOpNormal)

		areaDeFiltro= round(ValuepredimensionamientoFiltros(caudalLista)[5],2)
		
		listaconsumoAguaLavado2.append(areaDeFiltro)

		caudalLavado = round((velocidadDeLavado/60)*areaDeFiltro,3)

		listaconsumoAguaLavado2.append(caudalLavado)

		consumoAguaLavadoFiltro = round(tiempoRetrolavado*velocidadDeLavado*areaDeFiltro,3)

		listaconsumoAguaLavado2.append(consumoAguaLavadoFiltro)
		
		aguaProducidaFiltroCiclo= round((tasaFiltracionOpNormal/24.0)*areaDeFiltro*carreraFiltracionNormal,3)

		listaconsumoAguaLavado2.append(aguaProducidaFiltroCiclo)

		porcentajeAguaFiltrada = (consumoAguaLavadoFiltro/aguaProducidaFiltroCiclo)*100

		listaconsumoAguaLavado2.append(porcentajeAguaFiltrada)

		return listaconsumoAguaLavado2


	def consumoAguaLavado(listaE,tempValue,d60,caudalLista):
		

	
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		else:
			tiempoRetrolavado = float(listaE[0].get())





		consumoAguaLavado2Window = tk.Toplevel()
		consumoAguaLavado2Window.iconbitmap(bitmap='icons\\agua.ico')
		consumoAguaLavado2Window.geometry("600x400") 
		consumoAguaLavado2Window.resizable(0,0)	
		consumoAguaLavado2Window.configure(background="#9DC4AA")

		consumoAguaLavado2Frame=LabelFrame(consumoAguaLavado2Window, text="Cálculos para el consumo de agua de lavado", font=("Yu Gothic bold", 11))
		consumoAguaLavado2Frame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolconsumoAguaLavado2_frame = Frame(consumoAguaLavado2Frame)
		arbolconsumoAguaLavado2_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolconsumoAguaLavado2_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolconsumoAguaLavado2_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolconsumoAguaLavado2= ttk.Treeview(arbolconsumoAguaLavado2_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolconsumoAguaLavado2.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolconsumoAguaLavado2.xview)
		sedScrollY.configure(command=arbolconsumoAguaLavado2.yview)
		#Define columnas.
		arbolconsumoAguaLavado2["columns"]= (
		"Tiempo de retrolavado",
		"Carrera de filtración normal o duración del ciclo",
		"Velocidad de lavado",
		"Tasa de filtración en operación normal",
		"Área de un filtro",
		"Caudal de lavado",
		"Consumo de agua para lavado de un filtro (Volumen del tanque)",
		"Agua producida por un filtro en cada ciclo",
		"Porcentaje de agua filtrada usada en el lavado de un filtro",
		)

		#Headings
		arbolconsumoAguaLavado2.heading("#0",text="ID", anchor=CENTER)

		for col in arbolconsumoAguaLavado2["columns"]:
			arbolconsumoAguaLavado2.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolconsumoAguaLavado2["columns"])+1) :
				arbolconsumoAguaLavado2.column(f"#{i}",width=700, stretch=False)	
		arbolconsumoAguaLavado2.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolconsumoAguaLavado2.tag_configure("evenrow", background= "#1FCCDB")
		arbolconsumoAguaLavado2.tag_configure("oddrow", background= "#9DC4AA")    


		listaconsumoAguaLavado2=list()

		listaVelocidadVelocidadLavadoExpansion = ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60)

		listaconsumoAguaLavado2.append(tiempoRetrolavado)

		carreraFiltracionNormal=36.0

		listaconsumoAguaLavado2.append(carreraFiltracionNormal)

		velocidadDeLavado= round(listaVelocidadVelocidadLavadoExpansion[6],4)
		
		listaconsumoAguaLavado2.append(velocidadDeLavado)

		tasaFiltracionOpNormal=120

		listaconsumoAguaLavado2.append(tasaFiltracionOpNormal)

		areaDeFiltro= round(ValuepredimensionamientoFiltros(caudalLista)[5],2)
		
		listaconsumoAguaLavado2.append(areaDeFiltro)

		caudalLavado = round((velocidadDeLavado/60)*areaDeFiltro,3)

		listaconsumoAguaLavado2.append(caudalLavado)

		consumoAguaLavadoFiltro = round(tiempoRetrolavado*velocidadDeLavado*areaDeFiltro,3)

		listaconsumoAguaLavado2.append(consumoAguaLavadoFiltro)
		
		aguaProducidaFiltroCiclo= round((tasaFiltracionOpNormal/24.0)*areaDeFiltro*carreraFiltracionNormal,3)

		listaconsumoAguaLavado2.append(aguaProducidaFiltroCiclo)

		porcentajeAguaFiltrada = (consumoAguaLavadoFiltro/aguaProducidaFiltroCiclo)*100

		listaconsumoAguaLavado2.append(porcentajeAguaFiltrada)

		newDataTreeview(arbolconsumoAguaLavado2,listaconsumoAguaLavado2)
		
		consumoAguaLavado2Window.mainloop()




	def valuePerdidaCargaLechoExpandido():
		
		listaperdidaCargaLechoExpandido=list()
		
		profundidadLechoFijo= 0.64
		listaperdidaCargaLechoExpandido.append(profundidadLechoFijo)


		porosidadLechoFijo= 0.45
		listaperdidaCargaLechoExpandido.append(porosidadLechoFijo)

		densidadRelativaArena=2.650
		listaperdidaCargaLechoExpandido.append(densidadRelativaArena)

		perdidaCargaALechoExpandido= profundidadLechoFijo*(1-porosidadLechoFijo)*(densidadRelativaArena-1)
		listaperdidaCargaLechoExpandido.append(perdidaCargaALechoExpandido)

		return listaperdidaCargaLechoExpandido


	def perdidaCargaLechoExpandido():
		perdidaCargaLechoExpandidoWindow = tk.Toplevel()
		perdidaCargaLechoExpandidoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaLechoExpandidoWindow.geometry("600x400") 
		perdidaCargaLechoExpandidoWindow.resizable(0,0)	
		perdidaCargaLechoExpandidoWindow.configure(background="#9DC4AA")

		perdidaCargaLechoExpandidoFrame=LabelFrame(perdidaCargaLechoExpandidoWindow, text="Cálculos para la velocidad de expansión del lecho filtrante", font=("Yu Gothic bold", 11))
		perdidaCargaLechoExpandidoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaLechoExpandido_frame = Frame(perdidaCargaLechoExpandidoFrame)
		arbolperdidaCargaLechoExpandido_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaLechoExpandido_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidaCargaLechoExpandido_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaLechoExpandido= ttk.Treeview(arbolperdidaCargaLechoExpandido_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaLechoExpandido.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaLechoExpandido.xview)
		sedScrollY.configure(command=arbolperdidaCargaLechoExpandido.yview)
		#Define columnas.
		arbolperdidaCargaLechoExpandido["columns"]= (
		"Profundidad del lecho fijo", 
		"Porosidad del lecho fijo",
		"Densidad relativa de la arena",
		"Pérdida de carga a través del lecho expandido"
		)

		#Headings
		arbolperdidaCargaLechoExpandido.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaLechoExpandido["columns"]:
			arbolperdidaCargaLechoExpandido.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidaCargaLechoExpandido["columns"])+1) :
				arbolperdidaCargaLechoExpandido.column(f"#{i}",width=700, stretch=False)	
		arbolperdidaCargaLechoExpandido.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaLechoExpandido.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaLechoExpandido.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaLechoExpandido=list()
		

		profundidadLechoFijo= 0.64
		listaperdidaCargaLechoExpandido.append(profundidadLechoFijo)


		porosidadLechoFijo= 0.45
		listaperdidaCargaLechoExpandido.append(porosidadLechoFijo)

		densidadRelativaArena=2.650
		listaperdidaCargaLechoExpandido.append(densidadRelativaArena)

		perdidaCargaALechoExpandido= profundidadLechoFijo*(1-porosidadLechoFijo)*(densidadRelativaArena-1)
		listaperdidaCargaLechoExpandido.append(perdidaCargaALechoExpandido)

		newDataTreeview(arbolperdidaCargaLechoExpandido,listaperdidaCargaLechoExpandido)

		perdidaCargaLechoExpandidoWindow.mainloop()



		
	def valuePerdidacargaLechoGravaLavado(tempValue,d60):
		
		listaperdidacargaLechoGravaLavado=list()
		
		velocidadLavado= ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60)[6]
		listaperdidacargaLechoGravaLavado.append(velocidadLavado)

		profundidadLechoGrava= 0.100+0.075+0.075+0.100+0.100

		listaperdidacargaLechoGravaLavado.append(profundidadLechoGrava)

		perdidaLechoGrava= velocidadLavado*profundidadLechoGrava*(1/3)

		listaperdidacargaLechoGravaLavado.append(perdidaLechoGrava)

		return listaperdidacargaLechoGravaLavado


	def perdidacargaLechoGravaLavado(tempValue,d60):
		perdidacargaLechoGravaLavadoWindow = tk.Toplevel()
		perdidacargaLechoGravaLavadoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidacargaLechoGravaLavadoWindow.geometry("600x400") 
		perdidacargaLechoGravaLavadoWindow.resizable(0,0)	
		perdidacargaLechoGravaLavadoWindow.configure(background="#9DC4AA")

		perdidacargaLechoGravaLavadoFrame=LabelFrame(perdidacargaLechoGravaLavadoWindow, text="Cálculos para la pérdida de carga a través del lecho de grava", font=("Yu Gothic bold", 11))
		perdidacargaLechoGravaLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidacargaLechoGravaLavado_frame = Frame(perdidacargaLechoGravaLavadoFrame)
		arbolperdidacargaLechoGravaLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidacargaLechoGravaLavado= ttk.Treeview(arbolperdidacargaLechoGravaLavado_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidacargaLechoGravaLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidacargaLechoGravaLavado.xview)
		sedScrollY.configure(command=arbolperdidacargaLechoGravaLavado.yview)
		#Define columnas.
		arbolperdidacargaLechoGravaLavado["columns"]= (
		"Velocidad de lavado", 
		"Profundidad del lecho de grava",
		"Pérdida de carga a través del lecho de grava",
		)

		#Headings
		arbolperdidacargaLechoGravaLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidacargaLechoGravaLavado["columns"]:
			arbolperdidacargaLechoGravaLavado.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidacargaLechoGravaLavado["columns"])+1) :
				arbolperdidacargaLechoGravaLavado.column(f"#{i}",width=700, stretch=False)	
		arbolperdidacargaLechoGravaLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidacargaLechoGravaLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidacargaLechoGravaLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidacargaLechoGravaLavado=list()
		
		velocidadLavado= ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60)[6]
		listaperdidacargaLechoGravaLavado.append(velocidadLavado)

		profundidadLechoGrava= 0.100+0.075+0.075+0.100+0.100

		listaperdidacargaLechoGravaLavado.append(profundidadLechoGrava)

		perdidaLechoGrava= velocidadLavado*profundidadLechoGrava*(1/3)

		listaperdidacargaLechoGravaLavado.append(perdidaLechoGrava)

		newDataTreeview(arbolperdidacargaLechoGravaLavado,listaperdidacargaLechoGravaLavado)

		perdidacargaLechoGravaLavadoWindow.mainloop()



	def valuePerdidacargaLechoGravaLavado_2(tempValue,d60,tasa):

		listaperdidacargaLechoGravaLavado=list()
		if tasa == "Tasa media":
			velocidadLavado= 120/(24*60)
		elif tasa == "Tasa máxima":
			velocidadLavado= 150/(24*60)
		
		listaperdidacargaLechoGravaLavado.append(velocidadLavado)

		profundidadLechoGrava= 0.100+0.075+0.075+0.100+0.100

		listaperdidacargaLechoGravaLavado.append(profundidadLechoGrava)

		perdidaLechoGrava= velocidadLavado*profundidadLechoGrava*(1/3)

		listaperdidacargaLechoGravaLavado.append(perdidaLechoGrava)

		return listaperdidacargaLechoGravaLavado

	
	def perdidacargaLechoGravaLavado_2(tasaE):

		
		if tasaE.get() == "Tasa":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la tasa.")
			return None
		else:
			tasa = tasaE.get()

		perdidacargaLechoGravaLavadoWindow = tk.Toplevel()
		perdidacargaLechoGravaLavadoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidacargaLechoGravaLavadoWindow.geometry("600x400") 
		perdidacargaLechoGravaLavadoWindow.resizable(0,0)	
		perdidacargaLechoGravaLavadoWindow.configure(background="#9DC4AA")

		perdidacargaLechoGravaLavadoFrame=LabelFrame(perdidacargaLechoGravaLavadoWindow, text="Cálculos para la pérdida de carga a través del lecho de grava (Dixon)", font=("Yu Gothic bold", 11))
		perdidacargaLechoGravaLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidacargaLechoGravaLavado_frame = Frame(perdidacargaLechoGravaLavadoFrame)
		arbolperdidacargaLechoGravaLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidacargaLechoGravaLavado= ttk.Treeview(arbolperdidacargaLechoGravaLavado_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidacargaLechoGravaLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidacargaLechoGravaLavado.xview)
		sedScrollY.configure(command=arbolperdidacargaLechoGravaLavado.yview)
		#Define columnas.
		arbolperdidacargaLechoGravaLavado["columns"]= (
		"Tasa de filtración", 
		"Profundidad del lecho de grava",
		"Pérdida de carga a través del lecho de grava",
		)

		#Headings
		arbolperdidacargaLechoGravaLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidacargaLechoGravaLavado["columns"]:
			arbolperdidacargaLechoGravaLavado.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidacargaLechoGravaLavado["columns"])+1) :
				arbolperdidacargaLechoGravaLavado.column(f"#{i}",width=700, stretch=False)	
		arbolperdidacargaLechoGravaLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidacargaLechoGravaLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidacargaLechoGravaLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidacargaLechoGravaLavado=list()
		if tasa == "Tasa media":
			velocidadLavado= 120/(24*60)
		elif tasa == "Tasa máxima":
			velocidadLavado= 150/(24*60)
		
		listaperdidacargaLechoGravaLavado.append(velocidadLavado)

		profundidadLechoGrava= 0.100+0.075+0.075+0.100+0.100

		listaperdidacargaLechoGravaLavado.append(profundidadLechoGrava)

		perdidaLechoGrava= velocidadLavado*profundidadLechoGrava*(1/3)

		listaperdidacargaLechoGravaLavado.append(perdidaLechoGrava)

		newDataTreeview(arbolperdidacargaLechoGravaLavado,listaperdidacargaLechoGravaLavado)

		perdidacargaLechoGravaLavadoWindow.mainloop()

	def valuePerdidaCargaSistemaDrenajeLavado(tempValue,d60, caudal,listaEntradaDrenaje):
		
		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		velocidadDeLavado= round(ValuevelocidadLavadoExpansionLechoFiltrante(tempValue, d60)[6]*(1/60.0),4)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(velocidadDeLavado)

		coeficienteDeOrificio=0.6
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(coeficienteDeOrificio)

		areaTotalOrificios=round(ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[5],4)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(areaTotalOrificios)

		

		perdidaCargaSistemaDrenaje= (1/(2.0*9.806))*((velocidadDeLavado/(coeficienteDeOrificio*areaTotalOrificios))**2)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(perdidaCargaSistemaDrenaje)

		return listaperdidaCargaSistemaDrenajeLavadoLavado

		

		



	def perdidaCargaSistemaDrenajeLavado(tempValue,d60, caudal,listaEntradaDrenaje):

		
		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None
	

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		
		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
	
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		
	

		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
		

		



		
		
		
		
		perdidaCargaSistemaDrenajeLavadoLavadoWindow = tk.Toplevel()
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.geometry("600x400") 
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.resizable(0,0)	
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaSistemaDrenajeLavadoLavadoFrame=LabelFrame(perdidaCargaSistemaDrenajeLavadoLavadoWindow, text="Cálculos para la pérdida de carga a través del sistema de drenaje durante el lavado", font=("Yu Gothic bold", 11))
		perdidaCargaSistemaDrenajeLavadoLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame = Frame(perdidaCargaSistemaDrenajeLavadoLavadoFrame)
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado= ttk.Treeview(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaSistemaDrenajeLavadoLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.xview)
		sedScrollY.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.yview)
		#Define columnas.
		arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]= (
		"Velocidad de lavado",
		"Coeficiente de orificio",
		"Área total de orificios/ área filtrante",
		"Pérdida de carga a través del sistema de drenaje",
		)

		#Headings
		arbolperdidaCargaSistemaDrenajeLavadoLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]:
			arbolperdidaCargaSistemaDrenajeLavadoLavado.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"])+1) :
				arbolperdidaCargaSistemaDrenajeLavadoLavado.column(f"#{i}",width=700, stretch=False)	
		arbolperdidaCargaSistemaDrenajeLavadoLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		velocidadDeLavado= round(ValuevelocidadLavadoExpansionLechoFiltrante(tempValue, d60)[6]*(1/60.0),4)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(velocidadDeLavado)

		coeficienteDeOrificio=0.6
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(coeficienteDeOrificio)

		areaTotalOrificios=(ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[5])
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(areaTotalOrificios)

		print(velocidadDeLavado, coeficienteDeOrificio, areaTotalOrificios)
		#Pendiente. Valor extraño
		perdidaCargaSistemaDrenaje= (1.0/(2.0*9.806))*((velocidadDeLavado/(coeficienteDeOrificio*areaTotalOrificios))**2)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(perdidaCargaSistemaDrenaje)


		newDataTreeview(arbolperdidaCargaSistemaDrenajeLavadoLavado,listaperdidaCargaSistemaDrenajeLavadoLavado)

		perdidaCargaSistemaDrenajeLavadoLavadoWindow.mainloop()


	def valuePerdidaCargaSistemaDrenajeLavado_2(tempValue,d60, caudal,listaEntradaDrenaje, tasa):

		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		if tasa == "Tasa media":
			velocidadDeLavado= 120.0/86400.0
		elif tasa == "Tasa máxima":
			velocidadDeLavado= 150.0/86400.0
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(velocidadDeLavado)

		coeficienteDeOrificio=0.6
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(coeficienteDeOrificio)

		areaTotalOrificios=(ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[5])
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(areaTotalOrificios)

	

		perdidaCargaSistemaDrenaje= (1.0/(2.0*9.806))*((velocidadDeLavado/(coeficienteDeOrificio*areaTotalOrificios))**2)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(perdidaCargaSistemaDrenaje)
		return listaperdidaCargaSistemaDrenajeLavadoLavado



	def perdidaCargaSistemaDrenajeLavado_2(caudal,listaEntradaDrenaje, tasaE):

		if tasaE.get() == "Tasa":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la tasa.")
			return None
		else:
			tasa = tasaE.get()

		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())


		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())


		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()

		perdidaCargaSistemaDrenajeLavadoLavadoWindow = tk.Toplevel()
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.geometry("600x400") 
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.resizable(0,0)	
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaSistemaDrenajeLavadoLavadoFrame=LabelFrame(perdidaCargaSistemaDrenajeLavadoLavadoWindow, text="Cálculos para la pérdida de carga a través del sistema de drenaje durante el lavado", font=("Yu Gothic bold", 11))
		perdidaCargaSistemaDrenajeLavadoLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame = Frame(perdidaCargaSistemaDrenajeLavadoLavadoFrame)
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado= ttk.Treeview(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaSistemaDrenajeLavadoLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.xview)
		sedScrollY.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.yview)
		#Define columnas.
		arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]= (
		"Tasa de filtración",
		"Coeficiente de orificio",
		"Área total de orificios/ área filtrante",
		"Pérdida de carga a través del sistema de drenaje",
		)

		#Headings
		arbolperdidaCargaSistemaDrenajeLavadoLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]:
			arbolperdidaCargaSistemaDrenajeLavadoLavado.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"])+1) :
				arbolperdidaCargaSistemaDrenajeLavadoLavado.column(f"#{i}",width=700, stretch=False)	
		arbolperdidaCargaSistemaDrenajeLavadoLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		if tasa == "Tasa media":
			velocidadDeLavado= 120.0/86400.0
		elif tasa == "Tasa máxima":
			velocidadDeLavado= 150.0/86400.0
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(velocidadDeLavado)

		coeficienteDeOrificio=0.6
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(coeficienteDeOrificio)

		areaTotalOrificios=(ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[5])
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(areaTotalOrificios)

	

		perdidaCargaSistemaDrenaje= (1.0/(2.0*9.806))*((velocidadDeLavado/(coeficienteDeOrificio*areaTotalOrificios))**2)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(perdidaCargaSistemaDrenaje)


		newDataTreeview(arbolperdidaCargaSistemaDrenajeLavadoLavado,listaperdidaCargaSistemaDrenajeLavadoLavado)

		perdidaCargaSistemaDrenajeLavadoLavadoWindow.mainloop()

	
	def ValuePerdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista):
		
		

		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tubería de lavado")
						return None
					elif elemento.get() == "Diámetro nominal de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro nominal de la tubería de lavado")
						return None

					elif elemento.get() == "Codo 90° radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90° radio")
						return None
					
					
					elif elemento.get() == "Tipo de entrada":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de entrada del accesorio")
						return None

					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>50.0 or float(elemento.get())<5.0):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tubería de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricción debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None
			
		listaEU.append(temperatureValue)
		
		
		

		listaEntradaTemp1=list()
		listaEntradaTemp2=list()
		listaEntradaTemp3=list()
		

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]
		
		rugosidadLista=[0.1500, 0.1500, 0.2500,0.2500,0.0070,0.0070,0.0015,0.0015]


		rugosidadDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadDic[MaterialTuberiaLista[i]] = rugosidadLista[i]
		
		

		rugosidadAbsoluta= rugosidadDic[listaEU[0]]
		
		listaEntradaTemp1.append(rugosidadAbsoluta)


	
		diametroNominal = [(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		tuplasEntradas=list()
		
		i=-1

		for elemento in MaterialTuberiaLista:
			tuplaL = tuple()
			i=i+1
			for diam in diametroNominal[i]:
				tuplaL = (elemento,diam)
				tuplasEntradas.append(tuplaL)

		listaValoresDiametroInterno= [
		0.154, 0.203, 0.255, 0.303, 0.333, 0.381, 0.429, 0.478, 0.575,
		0.146, 0.194, 0.243, 0.289, 0.318, 0.364, 0.41, 0.456,0.502, 0.548,
		0.316,0.365,0.416,0.466,0.517,0.618, 
		0.161,0.213,0.263,0.314,0.364,0.413,0.463,0.513,0.613, 
		0.145,0.181,0.226,0.285,0.321,0.362,
		0.141,0.176,0.220,0.278,0.313,0.353, 
		0.155, 0.202, 0.252, 0.299, 0.328, 0.375, 0.422, 0.469, 0.563, 
		0.152, 0.198, 0.247, 0.293, 0.322, 0.368, 0.414, 0.46, 0.552]
		diametroInternoDic= dict()


		for i in range(0,len(listaValoresDiametroInterno)):

			diametroInternoDic[tuplasEntradas[i]]= listaValoresDiametroInterno[i]


		diametroInternoTuberiaLavado = diametroInternoDic[(listaEU[0],listaEU[1])]
		listaEntradaTemp1.append(diametroInternoTuberiaLavado)

		caudalLavado = ValueConsumoAguaLavado(listaE1,temperatureValue,d60,caudalLista)[5]
		velocidadFlujoTuberiaLavado = (4.0*caudalLavado)*(1.0/(pi*(diametroInternoTuberiaLavado**2)))
		listaEntradaTemp1.append(velocidadFlujoTuberiaLavado)
		
		cabezaVelocidad = (velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))
		listaEntradaTemp1.append(cabezaVelocidad)

		valorTemperaturas=list()
		tablaTemperaturaViscocidadCinematica=dict()


		for i in range(0,36):    
			valorTemperaturas.append(i)
					
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaViscocidadCinematica[valorTemperaturas[ind]]=valorViscocidad[ind]

		viscocidadCinematica= tablaTemperaturaViscocidadCinematica[temperatureValue]

		listaEntradaTemp1.append(viscocidadCinematica)

		numeroReynolds= velocidadFlujoTuberiaLavado*diametroInternoTuberiaLavado*(1/viscocidadCinematica)
		listaEntradaTemp1.append(numeroReynolds)

		factorFriccion=listaEU[3]

		for i in range(0,5):
			factorFriccion= (1/(-2*log10(((rugosidadAbsoluta/1000)*(1/(3.7*diametroInternoTuberiaLavado)))+(2.51*(1/(numeroReynolds*sqrt(factorFriccion)))))))**2
		
		listaEntradaTemp1.append(factorFriccion)

		perdidaCargaTuberiaLavadoDW= factorFriccion*(listaEU[2]/diametroInternoTuberiaLavado)*(velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))

		listaEntradaTemp1.append(perdidaCargaTuberiaLavadoDW)
			

		#DatosPara2

	
		coeficienteRugosidadHazenLista = [140, 140, 140, 140, 150, 150, 150, 150]

		rugosidadHazenDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadHazenDic[MaterialTuberiaLista[i]] = coeficienteRugosidadHazenLista[i]

		coeficienteRugosidadHazen= rugosidadHazenDic[listaEU[0]]
		listaEntradaTemp2.append(coeficienteRugosidadHazen)

		longitudTuberiaLavado = listaEU[2]
		listaEntradaTemp2.append(longitudTuberiaLavado)

		diametroNominalTuberiaLavado = listaEU[1]
		listaEntradaTemp2.append(diametroNominalTuberiaLavado)

		listaEntradaTemp2.append(diametroInternoTuberiaLavado)

		listaEntradaTemp2.append(velocidadFlujoTuberiaLavado)

		perdidaCargaUnitariaTuberiaLavado = (velocidadFlujoTuberiaLavado*(1/(0.354597213*coeficienteRugosidadHazen*(diametroInternoTuberiaLavado**0.63))))**(1/0.54)

		listaEntradaTemp2.append(perdidaCargaUnitariaTuberiaLavado)

		perdidaCargaTuberiaLavadoSinAccesorios = perdidaCargaUnitariaTuberiaLavado*longitudTuberiaLavado

		listaEntradaTemp2.append(perdidaCargaTuberiaLavadoSinAccesorios)
			
		#DatosPara3


		
		
		
		accesoriosLista = ["Válvula de compuerta completamente abierta",
		"Codo 90° radio corto (r/d 1)",
		"Codo 90° radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Unión",
		"Entrada recta a tope",
		"Entrada con boca acampanada",
		"Salida del tubo"]

		diametroNominalLista = [
		150,160,200,250,300,315,350,355,400,450,500,600,700,800,900,1000,6,8,10,12,14,16,18,20,24,28,32,34,36,40
		]
		tuplasEntradas2=[]

		for elemento in accesoriosLista:
			tuplaL = tuple()
			for diam in diametroNominalLista:
				tuplaL = (elemento,diam)
				tuplasEntradas2.append(tuplaL)

		listaValoresCoeficientePerdidaMenor= [

		0.12,	0.12,	0.11,	0.11,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.120,	0.110,	0.110,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.180,	0.178,	0.168,	0.168,	0.156,	0.156,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.132,	0.132,	0.132,	0.132,	0.180,	0.168,	0.168,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.13,	0.13,	0.13,	0.13,	0.13,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.90,	0.90,	0.84,	0.84,	0.78,	0.78,	0.78,	0.78,	0.78,	0.72,	0.72,	0.72,	0.66,	0.66,	0.66,	0.66,	0.900,	0.840,	0.840,	0.780,	0.780,	0.780,	0.720,	0.720,	0.720,	0.66,	0.66,	0.66,	0.66,	0.66,

		0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.30,	0.30,	0.30,	0.30,	0.30,

		0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.50,	0.50,	0.50,	0.50,	0.50,

		0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.00,	1.00,	1.00,	1.00,	1.00]


		CoeficientePerdidaMenorDic= dict()
		for i in range(0,len(listaValoresCoeficientePerdidaMenor)):
			CoeficientePerdidaMenorDic[tuplasEntradas2[i]]= listaValoresCoeficientePerdidaMenor[i]


		accesoriosListaEntrada= ["Válvula de compuerta completamente abierta",
		f"{listaEU[4]}",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Unión",
		f"{listaEU[5]}",
		"Salida del tubo"]

		
		
		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	
		sumaCoeficientesPerdidaMenor= 0
		
		for element in accesoriosListaEntrada:
			sumaCoeficientesPerdidaMenor=sumaCoeficientesPerdidaMenor+ CoeficientePerdidaMenorDic[(element,listaEU[1])]

		peridaCargaTuberiaLavadoAccesorios= sumaCoeficientesPerdidaMenor*cabezaVelocidad
		for elemento in accesoriosListaEntrada:
			listaEntradaTemp3=list()
			listaEntradaTemp3.append(elemento)
			listaEntradaTemp3.append(listaEU[1])
			listaEntradaTemp3.append(1)
			listaEntradaTemp3.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			listaEntradaTemp3.append(sumaCoeficientesPerdidaMenor)
			listaEntradaTemp3.append(peridaCargaTuberiaLavadoAccesorios)
		
		listaSalida = [listaEntradaTemp1,listaEntradaTemp2,peridaCargaTuberiaLavadoAccesorios]

		return listaSalida



	def perdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista):
		
	

		
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tubería de lavado")
						return None
					elif elemento.get() == "Diámetro nominal de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro nominal de la tubería de lavado")
						return None

					elif elemento.get() == "Codo 90° radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90° radio")
						return None
					
					
					elif elemento.get() == "Tipo de entrada":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de entrada del accesorio")
						return None

					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>50.0 or float(elemento.get())<5.0):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tubería de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricción debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None
			
		listaEU.append(temperatureValue)
		


		perdidaCargaTuberiaLavado_DW_HW2Window = tk.Toplevel()
		perdidaCargaTuberiaLavado_DW_HW2Window.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HW2Window.geometry("1000x500") 
		perdidaCargaTuberiaLavado_DW_HW2Window.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HW2Window.configure(background="#9DC4AA")




		##Panel:
		PanelPerdidaCargaTuberiaLavado = ttk.Notebook(perdidaCargaTuberiaLavado_DW_HW2Window)
		PanelPerdidaCargaTuberiaLavado.pack(fill=BOTH, expand=TRUE)
		###########Frame Principal1
		PerdidaCargaTuberiaLavado_DWFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimación de la pérdida de carga en la tubería de lavado", font=("Yu Gothic bold", 11))
		PerdidaCargaTuberiaLavado_DWFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(PerdidaCargaTuberiaLavado_DWFrame,text="Darcy - Weisbach")
		#Frame Treeview
		arbolPerdidaCargaTuberiaLavado_DW_frame = LabelFrame(PerdidaCargaTuberiaLavado_DWFrame, text="Darcy - Weisbach", font=("Yu Gothic bold", 11))
		arbolPerdidaCargaTuberiaLavado_DW_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaCargaTuberiaLavado_DW= ttk.Treeview(arbolPerdidaCargaTuberiaLavado_DW_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolPerdidaCargaTuberiaLavado_DW.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolPerdidaCargaTuberiaLavado_DW.xview)
		sedScrollY.configure(command=arbolPerdidaCargaTuberiaLavado_DW.yview)
		#Define columnas.
		arbolPerdidaCargaTuberiaLavado_DW["columns"]= (
		"Rugosidad absoluta de la tubería",
		"Diámetro interno de la tubería de lavado",
		"Velocidad de flujo en la tubería de lavado",
		"Cabeza de velocidad",
		f"Viscosidad cinemática del agua a {temperatureValue} °C ",
		"Número de Reynolds",
		"Factor de fricción (Iteración 4)",
		"Pérdida de carga en la tubería de lavado(Sin accesorios)", 
		)

		#Headings
		arbolPerdidaCargaTuberiaLavado_DW.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaCargaTuberiaLavado_DW["columns"]:
			arbolPerdidaCargaTuberiaLavado_DW.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolPerdidaCargaTuberiaLavado_DW["columns"])+1) :
				arbolPerdidaCargaTuberiaLavado_DW.column(f"#{i}",width=500, stretch=False)	
		arbolPerdidaCargaTuberiaLavado_DW.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("oddrow", background= "#1FCCDB")
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("evenrow", background= "#9DC4AA")

		################Frame principal2
		PerdidaCargaTuberiaLavado_HWFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimación de la pérdida de carga en la tubería de lavado", font=("Yu Gothic bold", 11))
		PerdidaCargaTuberiaLavado_HWFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(PerdidaCargaTuberiaLavado_HWFrame,text="Hazen - Williams")
		#Frame Treeview
		arbolPerdidaCargaTuberiaLavado_HW_frame = LabelFrame(PerdidaCargaTuberiaLavado_HWFrame, text="Hazen - Williams", font=("Yu Gothic bold", 11))
		arbolPerdidaCargaTuberiaLavado_HW_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolPerdidaCargaTuberiaLavado_HW_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPerdidaCargaTuberiaLavado_HW_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaCargaTuberiaLavado_HW= ttk.Treeview(arbolPerdidaCargaTuberiaLavado_HW_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolPerdidaCargaTuberiaLavado_HW.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolPerdidaCargaTuberiaLavado_HW.xview)
		sedScrollY.configure(command=arbolPerdidaCargaTuberiaLavado_HW.yview)
		#Define columnas.
		arbolPerdidaCargaTuberiaLavado_HW["columns"]= (
		"Coeficiente de rugosidad de Hazen-Williams",
		"Longitud de la tubería de lavado",
		"Diámetro nominal de la tubería de lavado",
		"Diámetro interno de la tubería de lavado",
		"Velocidad de flujo en la tubería de lavado",
		"Pérdida de carga unitaria en la tubería de lavado",
		"Pérdida de carga en la tubería de lavado(Sin accersorios)",
		)

		#Headings
		arbolPerdidaCargaTuberiaLavado_HW.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaCargaTuberiaLavado_HW["columns"]:
			arbolPerdidaCargaTuberiaLavado_HW.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolPerdidaCargaTuberiaLavado_HW["columns"])+1) :
				arbolPerdidaCargaTuberiaLavado_HW.column(f"#{i}",width=500, stretch=False)	
		arbolPerdidaCargaTuberiaLavado_HW.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPerdidaCargaTuberiaLavado_HW.tag_configure("oddrow", background= "#1FCCDB")
		arbolPerdidaCargaTuberiaLavado_HW.tag_configure("evenrow", background= "#9DC4AA")

		##########Frame principal3
		perdidaCargaTuberiaLavado_ACFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimación de la pérdida de carga en la tubería de lavado por accesorios", font=("Yu Gothic bold", 11))
		perdidaCargaTuberiaLavado_ACFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(perdidaCargaTuberiaLavado_ACFrame,text="Accesorios")
		#Frame Treeview
		arbolperdidaCargaTuberiaLavado_AC_frame = LabelFrame(perdidaCargaTuberiaLavado_ACFrame, text="Accesorios", font=("Yu Gothic bold", 11))
		arbolperdidaCargaTuberiaLavado_AC_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTuberiaLavado_AC= ttk.Treeview(arbolperdidaCargaTuberiaLavado_AC_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTuberiaLavado_AC.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaTuberiaLavado_AC.xview)
		sedScrollY.configure(command=arbolperdidaCargaTuberiaLavado_AC.yview)
		#Define columnas.
		arbolperdidaCargaTuberiaLavado_AC["columns"]= (
		"Accesorio",
		"Diámetro nominal",
		"Cantidad",
		"Coeficiente de pérdida menor",
		"Sumatoria de coeficientes de pérdida menor",
		"Pérdida de carga en la tubería de lavado por accesorios"
		)

		#Headings
		arbolperdidaCargaTuberiaLavado_AC.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTuberiaLavado_AC["columns"]:
			arbolperdidaCargaTuberiaLavado_AC.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidaCargaTuberiaLavado_AC["columns"])+1) :
				arbolperdidaCargaTuberiaLavado_AC.column(f"#{i}",width=500, stretch=False)	
		arbolperdidaCargaTuberiaLavado_AC.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("oddrow", background= "#1FCCDB")
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("evenrow", background= "#9DC4AA")



		############Insersión datos.
	
		
		contadorFiltro = 0

		listaEntradaTemp1=list()
		listaEntradaTemp2=list()
		listaEntradaTemp3=list()
		

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]
		
		rugosidadLista=[0.1500, 0.1500, 0.2500,0.2500,0.0070,0.0070,0.0015,0.0015]

		
		rugosidadDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadDic[MaterialTuberiaLista[i]] = rugosidadLista[i]
		
		rugosidadAbsoluta= rugosidadDic[listaEU[0]]
		
		listaEntradaTemp1.append(rugosidadAbsoluta)

		

		'listaEU[1]'
		diametroNominal = [(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]
		


		tuplasEntradas=list()
		
		i=-1

		for elemento in MaterialTuberiaLista:
			tuplaL = tuple()
			i=i+1
			for diam in diametroNominal[i]:
				tuplaL = (elemento,diam)
				tuplasEntradas.append(tuplaL)

		listaValoresDiametroInterno= [
		0.154, 0.203, 0.255, 0.303, 0.333, 0.381, 0.429, 0.478, 0.575,
		0.146, 0.194, 0.243, 0.289, 0.318, 0.364, 0.41, 0.456,0.502, 0.548,
		0.316,0.365,0.416,0.466,0.517,0.618, 
		0.161,0.213,0.263,0.314,0.364,0.413,0.463,0.513,0.613, 
		0.145,0.181,0.226,0.285,0.321,0.362,
		0.141,0.176,0.220,0.278,0.313,0.353, 
		0.155, 0.202, 0.252, 0.299, 0.328, 0.375, 0.422, 0.469, 0.563, 
		0.152, 0.198, 0.247, 0.293, 0.322, 0.368, 0.414, 0.46, 0.552]
		diametroInternoDic= dict()

		for i in range(0,len(listaValoresDiametroInterno)):

			diametroInternoDic[tuplasEntradas[i]]= listaValoresDiametroInterno[i]


		diametroInternoTuberiaLavado = diametroInternoDic[(listaEU[0],listaEU[1])]
		listaEntradaTemp1.append(diametroInternoTuberiaLavado)

		caudalLavado = ValueConsumoAguaLavado(listaE1,temperatureValue,d60,caudalLista)[5]
		velocidadFlujoTuberiaLavado = (4.0*caudalLavado)*(1.0/(pi*(diametroInternoTuberiaLavado**2)))
		listaEntradaTemp1.append(velocidadFlujoTuberiaLavado)
		
		cabezaVelocidad = (velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))
		listaEntradaTemp1.append(cabezaVelocidad)

		valorTemperaturas=list()
		tablaTemperaturaViscocidadCinematica=dict()


		for i in range(0,36):    
			valorTemperaturas.append(i)
					
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaViscocidadCinematica[valorTemperaturas[ind]]=valorViscocidad[ind]

		viscocidadCinematica= tablaTemperaturaViscocidadCinematica[temperatureValue]

		listaEntradaTemp1.append(viscocidadCinematica)

		numeroReynolds= velocidadFlujoTuberiaLavado*diametroInternoTuberiaLavado*(1/viscocidadCinematica)
		listaEntradaTemp1.append(numeroReynolds)

		factorFriccion=listaEU[3]

		for i in range(0,5):
			factorFriccion= (1/(-2*log10(((rugosidadAbsoluta/1000)*(1/(3.7*diametroInternoTuberiaLavado)))+(2.51*(1/(numeroReynolds*sqrt(factorFriccion)))))))**2
		
		listaEntradaTemp1.append(factorFriccion)

		perdidaCargaTuberiaLavadoDW= factorFriccion*(listaEU[2]/diametroInternoTuberiaLavado)*(velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))

		listaEntradaTemp1.append(perdidaCargaTuberiaLavadoDW)
		
		newDataTreeview(arbolPerdidaCargaTuberiaLavado_DW, listaEntradaTemp1)

			

		#DatosPara2
		
		
	
		coeficienteRugosidadHazenLista = [140, 140, 140, 140, 150, 150, 150, 150]

		rugosidadHazenDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadHazenDic[MaterialTuberiaLista[i]] = coeficienteRugosidadHazenLista[i]

		coeficienteRugosidadHazen= rugosidadHazenDic[listaEU[0]]
		listaEntradaTemp2.append(coeficienteRugosidadHazen)

		longitudTuberiaLavado = listaEU[2]
		listaEntradaTemp2.append(longitudTuberiaLavado)

		diametroNominalTuberiaLavado = listaEU[1]
		listaEntradaTemp2.append(diametroNominalTuberiaLavado)

		listaEntradaTemp2.append(diametroInternoTuberiaLavado)

		listaEntradaTemp2.append(velocidadFlujoTuberiaLavado)

		perdidaCargaUnitariaTuberiaLavado = (velocidadFlujoTuberiaLavado*(1/(0.354597213*coeficienteRugosidadHazen*(diametroInternoTuberiaLavado**0.63))))**(1/0.54)

		listaEntradaTemp2.append(perdidaCargaUnitariaTuberiaLavado)

		perdidaCargaTuberiaLavadoSinAccesorios = perdidaCargaUnitariaTuberiaLavado*longitudTuberiaLavado

		listaEntradaTemp2.append(perdidaCargaTuberiaLavadoSinAccesorios)

		newDataTreeview(arbolPerdidaCargaTuberiaLavado_HW, listaEntradaTemp2)
			
		#DatosPara3
	
		
		tuplasEntradas2=list()
		
		accesoriosLista = ["Válvula de compuerta completamente abierta",
		"Codo 90° radio corto (r/d 1)",
		"Codo 90° radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Unión",
		"Entrada recta a tope",
		"Entrada con boca acampanada",
		"Salida del tubo"]
	
		diametroNominalLista = [
		150,160,200,250,300,315,350,355,400,450,500,600,700,800,900,1000,6,8,10,12,14,16,18,20,24,28,32,34,36,40
		]
		tuplasEntradas2=[]

		for elemento in accesoriosLista:
			tuplaL = tuple()
			for diam in diametroNominalLista:
				tuplaL = (elemento,diam)
				tuplasEntradas2.append(tuplaL)


		listaValoresCoeficientePerdidaMenor= [

		0.12,	0.12,	0.11,	0.11,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.120,	0.110,	0.110,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.180,	0.178,	0.168,	0.168,	0.156,	0.156,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.132,	0.132,	0.132,	0.132,	0.180,	0.168,	0.168,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.13,	0.13,	0.13,	0.13,	0.13,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.90,	0.90,	0.84,	0.84,	0.78,	0.78,	0.78,	0.78,	0.78,	0.72,	0.72,	0.72,	0.66,	0.66,	0.66,	0.66,	0.900,	0.840,	0.840,	0.780,	0.780,	0.780,	0.720,	0.720,	0.720,	0.66,	0.66,	0.66,	0.66,	0.66,

		0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.30,	0.30,	0.30,	0.30,	0.30,

		0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.50,	0.50,	0.50,	0.50,	0.50,

		0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.00,	1.00,	1.00,	1.00,	1.00]


		CoeficientePerdidaMenorDic= dict()
		for i in range(0,len(listaValoresCoeficientePerdidaMenor)):
			CoeficientePerdidaMenorDic[tuplasEntradas2[i]]= listaValoresCoeficientePerdidaMenor[i]

		accesoriosListaEntrada= ["Válvula de compuerta completamente abierta",
		f"{listaEU[4]}",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Unión",
		f"{listaEU[5]}",
		"Salida del tubo"]

		
		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	
		sumaCoeficientesPerdidaMenor= 0
		
		for element in accesoriosListaEntrada:
			sumaCoeficientesPerdidaMenor=sumaCoeficientesPerdidaMenor+ CoeficientePerdidaMenorDic[(element,listaEU[1])]

		peridaCargaTuberiaLavadoAccesorios= sumaCoeficientesPerdidaMenor*cabezaVelocidad
		for elemento in accesoriosListaEntrada:
			listaEntradaTemp3=list()
			listaEntradaTemp3.append(elemento)
			listaEntradaTemp3.append(listaEU[1])
			listaEntradaTemp3.append(1)
			listaEntradaTemp3.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			listaEntradaTemp3.append(sumaCoeficientesPerdidaMenor)
			listaEntradaTemp3.append(peridaCargaTuberiaLavadoAccesorios)
			newDataTreeview(arbolperdidaCargaTuberiaLavado_AC, listaEntradaTemp3)

		perdidaCargaTuberiaLavado_DW_HW2Window.mainloop()


	def valuePerdidaCargaTuberiaLavado_DW_HW2_2(listaE,temperatureValue,listaE1, d60,caudalLista,tasa):
		

		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tubería de lavado")
						return None
					elif elemento.get() == "Diámetro nominal de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro nominal de la tubería de lavado")
						return None

					elif elemento.get() == "Codo 90° radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90° radio")
						return None
					
					
					elif elemento.get() == "Tipo de entrada":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de entrada del accesorio")
						return None

					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>2.5 or float(elemento.get())<1.5):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tubería del efluente debe estar entre 1.5 y 2.5 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricción debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None
			
		listaEU.append(temperatureValue)
		


		
		############Insersión datos.
		

		listaEntradaTemp1=list()
		
		listaEntradaTemp3=list()
		

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]
		
		rugosidadLista=[0.1500, 0.1500, 0.2500,0.2500,0.0070,0.0070,0.0015,0.0015]


		rugosidadDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadDic[MaterialTuberiaLista[i]] = rugosidadLista[i]
		
		rugosidadAbsoluta= rugosidadDic[listaEU[0]]
		
		listaEntradaTemp1.append(rugosidadAbsoluta)

		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	


		'listaEU[1]'
		diametroNominal = [(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		tuplasEntradas=list()

		i=-1

		for elemento in MaterialTuberiaLista:
			tuplaL = tuple()
			i=i+1
			for diam in diametroNominal[i]:
				tuplaL = (elemento,diam)
				tuplasEntradas.append(tuplaL)

		listaValoresDiametroInterno= [
		0.154, 0.203, 0.255, 0.303, 0.333, 0.381, 0.429, 0.478, 0.575,
		0.146, 0.194, 0.243, 0.289, 0.318, 0.364, 0.41, 0.456,0.502, 0.548,
		0.316,0.365,0.416,0.466,0.517,0.618, 
		0.161,0.213,0.263,0.314,0.364,0.413,0.463,0.513,0.613, 
		0.145,0.181,0.226,0.285,0.321,0.362,
		0.141,0.176,0.220,0.278,0.313,0.353, 
		0.155, 0.202, 0.252, 0.299, 0.328, 0.375, 0.422, 0.469, 0.563, 
		0.152, 0.198, 0.247, 0.293, 0.322, 0.368, 0.414, 0.46, 0.552]
		diametroInternoDic= dict()


		for i in range(0,len(listaValoresDiametroInterno)):

			diametroInternoDic[tuplasEntradas[i]]= listaValoresDiametroInterno[i]


		diametroInternoTuberiaLavado = diametroInternoDic[(listaEU[0],listaEU[1])]
		listaEntradaTemp1.append(diametroInternoTuberiaLavado)

		if tasa == "Tasa media":
			caudalLavado = (120.0/86400.0)*ValuepredimensionamientoFiltros(caudalLista)[8]
		elif tasa == "Tasa máxima":
			caudalLavado = (150.0/86400.0)*ValuepredimensionamientoFiltros(caudalLista)[8]

		listaEntradaTemp1.append(caudalLavado)

		velocidadFlujoTuberiaLavado = (4.0*caudalLavado)*(1.0/(pi*(diametroInternoTuberiaLavado**2)))
		listaEntradaTemp1.append(velocidadFlujoTuberiaLavado)
		
		cabezaVelocidad = (velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))
		listaEntradaTemp1.append(cabezaVelocidad)

		valorTemperaturas=list()
		tablaTemperaturaViscocidadCinematica=dict()


		for i in range(0,36):    
			valorTemperaturas.append(i)
					
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaViscocidadCinematica[valorTemperaturas[ind]]=valorViscocidad[ind]

		viscocidadCinematica= tablaTemperaturaViscocidadCinematica[temperatureValue]

		listaEntradaTemp1.append(viscocidadCinematica)

		numeroReynolds= velocidadFlujoTuberiaLavado*diametroInternoTuberiaLavado*(1/viscocidadCinematica)
		listaEntradaTemp1.append(numeroReynolds)

		factorFriccion=listaEU[3]

		for i in range(0,5):
			factorFriccion= (1/(-2*log10(((rugosidadAbsoluta/1000)*(1/(3.7*diametroInternoTuberiaLavado)))+(2.51*(1/(numeroReynolds*sqrt(factorFriccion)))))))**2
		
		listaEntradaTemp1.append(factorFriccion)

		perdidaCargaTuberiaLavadoDW= factorFriccion*(listaEU[2]/diametroInternoTuberiaLavado)*(velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))

		listaEntradaTemp1.append(perdidaCargaTuberiaLavadoDW)
		
			
		#DatosPara3
	
		
		tuplasEntradas2=list()

		accesoriosLista = ["Válvula de compuerta completamente abierta",
		"Codo 90° radio corto (r/d 1)",
		"Codo 90° radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Unión",
		"Entrada recta a tope",
		"Entrada con boca acampanada",
		"Salida del tubo"]

		diametroNominalLista = [
		150,160,200,250,300,315,350,355,400,450,500,600,700,800,900,1000,6,8,10,12,14,16,18,20,24,28,32,34,36,40
		]
		tuplasEntradas2=[]

		for elemento in accesoriosLista:
			tuplaL = tuple()
			for diam in diametroNominalLista:
				tuplaL = (elemento,diam)
				tuplasEntradas2.append(tuplaL)

		listaValoresCoeficientePerdidaMenor= [

		0.12,	0.12,	0.11,	0.11,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.120,	0.110,	0.110,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.180,	0.178,	0.168,	0.168,	0.156,	0.156,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.132,	0.132,	0.132,	0.132,	0.180,	0.168,	0.168,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.13,	0.13,	0.13,	0.13,	0.13,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.90,	0.90,	0.84,	0.84,	0.78,	0.78,	0.78,	0.78,	0.78,	0.72,	0.72,	0.72,	0.66,	0.66,	0.66,	0.66,	0.900,	0.840,	0.840,	0.780,	0.780,	0.780,	0.720,	0.720,	0.720,	0.66,	0.66,	0.66,	0.66,	0.66,

		0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.30,	0.30,	0.30,	0.30,	0.30,

		0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.50,	0.50,	0.50,	0.50,	0.50,

		0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.00,	1.00,	1.00,	1.00,	1.00]


		CoeficientePerdidaMenorDic= dict()
		for i in range(0,len(listaValoresCoeficientePerdidaMenor)):
			CoeficientePerdidaMenorDic[tuplasEntradas2[i]]= listaValoresCoeficientePerdidaMenor[i]

		accesoriosListaEntrada= ["Válvula de compuerta completamente abierta",
		"Tee en sentido recto",
		f"{listaEU[5]}",
		"Salida del tubo"]

		
		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	
		sumaCoeficientesPerdidaMenor= 0
		
		for element in accesoriosListaEntrada:
			sumaCoeficientesPerdidaMenor=sumaCoeficientesPerdidaMenor+ CoeficientePerdidaMenorDic[(element,listaEU[1])]

		peridaCargaTuberiaLavadoAccesorios= sumaCoeficientesPerdidaMenor*cabezaVelocidad
		for elemento in accesoriosListaEntrada:
			listaEntradaTemp3=list()
			listaEntradaTemp3.append(elemento)
			listaEntradaTemp3.append(listaEU[1])
			listaEntradaTemp3.append(1)
			listaEntradaTemp3.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			listaEntradaTemp3.append(sumaCoeficientesPerdidaMenor)
			listaEntradaTemp3.append(peridaCargaTuberiaLavadoAccesorios)

		listaEntradaTemp1.append(peridaCargaTuberiaLavadoAccesorios)
		return listaEntradaTemp1

	def perdidaCargaTuberiaLavado_DW_HW2_2(listaE,temperatureValue,listaE1, d60,caudalLista,tasa):
		
	

		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tubería de lavado")
						return None
					elif elemento.get() == "Diámetro nominal de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro nominal de la tubería de lavado")
						return None

					elif elemento.get() == "Codo 90° radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90° radio")
						return None
					
					
					elif elemento.get() == "Tipo de entrada":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de entrada del accesorio")
						return None

					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>2.5 or float(elemento.get())<1.5):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tubería del efluente debe estar entre 1.5 y 2.5 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricción debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None
			
		listaEU.append(temperatureValue)
		


		perdidaCargaTuberiaLavado_DW_HW2Window = tk.Toplevel()
		perdidaCargaTuberiaLavado_DW_HW2Window.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HW2Window.geometry("1000x500") 
		perdidaCargaTuberiaLavado_DW_HW2Window.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HW2Window.configure(background="#9DC4AA")




		##Panel:
		PanelPerdidaCargaTuberiaLavado = ttk.Notebook(perdidaCargaTuberiaLavado_DW_HW2Window)
		PanelPerdidaCargaTuberiaLavado.pack(fill=BOTH, expand=TRUE)
		###########Frame Principal1
		PerdidaCargaTuberiaLavado_DWFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimación de la pérdida de carga en la tubería de lavado", font=("Yu Gothic bold", 11))
		PerdidaCargaTuberiaLavado_DWFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(PerdidaCargaTuberiaLavado_DWFrame,text="Darcy - Weisbach")
		#Frame Treeview
		arbolPerdidaCargaTuberiaLavado_DW_frame = LabelFrame(PerdidaCargaTuberiaLavado_DWFrame, text="Darcy - Weisbach", font=("Yu Gothic bold", 11))
		arbolPerdidaCargaTuberiaLavado_DW_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaCargaTuberiaLavado_DW= ttk.Treeview(arbolPerdidaCargaTuberiaLavado_DW_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolPerdidaCargaTuberiaLavado_DW.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolPerdidaCargaTuberiaLavado_DW.xview)
		sedScrollY.configure(command=arbolPerdidaCargaTuberiaLavado_DW.yview)
		#Define columnas.
		arbolPerdidaCargaTuberiaLavado_DW["columns"]= (
		"Rugosidad absoluta de la tubería",
		"Diámetro interno de la tubería del efluente",
		"Caudal de filtración",
		"Velocidad de flujo en la tubería del efluente",
		"Cabeza de velocidad",
		f"Viscosidad cinemática del agua a {temperatureValue} °C ",
		"Número de Reynolds",
		"Factor de fricción (Iteración 4)",
		"Pérdida de carga en la tubería de lavado(Sin accesorios)", 
		)

		#Headings
		arbolPerdidaCargaTuberiaLavado_DW.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaCargaTuberiaLavado_DW["columns"]:
			arbolPerdidaCargaTuberiaLavado_DW.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolPerdidaCargaTuberiaLavado_DW["columns"])+1) :
				arbolPerdidaCargaTuberiaLavado_DW.column(f"#{i}",width=500, stretch=False)	
		arbolPerdidaCargaTuberiaLavado_DW.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("oddrow", background= "#1FCCDB")
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("evenrow", background= "#9DC4AA")



		##########Frame principal3
		perdidaCargaTuberiaLavado_ACFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimación de la pérdida de carga en la tubería de lavado por accesorios", font=("Yu Gothic bold", 11))
		perdidaCargaTuberiaLavado_ACFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(perdidaCargaTuberiaLavado_ACFrame,text="Accesorios")
		#Frame Treeview
		arbolperdidaCargaTuberiaLavado_AC_frame = LabelFrame(perdidaCargaTuberiaLavado_ACFrame, text="Accesorios", font=("Yu Gothic bold", 11))
		arbolperdidaCargaTuberiaLavado_AC_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTuberiaLavado_AC= ttk.Treeview(arbolperdidaCargaTuberiaLavado_AC_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTuberiaLavado_AC.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaTuberiaLavado_AC.xview)
		sedScrollY.configure(command=arbolperdidaCargaTuberiaLavado_AC.yview)
		#Define columnas.
		arbolperdidaCargaTuberiaLavado_AC["columns"]= (
		"Accesorio",
		"Diámetro nominal",
		"Cantidad",
		"Coeficiente de pérdida menor",
		"Sumatoria de coeficientes de pérdida menor",
		"Pérdida de carga en la tubería de lavado por accesorios"
		)

		#Headings
		arbolperdidaCargaTuberiaLavado_AC.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTuberiaLavado_AC["columns"]:
			arbolperdidaCargaTuberiaLavado_AC.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidaCargaTuberiaLavado_AC["columns"])+1) :
				arbolperdidaCargaTuberiaLavado_AC.column(f"#{i}",width=500, stretch=False)	
		arbolperdidaCargaTuberiaLavado_AC.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("oddrow", background= "#1FCCDB")
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("evenrow", background= "#9DC4AA")



		############Insersión datos.
	
		
		contadorFiltro = 0

		listaEntradaTemp1=list()
		listaEntradaTemp2=list()
		listaEntradaTemp3=list()
		datosSalida=list()

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]
		
		rugosidadLista=[0.1500, 0.1500, 0.2500,0.2500,0.0070,0.0070,0.0015,0.0015]


		rugosidadDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadDic[MaterialTuberiaLista[i]] = rugosidadLista[i]
		
		rugosidadAbsoluta= rugosidadDic[listaEU[0]]
		
		listaEntradaTemp1.append(rugosidadAbsoluta)

		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	


		'listaEU[1]'
		

		diametroNominal = [(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		tuplasEntradas=list()

		i=-1

		for elemento in MaterialTuberiaLista:
			tuplaL = tuple()
			i=i+1
			for diam in diametroNominal[i]:
				tuplaL = (elemento,diam)
				tuplasEntradas.append(tuplaL)

		listaValoresDiametroInterno= [
		0.154, 0.203, 0.255, 0.303, 0.333, 0.381, 0.429, 0.478, 0.575,
		0.146, 0.194, 0.243, 0.289, 0.318, 0.364, 0.41, 0.456,0.502, 0.548,
		0.316,0.365,0.416,0.466,0.517,0.618, 
		0.161,0.213,0.263,0.314,0.364,0.413,0.463,0.513,0.613, 
		0.145,0.181,0.226,0.285,0.321,0.362,
		0.141,0.176,0.220,0.278,0.313,0.353, 
		0.155, 0.202, 0.252, 0.299, 0.328, 0.375, 0.422, 0.469, 0.563, 
		0.152, 0.198, 0.247, 0.293, 0.322, 0.368, 0.414, 0.46, 0.552]
		diametroInternoDic= dict()


		for i in range(0,len(listaValoresDiametroInterno)):

			diametroInternoDic[tuplasEntradas[i]]= listaValoresDiametroInterno[i]



		diametroInternoTuberiaLavado = diametroInternoDic[(listaEU[0],listaEU[1])]
		listaEntradaTemp1.append(diametroInternoTuberiaLavado)

		if tasa == "Tasa media":
			caudalLavado = (120.0/86400.0)*ValuepredimensionamientoFiltros(caudalLista)[8]
		elif tasa == "Tasa máxima":
			caudalLavado = (150.0/86400.0)*ValuepredimensionamientoFiltros(caudalLista)[8]

		listaEntradaTemp1.append(caudalLavado)

		velocidadFlujoTuberiaLavado = (4.0*caudalLavado)*(1.0/(pi*(diametroInternoTuberiaLavado**2)))
		listaEntradaTemp1.append(velocidadFlujoTuberiaLavado)
		
		cabezaVelocidad = (velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))
		listaEntradaTemp1.append(cabezaVelocidad)

		valorTemperaturas=list()
		tablaTemperaturaViscocidadCinematica=dict()


		for i in range(0,36):    
			valorTemperaturas.append(i)
					
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaViscocidadCinematica[valorTemperaturas[ind]]=valorViscocidad[ind]

		viscocidadCinematica= tablaTemperaturaViscocidadCinematica[temperatureValue]

		listaEntradaTemp1.append(viscocidadCinematica)

		numeroReynolds= velocidadFlujoTuberiaLavado*diametroInternoTuberiaLavado*(1/viscocidadCinematica)
		listaEntradaTemp1.append(numeroReynolds)

		factorFriccion=listaEU[3]

		for i in range(0,5):
			factorFriccion= (1/(-2*log10(((rugosidadAbsoluta/1000)*(1/(3.7*diametroInternoTuberiaLavado)))+(2.51*(1/(numeroReynolds*sqrt(factorFriccion)))))))**2
		
		listaEntradaTemp1.append(factorFriccion)

		perdidaCargaTuberiaLavadoDW= factorFriccion*(listaEU[2]/diametroInternoTuberiaLavado)*(velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))

		listaEntradaTemp1.append(perdidaCargaTuberiaLavadoDW)
		
		newDataTreeview(arbolPerdidaCargaTuberiaLavado_DW, listaEntradaTemp1)

			
		#DatosPara3
	
		
		tuplasEntradas2=list()

		accesoriosLista = ["Válvula de compuerta completamente abierta",
		"Codo 90° radio corto (r/d 1)",
		"Codo 90° radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Unión",
		"Entrada recta a tope",
		"Entrada con boca acampanada",
		"Salida del tubo"]

		diametroNominalLista = [
		150,160,200,250,300,315,350,355,400,450,500,600,700,800,900,1000,6,8,10,12,14,16,18,20,24,28,32,34,36,40
		]
		tuplasEntradas2=[]

		for elemento in accesoriosLista:
			tuplaL = tuple()
			for diam in diametroNominalLista:
				tuplaL = (elemento,diam)
				tuplasEntradas2.append(tuplaL)

		listaValoresCoeficientePerdidaMenor= [

		0.12,	0.12,	0.11,	0.11,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.120,	0.110,	0.110,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.180,	0.178,	0.168,	0.168,	0.156,	0.156,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.132,	0.132,	0.132,	0.132,	0.180,	0.168,	0.168,	0.156,	0.156,	0.156,	0.144,	0.144,	0.144,	0.13,	0.13,	0.13,	0.13,	0.13,

		0.30,	0.30,	0.28,	0.28,	0.26,	0.26,	0.26,	0.26,	0.26,	0.24,	0.24,	0.24,	0.22,	0.22,	0.22,	0.22,	0.300,	0.280,	0.280,	0.260,	0.260,	0.260,	0.240,	0.240,	0.240,	0.22,	0.22,	0.22,	0.22,	0.22,

		0.90,	0.90,	0.84,	0.84,	0.78,	0.78,	0.78,	0.78,	0.78,	0.72,	0.72,	0.72,	0.66,	0.66,	0.66,	0.66,	0.900,	0.840,	0.840,	0.780,	0.780,	0.780,	0.720,	0.720,	0.720,	0.66,	0.66,	0.66,	0.66,	0.66,

		0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.30,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.300,	0.30,	0.30,	0.30,	0.30,	0.30,

		0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.50,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.500,	0.50,	0.50,	0.50,	0.50,	0.50,

		0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.10,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.100,	0.10,	0.10,	0.10,	0.10,	0.10,

		1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.00,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.000,	1.00,	1.00,	1.00,	1.00,	1.00]


		CoeficientePerdidaMenorDic= dict()
		for i in range(0,len(listaValoresCoeficientePerdidaMenor)):
			CoeficientePerdidaMenorDic[tuplasEntradas2[i]]= listaValoresCoeficientePerdidaMenor[i]


		accesoriosListaEntrada= ["Válvula de compuerta completamente abierta",
		"Tee en sentido recto",
		f"{listaEU[5]}",
		"Salida del tubo"]

		
		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	
		sumaCoeficientesPerdidaMenor= 0
		
		for element in accesoriosListaEntrada:
			sumaCoeficientesPerdidaMenor=sumaCoeficientesPerdidaMenor+ CoeficientePerdidaMenorDic[(element,listaEU[1])]

		peridaCargaTuberiaLavadoAccesorios= sumaCoeficientesPerdidaMenor*cabezaVelocidad
		for elemento in accesoriosListaEntrada:
			listaEntradaTemp3=list()
			listaEntradaTemp3.append(elemento)
			listaEntradaTemp3.append(listaEU[1])
			listaEntradaTemp3.append(1)
			listaEntradaTemp3.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			listaEntradaTemp3.append(sumaCoeficientesPerdidaMenor)
			listaEntradaTemp3.append(peridaCargaTuberiaLavadoAccesorios)
			newDataTreeview(arbolperdidaCargaTuberiaLavado_AC, listaEntradaTemp3)

		perdidaCargaTuberiaLavado_DW_HW2Window.mainloop()
				

	def perdidaCargaTuberiaLavado_DW_HW(TemperatureValue,listaE, d60,caudalLista):
		
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		

		perdidaCargaTuberiaLavado_DW_HWWindow = tk.Toplevel()
		perdidaCargaTuberiaLavado_DW_HWWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HWWindow.geometry("800x600") 
		perdidaCargaTuberiaLavado_DW_HWWindow.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HWWindow.configure(background="#9DC4AA")

		frameperdidaCargaTuberiaLavado_DW_HW= LabelFrame(perdidaCargaTuberiaLavado_DW_HWWindow, text="Estimación de la pérdida de carga en la tubería de lavado",font=("Yu Gothic bold", 11))
		frameperdidaCargaTuberiaLavado_DW_HW.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tubería de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
				elif elemento==codoRadio:
					codoRadio.set("Codo 90° radio")
				elif elemento==tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)




		inicialLabel=Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Datos adicionales para cálculos: ",font=("Yu Gothic bold",15))


		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]

		
		

		Valores=[(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		opcionesDic = dict()

		for i in range(0, len(listaValoresTemp)):
			opcionesDic[listaValoresTemp[i]]=Valores[i] 


		#Pendiente: ValoresDeAccesoriofinalconPolietileno21YDiametro200

		def on_combobox_select(event):
			diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])

		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tubería de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el material de la tubería de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="30", state="readonly")
		diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el diametro nominal de la tubería de lavado:",font=("Yu Gothic bold",10))
		


		#NombrePendiente
		codoRadio = StringVar()
		codoRadio.set("Codo 90° radio")
		listaValoresTemp3=['Codo 90° radio corto (r/d 1)', 'Codo 90° radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, codoRadio, *listaValoresTemp3)
		

		
		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, tipoEntrada, *listaValoresTemp3)
		

	
		
		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Longitud de la tubería de lavado [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el factor de fricción [0.0001 - 0.1]:", font =("Yu Gothic",9))


		divisorAccesoriosLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione los tipos de accesorios", font=("Yu Gothic bold",10))


		longitudTuberiaLavado = Entry(frameperdidaCargaTuberiaLavado_DW_HW)
		factorFriccion = Entry(frameperdidaCargaTuberiaLavado_DW_HW)




		listaEntradas=[materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada]

		listaLabel=[inicialLabel, materialTuberiaLabel , materialTuberiaLavado, diametroNominalTuberiaLavadoLabel, diametroNominalTuberiaLavado,longitudTuberiaLavadoLabel, factorFriccionLabel,divisorAccesoriosLabel, codoRadioName,tipoEntradaName,]

		alturaInicialLabel=20
		m=0
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=40
			m=m+1
			if m==3:
				alturaInicialEntradas=alturaInicialLabel
		
		i=0
		for elemento in listaEntradas:
				if i == 0 or i==1 or i==4 or i==5:
					i=i+1
					alturaInicialEntradas+=40
				else: 
					i=i+1
					elemento.place(x=400,y=alturaInicialEntradas)
					alturaInicialEntradas+=40

		#Botones.
		botonCalcular = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Calcular la estimación de carga en la tubería de lavado.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTuberiaLavado_DW_HW2(listaEntradas,TemperatureValue,listaE, d60,caudalLista))
		botonNewEntry = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		diametroNominalTuberiaLavado.set("10")
		longitudTuberiaLavado.insert(0,"20")
		factorFriccion.insert(0,"0.0200")
		codoRadio.set('Codo 90° radio mediano (r/d 3)')
		tipoEntrada.set('Entrada con boca acampanada')
		




		perdidaCargaTuberiaLavado_DW_HWWindow.mainloop()
	
	def perdidaCargaTuberiaLavado_DW_HW_2(TemperatureValue,listaE, d60,caudalLista, tasaE):

		if tasaE.get() == "Tasa":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la tasa.")
			return None
		else:
			tasa = tasaE.get()
			
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		


		perdidaCargaTuberiaLavado_DW_HWWindow = tk.Toplevel()
		perdidaCargaTuberiaLavado_DW_HWWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HWWindow.geometry("800x600") 
		perdidaCargaTuberiaLavado_DW_HWWindow.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HWWindow.configure(background="#9DC4AA")

		frameperdidaCargaTuberiaLavado_DW_HW= LabelFrame(perdidaCargaTuberiaLavado_DW_HWWindow, text=f"Estimación de la pérdida de carga en la tubería de lavado a {tasa.lower()}",font=("Yu Gothic bold", 11))
		frameperdidaCargaTuberiaLavado_DW_HW.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tubería de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
				else:
					elemento.delete(0, END)




		inicialLabel=Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Datos adicionales para cálculos: ",font=("Yu Gothic bold",15))




		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]


		Valores=[(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		opcionesDic = dict()

		for i in range(0, len(listaValoresTemp)):
			opcionesDic[listaValoresTemp[i]]=Valores[i] 


		def on_combobox_select(event):
			diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])

		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tubería de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el material de la tubería de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="30", state="readonly")
		diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el diametro nominal de la tubería de lavado:",font=("Yu Gothic bold",10))


		#NombrePendiente
		codoRadio = StringVar()
		codoRadio.set("Codo 90° radio")
		listaValoresTemp3=['Codo 90° radio corto (r/d 1)', 'Codo 90° radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, codoRadio, *listaValoresTemp3)
		

		
		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, tipoEntrada, *listaValoresTemp3)
		

	
		
		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Longitud de la tubería del efluente [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el factor de fricción [0.0001 - 0.1]:", font =("Yu Gothic",9))


		divisorAccesoriosLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el tipo de accesorio", font=("Yu Gothic bold",10))


		longitudTuberiaLavado = Entry(frameperdidaCargaTuberiaLavado_DW_HW)
		factorFriccion = Entry(frameperdidaCargaTuberiaLavado_DW_HW)




		listaEntradas=[materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada]

		listaLabel=[inicialLabel, materialTuberiaLabel , materialTuberiaLavado, diametroNominalTuberiaLavadoLabel, diametroNominalTuberiaLavado,longitudTuberiaLavadoLabel, factorFriccionLabel,divisorAccesoriosLabel,tipoEntradaName,]

		alturaInicialLabel=20
		m=0
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=40
			m=m+1
			if m==3:
				alturaInicialEntradas=alturaInicialLabel
		
		i=0
		for elemento in listaEntradas:
				if i == 0 or i==1 or i==4 or i==5:
					i=i+1
					alturaInicialEntradas+=40
				else: 
					i=i+1
					elemento.place(x=400,y=alturaInicialEntradas)
					alturaInicialEntradas+=40

		#Botones.#
		
		botonCalcular = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Calcular la estimación de carga en la tubería de lavado.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTuberiaLavado_DW_HW2_2(listaEntradas,TemperatureValue,listaE, d60,caudalLista,tasa))
		botonNewEntry = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		diametroNominalTuberiaLavado.set("10")
		longitudTuberiaLavado.insert(0,"1.5")
		factorFriccion.insert(0,"0.0200")
	
		tipoEntrada.set('Entrada con boca acampanada')
		
		#NOBorrar
		codoRadio.set('Codo 90° radio mediano (r/d 3)')



		perdidaCargaTuberiaLavado_DW_HWWindow.mainloop()


	def perdidaCargaTotalLavado2(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1):
		
		i=0
		listaEU = list()
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tubería de lavado")
						return None
					elif elemento.get() == "Diámetro nominal de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro nominal de la tubería de lavado")
						return None

					elif elemento.get() == "Codo 90° radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90° radio")
						return None
					
					
					elif elemento.get() == "Tipo de entrada":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de entrada del accesorio")
						return None

					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>50.0 or float(elemento.get())<5.0):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tubería de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricción debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None


	
		perdidaCargaTotalLavadoWindow = tk.Toplevel()
		perdidaCargaTotalLavadoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTotalLavadoWindow.geometry("600x600") 
		perdidaCargaTotalLavadoWindow.resizable(0,0)	
		perdidaCargaTotalLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaTotalLavadoFrame=LabelFrame(perdidaCargaTotalLavadoWindow, text="Pérdida de carga total durante el lavado", font=("Yu Gothic bold", 11))
		perdidaCargaTotalLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaTotalLavado_frame = Frame(perdidaCargaTotalLavadoFrame)
		arbolperdidaCargaTotalLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTotalLavado= ttk.Treeview(arbolperdidaCargaTotalLavado_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTotalLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaTotalLavado.xview)
		sedScrollY.configure(command=arbolperdidaCargaTotalLavado.yview)
		#Define columnas.
		arbolperdidaCargaTotalLavado["columns"]= (
		"Razón","hi","Pérdida de carga [m]"
		
		)

		#Headings
		arbolperdidaCargaTotalLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTotalLavado["columns"]:
			arbolperdidaCargaTotalLavado.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidaCargaTotalLavado["columns"])+1) :
				arbolperdidaCargaTotalLavado.column(f"#{i}",width=700, stretch=False)	
		arbolperdidaCargaTotalLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTotalLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaTotalLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaTotalLavado=list()

		listaValuePerdidaCargaTuberiaLavado = ValuePerdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista)
		
		perdidaCargaLechoExpandido = valuePerdidaCargaLechoExpandido()[3]
		perdidaCargaLechoGrava = valuePerdidacargaLechoGravaLavado(temperatureValue,d60)[2]
		perdidaCargaSistemaDrenaje = valuePerdidaCargaSistemaDrenajeLavado(temperatureValue,d60, caudal,listaEntradaDrenaje)[3]
		perdidaCargaDW= listaValuePerdidaCargaTuberiaLavado[0][7]
		perdidaCargaHZ= listaValuePerdidaCargaTuberiaLavado[1][6]
		perdidaCargaAccesorios= listaValuePerdidaCargaTuberiaLavado[2]
		
	

		perdidaTotalListaSinHZ= [perdidaCargaLechoExpandido, perdidaCargaLechoGrava, 
		perdidaCargaSistemaDrenaje, perdidaCargaDW, perdidaCargaAccesorios] 
		
		perdidaTotalListaSinDW= [perdidaCargaLechoExpandido, perdidaCargaLechoGrava, 
		perdidaCargaSistemaDrenaje, perdidaCargaHZ, perdidaCargaAccesorios]

		perdidaCargaTotalSinHZ=0.0
		for elemento in perdidaTotalListaSinHZ:
			perdidaCargaTotalSinHZ=perdidaCargaTotalSinHZ+elemento 

		perdidaCargaTotalSinDW=0.0
		for elemento in perdidaTotalListaSinDW:
			perdidaCargaTotalSinDW=perdidaCargaTotalSinDW+elemento 




		perdidaTotalFinal= [perdidaCargaLechoExpandido, perdidaCargaLechoGrava, 
		perdidaCargaSistemaDrenaje, perdidaCargaDW, perdidaCargaHZ, perdidaCargaAccesorios,perdidaCargaTotalSinHZ,
		perdidaCargaTotalSinDW] 


		listaDebidoA= [ 'Pérdida de carga a través del lecho expandido',					
		'Pérdida de carga a través del lecho de grava',					
		'Pérdidad de carga a través del sistema de drenaje',					
		'Pérdida de carga en la tubería de lavado (Darcy - Weisbach)',	
		'Pérdida de carga en la tubería de lavado (Hazen - Williams)',				
		'Pérdida de carga  por accesorios en la tubería de lavado',					
		'Pérdidad de carga total durante el lavado con Darcy - Weisbach',
		'Pérdidad de carga total durante el lavado con Hazen - Williams']
		j=1
		for i in range(0,len(perdidaTotalFinal)):
			listaperdidaCargaTotalLavado=list()
			listaperdidaCargaTotalLavado.append(listaDebidoA[i])
			listaperdidaCargaTotalLavado.append(f"h{j}")
			listaperdidaCargaTotalLavado.append(perdidaTotalFinal[i])
			newDataTreeview(arbolperdidaCargaTotalLavado,listaperdidaCargaTotalLavado)
			if i==3 and j==4:
				pass
			elif j==5 or j=="b":
				j="b"
			else:
				j=j+1
			

		perdidaCargaTotalLavadoWindow.mainloop()

	def perdidaCargaTotalLavado2_2(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1,tasa):
		
		perdidaCargaTotalLavadoWindow = tk.Toplevel()
		perdidaCargaTotalLavadoWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTotalLavadoWindow.geometry("600x600") 
		perdidaCargaTotalLavadoWindow.resizable(0,0)	
		perdidaCargaTotalLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaTotalLavadoFrame=LabelFrame(perdidaCargaTotalLavadoWindow, text="Pérdida de carga total durante el lavado", font=("Yu Gothic bold", 11))
		perdidaCargaTotalLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaTotalLavado_frame = Frame(perdidaCargaTotalLavadoFrame)
		arbolperdidaCargaTotalLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTotalLavado= ttk.Treeview(arbolperdidaCargaTotalLavado_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTotalLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaTotalLavado.xview)
		sedScrollY.configure(command=arbolperdidaCargaTotalLavado.yview)
		#Define columnas.
		arbolperdidaCargaTotalLavado["columns"]= (
		"Razón","hi","Pérdida de carga [m]"
		
		)

		#Headings
		arbolperdidaCargaTotalLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTotalLavado["columns"]:
			arbolperdidaCargaTotalLavado.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolperdidaCargaTotalLavado["columns"])+1) :
				arbolperdidaCargaTotalLavado.column(f"#{i}",width=700, stretch=False)	
		arbolperdidaCargaTotalLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTotalLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaTotalLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaTotalLavado=list()

		
		#Pendiente Rose

		listaValuePerdidaCargaTuberiaLavado = valuePerdidaCargaTuberiaLavado_DW_HW2_2(listaE,temperatureValue,listaE1, d60,caudalLista,tasa)

		perdidaCargaLechoGrava = valuePerdidacargaLechoGravaLavado_2(temperatureValue,d60,tasa)[2]
		perdidaCargaSistemaDrenaje = valuePerdidaCargaSistemaDrenajeLavado_2(temperatureValue,d60, caudal,listaEntradaDrenaje,tasa)[3]
		perdidaCargaDW= listaValuePerdidaCargaTuberiaLavado[8]
		perdidaCargaAccesorios= listaValuePerdidaCargaTuberiaLavado[9]
		
	

		perdidaTotalLista= [perdidaCargaLechoGrava, 
		perdidaCargaSistemaDrenaje, perdidaCargaDW, perdidaCargaAccesorios] 
		

		perdidaCargaTotal =0.0
		for elemento in perdidaTotalLista:
			perdidaCargaTotal= perdidaCargaTotal +elemento 

		perdidaTotalLista.append(perdidaCargaTotal)

		listaDebidoA= [					
		'Pérdida de energía a través del lecho de grava',					
		'Pérdidad de energía a través del sistema de drenaje',					
		'Pérdida de energía en la tubería del efluente',		
		'Pérdida de energía  por accesorios en la tubería del efluente',					
		f'Pérdidad de energía total a {tasa.lower()} de filtración']
	

		
		listaSub=["h{}".format(getSub("g")), "h{}".format(getSub("d")),"h{}".format(getSub("tef")),"h{}".format(getSub("acc")),"h{}".format(getSub("f"))]
		
		for i in range(0,len(perdidaTotalLista)):
			listaperdidaCargaTotalLavado=list()
			listaperdidaCargaTotalLavado.append(listaDebidoA[i])
			listaperdidaCargaTotalLavado.append(listaSub[i])
			listaperdidaCargaTotalLavado.append(perdidaTotalLista[i])

			newDataTreeview(arbolperdidaCargaTotalLavado,listaperdidaCargaTotalLavado)
		
		perdidaCargaTotalLavadoWindow.mainloop()


	def perdidaCargaTotalLavadoMain(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista):
		
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		
		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None
		
		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None

		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
	
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None

		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
	
	
	
		perdidaCargaTotalLavadoMainWindow = tk.Toplevel()
		perdidaCargaTotalLavadoMainWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTotalLavadoMainWindow.geometry("800x600") 
		perdidaCargaTotalLavadoMainWindow.resizable(0,0)	
		perdidaCargaTotalLavadoMainWindow.configure(background="#9DC4AA")

		frameperdidaCargaTotalLavadoMain= LabelFrame(perdidaCargaTotalLavadoMainWindow, text="Datos adicionales para el cálculo de la pérdida total durante el lavado.",font=("Yu Gothic bold", 11))
		frameperdidaCargaTotalLavadoMain.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tubería de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
				elif elemento==codoRadio:
					codoRadio.set("Codo 90° radio")
				elif elemento==tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)




		inicialLabel=Label(frameperdidaCargaTotalLavadoMain, text="Datos adicionales para cálculos: ",font=("Yu Gothic bold",15))


		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]


		Valores=[(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		opcionesDic = dict()

		for i in range(0, len(listaValoresTemp)):
			opcionesDic[listaValoresTemp[i]]=Valores[i] 


		def on_combobox_select(event):
			diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])

		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tubería de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el material de la tubería de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="30", state="readonly")
		diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el diametro nominal de la tubería de lavado:",font=("Yu Gothic bold",10))


		

		#NombrePendiente
		codoRadio = StringVar()
		codoRadio.set("Codo 90° radio")
		listaValoresTemp3=['Codo 90° radio corto (r/d 1)', 'Codo 90° radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTotalLavadoMain, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTotalLavadoMain, tipoEntrada, *listaValoresTemp3)


	

		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTotalLavadoMain, text="Longitud de la tubería de lavado [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el factor de fricción [0.0001 - 0.1]:", font =("Yu Gothic",9))


		divisorAccesoriosLabel = Label(frameperdidaCargaTotalLavadoMain, text="Seleccione los tipos de accesorios", font=("Yu Gothic bold",10))


		longitudTuberiaLavado = Entry(frameperdidaCargaTotalLavadoMain)
		factorFriccion = Entry(frameperdidaCargaTotalLavadoMain)




		listaEntradas=[materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada]

		listaLabel=[inicialLabel, materialTuberiaLabel , materialTuberiaLavado, diametroNominalTuberiaLavadoLabel, diametroNominalTuberiaLavado,longitudTuberiaLavadoLabel, factorFriccionLabel,divisorAccesoriosLabel, codoRadioName,tipoEntradaName,]

		alturaInicialLabel=20
		m=0
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=40
			m=m+1
			if m==3:
				alturaInicialEntradas=alturaInicialLabel

		i=0
		for elemento in listaEntradas:
				if i == 0 or i==1 or i==4 or i==5:
					i=i+1
					alturaInicialEntradas+=40
				else: 
					i=i+1
					elemento.place(x=400,y=alturaInicialEntradas)
					alturaInicialEntradas+=40

		#Botones.
		botonCalcular = HoverButton(frameperdidaCargaTotalLavadoMain, text="Calcular la pérdida de carga total durante el lavado", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTotalLavado2(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE))
		botonNewEntry = HoverButton(frameperdidaCargaTotalLavadoMain, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		diametroNominalTuberiaLavado.set("10")
		longitudTuberiaLavado.insert(0,"20")
		factorFriccion.insert(0,"0.0200")
		codoRadio.set('Codo 90° radio mediano (r/d 3)')
		tipoEntrada.set('Entrada con boca acampanada')





		perdidaCargaTotalLavadoMainWindow.mainloop()
	
	def perdidaCargaTotalLavadoMain_2(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,tasaE):
		
		if tasaE.get() == "Tasa":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la tasa.")
			return None
		else:
			tasa = tasaE.get()


		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		else:
			tiempoRetrolavado = float(listaE[0].get())

		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())


		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())


		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()
	
		perdidaCargaTotalLavadoMainWindow = tk.Toplevel()
		perdidaCargaTotalLavadoMainWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaCargaTotalLavadoMainWindow.geometry("800x600") 
		perdidaCargaTotalLavadoMainWindow.resizable(0,0)	
		perdidaCargaTotalLavadoMainWindow.configure(background="#9DC4AA")

		frameperdidaCargaTotalLavadoMain= LabelFrame(perdidaCargaTotalLavadoMainWindow, text= f"Datos adicionales para el cálculo de la pérdida total a {tasa.lower()} de filtración con lecho limpio",font=("Yu Gothic bold", 11))
		frameperdidaCargaTotalLavadoMain.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tubería de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
				elif elemento==tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)




		inicialLabel=Label(frameperdidaCargaTotalLavadoMain, text="Datos adicionales para cálculos: ",font=("Yu Gothic bold",15))




		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]


		Valores=[(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		opcionesDic = dict()

		for i in range(0, len(listaValoresTemp)):
			opcionesDic[listaValoresTemp[i]]=Valores[i] 


		def on_combobox_select(event):
			diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])

		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tubería de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el material de la tubería de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="30", state="readonly")
		diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el diametro nominal de la tubería de lavado:",font=("Yu Gothic bold",10))

		#NombrePendiente
		codoRadio = StringVar()
		codoRadio.set("Codo 90° radio")
		listaValoresTemp3=['Codo 90° radio corto (r/d 1)', 'Codo 90° radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTotalLavadoMain, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTotalLavadoMain, tipoEntrada, *listaValoresTemp3)


	

		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTotalLavadoMain, text="Longitud de la tubería del efluente [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el factor de fricción [0.0001 - 0.1]:", font =("Yu Gothic",9))


		divisorAccesoriosLabel = Label(frameperdidaCargaTotalLavadoMain, text="Seleccione los tipos de accesorios", font=("Yu Gothic bold",10))


		longitudTuberiaLavado = Entry(frameperdidaCargaTotalLavadoMain)
		factorFriccion = Entry(frameperdidaCargaTotalLavadoMain)




		listaEntradas=[materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada]

		listaLabel=[inicialLabel, materialTuberiaLabel , materialTuberiaLavado, diametroNominalTuberiaLavadoLabel, diametroNominalTuberiaLavado,longitudTuberiaLavadoLabel, factorFriccionLabel,divisorAccesoriosLabel,tipoEntradaName,]

		alturaInicialLabel=20
		m=0
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=40
			m=m+1
			if m==3:
				alturaInicialEntradas=alturaInicialLabel

		i=0
		for elemento in listaEntradas:
				if i == 0 or i==1 or i==4 or i==5:
					i=i+1
					alturaInicialEntradas+=40
				else: 
					i=i+1
					elemento.place(x=400,y=alturaInicialEntradas)
					alturaInicialEntradas+=40

		#Botones.
		botonCalcular = HoverButton(frameperdidaCargaTotalLavadoMain, text="Calcular la pérdida de carga total durante el lavado", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTotalLavado2_2(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE,tasa))
		botonNewEntry = HoverButton(frameperdidaCargaTotalLavadoMain, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		diametroNominalTuberiaLavado.set("10")
		longitudTuberiaLavado.insert(0,"1.50")
		factorFriccion.insert(0,"0.0200")	
		tipoEntrada.set('Entrada con boca acampanada')

		#NOBorrar
		codoRadio.set('Codo 90° radio mediano (r/d 3)')




		perdidaCargaTotalLavadoMainWindow.mainloop()


	def verificacionVelocidadesDiseñoTuberiaMain(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista):
		
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None

		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None
	

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		

		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
	

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
	

		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
	

	
		

		verificacionVelocidadesDiseñoTuberiaMainWindow = tk.Toplevel()
		verificacionVelocidadesDiseñoTuberiaMainWindow.iconbitmap(bitmap='icons\\agua.ico')
		verificacionVelocidadesDiseñoTuberiaMainWindow.geometry("800x600") 
		verificacionVelocidadesDiseñoTuberiaMainWindow.resizable(0,0)	
		verificacionVelocidadesDiseñoTuberiaMainWindow.configure(background="#9DC4AA")

																												

		frameverificacionVelocidadesDiseñoTuberiaMain= LabelFrame(verificacionVelocidadesDiseñoTuberiaMainWindow, text="Datos adicionales para el cálculo de las velocidades de diseño en las tuberías del filtro durante el lavado ",font=("Yu Gothic bold", 11))
		frameverificacionVelocidadesDiseñoTuberiaMain.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tubería de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
				elif elemento == codoRadio:
					codoRadio.set("Codo 90° radio")
				elif elemento == tipoEntrada:
					tipoEntrada.set("Tipo de entrada")



				else:
					elemento.delete(0, END)




		inicialLabel=Label(frameverificacionVelocidadesDiseñoTuberiaMain, text="Datos adicionales para cálculos: ",font=("Yu Gothic bold",15))



		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]


		Valores=[(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		opcionesDic = dict()

		for i in range(0, len(listaValoresTemp)):
			opcionesDic[listaValoresTemp[i]]=Valores[i] 


		def on_combobox_select(event):
			diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])

		materialTuberiaLavado = ttk.Combobox(frameverificacionVelocidadesDiseñoTuberiaMain, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tubería de lavado")

		materialTuberiaLabel= Label(frameverificacionVelocidadesDiseñoTuberiaMain, text="Seleccione el material de la tubería de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameverificacionVelocidadesDiseñoTuberiaMain, width="30", state="readonly")
		diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameverificacionVelocidadesDiseñoTuberiaMain, text="Seleccione el diametro nominal de la tubería de lavado:",font=("Yu Gothic bold",10))

		#NombrePendiente
		codoRadio = StringVar()
		codoRadio.set("Codo 90° radio")
		listaValoresTemp3=['Codo 90° radio corto (r/d 1)', 'Codo 90° radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameverificacionVelocidadesDiseñoTuberiaMain, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameverificacionVelocidadesDiseñoTuberiaMain, tipoEntrada, *listaValoresTemp3)




		longitudTuberiaLavadoLabel = Label(frameverificacionVelocidadesDiseñoTuberiaMain, text="Longitud de la tubería de lavado [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameverificacionVelocidadesDiseñoTuberiaMain, text="Seleccione el factor de fricción [0.0001 - 0.1]:", font =("Yu Gothic",9))

		longitudTuberiaLavado = Entry(frameverificacionVelocidadesDiseñoTuberiaMain)
		factorFriccion = Entry(frameverificacionVelocidadesDiseñoTuberiaMain)




		listaEntradas=[materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada]

		listaLabel=[inicialLabel, materialTuberiaLabel , materialTuberiaLavado, diametroNominalTuberiaLavadoLabel, diametroNominalTuberiaLavado,longitudTuberiaLavadoLabel, factorFriccionLabel]

		alturaInicialLabel=20
		m=0
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=40
			m=m+1
			if m==3:
				alturaInicialEntradas=alturaInicialLabel

		i=0
		for elemento in listaEntradas:
				if i == 0 or i==1 or i==4 or i==5:
					i=i+1
					alturaInicialEntradas+=40
				else: 
					i=i+1
					elemento.place(x=400,y=alturaInicialEntradas)
					alturaInicialEntradas+=40
		
		#Botones.
		botonCalcular = HoverButton(frameverificacionVelocidadesDiseñoTuberiaMain, text="Calcular las velocidades de diseño en las tuberías del filtro", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: verificacionVelocidadesDiseñoTuberias(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE))
		botonNewEntry = HoverButton(frameverificacionVelocidadesDiseñoTuberiaMain, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		diametroNominalTuberiaLavado.set("10")
		longitudTuberiaLavado.insert(0,"20")
		factorFriccion.insert(0,"0.0200")

		#NOBORRAR.
		codoRadio.set('Codo 90° radio mediano (r/d 3)')
		tipoEntrada.set('Entrada con boca acampanada')





		verificacionVelocidadesDiseñoTuberiaMainWindow.mainloop()







	def verificacionVelocidadesDiseñoTuberias(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1):
		
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tubería de lavado")
						return None
					elif elemento.get() == "Diámetro nominal de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro nominal de la tubería de lavado")
						return None
					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>50.0 or float(elemento.get())<5.0):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tubería de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricción debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None



		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()
		

		verificacionVelocidadesDiseñoTuberiasWindow = tk.Toplevel()
		verificacionVelocidadesDiseñoTuberiasWindow.iconbitmap(bitmap='icons\\agua.ico')
		verificacionVelocidadesDiseñoTuberiasWindow.geometry("1200x400") 
		verificacionVelocidadesDiseñoTuberiasWindow.resizable(0,0)	
		verificacionVelocidadesDiseñoTuberiasWindow.configure(background="#9DC4AA")

		verificacionVelocidadesDiseñoTuberiasFrame=LabelFrame(verificacionVelocidadesDiseñoTuberiasWindow, text="Pérdida de carga total durante el lavado", font=("Yu Gothic bold", 11))
		verificacionVelocidadesDiseñoTuberiasFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolverificacionVelocidadesDiseñoTuberias_frame = Frame(verificacionVelocidadesDiseñoTuberiasFrame)
		arbolverificacionVelocidadesDiseñoTuberias_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolverificacionVelocidadesDiseñoTuberias_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolverificacionVelocidadesDiseñoTuberias_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolverificacionVelocidadesDiseñoTuberias= ttk.Treeview(arbolverificacionVelocidadesDiseñoTuberias_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolverificacionVelocidadesDiseñoTuberias.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolverificacionVelocidadesDiseñoTuberias.xview)
		sedScrollY.configure(command=arbolverificacionVelocidadesDiseñoTuberias.yview)
		#Define columnas.
		arbolverificacionVelocidadesDiseñoTuberias["columns"]= (
			"Velocidad de diseño",
			"Rango de diseño (m/s)",
			"Calculada (m/s)",
		
		)

		#Headings
		arbolverificacionVelocidadesDiseñoTuberias.heading("#0",text="ID", anchor=CENTER)

		for col in arbolverificacionVelocidadesDiseñoTuberias["columns"]:
			arbolverificacionVelocidadesDiseñoTuberias.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolverificacionVelocidadesDiseñoTuberias["columns"])+1) :
				arbolverificacionVelocidadesDiseñoTuberias.column(f"#{i}",width=700, stretch=False)	
		arbolverificacionVelocidadesDiseñoTuberias.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolverificacionVelocidadesDiseñoTuberias.tag_configure("evenrow", background= "#1FCCDB")
		arbolverificacionVelocidadesDiseñoTuberias.tag_configure("oddrow", background= "#9DC4AA")    
		#Tablas
		
		listaSeccionTuberia=['6 X 6', '8 X 8', '10 X 10', '12 X 12', '14 X 14', '16 X 16', '18 X 18','20 X 20']

		listaAreaSeccion=list()

		ind=0

		for elemento in listaSeccionTuberia:
			if elemento == '10 X 10':
				ind=ind+1
			if ind==0:
				listaAreaSeccion.append((float(elemento[0])*0.0254)**2)
			else:
				listaAreaSeccion.append((float(elemento[0:2])*0.0254)**2)

		AreaSeccionDic=dict()

		for j in range(0,len(listaSeccionTuberia)):
			AreaSeccionDic[listaSeccionTuberia[j]]=listaAreaSeccion[j]
			
		listaDiametroLaterales= ("1 1/2", "2", "2 1/2", "3")
		listaAreasLaterales=[0.0011401,0.0020268,0.0031669,0.0045604]
		areaLateralesDic=dict()

		for i in range(0, len(listaDiametroLaterales)):
			areaLateralesDic[listaDiametroLaterales[i]]=listaAreasLaterales[i]







		listaverificacionVelocidadesDiseñoTuberias=list()

		listaVelocidadDiseño=["Velocidad en la tubería de lavado","Velocidad en tubería de drenaje en lavado (múltiple)",
		"Velocidad en tubería de drenaje en lavado (laterales)"]
		listaRangoDiseño=["1.5 - 3.0","0.9 - 2.4", "0.9 - 2.4"]
		
		velocidadTuberiaLavado= ValuePerdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista)[0][2]
		velocidadTuberiaDrenajeMultiple= ValueConsumoAguaLavado(listaE1, temperatureValue, d60, caudalLista)[5] *(1.0/AreaSeccionDic[seccionTransvMultiple])
		velocidadTuberiaDrenajeLaterales = ValueConsumoAguaLavado(listaE1, temperatureValue, d60, caudalLista)[5]/(( ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[2])*areaLateralesDic[diametroLaterales])

		listaCalculada=[velocidadTuberiaLavado, velocidadTuberiaDrenajeMultiple, velocidadTuberiaDrenajeLaterales]
		
	

		for i in range(0, len(listaVelocidadDiseño)):
			listaverificacionVelocidadesDiseñoTuberias=list()
			listaverificacionVelocidadesDiseñoTuberias.append(listaVelocidadDiseño[i])
			listaverificacionVelocidadesDiseñoTuberias.append(listaRangoDiseño[i])
			listaverificacionVelocidadesDiseñoTuberias.append(listaCalculada[i])
			newDataTreeview(arbolverificacionVelocidadesDiseñoTuberias,listaverificacionVelocidadesDiseñoTuberias)


		if velocidadTuberiaLavado<1.5:
			messagebox.showinfo(title="Información", message="La velocidad en la tubería de lavado es baja, seleccione otro diámetro.")
		elif velocidadTuberiaLavado>3.0:
			messagebox.showinfo(title="Información", message="La velocidad en la tubería de lavado es alta, seleccione otro diámetro.")

		if velocidadTuberiaDrenajeMultiple<0.9:
			messagebox.showinfo(title="Información", message="La velocidad en el múltiple es baja, seleccion otra sección")
		elif velocidadTuberiaDrenajeMultiple>2.4:
			messagebox.showinfo(title="Información", message="La velocidad en el múltiple es alta, seleccion otra sección")

		if velocidadTuberiaDrenajeLaterales<0.9:
			messagebox.showinfo(title="Información", message="La velocidad en el lateral es baja, seleccione otro diámetro o distanciamiento")
		elif velocidadTuberiaDrenajeLaterales>2.4:
			messagebox.showinfo(title="Información", message="La velocidad en el lateral es alta, seleccione otro diámetro o distanciamiento")

		verificacionVelocidadesDiseñoTuberiasWindow.mainloop()

	

	
	
	
	def hidraulicaSistemaLavado(listaTamiz, listaAR, optnValue, listaCaudal):
		#Hidraulica

		try: 
			caudalMedio=float(listaCaudal[0].get())
			
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un número.")
			return None

		listaNTamizTemp=listaTamiz.copy()
		listaARetenidaTemp=listaAR.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de los números de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de la arena retenida.")
			return None
		if optnValue.get() == "Seleccione la temperatura":
			messagebox.showwarning(title="Error", message="Hace falta elegir el valor de la temperatura del agua a tratar.")
			return None
		else:
			valorTemperatura= int(optnValue.get())


		for ind in range(0, len(listaNTamizTemp)):
			if listaNTamizTemp[ind].get() == "" and ind%2==0:
				break
			elif listaNTamizTemp[ind].get() == "" and ind%2 != 0:
				messagebox.showwarning(title="Error", message="Hace falta el rango de la derecha de alguna entrada.")
				return None
			else:
				try:
					CountControl=0
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m: 
							CountControl=CountControl+1
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m and CountControl==18:
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores estándar para número de tamiz. Pulse el botón para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de número de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de número de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento
		
		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None

		listaEntradaTemp=list()
		datosSalida=list()
		
		
			
	

		
	
		
		hidraulicaSistemaLavadoMainWindow = tk.Toplevel()
		hidraulicaSistemaLavadoMainWindow.iconbitmap(bitmap='icons\\agua.ico')
		hidraulicaSistemaLavadoMainWindow.geometry("800x600") 
		hidraulicaSistemaLavadoMainWindow.resizable(0,0)	
		hidraulicaSistemaLavadoMainWindow.configure(background="#9DC4AA")

		hidraulicaSistemaLavadoMainFrame=LabelFrame(hidraulicaSistemaLavadoMainWindow, text="Datos adicionales para la hidráulica del sistema de lavado", font=("Yu Gothic bold", 11))
		hidraulicaSistemaLavadoMainFrame.pack(side=TOP, fill=BOTH,expand=True)

		
		
		diametroOrificios = StringVar()
		diametroOrificios.set("Diametro de los orificios")
		listaValoresTempDiametroOrificios=list()
		listaValoresTempDiametroOrificios.append("1/4")
		listaValoresTempDiametroOrificios.append("3/8")
		listaValoresTempDiametroOrificios.append("1/2")
		listaValoresTempDiametroOrificios.append("5/8")
		diametroOrificiosName = OptionMenu(hidraulicaSistemaLavadoMainFrame, diametroOrificios, *listaValoresTempDiametroOrificios)
		diametroOrificiosLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione el diámetro de los orificios:", font=("Yu Gothic bold", 11))
		

		
		distanciaOrificios = StringVar()
		distanciaOrificios.set("Distancia entre los orificios")
		listaValoresTempDistanciaOrificios=list()
		listaValoresTempDistanciaOrificios.append("0.750")
		listaValoresTempDistanciaOrificios.append("0.100")
		listaValoresTempDistanciaOrificios.append("0.125")
		listaValoresTempDistanciaOrificios.append("0.150")
		distanciaOrificiosName = OptionMenu(hidraulicaSistemaLavadoMainFrame, distanciaOrificios, *listaValoresTempDistanciaOrificios)
		distanciaOrificiosLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione la distancia entre orificios:", font=("Yu Gothic bold", 11))


		seccionTransversal = StringVar()
		seccionTransversal.set("Sección transversal")
		listaValoresTempSeccionTransversal=list()
		listaValoresTempSeccionTransversal.append("6 X 6")
		listaValoresTempSeccionTransversal.append("8 X 8")
		listaValoresTempSeccionTransversal.append("10 X 10")
		listaValoresTempSeccionTransversal.append("12 X 12")
		listaValoresTempSeccionTransversal.append("14 X 14")
		listaValoresTempSeccionTransversal.append("16 X 16")
		listaValoresTempSeccionTransversal.append("18 X 18")
		listaValoresTempSeccionTransversal.append("20 X 20")
		seccionTransversalName = OptionMenu(hidraulicaSistemaLavadoMainFrame, seccionTransversal, *listaValoresTempSeccionTransversal)
		seccionTransversalLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione la sección transversal comercial del múltiple:", font=("Yu Gothic bold", 11))


		distanciaLaterales = StringVar()
		distanciaLaterales.set("Distancia entre laterales")
		listaValoresTempDistanciaLaterales=list()
		listaValoresTempDistanciaLaterales.append("0.20")
		listaValoresTempDistanciaLaterales.append("0.25")
		listaValoresTempDistanciaLaterales.append("0.30")
		distanciaLateralesName = OptionMenu(hidraulicaSistemaLavadoMainFrame, distanciaLaterales, *listaValoresTempDistanciaLaterales)
		distanciaLateralesLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione la distancia entre laterales:", font=("Yu Gothic bold", 11))
		

		
		diametroEntreLaterales = StringVar()
		diametroEntreLaterales.set("Diámetro de los laterales")
		listaValoresTempDiametroEntreLaterales=list()
		listaValoresTempDiametroEntreLaterales.append("1 1/2")
		listaValoresTempDiametroEntreLaterales.append("2")
		listaValoresTempDiametroEntreLaterales.append("2 1/2")
		listaValoresTempDiametroEntreLaterales.append("3")
		diametroEntreLateralesName = OptionMenu(hidraulicaSistemaLavadoMainFrame, diametroEntreLaterales, *listaValoresTempDiametroEntreLaterales)
		diametroEntreLateralesLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione el diámetro de los laterales:", font=("Yu Gothic bold", 11))

		tiempoRetrolavado = StringVar()
		tiempoRetrolavado.set("Tiempo de retrolavado")
		listaValoresTemptiempoRetrolavado=list()
		listaValoresTemptiempoRetrolavado.append("10")
		listaValoresTemptiempoRetrolavado.append("11")
		listaValoresTemptiempoRetrolavado.append("12")
		listaValoresTemptiempoRetrolavado.append("13")
		listaValoresTemptiempoRetrolavado.append("14")
		tiempoRetrolavadoName = OptionMenu(hidraulicaSistemaLavadoMainFrame, tiempoRetrolavado, *listaValoresTemptiempoRetrolavado)
		tiempoRetrolavadoLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione el tiempo de retrolavado.", font=("Yu Gothic bold", 11))

		
		listaEntradaDrenaje2=[diametroOrificiosName,distanciaOrificiosName,seccionTransversalName,distanciaLateralesName, diametroEntreLateralesName,tiempoRetrolavadoName]
		listaLabel= [diametroOrificiosLabel,distanciaOrificiosLabel, seccionTransversalLabel, distanciaLateralesLabel, diametroEntreLateralesLabel,tiempoRetrolavadoLabel]
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]
		listaEntradaExtra=[tiempoRetrolavado]
		
		#Borrar

		diametroOrificios.set("1/4")
		distanciaOrificios.set("0.100")
		seccionTransversal.set("14 X 14")
		distanciaLaterales.set("0.25")
		diametroEntreLaterales.set("1 1/2")
		tiempoRetrolavado.set("12")


		
	
		altIn= 30
		altIn2=30
		for ind in range(0,len(listaLabel)):
			if ind%2==0:
				listaLabel[ind].place(x=20,y=altIn)
				listaEntradaDrenaje2[ind].place(x=20, y= altIn+20)
				altIn=altIn+80
			else:
				listaLabel[ind].place(x=500,y=altIn2)
				listaEntradaDrenaje2[ind].place(x=500, y= altIn2+20)
				altIn2=altIn2+80
			
		#BotonesHidraulica
		#botonCalculoDrenaje = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Cálculos para el drenaje del filtro", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: calculoDrenaje())

		botonVelocidadLavadoExpansionLechoFiltrante = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Velocidad de lavado\n y expansión del lecho filtrante", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: velocidadLavadoExpansionLechoFiltrante(valorTemperatura,d60) )

		botonConsumoAguaLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Consumo de agua de\n lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: consumoAguaLavado(listaEntradaExtra,valorTemperatura,d60,listaCaudal))

		botonPerdidaCargaLechoExpandido = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Pérdida de carga a través\n del lecho expandido", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaLechoExpandido() )
 
		botonPerdidacargaLechoGravaLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Pérdida de carga a través\n del lecho de grava durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidacargaLechoGravaLavado(valorTemperatura,d60) )

		botonPerdidaCargaSistemaDrenajeLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Pérdida de carga a través\n del sistema de drenaje durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaSistemaDrenajeLavado(valorTemperatura,d60, caudalMedio, listaEntradaDrenaje) )

		botonPerdidaCargaTuberiaLavado_DW = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Pérdida de carga en la tubería\n de lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTuberiaLavado_DW_HW(valorTemperatura,listaEntradaExtra,d60,listaCaudal)) 

		botonPerdidaCargaTotalLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Pérdida de carga total durante\n el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTotalLavadoMain(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal) )

		botonVerificacionVelocidadesDiseñoTuberias = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Verificación de velocidad de diseño\n en tuberías de filtro durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: verificacionVelocidadesDiseñoTuberiaMain(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal) )

	

				
		def newEntryFiltroHidraulica(lista): 
			lista2= [
						"Diametro de los orificios",
						"Distancia entre los orificios",
						"Sección transversal",
						"Distancia entre laterales",
						"Diámetro de los laterales",
						"Tiempo de retrolavado"]

			for i in range(0, len(lista)):
					lista[i].set(lista2[i])

		botonLimpiarEntradasHidraulica = HoverButton(hidraulicaSistemaLavadoMainFrame, text="L\ni\nm\np\ni\na\nr\n\ne\nn\nt\nr\na\nd\na\ns", activebackground="#9DC4AA", anchor=CENTER , width=3, height=16, bg= "#09C5CE", font =("Courier",9), command= lambda: newEntryFiltroHidraulica(listaEntradaDrenaje+listaEntradaExtra))

			

		listaBotones=[botonVelocidadLavadoExpansionLechoFiltrante ,botonConsumoAguaLavado ,
		botonPerdidaCargaLechoExpandido ,botonPerdidacargaLechoGravaLavado ,botonPerdidaCargaSistemaDrenajeLavado 
		,botonPerdidaCargaTuberiaLavado_DW,botonPerdidaCargaTotalLavado ,botonVerificacionVelocidadesDiseñoTuberias]
		 
		counter= 0
		altIn2= altIn
		botonLimpiarEntradasHidraulica.place(x=400, y=altIn)

		for elemento in listaBotones:
			if counter < 4:
				elemento.place(x=20,y=altIn)
				altIn=altIn+60
				counter=counter+1
			else: 
				elemento.place(x=500,y=altIn2)
				altIn2=altIn2+60
		#botonCalculoDrenaje.place(x=0, y=altIn)
			
	
		
		listaCU = valorCoeficienteDeUniformidad(listaTamiz,listaAR)
		d10= listaCU[0]
		CU=listaCU[1]
		d60=d10*CU

		##return [d10,CU]
		
		hidraulicaSistemaLavadoMainWindow.mainloop()

	def canaletasDeLavado2(tempValue,d60, listaCaudal, listaExtra, ValorNuevo):
		
		if ValorNuevo.get() == "Ancho de la canaleta":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el ancho de la canaleta")
			return None
		else:
			anchoCanaleta = float(ValorNuevo.get())
	


		canaletasDeLavado2Window = tk.Toplevel()
		canaletasDeLavado2Window.iconbitmap(bitmap='icons\\agua.ico')
		canaletasDeLavado2Window.geometry("600x400") 
		canaletasDeLavado2Window.resizable(0,0)	
		canaletasDeLavado2Window.configure(background="#9DC4AA")

		canaletasDeLavado2Frame=LabelFrame(canaletasDeLavado2Window, text="Cálculos para las canaletas de lavado.", font=("Yu Gothic bold", 11))
		canaletasDeLavado2Frame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolcanaletasDeLavado2_frame = Frame(canaletasDeLavado2Frame)
		arbolcanaletasDeLavado2_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolcanaletasDeLavado2_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolcanaletasDeLavado2_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolcanaletasDeLavado2= ttk.Treeview(arbolcanaletasDeLavado2_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolcanaletasDeLavado2.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolcanaletasDeLavado2.xview)
		sedScrollY.configure(command=arbolcanaletasDeLavado2.yview)
		#Define columnas.
		arbolcanaletasDeLavado2["columns"]= (
			'Espaciamiento entre ejes de canaletas (asumido)',
			'Longitud del filtro',
			'Número de canaletas',					
			'Caudal de lavado',				
			'Caudal de lavado ecuado por cada canaleta',
			'Profundidad máxima del agua en la canaleta',							
			'Borde libre de la canaleta',	
			'Altura total interna de la canaleta',
			'Profundidad del lecho fijo',				
			'Profundidad del lecho expandido',					
			'Altura de la canaleta sobre el medio filtrante',
			'Espaciamiento entre ejes de canaletas (corregido)',					
			'Distancia de seguridad entre lecho expandido y fondo canaleta'

		)

		#Headings
		arbolcanaletasDeLavado2.heading("#0",text="ID", anchor=CENTER)

		for col in arbolcanaletasDeLavado2["columns"]:
			arbolcanaletasDeLavado2.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arbolcanaletasDeLavado2["columns"])+1) :
				arbolcanaletasDeLavado2.column(f"#{i}",width=700, stretch=False)	
		arbolcanaletasDeLavado2.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolcanaletasDeLavado2.tag_configure("evenrow", background= "#1FCCDB")
		arbolcanaletasDeLavado2.tag_configure("oddrow", background= "#9DC4AA")    

		listacanaletasDeLavado2=list()
		espaciamientoEntreEjesCanaletas=1.5
		listacanaletasDeLavado2.append(espaciamientoEntreEjesCanaletas)
		
		longitudFiltro= ValuepredimensionamientoFiltros(listaCaudal)[9]
		listacanaletasDeLavado2.append(longitudFiltro)

		numeroCanaletas= round(longitudFiltro/espaciamientoEntreEjesCanaletas,0)
		listacanaletasDeLavado2.append(numeroCanaletas)

		caudalLavado = ValueConsumoAguaLavado(listaExtra, tempValue, d60, listaCaudal)[5]
		listacanaletasDeLavado2.append(caudalLavado)

		caudalLavadoEcuadoCanaleta = caudalLavado/float(numeroCanaletas)
		listacanaletasDeLavado2.append(caudalLavadoEcuadoCanaleta)

		
		profundidadMaximaAguaCanaleta = (caudalLavadoEcuadoCanaleta/(anchoCanaleta*1.38))**(2/3)
		listacanaletasDeLavado2.append(profundidadMaximaAguaCanaleta)

		if profundidadMaximaAguaCanaleta/2 <0.05:
			bordeLibreCanaleta=0.05
		elif profundidadMaximaAguaCanaleta/2 > 0.1:
			bordeLibreCanaleta=0.1
		else:
			bordeLibreCanaleta= bordeLibreCanaleta*(0.5)

		listacanaletasDeLavado2.append(bordeLibreCanaleta)

		alturaTotalInternaCanaleta= round(profundidadMaximaAguaCanaleta+bordeLibreCanaleta,2)
		listacanaletasDeLavado2.append(alturaTotalInternaCanaleta)

		profundidadLechoFijo= 0.64

		listacanaletasDeLavado2.append(profundidadLechoFijo)

		profundidadLechoExpandido = ValuevelocidadLavadoExpansionLechoFiltrante(tempValue, d60)[9]

		listacanaletasDeLavado2.append(profundidadLechoExpandido)

		alturaCanaletaMedioFiltrante = ((0.75*profundidadLechoFijo)+alturaTotalInternaCanaleta+(alturaTotalInternaCanaleta+profundidadLechoFijo))*(1/2)
		
		listacanaletasDeLavado2.append(alturaCanaletaMedioFiltrante)

		espaciamientoEjesCorregido= longitudFiltro/numeroCanaletas
		
		listacanaletasDeLavado2.append(espaciamientoEjesCorregido)

		distanciaSeguridadLechoExpandidoYFondoCanaleta = alturaCanaletaMedioFiltrante -(profundidadLechoExpandido-profundidadLechoFijo)

		listacanaletasDeLavado2.append(distanciaSeguridadLechoExpandidoYFondoCanaleta)


				

		newDataTreeview(arbolcanaletasDeLavado2,listacanaletasDeLavado2)

		canaletasDeLavado2Window.mainloop()

	def dimensionesYCotasFiltros(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1,tasa):

		
		
		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5 or i==6:
					if elemento.get() == "Material de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tubería de lavado")
						return None
					elif elemento.get() == "Diámetro nominal de la tubería de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro nominal de la tubería de lavado")
						return None

					elif elemento.get() == "Codo 90° radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90° radio")
						return None
					
					
					elif elemento.get() == "Tipo de entrada":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de entrada del accesorio")
						return None
					
					elif elemento.get() == "Ancho de la canaleta":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el ancho de la canaleta")
						return None
					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>2.5 or float(elemento.get())<1.5):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tubería del efluente debe estar entre 1.5 y 2.5 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricción debe estar entre 0.00001 y 0.1")
						return None   
					
						


					
					elif i==7 and (float(elemento.get())>0.2 or float(elemento.get())<0.15):
						messagebox.showwarning(title="Error", message="El nivel del vertedero sobre el lecho fijo de arena debe estar entre 0.15 y 0.20")
						return None   

					elif i==8 and (float(elemento.get())>2.0 or float(elemento.get())<1.8):
						messagebox.showwarning(title="Error", message="El valor de la energía disponible de filtración debe estar entre 1.8 y 2.0")
						return None 


					elif i==9 and (float(elemento.get())>0.50 or float(elemento.get())<0.40):
						messagebox.showwarning(title="Error", message="El valor del borde libre debe estar entre 0.40 y 0.50")
						return None 

					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un número")
				return None
			
		



		dimensionesYCotasFiltrosWindow = tk.Toplevel()
		dimensionesYCotasFiltrosWindow.iconbitmap(bitmap='icons\\agua.ico')
		dimensionesYCotasFiltrosWindow.geometry("600x600") 
		dimensionesYCotasFiltrosWindow.resizable(0,0)	
		dimensionesYCotasFiltrosWindow.configure(background="#9DC4AA")

		dimensionesYCotasFiltrosFrame=LabelFrame(dimensionesYCotasFiltrosWindow, text="Cálculo de dimensiones y cotas en los filtros", font=("Yu Gothic bold", 11))
		dimensionesYCotasFiltrosFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboldimensionesYCotasFiltros_frame = Frame(dimensionesYCotasFiltrosFrame)
		arboldimensionesYCotasFiltros_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arboldimensionesYCotasFiltros_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldimensionesYCotasFiltros_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldimensionesYCotasFiltros= ttk.Treeview(arboldimensionesYCotasFiltros_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arboldimensionesYCotasFiltros.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arboldimensionesYCotasFiltros.xview)
		sedScrollY.configure(command=arboldimensionesYCotasFiltros.yview)
		#Define columnas.
		arboldimensionesYCotasFiltros["columns"]= (

		'Profundidad del lecho de grava',		
		'Profundidad del lecho fijo de arena',	
		'Pérdida de energía total a tasa media de filtración con lecho limpio',
		'Nivel de la lámina de agua con lecho limpio',
		'Nivel de la lámina de agua con pérdida de energía máxima',
		'Altura interna total del filtro',

		
		)

		#Headings
		arboldimensionesYCotasFiltros.heading("#0",text="ID", anchor=CENTER)

		for col in arboldimensionesYCotasFiltros["columns"]:
			arboldimensionesYCotasFiltros.heading(col, text=col,anchor=CENTER)	

		for i in range(0,len(arboldimensionesYCotasFiltros["columns"])+1) :
				arboldimensionesYCotasFiltros.column(f"#{i}",width=700, stretch=False)	
		arboldimensionesYCotasFiltros.column("#0",width=0, stretch=False)

		#Striped row tags
		arboldimensionesYCotasFiltros.tag_configure("evenrow", background= "#1FCCDB")
		arboldimensionesYCotasFiltros.tag_configure("oddrow", background= "#9DC4AA")    

		#CálculoPérdidaTotal
		listadimensionesYCotasFiltros=list()
		tasa="Tasa media"
		listaValuePerdidaCargaTuberiaLavado = valuePerdidaCargaTuberiaLavado_DW_HW2_2(listaE,temperatureValue,listaE1, d60,caudalLista,tasa)
		perdidaCargaLechoGrava = valuePerdidacargaLechoGravaLavado_2(temperatureValue,d60,tasa)[2]
		perdidaCargaSistemaDrenaje = valuePerdidaCargaSistemaDrenajeLavado_2(temperatureValue,d60, caudal,listaEntradaDrenaje,tasa)[3]
		
		perdidaCargaDW= listaValuePerdidaCargaTuberiaLavado[8]
		perdidaCargaAccesorios= listaValuePerdidaCargaTuberiaLavado[9]
		

		perdidaTotalLista= [perdidaCargaLechoGrava, 
		perdidaCargaSistemaDrenaje, perdidaCargaDW, perdidaCargaAccesorios] 
		

		perdidaCargaTotal =0.0
		for elemento in perdidaTotalLista:
			perdidaCargaTotal= perdidaCargaTotal +elemento 

		#############perdidaCargaTotal
		
		#Insersión datos. 
		profundidadLechoGrava = 0.450
		listadimensionesYCotasFiltros.append(profundidadLechoGrava)
		profundidadLechoFijoArena= 0.640
		listadimensionesYCotasFiltros.append(profundidadLechoFijoArena)
		listadimensionesYCotasFiltros.append(perdidaCargaTotal)
		nivelLaminaAguaLechoLimpio= profundidadLechoGrava+ profundidadLechoFijoArena+listaEU[7]+perdidaCargaTotal
		listadimensionesYCotasFiltros.append(nivelLaminaAguaLechoLimpio)

		nivelLaminaAguaPerdidaEnergiaMaxima= profundidadLechoGrava+ profundidadLechoFijoArena+listaEU[7]+listaEU[8]
		listadimensionesYCotasFiltros.append(nivelLaminaAguaPerdidaEnergiaMaxima)

		alturaInternaTotal = nivelLaminaAguaPerdidaEnergiaMaxima+ listaEU[9]
		listadimensionesYCotasFiltros.append(alturaInternaTotal)
		 
		
		


		newDataTreeview(arboldimensionesYCotasFiltros,listadimensionesYCotasFiltros)
		
		dimensionesYCotasFiltrosWindow.mainloop()
	


		

	def canaletasDeLavadoYDimensionesFiltros(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,tasaE):
		
		if tasaE.get() == "Tasa":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la tasa.")
			return None
		else:
			tasa = tasaE.get()

		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los orificios.")
			return None

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())


		if listaEntradaDrenaje[2].get() == "Sección transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la sección transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())


		if listaEntradaDrenaje[4].get() == "Diámetro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el diámetro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()

		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		else:
			tiempoRetrolavado = float(listaE[0].get())

		

		canaletasDeLavadoYDimensionesFiltrosWindow = tk.Toplevel()
		canaletasDeLavadoYDimensionesFiltrosWindow.iconbitmap(bitmap='icons\\agua.ico')
		canaletasDeLavadoYDimensionesFiltrosWindow.geometry("800x650") 
		canaletasDeLavadoYDimensionesFiltrosWindow.resizable(0,0)	
		canaletasDeLavadoYDimensionesFiltrosWindow.configure(background="#9DC4AA")

		framecanaletasDeLavadoYDimensionesFiltros= LabelFrame(canaletasDeLavadoYDimensionesFiltrosWindow, text= f"Datos adicionales para el cálculo de la pérdida total a {tasa.lower()} de filtración con lecho limpio",font=("Yu Gothic bold", 11))
		framecanaletasDeLavadoYDimensionesFiltros.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tubería de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
				elif elemento==tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)




		inicialLabel=Label(framecanaletasDeLavadoYDimensionesFiltros, text="Datos adicionales para cálculos: ",font=("Yu Gothic bold",15))

		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro dúctil C30",
		"Hierro dúctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]


		Valores=[(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
		(300,350,400,450,500,600),
		(150, 200, 250, 300, 350, 400, 450, 500, 600), 
		(160, 200, 250, 315, 355, 400), 
		(160, 200, 250, 315, 355, 400), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24), 
		(6, 8, 10, 12, 14, 16, 18, 20, 24)]

		opcionesDic = dict()

		for i in range(0, len(listaValoresTemp)):
			opcionesDic[listaValoresTemp[i]]=Valores[i] 


		def on_combobox_select(event):
			diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])

		materialTuberiaLavado = ttk.Combobox(framecanaletasDeLavadoYDimensionesFiltros, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tubería de lavado")

		materialTuberiaLabel= Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione el material de la tubería de lavado:",font=("Yu Gothic bold",10))
		

		diametroNominalTuberiaLavado = ttk.Combobox(framecanaletasDeLavadoYDimensionesFiltros, width="30", state="readonly")
		diametroNominalTuberiaLavado.set("Diámetro nominal de la tubería de lavado")
		diametroNominalTuberiaLavadoLabel= Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione el diametro nominal de la tubería de lavado:",font=("Yu Gothic bold",10))



		
		#NombrePendiente
		codoRadio = StringVar()
		codoRadio.set("Codo 90° radio")
		listaValoresTemp3=['Codo 90° radio corto (r/d 1)', 'Codo 90° radio mediano (r/d 3)']
		codoRadioName = OptionMenu(framecanaletasDeLavadoYDimensionesFiltros, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(framecanaletasDeLavadoYDimensionesFiltros, tipoEntrada, *listaValoresTemp3)

		AnchoCanaleta = StringVar()
		AnchoCanaleta.set("Ancho de la canaleta")
		listaValoresTemp3=['0.10','0.15','0.20','0.25','0.30','0.35']
		AnchoCanaletaName = OptionMenu(framecanaletasDeLavadoYDimensionesFiltros, AnchoCanaleta, *listaValoresTemp3)


		


		longitudTuberiaLavadoLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Longitud de la tubería del efluente [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione el factor de fricción [0.0001 - 0.1]:", font =("Yu Gothic",9))
		
		divisorAccesoriosLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione los tipos de accesorios", font=("Yu Gothic bold",10))
		
		divisorCanaletasLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione los valores para las canaletas de lavado:", font=("Yu Gothic bold",10))
		
		divisorDimensionesYCotasFiltrosLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione los valores para las dimensiones y cotas en los filtros:", font=("Yu Gothic bold",10))

		alturaVertederoControlLechoFijoLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Introduzca el nivel de vertedero sobre el lecho fijo de arena [0.15m - 0.20m]:", font=("Yu Gothic bold",10))

		energiaDisponibleFiltracionLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Introduzca la energía disponible de filtración [1.8m - 2.0m]", font=("Yu Gothic bold",10))

		bordeLibreLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Introduzca el valor del borde libre [0.40m - 0.50m]", font=("Yu Gothic bold",10))


		longitudTuberiaLavado = Entry(framecanaletasDeLavadoYDimensionesFiltros)
		factorFriccion = Entry(framecanaletasDeLavadoYDimensionesFiltros)	


		alturaVertederoControlLechoFijo = Entry(framecanaletasDeLavadoYDimensionesFiltros)	
		energiaDisponibleFiltracion = Entry(framecanaletasDeLavadoYDimensionesFiltros)	
		bordeLibre = Entry(framecanaletasDeLavadoYDimensionesFiltros)	

		




		listaEntradas=[materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada,AnchoCanaleta,
		alturaVertederoControlLechoFijo, energiaDisponibleFiltracion, bordeLibre]

		listaLabel=[inicialLabel, materialTuberiaLabel , materialTuberiaLavado, diametroNominalTuberiaLavadoLabel, 
		diametroNominalTuberiaLavado,longitudTuberiaLavadoLabel, factorFriccionLabel,divisorAccesoriosLabel,tipoEntradaName,
		divisorCanaletasLabel, AnchoCanaletaName, divisorDimensionesYCotasFiltrosLabel, alturaVertederoControlLechoFijoLabel,
		 energiaDisponibleFiltracionLabel,
		bordeLibreLabel]

		alturaInicialLabel=20
		m=0
		for elemento in listaLabel:
			elemento.place(x=50,y=alturaInicialLabel)
			alturaInicialLabel+=35
			m=m+1
			if m==3:
				alturaInicialEntradas=alturaInicialLabel
			if m==12:
				alturaInicialEntradas2= alturaInicialLabel

		i=0
		for elemento in listaEntradas:
				if i == 0 or i==1 or i==4 or i==5 or i==6:
					i=i+1
					alturaInicialEntradas+=35
				else: 
					if i>6:
						elemento.place(x=600,y=alturaInicialEntradas2)
						alturaInicialEntradas2+=35
					else:	
						i=i+1
						elemento.place(x=400,y=alturaInicialEntradas)
						alturaInicialEntradas+=35


	

		#BotonesCanaletasDimensiones
		botonCalcularCanaletas = HoverButton(framecanaletasDeLavadoYDimensionesFiltros, text="Cálculos canaletas de lavado", activebackground="#9DC4AA", width=100, height=1, bg= "#09C5CE", font =("Courier",9),command= lambda: canaletasDeLavado2(TemperatureValue,d60, caudalLista,listaE, listaEntradas[6]))
		botonCalcularDimensionesYCotasFiltros = HoverButton(framecanaletasDeLavadoYDimensionesFiltros, text="Cálculos dimensiones y cotas en los filtros", activebackground="#9DC4AA", width=100, height=1, bg= "#09C5CE", font =("Courier",9),command= lambda: dimensionesYCotasFiltros(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE,tasa))
		botonNewEntry = HoverButton(framecanaletasDeLavadoYDimensionesFiltros, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=1, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas))
		botones=[botonCalcularCanaletas, botonCalcularDimensionesYCotasFiltros, botonNewEntry]
		alturaBotones= alturaInicialEntradas2-10
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+30

		#Borrar

		materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		diametroNominalTuberiaLavado.set("10")
		longitudTuberiaLavado.insert(0,"1.50")
		factorFriccion.insert(0,"0.0200")	
		tipoEntrada.set('Entrada con boca acampanada')
		alturaVertederoControlLechoFijo.insert(0,"0.2")
		energiaDisponibleFiltracion.insert(0,"1.8")
		bordeLibre.insert(0,"0.4")
		AnchoCanaleta.set("0.15")
		#NOBorrar
		codoRadio.set('Codo 90° radio mediano (r/d 3)')
		




		canaletasDeLavadoYDimensionesFiltrosWindow.mainloop()


	def perdidaEnergiaLechoLimpio(listaTamiz, listaAR, optnValue, listaCaudal):
		#PerdidaLechoLimpio
		try: 
			caudalMedio=float(listaCaudal[0].get())
			
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un número.")
			return None

		listaNTamizTemp=listaTamiz.copy()
		listaARetenidaTemp=listaAR.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de los números de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta algún dato de la arena retenida.")
			return None
		if optnValue.get() == "Seleccione la temperatura":
			messagebox.showwarning(title="Error", message="Hace falta elegir el valor de la temperatura del agua a tratar.")
			return None
		else:
			valorTemperatura= int(optnValue.get())


		for ind in range(0, len(listaNTamizTemp)):
			if listaNTamizTemp[ind].get() == "" and ind%2==0:
				break
			elif listaNTamizTemp[ind].get() == "" and ind%2 != 0:
				messagebox.showwarning(title="Error", message="Hace falta el rango de la derecha de alguna entrada.")
				return None
			else:
				try:
					CountControl=0
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m: 
							CountControl=CountControl+1
					for m in [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]:
						if int(listaNTamizTemp[ind].get()) != m and CountControl==18:
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores estándar para número de tamiz. Pulse el botón para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de número de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None


		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un número")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de número de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento
		
		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None

		listaEntradaTemp=list()
		datosSalida=list()
		
		
			


		

		
		perdidaEnergiaLechoLimpioMainWindow = tk.Toplevel()
		perdidaEnergiaLechoLimpioMainWindow.iconbitmap(bitmap='icons\\agua.ico')
		perdidaEnergiaLechoLimpioMainWindow.geometry("800x600") 
		perdidaEnergiaLechoLimpioMainWindow.resizable(0,0)	
		perdidaEnergiaLechoLimpioMainWindow.configure(background="#9DC4AA")

		perdidaEnergiaLechoLimpioMainFrame=LabelFrame(perdidaEnergiaLechoLimpioMainWindow, text="Datos adicionales para calcular la pérdida de energía durante filtrado con lecho limpio", font=("Yu Gothic bold", 11))
		perdidaEnergiaLechoLimpioMainFrame.pack(side=TOP, fill=BOTH,expand=True)

		
		
		diametroOrificios = StringVar()
		diametroOrificios.set("Diametro de los orificios")
		listaValoresTempDiametroOrificios=list()
		listaValoresTempDiametroOrificios.append("1/4")
		listaValoresTempDiametroOrificios.append("3/8")
		listaValoresTempDiametroOrificios.append("1/2")
		listaValoresTempDiametroOrificios.append("5/8")
		diametroOrificiosName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, diametroOrificios, *listaValoresTempDiametroOrificios)
		diametroOrificiosLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione el diámetro de los orificios:", font=("Yu Gothic bold", 11))
		

		
		distanciaOrificios = StringVar()
		distanciaOrificios.set("Distancia entre los orificios")
		listaValoresTempDistanciaOrificios=list()
		listaValoresTempDistanciaOrificios.append("0.750")
		listaValoresTempDistanciaOrificios.append("0.100")
		listaValoresTempDistanciaOrificios.append("0.125")
		listaValoresTempDistanciaOrificios.append("0.150")
		distanciaOrificiosName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, distanciaOrificios, *listaValoresTempDistanciaOrificios)
		distanciaOrificiosLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la distancia entre orificios:", font=("Yu Gothic bold", 11))


		seccionTransversal = StringVar()
		seccionTransversal.set("Sección transversal")
		listaValoresTempSeccionTransversal=list()
		listaValoresTempSeccionTransversal.append("6 X 6")
		listaValoresTempSeccionTransversal.append("8 X 8")
		listaValoresTempSeccionTransversal.append("10 X 10")
		listaValoresTempSeccionTransversal.append("12 X 12")
		listaValoresTempSeccionTransversal.append("14 X 14")
		listaValoresTempSeccionTransversal.append("16 X 16")
		listaValoresTempSeccionTransversal.append("18 X 18")
		listaValoresTempSeccionTransversal.append("20 X 20")
		seccionTransversalName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, seccionTransversal, *listaValoresTempSeccionTransversal)
		seccionTransversalLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la sección transversal comercial del múltiple:", font=("Yu Gothic bold", 11))


		distanciaLaterales = StringVar()
		distanciaLaterales.set("Distancia entre laterales")
		listaValoresTempDistanciaLaterales=list()
		listaValoresTempDistanciaLaterales.append("0.20")
		listaValoresTempDistanciaLaterales.append("0.25")
		listaValoresTempDistanciaLaterales.append("0.30")
		distanciaLateralesName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, distanciaLaterales, *listaValoresTempDistanciaLaterales)
		distanciaLateralesLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la distancia entre laterales:", font=("Yu Gothic bold", 11))
		

		
		diametroEntreLaterales = StringVar()
		diametroEntreLaterales.set("Diámetro de los laterales")
		listaValoresTempDiametroEntreLaterales=list()
		listaValoresTempDiametroEntreLaterales.append("1 1/2")
		listaValoresTempDiametroEntreLaterales.append("2")
		listaValoresTempDiametroEntreLaterales.append("2 1/2")
		listaValoresTempDiametroEntreLaterales.append("3")
		diametroEntreLateralesName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, diametroEntreLaterales, *listaValoresTempDiametroEntreLaterales)
		diametroEntreLateralesLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione el diámetro de los laterales:", font=("Yu Gothic bold", 11))

		tiempoRetrolavado = StringVar()
		tiempoRetrolavado.set("Tiempo de retrolavado")
		listaValoresTemptiempoRetrolavado=list()
		listaValoresTemptiempoRetrolavado.append("10")
		listaValoresTemptiempoRetrolavado.append("11")
		listaValoresTemptiempoRetrolavado.append("12")
		listaValoresTemptiempoRetrolavado.append("13")
		listaValoresTemptiempoRetrolavado.append("14")
		tiempoRetrolavadoName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, tiempoRetrolavado, *listaValoresTemptiempoRetrolavado)
		tiempoRetrolavadoLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione el tiempo de retrolavado.", font=("Yu Gothic bold", 11))

		
		TasaElegir = StringVar()
		TasaElegir.set("Tasa")
		listaValoresTempTasaElegir=list()
		listaValoresTempTasaElegir.append("Tasa media")
		listaValoresTempTasaElegir.append("Tasa máxima")
		TasaElegirName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, TasaElegir, *listaValoresTempTasaElegir)
		TasaElegirLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la tasa.", font=("Yu Gothic bold", 11))






		listaEntradaDrenaje2=[diametroOrificiosName,distanciaOrificiosName,seccionTransversalName,distanciaLateralesName, diametroEntreLateralesName,tiempoRetrolavadoName,TasaElegirName]
		listaLabel= [diametroOrificiosLabel,distanciaOrificiosLabel, seccionTransversalLabel, distanciaLateralesLabel, diametroEntreLateralesLabel,tiempoRetrolavadoLabel,TasaElegirLabel]
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]
		listaEntradaExtra=[tiempoRetrolavado]
		
		#Borrar

		diametroOrificios.set("1/4")
		distanciaOrificios.set("0.100")
		seccionTransversal.set("14 X 14")
		distanciaLaterales.set("0.25")
		diametroEntreLaterales.set("1 1/2")
		tiempoRetrolavado.set("12")
		TasaElegir.set('Tasa media')
		
		

		altIn= 30
		altIn2=30
		for ind in range(0,len(listaLabel)):
			if ind%2==0:
				listaLabel[ind].place(x=20,y=altIn)
				listaEntradaDrenaje2[ind].place(x=20, y= altIn+20)
				altIn=altIn+80
			else:
				listaLabel[ind].place(x=500,y=altIn2)
				listaEntradaDrenaje2[ind].place(x=500, y= altIn2+20)
				altIn2=altIn2+80
			
		#BotonesPerdidaEnergiaLechoLimpio
		

		#TasaElegir
		

		
		#Pendiente: Quitar elementos que no se usan en manejo de errores. 
		botonPerdidacargaLechoGravaLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Pérdida de carga a través\n del lecho de grava durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidacargaLechoGravaLavado_2(TasaElegir) ) 
		botonPerdidaCargaSistemaDrenajeLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Pérdida de carga a través\n del sistema de drenaje durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaSistemaDrenajeLavado_2(caudalMedio, listaEntradaDrenaje, TasaElegir) )
		botonPerdidaCargaTuberiaLavado_DW = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Pérdida de carga en la tubería\n de lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTuberiaLavado_DW_HW_2(valorTemperatura,listaEntradaExtra,d60,listaCaudal,TasaElegir)) 
		botonPerdidaCargaTotalLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Pérdida de carga total durante\n el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTotalLavadoMain_2(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal,TasaElegir))
		botonCanaletasLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Canaletas de lavado &\n dimensiones y cotas en los filtros", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: canaletasDeLavadoYDimensionesFiltros(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal,TasaElegir) )
		

		def newEntryPerdidaTotal(lista): 
			lista2= [
						"Diametro de los orificios",
						"Distancia entre los orificios",
						"Sección transversal",
						"Distancia entre laterales",
						"Diámetro de los laterales",
						"Tiempo de retrolavado",
						"Tasa"]

			for i in range(0, len(lista)):
					lista[i].set(lista2[i])
		
		listaTasa= [TasaElegir]
		botonLimpiarEntradasPerdidaTotal =  HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Limpiar Entradas", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: newEntryPerdidaTotal(listaEntradaDrenaje+listaEntradaExtra+listaTasa))


		 

		

		listaBotones=[botonPerdidacargaLechoGravaLavado ,botonPerdidaCargaSistemaDrenajeLavado 
		,botonPerdidaCargaTuberiaLavado_DW,botonPerdidaCargaTotalLavado, botonCanaletasLavado, botonLimpiarEntradasPerdidaTotal]
			
		counter= 0
		altIn2= altIn
		for elemento in listaBotones:
			if counter < 3:
				elemento.place(x=20,y=altIn)
				altIn=altIn+60
				counter=counter+1
			else: 
				elemento.place(x=500,y=altIn2)
				altIn2=altIn2+60
		
			

		
		listaCU = valorCoeficienteDeUniformidad(listaTamiz,listaAR)
		d10= listaCU[0]
		CU=listaCU[1]
		d60=d10*CU

		##return [d10,CU]
		
		perdidaEnergiaLechoLimpioMainWindow.mainloop()



        


	mainWindow.withdraw()
	filtroWindow = tk.Toplevel()
	filtroWindow.protocol("WM_DELETE_WINDOW", on_closing)
	filtroWindow.iconbitmap(bitmap='icons\\agua.ico')
	filtroWindow.geometry("1000x650") 
	filtroWindow.resizable(0,0)	
	filtroWindow.configure(background="#9DC4AA")

	#panelF = ttk.Notebook(filtroWindow)
	#panelF.pack(fill=BOTH, expand=TRUE)
	frameFiltro= LabelFrame(filtroWindow, text="Filtro rápido", font=("Yu Gothic bold", 11))
	frameFiltro.pack(side=LEFT,fill=BOTH,expand=TRUE)
	#panelF.add(frameFiltro, text="Filtro rápido")
	
	imageAtras= PhotoImage(file="images\\atras.png")
	imageRestringido=PhotoImage(file="images\\restringido.png")
	#BotonesFiltro 


	botonAtras= HoverButton(frameFiltro, image=imageAtras , width=100, height=40, bg= None, command=lambda: returnMainWindow(filtroWindow))
	botonAtras.place(x=0,y=10)
	botonRestriccionNumTamiz=  HoverButton(frameFiltro, image=imageRestringido, bg=None, width=20, height=20,command= lambda: messagebox.showinfo(title="Valores estándar tamaño de tamiz",message=f"Los tamaños estándar son: 4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140") )
	botonRestriccionNumTamiz.place(x=150,y=65)


	botonNewEntryFiltro = HoverButton(frameFiltro, text="Limpiar entradas", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: newEntryFiltro(lista_entradas, tempAgua, entradasCaudal))

	botonPrincipalesCaracteristicasDelFiltro = HoverButton(frameFiltro, text="Ver principales características del filtro", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=principalesCaracFiltro)

	botonGranulometria = HoverButton(frameFiltro, text="Granulometría del medio filtrante de arena", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: granulometria(listaNumTamiz,listaAR))

	botonCoefUniformidad = HoverButton(frameFiltro, text="Coeficiente de uniformidad", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: coeficienteDeUniformidad(listaNumTamiz, listaAR) )
	######DEF TEMP AGUA
	tempAgua = StringVar()
	tempAgua.set("Seleccione la temperatura")
	listaValoresTemp=list()
	for i in range(0,36):
		listaValoresTemp.append(f"{i}")
	
	tempAguaName = OptionMenu(frameFiltro, tempAgua, *listaValoresTemp)
	tempAguaName.place(x=350, y=99)
	
	
	#DEF CaudalEntry
	
	#tipoCaudalName.place(x=350, y=186)
	tipoCaudalLabel = Label(frameFiltro, text="Caudal de diseño:",font=("Yu Gothic bold",10))
	#tipoCaudalLabel.place(x=250, y=157)
	caudalMedioLabel= Label(frameFiltro, text="Caudal medio diario: ",font=("Yu Gothic bold",10))	
	caudalMedio = Entry(frameFiltro, width=6)

	altIninicial=157
	listaTipoCaudal = [tipoCaudalLabel, caudalMedioLabel]
	for elem in listaTipoCaudal:
		elem.place(x=350, y=altIninicial)
		altIninicial=altIninicial+35
	caudalMedio.place(x=500, y=altIninicial-35)
	entradasCaudal= [caudalMedio]

	#####FIN TEMP AGUA
	
	#BotonesFiltro2

	botonEstimacionPerdidaEnergiaLechoFiltranteArenaLimpio = HoverButton(frameFiltro, text="Pérdida de energía en el lecho filtrante de arena limpio", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: estimacionPerdidaEnergiaArena(listaNumTamiz,listaAR,tempAgua))

	#botonEstimacionPerdidaLechoGrava = HoverButton(frameFiltro, text="Estimación de la pérdida de energía en el lecho de grava, y\n ¿Carga?", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: estPerdidaLechoGravaYPredimensionamientoFiltros(listaNumTamiz, listaAR,tempAgua))

	#botonPerdidaCargaLechoExpandido = HoverButton(frameFiltro, text="Pérdida de carga a través del lecho expandido", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command= perdidaCargaLechoExpandido)

	botonPredimensionamientoFiltros = HoverButton(frameFiltro, text="Predimensionamiento de los filtros", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: predimensionamientoFiltros(entradasCaudal))

	botonDrenajeFiltro = HoverButton(frameFiltro, text="Drenaje del filtro - Tuberías perforadas", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: drenajeFiltro(entradasCaudal))

	botonHidraulicaSistemaLavado = HoverButton(frameFiltro, text="Hidráulica del sistema de lavado", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: hidraulicaSistemaLavado(listaNumTamiz,listaAR,tempAgua, entradasCaudal))

	botonPerdidaEnergiaLechoLimpio = HoverButton(frameFiltro, text="Pérdidas de energía durante el filtrado con lecho limpio", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: perdidaEnergiaLechoLimpio(listaNumTamiz,listaAR,tempAgua, entradasCaudal))
 
			



	listaBotonesOrg=[botonNewEntryFiltro,botonPrincipalesCaracteristicasDelFiltro, botonGranulometria,botonCoefUniformidad,botonEstimacionPerdidaEnergiaLechoFiltranteArenaLimpio,botonPredimensionamientoFiltros,botonDrenajeFiltro,botonHidraulicaSistemaLavado,botonPerdidaEnergiaLechoLimpio]#,botonEstimacionPerdidaLechoGrava,botonPerdidaCargaLechoExpandido]

	alturaInicialBotones=70
	for boton in listaBotonesOrg:
		boton.place(x=560, y=alturaInicialBotones)
		alturaInicialBotones=alturaInicialBotones+60
	

	Label(frameFiltro, text="Diseño de filtro",font=("Yu Gothic bold",10)).place(x=170, y=30)

	numTamizLabel = Label(frameFiltro, text="Número de tamiz",font=("Yu Gothic bold",10))
	numTamizLabel.place(x=30, y=70)
	arenaRetenidaLabel = Label(frameFiltro, text="Arena retenida [%]",font=("Yu Gothic bold",10))
	arenaRetenidaLabel.place(x=200, y=70)
	tempAguaLabel = Label(frameFiltro, text="Temperatura del agua a tratar:",font=("Yu Gothic bold",10))
	tempAguaLabel.place(x=250, y=70)
	
	#salidaLabel = Label(frameFiltro, text="Final",font=("Yu Gothic bold",10))
	#salidaLabel.place(x=30, y=450)

	valoresAceptadosTamiz2=["4","6","8","12","14","18","20","25","30","35","40","45","50","60","70","80","100","140"]


	def celda2(col2,col1):
		if col1.get() != "":
			col1.delete(0,END)
		ent = col2.get()
		for val in valoresAceptadosTamiz2:
			if ent == val:
				col1.insert(0, ent)
	
	nT11 = Entry(frameFiltro, width=6)

	var12=StringVar()
	nT12 = Entry(frameFiltro, width=6, textvariable=var12)
	nT21 = Entry(frameFiltro, width=6)
	var12.trace_add("write", lambda *args: celda2(nT12,nT21))
	
	var22=StringVar()
	nT22 = Entry(frameFiltro, width=6, textvariable=var22)
	nT31 = Entry(frameFiltro, width=6)
	var22.trace_add("write", lambda *args: celda2(nT22,nT31))
	
	var32=StringVar()
	nT32 = Entry(frameFiltro, width=6, textvariable=var32)
	nT41 = Entry(frameFiltro, width=6)
	var32.trace_add("write", lambda *args: celda2(nT32,nT41))


	var42=StringVar()
	nT42 = Entry(frameFiltro, width=6, textvariable=var42)
	nT51 = Entry(frameFiltro, width=6)
	var42.trace_add("write", lambda *args: celda2(nT42,nT51))
	
	var52=StringVar()
	nT52 = Entry(frameFiltro, width=6, textvariable=var52)
	nT61 = Entry(frameFiltro, width=6)
	var52.trace_add("write", lambda *args: celda2(nT52,nT61))

	var62=StringVar()
	nT62 = Entry(frameFiltro, width=6, textvariable=var62)
	nT71 = Entry(frameFiltro, width=6)
	var62.trace_add("write", lambda *args: celda2(nT62,nT71))

	var72= StringVar()
	nT72 = Entry(frameFiltro, width=6, textvariable=var72)
	nT81 = Entry(frameFiltro, width=6)
	var72.trace_add("write", lambda *args: celda2(nT72,nT81))

	var82=StringVar()
	nT82 = Entry(frameFiltro, width=6, textvariable=var82)
	nT91 = Entry(frameFiltro, width=6)
	var82.trace_add("write", lambda *args: celda2(nT82,nT91))

	var92=StringVar()
	nT92 = Entry(frameFiltro, width=6, textvariable=var92)
	nT101 = Entry(frameFiltro, width=6)
	var92.trace_add("write", lambda *args: celda2(nT92,nT101))

	var102=StringVar()
	nT102 = Entry(frameFiltro, width=6, textvariable=var102)
	nT111 = Entry(frameFiltro, width=6)
	var102.trace_add("write", lambda *args: celda2(nT102,nT111))

	var112=StringVar()
	nT112 = Entry(frameFiltro, width=6, textvariable=var112)
	nT121 = Entry(frameFiltro, width=6)
	var112.trace_add("write", lambda *args: celda2(nT112,nT121))

	nT122 = Entry(frameFiltro, width=6)



	labelSepnT1= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT2= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT3= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT4= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT5= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT6= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT7= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT8= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT9= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT10= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT11= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))
	labelSepnT12= Label(frameFiltro, text="-",font=("Yu Gothic bold",10))

	aR1 = Entry(frameFiltro, width=6)
	aR2 = Entry(frameFiltro, width=6)
	aR3 = Entry(frameFiltro, width=6)
	aR4 = Entry(frameFiltro, width=6)
	aR5 = Entry(frameFiltro, width=6)
	aR6 = Entry(frameFiltro, width=6)
	aR7 = Entry(frameFiltro, width=6)
	aR8 = Entry(frameFiltro, width=6)
	aR9 = Entry(frameFiltro, width=6)
	aR10 = Entry(frameFiltro, width=6)
	aR11 = Entry(frameFiltro, width=6)
	aR12 = Entry(frameFiltro, width=6)

	
	

	listaNumTamiz=[nT11,nT12,nT21,nT22,nT31,nT32,nT41,nT42,nT51,nT52,nT61,nT62,nT71,nT72,nT81,nT82,nT91,nT92,nT101,nT102,nT111,nT112,nT121,nT122]
	listaSepnT=[labelSepnT1, labelSepnT2, labelSepnT3, labelSepnT4, labelSepnT5, labelSepnT6, labelSepnT7, labelSepnT8, labelSepnT9, labelSepnT10, labelSepnT11, labelSepnT12]	
	listaAR=[aR1,aR2,aR3,aR4,aR5,aR6,aR7,aR8,aR9,aR10,aR11,aR12]
	
	#Borrar
	
	
	tempAgua.set("3")
	caudalMedio.insert(0,"0.04404")
	listaNTamiz=[14, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 50, 50, 60, 60, 70, 70, 100]
	listaARetenida= [16.20 , 33.70, 33.90, 6.20, 3.50, 3.00, 2.00, 1.0, 0.50]
	for i in range(0, len(listaNTamiz)):
		listaNumTamiz[i].insert(0, listaNTamiz[i])
		listaNumTamiz[i+1].delete(0,END)
	
	
	for i in range(0, len(listaARetenida)):
		listaAR[i].insert(0,listaARetenida[i])
		
	
	#Borrar
	

	i=0
	alturaInicial = 99
	for elemento in listaNumTamiz:
		if i%2==0:
			elemento.place(x=30, y=alturaInicial)
			i=i+1
		else:
			elemento.place(x=110, y=alturaInicial)
			i=i+1
			alturaInicial=alturaInicial+29
	alturaInicial = 99

	for j in range(0,len(listaSepnT)):
		listaSepnT[j].place(x=80, y=alturaInicial)
		listaAR[j].place(x=235, y=alturaInicial)
		alturaInicial=alturaInicial+29

	tempAguaLabel.place(x=350, y=70)
	nT11.focus()
	
	lista_entradas= listaNumTamiz+listaAR


	filtroWindow.mainloop()


def openFloculadorWindow():
	global contadorFloculador
	#Style
	style = ttk.Style()
	#Pick a theme
	style.theme_use("clam")

	#Configure colors

	style.configure("Treeview",background="#9DC4AA", foreground="black", rowheight=40,fieldbackground="#9DC4AA")
	style.configure("Treeview.Heading", foreground="black", font =("Courier",12))
	#Change selected color
	style.map("Treeview", background=[("selected", "#09C5CE")])	 

	def newEntryFiltro(lista):
		for elemento in lista:
				elemento.delete(0, END)
		lista[10].insert(0,9.81)
		

	def newDataTreeview(tree,listaS):
		global contadorFloculador

		if contadorFloculador%2 ==0:
			tree.insert("",END,text= f"{contadorFloculador+1}", values=tuple(listaS),
			iid=contadorFloculador, tags=("evenrow",))	
		else:	
			tree.insert("",END,text= f"{contadorFloculador+1}", values=tuple(listaS),
				iid=contadorFloculador, tags=("oddrow",))
		contadorFloculador=contadorFloculador+1
	
	def calculosFloculador(listaEntry):
		listaE2=list()
		for elemento in listaEntry:
			try:
				listaE2.append(float(elemento.get()))
			except:	
				messagebox.showwarning(title="Error", message="Uno o varios de los valores ingresados no son números")
				return None
		#listaE2 = [57.26,20.00,0.39,0.45964,0.508,1.30,1.60,2.75,998.30,0.00000101,9.81,20.00,0.76,0.80]
		listaE=list()
		numeroCamaras=12
		#Ingreso datos completos.
		listaE.append(listaE2[0])
		listaE.append(listaE2[0]/1000)
		listaE.append(listaE2[1])
		listaE.append(listaE2[1]*60)
		listaE.append((listaE2[1]*60)/numeroCamaras)
		listaE.append(((listaE2[1]*60)/numeroCamaras)*(listaE2[0]/1000))
		listaE.append(listaE2[2])
		listaE.append(listaE2[3])
		listaE.append((listaE2[3]**2)*pi*(1/4))
		listaE.append(listaE2[4])
		listaE.append((listaE2[4]**2)*pi*(1/4))
		listaE.append(listaE2[5])
		listaE.append(listaE2[6])
		listaE.append(listaE2[7])
		listaE.append(listaE2[8])
		listaE.append(listaE2[9])
		listaE.append(listaE2[10])
		listaE.append(listaE2[11])
		listaE.append(listaE2[12])
		listaE.append(listaE2[13])
		
		CFloculadorWindow = tk.Toplevel()
		CFloculadorWindow.iconbitmap(bitmap='icons\\agua.ico')
		CFloculadorWindow.geometry("1000x200") 
		CFloculadorWindow.resizable(0,0)	
		CFloculadorWindow.configure(background="#9DC4AA")

		#Frame Treeview
		arbolCFloculador_frame = LabelFrame(CFloculadorWindow, text="Principales caracterísiticas del filtro", font=("Yu Gothic bold", 11))
		arbolCFloculador_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolCFloculador_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolCFloculador_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCFloculador= ttk.Treeview(arbolCFloculador_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolCFloculador.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolCFloculador.xview)
		sedScrollY.configure(command=arbolCFloculador.yview)
		#Define columnas.
		arbolCFloculador["columns"]= (
		"V = Volumen floculador [m^3]",
		"#c = Número de cámaras [und]",
		"{} = Velocidad de flujo entre codos [m/s]".format(getSub("v")),
		"H\' = Pérdida Pasamuro [m]",
		"H\'\' = Perdida Codo [m]",
		"H\'\'\' = Perdidas Orificio [m]",
		"H = Perdida total floculador [m]",
		"Pc = Perdidas de carga en las 12 cámaras [m]",
		"G = Gradiente de mezcla [s^(-1)]",
		"Gt = Numero de camp",
		"P = Pendiente [%]"
		)

		#Headings
		arbolCFloculador.heading("#0",text="ID", anchor=CENTER)

		for col in arbolCFloculador["columns"]:
			arbolCFloculador.heading(col, text=col,anchor=CENTER)

		for i in range(0,len(arbolCFloculador["columns"])) :
				arbolCFloculador.column(f"#{i}",width=300, stretch=False)	

		
		arbolCFloculador.column("#3",width=600, stretch=False)
		arbolCFloculador.column("#7",width=500, stretch=False)
		arbolCFloculador.column("#8",width=600, stretch=False)
		arbolCFloculador.column("#9",width=600, stretch=False)
		arbolCFloculador.column("#10",width=600, stretch=False)

		arbolCFloculador.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolCFloculador.tag_configure("evenrow", background= "#1FCCDB")
		arbolCFloculador.tag_configure("oddrow", background= "#9DC4AA")
		contadorFloculador=0
		listaEntrada= list()
		volFloculador = listaE[15-4]*listaE[16-4]*listaE[17-4]*numeroCamaras
		numeroCamaras=12
		velFlujoCodos=listaE[5-4]/listaE[12-4]
		perdidadPasamuro = (listaE[5-4]**2)/(2*listaE[20-4]*(listaE[22-4]**2)*(listaE[12-4]**2))
		perdidaCodo = 0.4*((velFlujoCodos**2)/(2*listaE[20-4]))
		perdidaOrificio= (listaE[5-4]**2)/((2*listaE[20-4])*(listaE[23-4]**2)*(listaE[14-4]**2))		
		perdidaFloculador= perdidadPasamuro+perdidaCodo+perdidaOrificio
		perdidadCargaenCamaras=perdidaFloculador*numeroCamaras
		gradienteMezcla=sqrt((listaE[20-4]*perdidaFloculador)/(listaE[19-4]*listaE[8-4]))
		numeroCamp=gradienteMezcla*listaE[8-4]
		pendiente= perdidaFloculador/listaE[16-4]
		listaValores=[volFloculador,numeroCamaras,velFlujoCodos,perdidadPasamuro,perdidaCodo,perdidaOrificio,
		perdidaFloculador,perdidadCargaenCamaras,gradienteMezcla,numeroCamp,pendiente]
		for valor in listaValores:
			listaEntrada.append(valor)

		newDataTreeview(arbolCFloculador,listaEntrada)
		if velFlujoCodos>=0.25 and velFlujoCodos<=0.65:
			messagebox.showinfo(title="Información", message="El valor de la velocidad de flujo entre codos cumple. Se encuentra entre 0.25 y 0.65.")
		else:
			messagebox.showarning(title="¡Cuidado!", message="El valor de la velocidad de flujo entre codos NO cumple. No se encuentra entre 0.25 y 0.65.")
		
		if gradienteMezcla>=35 and gradienteMezcla<=55:
			messagebox.showinfo(title="Información", message="El valor del gradiente de mezcla cumple. Se encuentra entre 35 y 55.")
		else:
			messagebox.showarning(title="¡Cuidado!", message="El valor del gradiente de mezcla NO cumple. No se encuentra entre 35 y 55.")
		
		
		
		CFloculadorWindow.mainloop()


	def salidaCamara(listaEntry,diametroInternoOrificio):
		
		listaE2=list()
		for elemento in listaEntry:
			try:
				listaE2.append(float(elemento.get()))
			except:	
				messagebox.showwarning(title="Error", message="Uno o varios de los valores ingresados no son números")
				return None
		##########Datos eliminar
		listaE2 = [57.26,20.00,0.39,0.45964,0.51,1.30,1.60,2.75,998.30,0.00000101,9.81,20.00,0.76,0.80]		
		############
		listaE=list()
		numeroCamaras=12
		#Ingreso datos completos.
		listaE.append(listaE2[0])
		listaE.append(listaE2[0]/1000)
		listaE.append(listaE2[1])
		listaE.append(listaE2[1]*60)
		listaE.append((listaE2[1]*60)/numeroCamaras)
		listaE.append(((listaE2[1]*60)/numeroCamaras)*(listaE2[0]/1000))
		listaE.append(listaE2[2])
		listaE.append(listaE2[3])
		listaE.append((listaE2[3]**2)*pi*(1/4))
		listaE.append(listaE2[4])
		listaE.append((listaE2[4]**2)*pi*(1/4))
		listaE.append(listaE2[5])
		listaE.append(listaE2[6])
		listaE.append(listaE2[7])
		listaE.append(listaE2[8])
		listaE.append(listaE2[9])
		listaE.append(listaE2[10])
		listaE.append(listaE2[11])
		listaE.append(listaE2[12])
		listaE.append(listaE2[13])
		
		salidaCamaraWindow = tk.Toplevel()
		salidaCamaraWindow.iconbitmap(bitmap='icons\\agua.ico')
		salidaCamaraWindow.geometry("1000x200") 
		salidaCamaraWindow.resizable(0,0)	
		salidaCamaraWindow.configure(background="#9DC4AA")

		#Frame Treeview
		arbolSalidaCamara_frame = LabelFrame(salidaCamaraWindow, text="Principales caracterísiticas del filtro", font=("Yu Gothic bold", 11))
		arbolSalidaCamara_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolSalidaCamara_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolSalidaCamara_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolSalidaCamara= ttk.Treeview(arbolSalidaCamara_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolSalidaCamara.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolSalidaCamara.xview)
		sedScrollY.configure(command=arbolSalidaCamara.yview)
		#Define columnas.
		arbolSalidaCamara["columns"]= (
		"Di = Diametro de interno Orificio [m]",
		"A= Área del orificio [m^2]",
		"Cd = Coeficiente de descarga",
		"H\' = Pérdida Pasamuro [m]",
		"H\'\' = Perdida Codo [m]",
		"H\'\'\' = Perdidas Orificio [m]",
		"H = Perdida total floculador [m]",
		"G = Gradiente de mezcla [s^(-1)]",
		"Gt = Numero de camp",
		"P = Pendiente [%]"			)

		#Headings
		arbolSalidaCamara.heading("#0",text="ID", anchor=CENTER)

		for col in arbolSalidaCamara["columns"]:
			arbolSalidaCamara.heading(col, text=col,anchor=CENTER)

		for i in range(0,len(arbolSalidaCamara["columns"])) :
				arbolSalidaCamara.column(f"#{i}",width=300, stretch=False)	

		
		arbolSalidaCamara.column("#1",width=600, stretch=False)
		arbolSalidaCamara.column("#3",width=600, stretch=False)
		arbolSalidaCamara.column("#7",width=600, stretch=False)
		arbolSalidaCamara.column("#8",width=600, stretch=False)
		arbolSalidaCamara.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolSalidaCamara.tag_configure("oddrow", background= "#1FCCDB")
		arbolSalidaCamara.tag_configure("evenrow", background= "#9DC4AA")
		contadorFloculador=0
		listaEntrada=list()
		velocidadFlujoCodos=listaE[5-4]/listaE[12-4]
		arenaOrificio= pi*(diametroInternoOrificio**2)*(1/4)
		coeficienteDescarga= listaE[23-4]
		perdidaPasamuros= (listaE[5-4]**2)/((2*listaE[20-4])*(coeficienteDescarga**2)*(listaE[12-4]**2))
		perdidaCodo= (0.4)*((velocidadFlujoCodos**2)/(2*listaE[20-4]))
		perdidaOrificio= (listaE[5-4]**2)/((2*listaE[20-4])*(listaE[23-4]**2)*(arenaOrificio**2))
		perdidaFloculador= perdidaPasamuros+perdidaCodo+perdidaOrificio
		gradienteMezcla= sqrt((listaE[20-4]*perdidaFloculador)/(listaE[19-4]*listaE[8-4]))
		numeroCamp= gradienteMezcla*listaE[8-4]
		pendiente= perdidaFloculador/listaE[16-4]

		listaValores=[diametroInternoOrificio,arenaOrificio,coeficienteDescarga,perdidaPasamuros,perdidaCodo,
		perdidaOrificio,perdidaFloculador,gradienteMezcla,numeroCamp,pendiente]
		for valores in listaValores:
			listaEntrada.append(valores)

		newDataTreeview(arbolSalidaCamara,listaEntrada)
		
		if gradienteMezcla>=35 and gradienteMezcla<=55:
			messagebox.showinfo(title="Información", message="El valor del gradiente de mezcla cumple. Se encuentra entre 35 y 55.")
		else:
			messagebox.showarning(title="¡Cuidado!", message="El valor del gradiente de mezcla NO cumple. No se encuentra entre 35 y 55.")
		


		salidaCamaraWindow.mainloop()
	

	mainWindow.withdraw()
	floculadorWindow = tk.Toplevel()
	floculadorWindow.protocol("WM_DELETE_WINDOW", on_closing)
	floculadorWindow.iconbitmap(bitmap='icons\\agua.ico')
	floculadorWindow.geometry("1000x600") 
	floculadorWindow.resizable(0,0)	
	floculadorWindow.configure(background="#9DC4AA")


	frameFloculador= LabelFrame(floculadorWindow, text="Diseño Floculador Alabama", font=("Yu Gothic bold", 11))
	frameFloculador.pack(side=LEFT,fill=BOTH,expand=TRUE)


	imageAtras= PhotoImage(file="images\\atras.png")

	#Botones. 

	botonAtrasFlo= HoverButton(frameFloculador, image=imageAtras , width=100, height=40, bg= None, command=lambda: returnMainWindow(floculadorWindow))
	botonAtrasFlo.place(x=0,y=10)

	botonNewEntryFiltro = HoverButton(frameFloculador, text="Limpiar entradas", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: newEntryFiltro(listaEntry))
	botonVerCalculos = HoverButton(frameFloculador, text="Ver cálculos", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT, command= lambda: calculosFloculador(listaEntry))
	botonDatosSalidaCamaraPar = HoverButton(frameFloculador, text="Datos de salida Cámara No. (par)", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: salidaCamara(listaEntry,0.46))
	botonDatosSalidaCamaraImpar = HoverButton(frameFloculador, text="Datos de salida Cámara No. (impar)", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: salidaCamara(listaEntry,0.41))


	listaBotones=[botonNewEntryFiltro, botonVerCalculos,botonDatosSalidaCamaraPar,botonDatosSalidaCamaraImpar]


	datosEntradaLabel = Label(frameFloculador, text="Datos iniciales: ",font=("Yu Gothic bold",10))
	caudalDiseñoLabel = Label(frameFloculador, text="QMD = Caudal de diseño [L/s]:",font=("Yu Gothic bold",10))
	tiempoFloculacionLabel = Label(frameFloculador, text="T = Tiempo de floculación [min]:",font=("Yu Gothic bold",10))
	diametroInterconexionLabel = Label(frameFloculador, text="D = Diámetro de interconexión [m]:",font=("Yu Gothic bold",10))
	diametroInternoLabel = Label(frameFloculador, text="Di = Diámetro interno 20\'\' [m]:",font=("Yu Gothic bold",10))
	diametroExternoLabel = Label(frameFloculador, text="Di = Diámetro externo 20\'\' [m]:",font=("Yu Gothic bold",10))
	anchoLabel = Label(frameFloculador, text="W = Ancho [m]:",font=("Yu Gothic bold",10))
	longitudLabel = Label(frameFloculador, text="L = Longitud [m]:",font=("Yu Gothic bold",10))
	alturaLabel = Label(frameFloculador, text="a = Altura [m]:",font=("Yu Gothic bold",10))
	densidadAguaLabel = Label(frameFloculador, text=u"\u03C1 = Densidad del agua [Kg/(m^3)]:",font=("Yu Gothic bold",10))
	viscocidadCinematicaLabel = Label(frameFloculador, text=u"\u03BC = Viscosidad Cinemática del agua [(m^2)/s]:",font=("Yu Gothic bold",10))
	gravedadLabel = Label(frameFloculador, text="g = Gravedad [m/(s^2)]",font=("Yu Gothic bold",10))
	temperaturaLabel = Label(frameFloculador, text="°C = Temperatura [°C]:",font=("Yu Gothic bold",10))
	coeficienteDescargaLabel = Label(frameFloculador, text="Cd = Coeficiente de descarga [K]",font=("Yu Gothic bold",10))
	coeficienteDescargaOrificiosLabel = Label(frameFloculador, text="Cd = Coeficiente de descarga Orificios [K]",font=("Yu Gothic bold",10))
	
	
	listaLabel = [datosEntradaLabel,caudalDiseñoLabel,tiempoFloculacionLabel,diametroInterconexionLabel,diametroInternoLabel,diametroExternoLabel,
				anchoLabel , longitudLabel,alturaLabel,densidadAguaLabel,viscocidadCinematicaLabel,gravedadLabel,temperaturaLabel,
				coeficienteDescargaLabel,coeficienteDescargaOrificiosLabel]

	caudalDiseño = Entry(frameFloculador)
	caudalDiseño.focus()
	tiempoFloculacion = Entry(frameFloculador)
	diametroInterconexion = Entry(frameFloculador)
	diametroInterno = Entry(frameFloculador)
	diametroExterno = Entry(frameFloculador)
	ancho = Entry(frameFloculador)
	longitud = Entry(frameFloculador)
	altura = Entry(frameFloculador)
	densidadAgua = Entry(frameFloculador)
	viscocidadCinematica = Entry(frameFloculador)
	gravedad = Entry(frameFloculador)
	gravedad.insert(0,9.81)
	temperatura = Entry(frameFloculador)
	coeficienteDescarga = Entry(frameFloculador)
	coeficienteDescargaOrificios = Entry(frameFloculador)
	

	listaEntry= [caudalDiseño,tiempoFloculacion,diametroInterconexion,diametroInterno,diametroExterno,
				ancho,longitud,altura,densidadAgua,viscocidadCinematica,gravedad,temperatura,
				coeficienteDescarga,coeficienteDescargaOrificios]


	
	control=0
	alturaInicial=70
	alturaInicial2=113
	for elemento in listaLabel:
		if control<8:
			elemento.place(x=20,y=alturaInicial)
			alturaInicial+=43
		else:
			elemento.place(x=450,y=alturaInicial2)
			alturaInicial2+=43
		control=control+1
	control=0
	alturaInicial=113
	alturaInicial2=113
	for elemento in listaEntry:
		if control<7:
			elemento.place(x=300,y=alturaInicial)
			alturaInicial+=43
		else:
			elemento.place(x=770,y=alturaInicial2)
			alturaInicial2+=43
		control=control+1
	xInicial=20
	xInicial2=20
	control=0
	for elemento in listaBotones:
		if control<2:
			elemento.place(x=xInicial ,y=alturaInicial2)
			xInicial+=500
		else:
			elemento.place(x=xInicial2 ,y=alturaInicial2+86)
			xInicial2+=500
		control+=1


	#Borrar
	listaValores=[57.26,20.00,0.39,0.45964,0.508,1.30,1.60,2.75,998.30,0.00000101,9.81,20.00,0.76,0.80]
	for i in range(0, len(listaValores)):
		if i == 9:
			pass
		else:
			listaEntry[i].insert(0, listaValores[i])

	floculadorWindow.mainloop()



mainWindow = Tk()
mainWindow.title("FlocSedFil")
mainWindow.iconbitmap(bitmap='icons\\agua.ico')
mainWindow.geometry("370x350")
#Anchoxalto
mainWindow.resizable(0,0)


frame = LabelFrame(mainWindow, text="Página principal")
frame.grid(row=0, column=0)

bg= PhotoImage(file="images\\fondo31.png")


my_canvas = Canvas(frame, width=370, height=350)
my_canvas.grid(row=0,column=0)
my_canvas.create_image(0,0, image=bg, anchor="nw")


#Label
my_canvas.create_text(175,20, text= "Seleccione una de las siguientes opciones:", font=("Courier",10), fill="white")

#Buttons

boton_sed= HoverButton(frame, text="Sedimentador alta tasa", activebackground="#9DC4AA", justify=CENTER, width=50, height=2, bg= "#09C5CE", font =("Courier",9), command= openSedWindow)
boton_sed_window = my_canvas.create_window(5,160, anchor= "nw", window=boton_sed)

boton_filtro= HoverButton(frame, text="Filtro rápido", activebackground="#9DC4AA", justify=CENTER, width=50, height=2, bg= "#09C5CE", font =("Courier",9), command=openFiltroWindow)
boton_filtro_window = my_canvas.create_window(5,210, anchor= "nw", window=boton_filtro)

boton_floc= HoverButton(frame, text="Floculador Alabama", activebackground="#9DC4AA", justify=CENTER, width=50, height=2, bg= "#09C5CE", font =("Courier",9), command=openFloculadorWindow)
boton_floc_window = my_canvas.create_window(5,110, anchor= "nw", window=boton_floc)


'''
5,110
5,160
5,210
#09C5CE
#9DC4AA
#83C740
#DECB3C
#CC9231
'''
mainWindow.mainloop()




from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import pandas as pd
from math import pi,sin,cos,tan,sqrt

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
contador2 = 0

def openSedWindow():

	def velocidadPromedioFlujo(listaEntrada):
		vuelta= (listaEntrada[6]/listaEntrada[4])*(sin(listaEntrada[10]) + (listaEntrada[7]/listaEntrada[5])*cos(listaEntrada[10]))
		return vuelta

	def velocidadPromedioFlujoCorregida(listaE):
		#¿Cuál es criterio de parada?
		#valorParada= velocidadPromedioFlujo(listaE)*(listaE[5]/listaE[3])
		v0=velocidadPromedioFlujo(listaE)
		v1= (listaE[6]/listaE[4])*(sin(listaE[10]) + ((listaE[7]/listaE[5]) - 0.058*v0*(listaE[5]/listaE[3]) )*cos(listaE[10]))
		bandera=1
		while(v1-v0 != 0):
			bandera=bandera+1
			v0=v1
			v1= (listaE[6]/listaE[4])*(sin(listaE[10]) + ((listaE[7]/listaE[5]) - 0.058*v0*(listaE[5]/listaE[3]) )*cos(listaE[10]))
			print(v1-v0)
			if bandera>100:
				break
		return v0

	def tiempoDeRetencionCanal(listaE):
		vuelta= (listaE[7]/velocidadPromedioFlujoCorregida(listaE))*(1/60)
		return vuelta

	def numeroCanalesModulo(listaE):
		vuelta= (listaE[2]/(listaE[9]*listaE[5]*velocidadPromedioFlujoCorregida(listaE)))
		return round(vuelta)

	def longitudOcupadaPlacas(listaE):
		valor= (listaE[7]*cos(listaE[10]))+ ((listaE[5]*numeroCanalesModulo(listaE) + (numeroCanalesModulo(listaE)+1)*listaE[8])/sin(listaE[10]))
		return valor
	def alturaPlacas(listaE):
		return listaE[7]*sin(listaE[10])

	def distanciaCanaletasRecoleccion(listaE):
		#¿Qué va aquí?
		return 1.5*listaE[11]

	def alturaDeSedimentacion(listaE):
		return listaE[12]+listaE[11]+ alturaPlacas(listaE)

	def volumenTanqueSedimentacion(listaE):
		return (alturaDeSedimentacion(listaE)*longitudOcupadaPlacas(listaE)*listaE[9]) - ((numeroCanalesModulo(listaE)+1)*listaE[7]*listaE[8]*listaE[9]) 

	def tiempoRetencionTotal(listaE):
		return volumenTanqueSedimentacion(listaE)*(1/60)*(1/listaE[2])

	def cargaSuperficial(listaE):
		return (listaE[2]*86400)/(longitudOcupadaPlacas(listaE)*listaE[9])

	def relacionLongitudAncho(listaE):
		return f"{round(longitudOcupadaPlacas(listaE)/listaE[9],1)}:1"

	def alturaTolvaLodos(listaE):
		return (listaE[9]- listaE[17])*(1/2)*tan(listaE[16])

	def largoTotalSed(listaE):
		return (2*listaE[15])+longitudOcupadaPlacas(listaE)

	def anchoTotalSed(listaE):
		return ((2*listaE[15]+listaE[9])*listaE[1])+ (listaE[1]-1)*listaE[14]

	def alturaTotalSed(listaE):
		return listaE[15]+alturaTolvaLodos(listaE)+ alturaPlacas(listaE)+ listaE[12]+listaE[11]+listaE[14]

	##Añadir
	def numeroCanaletasDeRecoleccion(listaE):
		return round(longitudOcupadaPlacas(listaE)/distanciaCanaletasRecoleccion(listaE))

	def distanciaEntreCanaletasAjust(listaE):
		return longitudOcupadaPlacas(listaE)/numeroCanaletasDeRecoleccion(listaE)

	def longitudDelMultipleDescarga(listaE):
		return longitudOcupadaPlacas(listaE)+listaE[15]

	def diametroNominalMult(listaE):
		try:
			m=longitudDelMultipleDescarga(listaE)
			if 2<=m<=3.5:
				valor=4
			elif 3.5<=m<=6.5:
				valor=6
			else:
				valor="No hay valor con los límites establecidos."
		except:
			valor="No hay valor con los límites establecidos."
		return valor 

	def diametroInternoMultiple(listaE):
		try:
			j=diametroNominalMult(listaE)
			if j==4:
				valor = 0.10342
			elif j==6:
				valor = 0.15222
			elif j==8:
				valor= 0.20942
			else:
				valor="No se encontró el valor del diámetro nominal del múltiple de descarga para el cálculo."
		except: valor="No se encontró el valor del diámetro nominal del múltiple de descarga para el cálculo."
		return valor

	def diametroInternoOrificios(listaE):
		try:
			return diametroInternoMultiple(listaE)*sqrt(0.4/listaE[18])
		except: 
			return "No se encontró el diámetro interno del múltiple de descarga en PVC Presión para el cálculo."
	def diametroNominalMasCercano(listaE):
		try:
			m=diametroInternoOrificios(listaE)
			if 0.02363<=m<=0.0302:
				valor=1
			elif m>=0.0302 and m<=0.03814:
				valor=1.25
			elif m>=0.03814 and m<=0.04368:
				valor=1.5
			elif m>=0.04368 and m<=0.05458:
				valor=2
			elif m<=0.05458 and m<=0.06607:
				valor=2.5
			elif m>=0.06607 and m<=0.08042:
				valor=3
			elif m>=0.08042 and m<= 0.10342:
				valor=4
			else:
				valor="No se encontró el diámetro interno de los orificios del múltiple de descarga para el cálculo."
		except:
			valor="No se encontró el diámetro interno de los orificios del múltiple de descarga para el cálculo."
		return valor

	def diametroInternoMultipleAjust(listaE):
		m= diametroNominalMasCercano
		if m==1:
			valor=0.0302
		elif m==1.25:
			valor=0.03814
		elif m==1.5:
			valor=0.04368
		elif m==2:
			valor=0.05458
		elif m==2.5:
			valor=0.06607
		elif m==3:
			valor=0.0842
		elif m==4:
			valor=0.10342
		else:
			valor="No se encontró el diametro Nominal más cercano de los orificios del múltiple de descarga para el cálculo."

		return valor

	def cuadroRelacionDiametroyMultiple(listaE):
		try:
			m= ((diametroInternoMultipleAjust(listaE)/diametroInternoMultiple(listaE))**2)*listaE[18]
		except:
			return "No se encontró el valor del diámetro nominal del múltiple de descarga ó el diámetro nominal más cercano de los orificios del múltiple de descarga para el cálculo."
		if m<0.4 or m>0.45:
			valor="El valor no se encuentra entre 0.40 y 0.45"
		else:
			valor=m
		return valor

	def diametroNominalMasCercanoAjust(listaE):
			return "Pendiente"
		
	def diametroInternoMultipleAjust2(listaE):
		return "Pendiente"

	def tiranteSobreOrificio(listaE):
		return alturaTolvaLodos(listaE)+listaE[11]+listaE[12]+alturaPlacas(listaE)

	def relacionLongitudMultipleNumOrificios(listaE):
		return longitudDelMultipleDescarga(listaE)/listaE[18]

	def separacionEntreOrificiosMult(listaE):
		return "Pendiente"
		
	def separacionEntreOrificiosMultConf(listaE):
		return longitudOcupadaPlacas(listaE)/listaE[18]



	listaSed=list()
	def calcularSed(lista_ent):
		lista_entry=[0]*20

		for entryID in range(0,len(lista_ent)):
			try:
				if entryID != 4:
					lista_entry[entryID]=(float(lista_ent[entryID].get()))
				else: 
					lista_entry[entryID]= lista_ent[entryID].get()
			except:
				messagebox.showwarning(message="El ingreso de datos es erróneo, vuelva a intentarlo", title= "¡Cuidado!")
				return None
		#Quitar
		lista_entry=[0.05726,4,0.01432,0.000001007,lista_ent[4].get(),0.05,23,1.2192,0.004,1.2192,60.00,0.60,0.60,0.30,0.20,0.30,55,0.10,10,0.01]
		#Quitar



		#Conversiones:
		lista_entry[6]= lista_entry[6]/86400
		lista_entry[10]= (lista_entry[10]*pi)/180
		lista_entry[16]= (lista_entry[16]*pi)/180	

		if lista_entry[4] == "Seleccione":
			messagebox.showwarning(message="Seleccione el tipo de placa")
			return None
		elif lista_entry[4] == "Placas paralelas":
			lista_entry[4] = 1
		elif lista_entry[4] == "Opcion 2":
			lista_entry[4] = 4				
				
		listaTemp=list()
		listaTemp.clear()
		
		#Todas los calculos.
		listaTemp.append(velocidadPromedioFlujo(lista_entry))
		listaTemp.append(velocidadPromedioFlujoCorregida(lista_entry))
		listaTemp.append(tiempoDeRetencionCanal(lista_entry))
		listaTemp.append(numeroCanalesModulo(lista_entry))
		listaTemp.append(longitudOcupadaPlacas(lista_entry))
		listaTemp.append(alturaPlacas(lista_entry))
		listaTemp.append(distanciaCanaletasRecoleccion(lista_entry))
		listaTemp.append(alturaDeSedimentacion(lista_entry))
		listaTemp.append(volumenTanqueSedimentacion(lista_entry))
		listaTemp.append(tiempoRetencionTotal(lista_entry))
		listaTemp.append(cargaSuperficial(lista_entry))
		listaTemp.append(relacionLongitudAncho(lista_entry))
		listaTemp.append(alturaTolvaLodos(lista_entry))
		listaTemp.append(largoTotalSed(lista_entry))
		listaTemp.append(anchoTotalSed(lista_entry))
		listaTemp.append(alturaTotalSed(lista_entry))		
		listaTemp.append(numeroCanaletasDeRecoleccion(lista_entry))
		listaTemp.append(distanciaEntreCanaletasAjust(lista_entry))
		listaTemp.append(longitudDelMultipleDescarga(lista_entry))
		listaTemp.append(diametroNominalMult(lista_entry))
		listaTemp.append(diametroInternoMultiple(lista_entry))
		listaTemp.append(diametroInternoOrificios(lista_entry))
		listaTemp.append(diametroNominalMasCercano(lista_entry))
		listaTemp.append(diametroInternoMultipleAjust(lista_entry))
		listaTemp.append(cuadroRelacionDiametroyMultiple(lista_entry))
		listaTemp.append(diametroNominalMasCercanoAjust(lista_entry))
		listaTemp.append(diametroInternoMultipleAjust2(lista_entry))
		listaTemp.append(tiranteSobreOrificio(lista_entry))
		listaTemp.append(relacionLongitudMultipleNumOrificios(lista_entry))
		listaTemp.append(separacionEntreOrificiosMult(lista_entry))
		listaTemp.append(separacionEntreOrificiosMultConf(lista_entry))
		
		
		
		
		listaTemp=lista_entry+listaTemp
		listaSed.append(listaTemp)
		

		newDataTreeview(arbolSed,listaTemp)
		
		
		
		df=pd.DataFrame(listaSed, columns=[
	"Caudal de diseño (QMD)[m^3/s]",
	"Número de módulos [und]",
	"Caudal por módulo [m^3/s]", 
	"Viscocidad cinemática [m^2/s]",
	"Eficiencia crítica para sedimentador de placas paralelas []",
	"Espacio entre placas [m]",
	"Velocidad de sedimentación crítica [m/s]",
	"Largo de la placa [m]",
	"Espesor de la placa [m]",
	"Ancho de la placa [m]",
	"Ángulo de inclinación de la placa [°]",
	"Nivel del agua sobre las palcas [m]",
	"Distancia vertical orificios de distribución a placas [m]",
	"Borde libre [m]",
	"Ancho interno de canales de distribución [m]",
	"Espesor de muros y placas de concreto [m]",
	"Pendiente transversal de la tolva de lodos [°]",
	"Longitud de la sección plana de la tolva de lodos [m]",
	"Número de orificios del múltiple de descarga por módulo [und]",
	"Velocidad mínima de arraste asignada [m/s]",
	"Velocidad promedio de flujo [m/s]", 
	"Velocidad promedio de flujo corregida [m/s]",
	"Tiempo de retención en cada canal [min]",
	"Número de canales por módulo [und]",
	"Longitud ocupada por las placas [m]", 
	"Altura de las placas [m]", 
	"Disancia entre las canaletas de recoleeción [m]",
	"Altura de sedimentación [m]",
	"Volumen de cada tanque de sedimentación [m^3]",
	"Tiempo de retención total en el tanque [min]",
	"Carga superficial [m^3/(m^2*día)]",
	"Relación longitud ancho de cada tanque [L:A]",
	"Altura de la tolva de lodos [m]",
	"Largo total del sedimentador [m]",
	"Ancho total del sedimentador [m]",
	"Altura total del sedimentador [m]",
	"Número de canaletas de recolección por módulo [und]",
	"Distancia entre canaletas de recolección(Ajsutado) [m]",
	"Longitud del múltiple de descarga [m]",
	"Diametro nominal del múltiple de descarga [pulg]",
	"Diamentro interno del múltiple de descarga en PVC presión [m]",
	"Diámetro interno de los orificos del múltiple de descarga [m]",
	"Diámetro nominal más cercano a los orificios del múltiple de descarga [pulg]",
	"Diámetro interno de los orificios del múltiple de descarga en PVC Presión (ajustado) [m]",
	"Cuadrado de la relación entre el diámetro de orificos y el del múltiple por el número de orificios []",
	"Diámetro nominal más cercano de los orificios del múltiple de descarga (ajustado) [pulg]",
	"Diámetro interno de los orificios del múltiple de descarga en PVC Presión (ajustado nuevamente) [m]",
	"Tirante sobre el orificio [m]",
	"Relación longitud del múltiple y número de orificios []",
	"Separación entre orificios del múltiple [m]",
	"Separación entre orificios del múltiple (confirmada) [m]"
	])
		df.to_excel("DatosSed_Clase.xlsx")
		
	


	def newDataTreeview(tree,listaS):
		global contador
		
		if contador%2 ==0:
			
			tree.insert("",END,text= f"{contador+1}", values=(listaS[20],listaS[21],listaS[22],listaS[23],listaS[24],listaS[25],listaS[26],listaS[27],listaS[28],listaS[29],listaS[30],listaS[31],listaS[32],listaS[33],listaS[34],listaS[35],listaS[36],listaS[37],listaS[38],listaS[39],listaS[40],listaS[41],listaS[42],listaS[43],listaS[44],listaS[45],listaS[46],listaS[47],listaS[48],listaS[49],listaS[50]),
			iid=contador, tags=("evenrow",))	
		else:	
			tree.insert("",END,text= f"{contador+1}", values=(listaS[20],listaS[21],listaS[22],listaS[23],listaS[24],listaS[25],listaS[26],listaS[27],listaS[28],listaS[29],listaS[30],listaS[31],listaS[32],listaS[33],listaS[34],listaS[35],listaS[36],listaS[37],listaS[38],listaS[39],listaS[40],listaS[41],listaS[42],listaS[43],listaS[44],listaS[45],listaS[46],listaS[47],listaS[48],listaS[49],listaS[50]),
				iid=contador, tags=("oddrow",))
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



	mainWindow.withdraw()
	sedWindow= tk.Toplevel()
	sedWindow.protocol("WM_DELETE_WINDOW", on_closing)
	sedWindow.iconbitmap(bitmap='icons\\agua.ico')
	sedWindow.geometry("1366x680") 
	sedWindow.resizable(1366,763)
	sedWindow.configure(background="#9DC4AA")

	##Panel:
	panel = ttk.Notebook(sedWindow)
	panel.pack(fill=BOTH, expand=TRUE)

	frameSed= LabelFrame(panel, text="Sedimentador de alta tasa")
	frameSed.pack(side=TOP,fill=BOTH,expand=True)
	panel.add(frameSed, text="Procedimiento clase")
	
	
	imageAtras= PhotoImage(file="images\\atras.png")
	#Botones.
	botonAtras= HoverButton(frameSed, image=imageAtras, width=100, height=40, bg= None, command=lambda: returnMainWindow(sedWindow))
	botonAtras.place(x=0,y=10)

	botonCalcular2 = HoverButton(frameSed, text="Calcular parámetros básicos de diseño", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularSed(lista_entradas))
	botonCalcular2.place(x=320,y=415)

	botonNewEntry2 = HoverButton(frameSed, text="Limpiar entradas", activebackground="#9DC4AA", width=20, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntrySed(lista_entradas, valueEfiCriticaName))
	botonNewEntry2.place(x=160,y=415)
	
	botonDeleteTabla2 = HoverButton(frameSed, text="Borrar tabla", activebackground="#9DC4AA", width=20, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: deleteSedTable(arbolSed))
	botonDeleteTabla2.place(x=0,y=415)

	#Input
	lista_inputs=["Caudal de diseño (QMD)[m^3/s]",
	"Número de módulos [und]",
	"Caudal por módulo [m^3/s]", 
	"Viscocidad cinemática [m^2/s]",
	"Eficiencia crítica para sedimentador de placas paralelas []",
	"Espacio entre placas [m]",
	"Velocidad de sedimentación crítica [m/s]",
	"Largo de la placa [m]",
	"Espesor de la placa [m]",
	"Ancho de la placa [m]",
	"Ángulo de inclinación de la placa [°]",
	"Nivel del agua sobre las palcas [m]",
	"Distancia vertical orificios de distribución a placas [m]",
	"Borde libre [m]",
	"Ancho interno de canales de distribución [m]",
	"Espesor de muros y placas de concreto [m]",
	"Pendiente transversal de la tolva de lodos [°]",
	"Longitud de la sección plana de la tolva de lodos [m]",
	"Número de orificios del múltiple de descarga por módulos [und]",
	"Velocidad mínima de arraste asignada [m/s]"
				]
	

	Label(frameSed, text="Pulse el encabezado de cada columna de la tabla para ver la fórmula del cálculo.",font=("Yu Gothic bold",10)).place(x=170, y=30)

	Label(frameSed, text="Datos de entrada para parámetros básicos: ",font=("Yu Gothic bold",10)).place(x=0, y=70)

	Label(frameSed, text="Q = Caudal de diseño (QMD)[m^3/s]: ", font =("Yu Gothic",9)).place(x=0 , y=106.25)
	caudalName = Entry(frameSed)
	caudalName.focus()
	caudalName.place(x=330 , y=106.25)
	
	Label(frameSed, text="m = Número de modulos [und]: ", font =("Yu Gothic",9)).place(x=0 , y=142.5)
	modulosName = Entry(frameSed)
	modulosName.place(x=330 , y=142.5)
	
	Label(frameSed, text="Q{} = Caudal por módulo [m^3/s]: ".format(getSub("mod")), font =("Yu Gothic",9)).place(x=0 , y=178.75)
	cModulosName = Entry(frameSed)
	cModulosName.place(x=330, y=178.75)
	
	Label(frameSed, text="V = Viscocidad cinemática [m^2/s]: ", font =("Yu Gothic",9)).place(x=0 , y=215)
	ViscocidadName = Entry(frameSed)
	ViscocidadName.place(x=330 , y=215)

	Label(frameSed, text="Tipo de placas (Cálculo de Eficiencia (S{})) []: ".format(getSub("c")), font =("Yu Gothic",9)).place(x=0 , y=251.25)
	valueEfiCriticaName= StringVar()
	valueEfiCriticaName.set("Seleccione")
	efiCriticaName = OptionMenu(frameSed, valueEfiCriticaName, "Placas paralelas", "Opcion 2")
	efiCriticaName.place(x=330 , y=251.25)
	
	Label(frameSed, text="{} = Espacio entre placas [m]: ".format(getSub("e")), font =("Yu Gothic",9)).place(x=0 , y=287.5)
	espacioPlacasName = Entry(frameSed)
	espacioPlacasName.place(x=330 , y=287.5)

	Label(frameSed, text= "V{} = Velocidad de sedimentación crítica [m/d]: ".format(getSub("sc")), font =("Yu Gothic",9)).place(x=0 , y=323.75)
	velocidadCriticaName = Entry(frameSed)
	velocidadCriticaName.place(x=330 , y=323.75)

	Label(frameSed, text="l = Largo de la placa [m]: ", font =("Yu Gothic",9)).place(x=0 , y=360)
	largoPlacaName = Entry(frameSed)
	largoPlacaName.place(x=330 , y=360)

	Label(frameSed, text=u"\u03C9 = Espesor de la placa [m]: ", font =("Yu Gothic",9)).place(x=470 , y=70)
	espesorPlacaName = Entry(frameSed)
	espesorPlacaName.place(x=800 , y=70)

	Label(frameSed, text="a = Ancho de la placa [m]: ", font =("Yu Gothic",9)).place(x=470, y=106.25)
	anchoPlacaName = Entry(frameSed)
	anchoPlacaName.place(x=800 , y=106.25)

	Label(frameSed, text=u"\u03B8 = Ángulo de inclinación de la placa [°]: ", font =("Yu Gothic",9)).place(x=470 , y=142.5)
	anguloInclinacionName = Entry(frameSed)
	anguloInclinacionName.place(x=800 , y=142.5)

	Label(frameSed, text="Otros datos para el dimensionamiento de la estructura: ",font=("Yu Gothic bold",10)).place(x=470, y=178.75)
	
	Label(frameSed, text="h{} = Nivel del agua sobre las palcas [m]: ".format(getSub("a")), font =("Yu Gothic",9)).place(x=470 , y=215)
	nivelAguaName = Entry(frameSed)
	nivelAguaName.place(x=800 , y=215)
	
	Label(frameSed, text="h{} = Distancia vertical orificios de distribución a placas [m]: ".format(getSub("e")), font =("Yu Gothic",9)).place(x=470 , y=251.25)
	distVerticalName = Entry(frameSed)
	distVerticalName.place(x=800 , y=251.25)

	Label(frameSed, text="bl = Borde libre [m]: ", font =("Yu Gothic",9)).place(x=470 , y=287.5)
	bordeLibreName = Entry(frameSed)
	bordeLibreName.place(x=800 , y=287.5)

	Label(frameSed, text="w{} = Ancho interno de canales de distribución [m]: ".format(getSub("d")), font =("Yu Gothic",9)).place(x=470 , y=323.75)
	anchoInternoName = Entry(frameSed)
	anchoInternoName.place(x=800 , y=323.75)

	Label(frameSed, text="e{} = Espesor de muros y placas de concreto [m]: ".format(getSub("c")), font =("Yu Gothic",9)).place(x=470 , y=360)
	espesorMurosName = Entry(frameSed)
	espesorMurosName.place(x=800 , y=360)

	Label(frameSed, text=u"\u03B1 = Pendiente transversal de la tolva de lodos [°]: ", font =("Yu Gothic",9)).place(x=930 , y=70)
	pendienteTransvName = Entry(frameSed)
	pendienteTransvName.place(x=1230 , y=70)

	Label(frameSed, text="p{} = Longitud de sección plana de la tolva de lodos [m]: ".format(getSub("c")), font =("Yu Gothic",8)).place(x=930, y=142.5)
	longSecName = Entry(frameSed)
	longSecName.place(x=1230 , y=142.5)

	Label(frameSed, text="Datos para el diseñor de la evacuación de lodos: ",font=("Yu Gothic bold",10)).place(x=930, y=215)

	Label(frameSed, text="n{}=Número orificios del múltiple de descarga por mod:".format(getSub("o")), font =("Yu Gothic",9)).place(x=930, y=287.5)
	numOrificios = Entry(frameSed)
	numOrificios.place(x=1240 , y=287.5)

	
	Label(frameSed, text="V{} = Velocidad mínima de arrastre asignada [m/s]".format(getSub("c")), font =("Yu Gothic",9)).place(x=930, y=360)
	velMinArrastre = Entry(frameSed)
	velMinArrastre.place(x=1230 , y=360)

	
	
	lista_entradas=[caudalName,
	modulosName,
	cModulosName,
	ViscocidadName,
	valueEfiCriticaName,
	espacioPlacasName,
	velocidadCriticaName,
	largoPlacaName,
	espesorPlacaName,
	anchoPlacaName,
	anguloInclinacionName,
	nivelAguaName,
	distVerticalName,
	bordeLibreName,
	anchoInternoName,
	espesorMurosName,
	pendienteTransvName,
	longSecName,
	numOrificios,
	velMinArrastre]

	
	
	#Style
	style = ttk.Style()
	#Pick a theme
	style.theme_use("clam")

	#Configure colors
	
	style.configure("Treeview",background="#9DC4AA", foreground="black", rowheight=20,fieldbackground="#9DC4AA")
	style.configure("Treeview.Heading", foreground="black", font =("Courier",9))
	#Change selected color
	style.map("Treeview", background=[("selected", "#09C5CE")])	 

	#Frame Treeview
	arbolSed_frame = Frame(frameSed)
	arbolSed_frame.pack(side=BOTTOM, fill=BOTH)
	
	#Scrollbar
	sedScrollX=Scrollbar(arbolSed_frame,orient=HORIZONTAL)
	sedScrollX.pack(side=BOTTOM, fill=X)
	sedScrollY=Scrollbar(arbolSed_frame,orient=VERTICAL)
	sedScrollY.pack(side=LEFT, fill=Y)


	#Treeview
	arbolSed= ttk.Treeview(arbolSed_frame,selectmode=BROWSE, height=6,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
	arbolSed.pack()

	sedScrollX.configure(command=arbolSed.xview)
	sedScrollY.configure(command=arbolSed.yview)
	#Define columnas.
	
	arbolSed["columns"]= ("Velocidad promedio de flujo [m/s]", 
	"Velocidad promedio de flujo corregida [m/s]",
	"Tiempo de retención en cada canal [min]",
	"Número de canales por módulo [und]",
	"Longitud ocupada por las placas [m]", 
	"Altura de las placas [m]", 
	"Disancia entre las canaletas de recoleeción [m]",
	"Altura de sedimentación [m]",
	"Volumen de cada tanque de sedimentación [m^3]",
	"Tiempo de retención total en el tanque [min]",
	"Carga superficial [m^3/(m^2*día)]",
	"Relación longitud ancho de cada tanque [L:A]",
	"Altura de la tolva de lodos [m]",
	"Largo total del sedimentador [m]",
	"Ancho total del sedimentador [m]",
	"Altura total del sedimentador [m]",
	"Número de canaletas de recolección por módulo [und]",
	"Distancia entre canaletas de recolección(Ajsutado) [m]",
	"Longitud del múltiple de descarga [m]",
	"Diametro nominal del múltiple de descarga [pulg]",
	"Diamentro interno del múltiple de descarga en PVC presión [m]",
	"Diámetro interno de los orificos del múltiple de descarga [m]",
	"Diámetro nominal más cercano a los orificios del múltiple de descarga [pulg]",
	"Diámetro interno de los orificios del múltiple de descarga en PVC Presión (ajustado) [m]",
	"Cuadrado de la relación entre el diámetro de orificos y el del múltiple por el número de orificios []",
	"Diámetro nominal más cercano de los orificios del múltiple de descarga (ajustado) [pulg]",
	"Diámetro interno de los orificios del múltiple de descarga PVC Presión (ajustado nuevamente)[m]",
	"Tirante sobre el orificio [m]",
	"Relación longitud del múltiple y número de orificios []",
	"Separación entre orificios del múltiple [m]",
	"Separación entre orificios del múltiple (confirmada) [m]"
	)
	
	#Headings
	arbolSed.heading("#0",text="ID", anchor=CENTER)
	
	for col in arbolSed["columns"]:
		arbolSed.heading(col, text=col,anchor=CENTER, command = lambda: formulaN("images\\Ecuacion_1.png"))

	
		
	for i in range(0,len(arbolSed["columns"])-1) :
			arbolSed.column(f"#{i}",width=300, stretch=False)	
	for i in [2,7,9,10,12,16]:
		arbolSed.column(f"#{i}",width=400, stretch=False)
	for i in [17,18,19,20,21,22,28]:
		arbolSed.column(f"#{i}",width=500, stretch=False)
	for i in [23,25,27]:
		arbolSed.column(f"#{i}",width=700, stretch=False)
		for i in [26,24,29]:
			arbolSed.column(f"#{i}",width=1000, stretch=False)
	arbolSed.column("#30",width=700, stretch=True)
	arbolSed.column("#0",width=100, stretch=False)

	#Striped row tags
	arbolSed.tag_configure("oddrow", background= "#23D95F")
	arbolSed.tag_configure("evenrow", background= "#9DC4AA")
	

	sedWindow.mainloop()

contador3=0
def openFiltroWindow():

	def newEntryFiltro(lista):
		global contador3
		for elemento in lista:
				elemento.delete(0, END)
		lista[5].insert(0, 9.806)

	def newDataTreeviewFH(tree,listaS):	
		if contador3%2 ==0:
			
			tree.insert("",END,text= f"{contador3+1}", values=(listaS[20],listaS[21],listaS[22],listaS[23],listaS[24],listaS[25],listaS[26],listaS[27],listaS[28],listaS[29],listaS[30],listaS[31],listaS[32],listaS[33],listaS[34],listaS[35],listaS[36],listaS[37],listaS[38],listaS[39],listaS[40],listaS[41],listaS[42],listaS[43],listaS[44],listaS[45],listaS[46],listaS[47],listaS[48],listaS[49],listaS[50]),
			iid=contador3, tags=("evenrow",))	
		else:	
			tree.insert("",END,text= f"{contador3+1}", values=(listaS[20],listaS[21],listaS[22],listaS[23],listaS[24],listaS[25],listaS[26],listaS[27],listaS[28],listaS[29],listaS[30],listaS[31],listaS[32],listaS[33],listaS[34],listaS[35],listaS[36],listaS[37],listaS[38],listaS[39],listaS[40],listaS[41],listaS[42],listaS[43],listaS[44],listaS[45],listaS[46],listaS[47],listaS[48],listaS[49],listaS[50]),
				iid=contador3, tags=("oddrow",))
		contador=contador3+1
	
	def deleteSedTable(arbol):
		global contador3
		m= arbol.get_children()	
		for j in m:
			arbol.delete(j)
		contador3=0

	def calcularFH(lista_ent):
		lista_entry=[0]*10

		for entryID in range(0,len(lista_ent)-1):
			try:
				lista_entry[entryID]=(float(lista_ent[entryID].get()))
			except:
				messagebox.showwarning(message="El ingreso de datos es erróneo, vuelva a intentarlo", title= "¡Cuidado!")
				return None
		
		fhWindow = tk.Toplevel()
		fhWindow.iconbitmap(bitmap='icons\\agua.ico')
		fhWindow.geometry("600x400") 
		fhWindow.resizable(0,0)
		fhWindow.configure(background="#9DC4AA")
		######################Treeview############################
		style = ttk.Style()
		style.theme_use("clam")

		#Configure colors
		style.configure("Treeview",background="#9DC4AA", foreground="black", rowheight=20,fieldbackground="#9DC4AA")
		style.configure("Treeview.Heading", foreground="black", font =("Courier",9))
		#Change selected color
		style.map("Treeview", background=[("selected", "#09C5CE")])	 

		#Frame Treeview
		arbolFH_frame = Frame(fhWindow)
		arbolFH_frame.pack(side=TOP, expand=True)

		#Scrollbar
		sedScrollX=Scrollbar(arbolFH_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolFH_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)


		#Treeview
		arbolFH= ttk.Treeview(arbolFH_frame,selectmode=BROWSE, height=6,show="tree headings",xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolFH.pack()

		sedScrollX.configure(command=arbolFH.xview)
		sedScrollY.configure(command=arbolFH.yview)
		#Define columnas.
		
		arbolFH["columns"]= (
		"Número de tamiz",
		"Área retenida (%)",
		"Tamaño de abertura del tamiz superior, d1(mm)",
		"Tamaño de abertura del tamiz inferior, d2(mm)",
		"Tamaño promedio geométrico",
		"Fair - Hatch"
		)
		
		#Headings
		arbolFH.heading("#0",text="ID", anchor=CENTER)
		
		for col in arbolFH["columns"]:
			arbolFH.heading(col, text=col,anchor=CENTER)

		for i in range(0,len(arbolFH["columns"])-1) :
				arbolFH.column(f"#{i}",width=300, stretch=False)	

				
		arbolFH.column("#6",width=700, stretch=True)
		arbolFH.column("#0",width=100, stretch=False)

		#Striped row tags
		arbolFH.tag_configure("oddrow", background= "#23D95F")
		arbolFH.tag_configure("evenrow", background= "#9DC4AA")




		######################FinTreeview#############################
		
		






	mainWindow.withdraw()
	filtroWindow = tk.Toplevel()
	filtroWindow.protocol("WM_DELETE_WINDOW", on_closing)
	filtroWindow.iconbitmap(bitmap='icons\\agua.ico')
	filtroWindow.geometry("800x600") 
	filtroWindow.resizable(0,0)
	filtroWindow.configure(background="#9DC4AA")

	#panelF = ttk.Notebook(filtroWindow)
	#panelF.pack(fill=BOTH, expand=TRUE)
	frameFiltro= LabelFrame(filtroWindow, text="Filtro rápido", font=("Courier", 11))
	frameFiltro.pack(side=LEFT,fill=BOTH,expand=TRUE)
	#panelF.add(frameFiltro, text="Filtro rápido")
	
	imageAtras= PhotoImage(file="images\\atras.png")
	#Botones. 

	botonAtras= HoverButton(frameFiltro, image=imageAtras , width=100, height=40, bg= None, command=lambda: returnMainWindow(filtroWindow))
	botonAtras.place(x=0,y=10)

	frameEnergia=Label(filtroWindow,borderwidth=3, relief="groove" ,text= "Estimación de las pérdidas de energía a\ntravés del lecho filtrante limpio: ",font=("Courier", 9), width=40, height=18, anchor=NW, justify=LEFT)
	frameEnergia.place(x=500, y=130)

	botonCalcularFH = HoverButton(frameEnergia, text="Fair - Hatch", activebackground="#9DC4AA", anchor=CENTER,width=38, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularFH(lista_entradas))
	botonCalcularFH.place(x=2,y=80)

	botonCalcularCK = HoverButton(frameEnergia, text="Carmen - Kozeny", activebackground="#9DC4AA", anchor=CENTER, width=38, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: print("Funciona"))
	botonCalcularCK.place(x=2,y=140)
	
	botonCalcularR = HoverButton(frameEnergia, text="Rose", activebackground="#9DC4AA", anchor=CENTER , width=38, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: print("Funciona"))
	botonCalcularR.place(x=2,y=200)

	botonCalcularCoefUnif = HoverButton(frameFiltro, text="Calcular coeficiente de uniformidad", activebackground="#9DC4AA", anchor=CENTER , width=38, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: print("Funciona"))
	botonCalcularCoefUnif.place(x=500,y=428)

	botonNewEntryFiltro = HoverButton(frameFiltro, text="Limpiar entradas", activebackground="#9DC4AA", anchor=CENTER , width=38, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltro(lista_entradas))
	botonNewEntryFiltro.place(x=500,y=500)

	#botonCalcular = HoverButton(frameEnergia, text="Rose", activebackground="#9DC4AA", anchor=CENTER , width=38, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: print("Funciona"))
	#botonCalcular.place(x=2,y=200)
	
	Label(frameFiltro, text="¿?",font=("Yu Gothic bold",10)).place(x=170, y=30)

	entradaLabel=Label(frameFiltro, text="Datos de entrada: ",font=("Yu Gothic bold",10))

	caudalLabel=Label(frameFiltro, text="Q = Caudal de diseño (QMD)[m^3/s]: ", font =("Yu Gothic",9))
	caudalName = Entry(frameFiltro)
	caudalName.focus()
	
	tasaFiltracionesLabel=Label(frameFiltro, text="V{} = Tasa de filtración [m/d]: ".format(getSub("f")), font =("Yu Gothic",9))
	tasaFiltracionName = Entry(frameFiltro)

	viscocidadCinematicaLabel= Label(frameFiltro, text="v = Viscocidad cinemática del agua [(m^2)/s]: ", font =("Yu Gothic",9))
	viscocidadCinematicaName = Entry(frameFiltro)

	caracaLabel=Label(frameFiltro, text="Características del lecho filtrante: ",font=("Yu Gothic bold",10))

	factorDeFormaLabel= Label(frameFiltro, text=u"\u03A6 = Factor de forma (Fair-Hatch y Carmen-Koenzy) []: ", font =("Yu Gothic",9))
	factorDeFormaName = Entry(frameFiltro)

	velocidadSupFiltracionLabel	= Label(frameFiltro, text="v{} = Velocidad superficial de filtación [m/h]: ".format(getSub("a")), font =("Yu Gothic",9))
	velocidadSupFiltracionName = Entry(frameFiltro)

	gravedadLabel = Label(frameFiltro, text="g = Gravedad [m/s^2]: ", font =("Yu Gothic",9))
	gravedadName = Entry(frameFiltro)

	profundidadLabel = Label(frameFiltro, text="L = Profundidad [m]: ", font =("Yu Gothic",9))
	profuncidadName = Entry(frameFiltro)

	PorosidadLabel= Label(frameFiltro, text=u"\u03B5 = Porosidad []: ", font =("Yu Gothic",9))
	PorosidadName = Entry(frameFiltro)

	constanteFiltracionLabel= Label(frameFiltro, text=u"\u03BA = Constante de filtración(Fair - Hatch) []:", font =("Yu Gothic",9))
	constanteFiltracionName = Entry(frameFiltro)

	factorEsfericidadLabel= Label(frameFiltro, text=u"\u04A8 = Factor de esfericidad(Rose) []: ", font =("Yu Gothic",9))
	factorEsfericidadName = Entry(frameFiltro)


	lista_labels=[entradaLabel, caudalLabel, tasaFiltracionesLabel,viscocidadCinematicaLabel,caracaLabel,factorDeFormaLabel,velocidadSupFiltracionLabel,gravedadLabel,profundidadLabel,PorosidadLabel,constanteFiltracionLabel,factorEsfericidadLabel]
	lista_entry=["noEntry", caudalName, tasaFiltracionName,viscocidadCinematicaName,"noEntry",factorDeFormaName,velocidadSupFiltracionName,gravedadName,profuncidadName,PorosidadName,constanteFiltracionName,factorEsfericidadName]
	lista_entradas=[caudalName, tasaFiltracionName,viscocidadCinematicaName,factorDeFormaName,velocidadSupFiltracionName,gravedadName,profuncidadName,PorosidadName,constanteFiltracionName,factorEsfericidadName]
	valorInitFrame= 70
	valorInitLabel= 70

	for name in lista_labels:
		valorInitFrame=valorInitFrame+ 35.8
		name.place(x=0, y= valorInitFrame )

	for name in lista_entry:
		if name == "noEntry":
			valorInitLabel=valorInitLabel+ 35.8
		else:
			valorInitLabel=valorInitLabel+ 35.8
			name.place(x=310, y= valorInitLabel)
	gravedadName.insert(0, 9.806)
	filtroWindow.mainloop()







mainWindow = Tk()
mainWindow.title("Diseño de plantas de potabilización")
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
boton_sed_window = my_canvas.create_window(5,110, anchor= "nw", window=boton_sed)

boton_filtro= HoverButton(frame, text="Filtro rápido", activebackground="#9DC4AA", justify=CENTER, width=50, height=2, bg= "#09C5CE", font =("Courier",9), command=openFiltroWindow)
boton_filtro_window = my_canvas.create_window(5,160, anchor= "nw", window=boton_filtro)

boton_floc= HoverButton(frame, text="Floculador Alabama", activebackground="#9DC4AA", justify=CENTER, width=50, height=2, bg= "#09C5CE", font =("Courier",9))
boton_floc_window = my_canvas.create_window(5,210, anchor= "nw", window=boton_floc)

'''
#09C5CE
#9DC4AA
#83C740
#DECB3C
#CC9231
'''
mainWindow.mainloop()




from msilib.schema import Font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
# from numpy import mat
import pandas as pd
from math import pi,sin,cos,tan,sqrt,log10
from functools import partial
import os,errno,sys,re
from os import mkdir
from os import path
import xlsxwriter


def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)


def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    # try:
    #     # PyInstaller creates a temp folder and stores path in _MEIPASS
    #     base_path = sys._MEIPASS
    # except Exception:
    base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




def PasarExcelDatos(ubicacionDoc,nombreHoja,listaEncabezados,anchoListaEncabezados, listaDatos, anchoListaDatos, listaUnidades, anchoListaUnidades,whetherAdicional,listaAdicional, anchoListaAdicional):
	try:
		
		if whetherAdicional == False:
			entradaExcel=dict()

			entradaExcel['Encabezado'] = listaEncabezados
			entradaExcel['Valor'] = listaDatos
			entradaExcel['Unidades'] = listaUnidades

			entradaExcelDataFrame = pd.DataFrame(data=entradaExcel)
			pathExcel=resource_path2(f'{ubicacionDoc}')
				
			writer = pd.ExcelWriter(pathExcel, engine='xlsxwriter')  
				
			entradaExcelDataFrame.to_excel(writer,sheet_name=nombreHoja,index=False,startcol=1,startrow=1)
			workbook = writer.book
			worksheet = writer.sheets[nombreHoja]
			worksheet.set_column('B:B',anchoListaEncabezados) 
			worksheet.set_column('C:C', anchoListaDatos) 
			worksheet.set_column('D:D', anchoListaUnidades) 
			writer.save()

		else:
			entradaExcel=dict()

			entradaExcel['Encabezado'] = listaEncabezados
			entradaExcel['Valor'] = listaDatos
			entradaExcel['Unidades'] = listaUnidades
			entradaExcel['Adicional'] = listaAdicional

			entradaExcelDataFrame = pd.DataFrame(data=entradaExcel)
			pathExcel=resource_path2(f'{ubicacionDoc}')

			writer = pd.ExcelWriter(pathExcel, engine='xlsxwriter')
			entradaExcelDataFrame.to_excel(writer,sheet_name=nombreHoja,index=False,startcol=1,startrow=1)
			workbook = writer.book
			worksheet = writer.sheets[nombreHoja]
			worksheet.set_column('B:B',anchoListaEncabezados) 
			worksheet.set_column('C:C', anchoListaDatos) 
			worksheet.set_column('D:D', anchoListaUnidades) 
			worksheet.set_column('E:E', anchoListaAdicional) 
			writer.save()
	except: 
		messagebox.showwarning(message=f"No fue posible crear el documento en la ubicaci??n {ubicacionDoc} porque est?? en uso. Ci??rrelo y vuelta a intentarlo", title= "Error")


def pasarTreeViewExcel(colsDatos,arbol,ruta):
	try:
		entradaExcel=dict()
		
		for i in range(0,len(arbol["columns"])):
			entradaExcel[arbol["columns"][i]] = colsDatos[i]

		entradaExcelDataFrame = pd.DataFrame(data=entradaExcel)
		pathExcel=resource_path2(f'{ruta}')
			
		writer = pd.ExcelWriter(pathExcel, engine='xlsxwriter')  
			
		entradaExcelDataFrame.to_excel(writer,sheet_name='Resultados',index=False,startcol=1,startrow=1)
		workbook = writer.book
		worksheet = writer.sheets['Resultados']
		worksheet.set_column('B:L',40) 
		writer.save()
	except: 
		messagebox.showwarning(message=f"No fue posible crear el documento en la ubicaci??n {ruta} porque est?? en uso. Ci??rrelo y vuelta a intentarlo", title= "Error")
		



os.makedirs("ResultadosFloculador", exist_ok=True)
os.makedirs("ResultadosSedimentador", exist_ok=True)
os.makedirs("ResultadosFiltro", exist_ok=True)

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


def proyectarImg(archivo,dim1,dim2):
		forWindow= tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		forWindow.iconbitmap(bitmap=path)
		forWindow.geometry(f"{dim1}x{dim2}") 
		forWindow.resizable(0,0)
		forWindow.configure(background="#9DC4AA")
		framefor=Frame(forWindow)
		framefor.pack(side=TOP, fill=BOTH, expand=True)
		path2=resource_path(archivo)
		ima= PhotoImage(file=path2)
		l=Label(framefor, image=ima)
		l.pack()
		forWindow.mainloop()


def getSuper(x): 
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "????????????????????????????????????????????????Q???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????"
    res = x.maketrans(''.join(normal), ''.join(super_s)) 
    return x.translate(res) 
  
def getSub(x): 
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "??????CD?????G???????????????????????????Q???????????????w??????Z?????????????????????????????????????????????????????????????????w??????????????????????????????????????????????????????"
    res = x.maketrans(''.join(normal), ''.join(sub_s)) 
    return x.translate(res) 


def returnMainWindow(window):
	window.withdraw()
	mainWindow.deiconify()

def destroyMainWindow():
	mainWindow.destroy()

def on_closing():
	if messagebox.askokcancel("Salir","??Desea salir?"):
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


	def newDataTreeview(tree,listaS):
		global contador
		
		if contador%2 ==0:
			
			tree.insert("",END,text= f"{contador+1}", values=listaS,
			iid=contador, tags=("evenrow"))	
		else:	
			tree.insert("",END,text= f"{contador+1}", values=listaS,
				iid=contador, tags=("oddrow"))
		contador=contador+1
		
		
	def newEntrySed(lista, lista2):
		j=0
		inicialesComboBox=["Seleccione la temperatura","Seleccione el tipo de floc","Seleccione el tipo de celda",
		"Seleccione el material del tipo de celda", "Seleccione las dimensiones del tipo de celda", "Seleccione el n??mero de unidades","Seleccione el di??metro nominal de los orificios del m??ltiple de descarga"]
		for i in range(0, len(lista)):
			if i==3 or i==4 or i==5 or i==6 or i==7 or i==9 or i==19:
				lista[i].set(inicialesComboBox[j])
				j=j+1
			else:
				lista[i].delete(0, END)
		
		listaReiLabels= ["??ngulo de inclinaci??n [??]:", "Distancia del tipo de celda [5cm - 6cm]:","Longitud del tipo de celda [2m - 12m]:",
		"Seleccione el material del tipo de celda:","Seleccione las dimensiones del tipo de celda [mm x mm]:"]		
		for m in range(0, len(lista2)):
			lista2[m].config(text = listaReiLabels[m], font=("Yu Gothic",8))
	


	def deleteSedTable(arbol):
		global contador
		m= arbol.get_children()	
		for j in m:
			arbol.delete(j)
		contador=0
	
	def datosEntradaParametrosBasicosCalculos(tipoFloc, tipoCelda, materialCelda, dimensiones, anguloInclinacion, numeroUnidades2,distanciaPlacas, caudalMD,factorMayoracionCMD, temperatura2):
			#ENTRANVALORESYAOBTENIDOS. CON get()
			numeroUnidades = float(numeroUnidades2)
			temperatura = float(temperatura2)
			oP2 = {
			"Placas planas paralelas": ("Acero inoxidable AISI 316","Polietileno alta densidad (HDPE)","Poliestireno de alto impacto(HIPS)") , 
			"Placas onduladas paralelas":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)"),
			"Conductos cuadrados":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)")}
			
			dimensionesLista= [	
			('1219 x 1219', '1219 x 2438', '1524 x 1524', '1524 x 3048'), 
			('1200 x 1200', '1200 x 1400', '1200 x 1600', '1200 x 1800', '1200 x 2000', '1200 x 2200', '1200 x 2400', '1200 x 2600', '1200 x 2800', '1200 x 3000'), 
			('1200 x 1200', '1200 x 1500', '1200 x 2400', '1200 x 3000'), 
			('1200 x 1200', '1200 x 1400', '1200 x 1600', '1200 x 1800', '1200 x 2000', '1200 x 2200', '1200 x 2400', '1200 x 2600', '1200 x 2800', '1200 x 3000'), 
			('1200 x 1200', '1200 x 1400', '1200 x 1600', '1200 x 1800', '1200 x 2000', '1200 x 2200', '1200 x 2400', '1200 x 2600', '1200 x 2800', '1200 x 3000'), 
			('1200 x 1500', '1200 x 2000', '1200 x 2500', '1200 x 3000'), 
			('1200 x 1500', '1200 x 2000', '1200 x 2500', '1200 x 3000')]

			combinacionesTipoCeldaMaterialDimension = list()

			i=0
			for elemento in tuple(oP2.keys()):
				for ele2 in oP2[elemento]:
					for dim in dimensionesLista[i]:
						combinacionesTipoCeldaMaterialDimension.append((elemento, ele2, dim))
					i=i+1

			espesorDic= dict()
			espesorLista= [
			4,
			4,
			4,
			5,
			8,
			8,
			8,
			8,
			8,
			8,
			8,
			8,
			8,
			8,
			3,
			5,
			3,
			5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,
			1.5,

			]





			for i in range(0, len(combinacionesTipoCeldaMaterialDimension)):
				espesorDic[combinacionesTipoCeldaMaterialDimension[i]]= espesorLista[i]

			espesor = espesorDic[tipoCelda, materialCelda, dimensiones]
			
			EficienciaCriticaLista=[1,1.3,1.375]
			eficienciaCriticaDic = dict()
			i=0
			for elemento in tuple(oP2.keys()):
				eficienciaCriticaDic[elemento]=EficienciaCriticaLista[i]
				i=i+1
			
			eficienciaCritica= eficienciaCriticaDic[tipoCelda]
			caudalDise??o = caudalMD*factorMayoracionCMD
			caudalUnidad = caudalDise??o/numeroUnidades

			
			valorTemperaturas=list()
			tablaTemperaturaViscocidadCinematica=dict()


			for i in range(0,36):    
				valorTemperaturas.append(i)
						
			valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
			,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
			1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

			for ind in range(0,len(valorTemperaturas)):
				tablaTemperaturaViscocidadCinematica[valorTemperaturas[ind]]=valorViscocidad[ind]
			
			viscosidadCinematica = tablaTemperaturaViscocidadCinematica[temperatura]
			
			listaSalida=[tipoFloc,tipoCelda,materialCelda, dimensiones,espesor,anguloInclinacion,eficienciaCritica, caudalDise??o, numeroUnidades,
			caudalUnidad,viscosidadCinematica,distanciaPlacas]

			return listaSalida
	
	def parametrosDeDise??oSedimentadorAltaTasa():
		
		parametrosDeDise??oSedimentadorAltaTasaWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		parametrosDeDise??oSedimentadorAltaTasaWindow.iconbitmap(bitmap=path)
		parametrosDeDise??oSedimentadorAltaTasaWindow.geometry("700x500") 
		parametrosDeDise??oSedimentadorAltaTasaWindow.resizable(0,0)	
		parametrosDeDise??oSedimentadorAltaTasaWindow.configure(background="#9DC4AA")

		parametrosDeDise??oSedimentadorAltaTasaFrame=LabelFrame(parametrosDeDise??oSedimentadorAltaTasaWindow, text="Par??metros de dise??o de sedimentador de alta tasa", font=("Yu Gothic bold", 11))
		parametrosDeDise??oSedimentadorAltaTasaFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolparametrosDeDise??oSedimentadorAltaTasa_frame = Frame(parametrosDeDise??oSedimentadorAltaTasaFrame)
		arbolparametrosDeDise??oSedimentadorAltaTasa_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		#sedScrollX=Scrollbar(arbolparametrosDeDise??oSedimentadorAltaTasa_frame,orient=HORIZONTAL)
		#sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolparametrosDeDise??oSedimentadorAltaTasa_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolparametrosDeDise??oSedimentadorAltaTasa= ttk.Treeview(arbolparametrosDeDise??oSedimentadorAltaTasa_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arbolparametrosDeDise??oSedimentadorAltaTasa.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arbolparametrosDeDise??oSedimentadorAltaTasa.xview)
		sedScrollY.configure(command=arbolparametrosDeDise??oSedimentadorAltaTasa.yview)
		#Define columnas.
		arbolparametrosDeDise??oSedimentadorAltaTasa["columns"]= (
		"1","Valores","Unidades")

		#Headings
		arbolparametrosDeDise??oSedimentadorAltaTasa.heading("#0",text="ID", anchor=CENTER)


		for col in arbolparametrosDeDise??oSedimentadorAltaTasa["columns"]:
			arbolparametrosDeDise??oSedimentadorAltaTasa.heading(col, text=col,anchor=CENTER)	

		
		arbolparametrosDeDise??oSedimentadorAltaTasa.column("#0",width=0, stretch=False)
		arbolparametrosDeDise??oSedimentadorAltaTasa.column("#1",width=450, stretch=False)	
		arbolparametrosDeDise??oSedimentadorAltaTasa.column("#2",width=100, stretch=False)	
		arbolparametrosDeDise??oSedimentadorAltaTasa.column("#3",width=150, stretch=False)	
		#Striped row tags
		arbolparametrosDeDise??oSedimentadorAltaTasa.tag_configure("evenrow", background= "#1FCCDB")
		arbolparametrosDeDise??oSedimentadorAltaTasa.tag_configure("oddrow", background= "#9DC4AA")






		encabezadosLista=["Carga superficial en placas angostas",
		"Carga superficial en placas profundas",
		"Velocidad de sedimentaci??n cr??tica para floc de alumbre",
		"Velocidad de sedimentaci??n cr??tica para floc de alumbre y polielectrolitos",
		"Tiempo de retenci??n en placas",
		"Tiempo de retenci??n en tubos",
		"Inclinaci??n de placas",
		"N??mero de Reynolds",
		"Tasa de rebose",
		"Distancia entre placas",
		"Profundidad",
		"Fracci??n del tanque a tasa acelerada"]

		listaparametrosDeDise??oSedimentadorAltaTasa =[ "120 - 185",
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
		"??",
		"",
		"L/s.m",
		"cm",
		"m",
		"%"
		]


		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listaparametrosDeDise??oSedimentadorAltaTasa[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolparametrosDeDise??oSedimentadorAltaTasa,listaTemp)

		PasarExcelDatos(".\\ResultadosSedimentador\\ParametrosDeDisenoSedimentadorAltaTasa.xlsx",'Resultados',encabezadosLista,80,listaparametrosDeDise??oSedimentadorAltaTasa , 15, unidadesLista, 15,False,[], 50)
		parametrosDeDise??oSedimentadorAltaTasaWindow.mainloop()

	def determinacionParametrosBasicosDiseno(listaDeterminacionParametrosBasicosDiseno, tipoCelda):
		#ManejoEntradasListaEntradaParametrosBasicos:
		


		'''
	listaEntradaParametrosBasicos=[tipoFloc = 0 ,tipoCelda = 1, materialTipoCelda =2 , dimensionesTipoCeldaMaterial =3 
	,anguloInclinacion =4
	,numeroUnidades =5,
	distanciaPlacas = 6, 
	caudalMedioEntry = 7, 
	factorMayoracionCaudalMD = 8,temperaturaEntry=  9]

	listaDeterminacionParametrosBasicosDiseno = listaEntradaParametrosBasicos + [longitudPlacas = 10]

	listaCanaletasRecoleccionAgua = [distanciaCanaletasRecoleccion,longitudPlacas]
	listaTiempoRetencionTotalTanque = listaDeterminacionParametrosBasicosDiseno + [distanciaVerticalDistribucionPlacas] + listaCanaletasRecoleccionAgua
	listaDimensionesDelSedimentador = listaTiempoRetencionTotalTanque + [bordeLibre,espesorMuros,pendienteTransversalTolva,anchoBasePlanaTolva] 
	listaDisenoSistemaEvacuacionLodos = listaDimensionesDelSedimentador + [velocidadMinimaArrastre,longitudPlacas, diametroNominalOrificionesMultipleDescarga]
		'''
		
		inicialesComboBox=["Seleccione el tipo de floc","Seleccione el tipo de celda",
		f"Seleccione el material de {tipoCelda}", f"Seleccione las dimensiones de {tipoCelda}", "Seleccione el n??mero de unidades","Seleccione la temperatura"]
		
		listaComboBox=[listaDeterminacionParametrosBasicosDiseno[0],listaDeterminacionParametrosBasicosDiseno[1],listaDeterminacionParametrosBasicosDiseno[2],
		listaDeterminacionParametrosBasicosDiseno[3],listaDeterminacionParametrosBasicosDiseno[5], listaDeterminacionParametrosBasicosDiseno[9]]
		listaSinComboBox=[listaDeterminacionParametrosBasicosDiseno[4],listaDeterminacionParametrosBasicosDiseno[6],
		listaDeterminacionParametrosBasicosDiseno[7],listaDeterminacionParametrosBasicosDiseno[8], listaDeterminacionParametrosBasicosDiseno[10]]

		parametrosCombobox=list()

		for i in range(0,len(listaComboBox)):
			if listaComboBox[i].get()[0:10] == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta seleccionar {inicialesComboBox[i][10:].lower()}")
				return None	
			else:
				parametrosCombobox.append(listaComboBox[i].get())
		#Verifica que no sean nulos.
		if tipoCelda == "Conductos cuadrados":
			labels=["??ngulo de inclinaci??n", "lado interno de los conductos","caudal medio diario",
			"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por los m??dulos"]
		else: 

			labels=["??ngulo de inclinaci??n", "distancia entre placas","caudal medio diario",
			"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por las placas"]
		
		
		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None

		try:
			if float(listaDeterminacionParametrosBasicosDiseno[4].get()) != 60.0  :
				messagebox.showwarning(title="Error", message="El valor del ??ngulo de inclinaci??n solo puede ser 60??")	
				return None
			elif float(listaDeterminacionParametrosBasicosDiseno[6].get())>6.0 or float(listaDeterminacionParametrosBasicosDiseno[6].get())<5.0:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message=f"El valor del lado interno de los conductos cuadrados no puede ser menor que 5 ni mayor que 6.")	
					return None
				else: 
					messagebox.showwarning(title="Error", message=f"El valor de la distancia entre placas no puede ser menor que 5 ni mayor que 6.")	
					return None
			elif float(listaDeterminacionParametrosBasicosDiseno[7].get())<0.01 or float(listaDeterminacionParametrosBasicosDiseno[7].get())>0.2:
				messagebox.showwarning(title="Error", message="El valor del caudal medio diario debe estar entre 0.01 y 0.2")	
				return None
			elif float(listaDeterminacionParametrosBasicosDiseno[8].get())>1.3 or float(listaDeterminacionParametrosBasicosDiseno[8].get())<1:
				messagebox.showwarning(title="Error", message="El valor de factoraci??n de mayoraci??n del caudal m??ximo diario debe estar entre 1 y 1.3")	
				return None
			elif float(listaDeterminacionParametrosBasicosDiseno[10].get())<2 or float(listaDeterminacionParametrosBasicosDiseno[10].get())>12:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message="La longitud ocupada por los m??dulos no puede ser menor que 2 ni mayor a 12")	
					return None
				else:
					messagebox.showwarning(title="Error", message="La longitud ocupada por las placas no puede ser menor que 2 ni mayor a 12")	
					return None
		except:
			messagebox.showwarning(title="Error", message="Alguno de los datos ingresados no es un n??mero.")
			return None	

		anguloInclinacion = float(listaDeterminacionParametrosBasicosDiseno[4].get())
		distanciaPlacas = float(listaDeterminacionParametrosBasicosDiseno[6].get())
		caudalMedio = float(listaDeterminacionParametrosBasicosDiseno[7].get())
		factorMayoracionCaudalMD = float(listaDeterminacionParametrosBasicosDiseno[8].get())
		longitudPlacas = float(listaDeterminacionParametrosBasicosDiseno[10].get())

		tipoFloc = parametrosCombobox[0]
		tipoCelda = parametrosCombobox[1]
		materialTipoCelda = parametrosCombobox[2]
		dimensionesTipoCeldaMaterial = parametrosCombobox[3]
		numeroUnidades = parametrosCombobox[4]
		temperatura=  parametrosCombobox[5]
		
		
		
		

		
		determinacionParametrosBasicosDisenoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		determinacionParametrosBasicosDisenoWindow.iconbitmap(bitmap=path)
		determinacionParametrosBasicosDisenoWindow.geometry("620x420") 
		determinacionParametrosBasicosDisenoWindow.resizable(0,0)	
		determinacionParametrosBasicosDisenoWindow.configure(background="#9DC4AA")

		determinacionParametrosBasicosDisenoFrame=LabelFrame(determinacionParametrosBasicosDisenoWindow, text="Determinaci??n de par??metro b??sicos de dise??o", font=("Yu Gothic bold", 11))
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
		arboldeterminacionParametrosBasicosDiseno= ttk.Treeview(arboldeterminacionParametrosBasicosDiseno_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set, xscrollcommand=sedScrollX.set)
		arboldeterminacionParametrosBasicosDiseno.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arboldeterminacionParametrosBasicosDiseno.xview)
		sedScrollY.configure(command=arboldeterminacionParametrosBasicosDiseno.yview)
		#Define columnas.
		arboldeterminacionParametrosBasicosDiseno["columns"]= (
		"Presione para ver Excel","Valores","Unidades","Adicionales")
		
		

		#Headings
		arboldeterminacionParametrosBasicosDiseno.heading("#0",text="ID", anchor=CENTER)


		
		
		for col in arboldeterminacionParametrosBasicosDiseno["columns"]:
			arboldeterminacionParametrosBasicosDiseno.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg('images\\Sed_DeterminacionParametrosBasicosDiseno.png',781,439) )	

		arboldeterminacionParametrosBasicosDiseno.column("#1",width=400, stretch=False)
		arboldeterminacionParametrosBasicosDiseno.column("#2",width=100, stretch=False)
		arboldeterminacionParametrosBasicosDiseno.column("#3",width=100, stretch=False)
		arboldeterminacionParametrosBasicosDiseno.column("#4",width=270, stretch=False)


		arboldeterminacionParametrosBasicosDiseno.column("#0",width=0, stretch=False)
		
		

		#Striped row tags
		arboldeterminacionParametrosBasicosDiseno.tag_configure("evenrow", background= "#1FCCDB")
		arboldeterminacionParametrosBasicosDiseno.tag_configure("oddrow", background= "#9DC4AA")


		listadeterminacionParametrosBasicosDiseno=list()


		if tipoCelda == "Conductos cuadrados":
			encabezadosLista=["Longitud ocupada por los m??dulos (longitud de tanque)",
				"Ancho de m??dulos (ancho de tanque)",
				"Largo de placa (en el sentido del flujo)",
				"Carga superficial",			
				"N??mero de conductos a lo largo de la unidad",
				"Velocidad promedio del flujo entre conductos",			
				"Longitud relativa del sedimentador",
				"Longitud relativa para la regi??n de transici??n",
				"Longitud relativa para la regi??n de transici??n corregida",
				"Velocidad de sedimentaci??n cr??tica ",
				"N??mero de Reynolds",
				"Tiempo de retenci??n en cada conducto"]

		else:
			encabezadosLista=["Longitud ocupada por las placas (longitud de tanque)",
				"Ancho de placas (ancho de tanque)",
				"Largo de placa (en el sentido del flujo)",
				"Carga superficial",			
				"N??mero de canales a lo largo de la unidad",
				"Velocidad promedio del flujo entre placas",			
				"Longitud relativa del sedimentador",
				"Longitud relativa para la regi??n de transici??n",
				"Longitud relativa para la regi??n de transici??n corregida",
				"Velocidad de sedimentaci??n cr??tica ",
				"N??mero de Reynolds",
				"Tiempo de retenci??n en cada canal"]
		unidadesLista=["m",
						"m",
						"m",
						"m^3/m^2/d??a",
						"und",
						"m/s",
						"",
						"",
						"",
						"m/d",
						"",
						"min"]
		
		
		listaSalidaDatosEntradaPrametrosBasicosCalculos = datosEntradaParametrosBasicosCalculos(tipoFloc, tipoCelda, materialTipoCelda, dimensionesTipoCeldaMaterial, anguloInclinacion, numeroUnidades,distanciaPlacas, caudalMedio,factorMayoracionCaudalMD, temperatura)
		# listaSalida=[0 = tipoFloc,1 = tipoCelda,
		# 2= materialCelda, 3= dimensiones,
		# 4= espesor,5= anguloInclinacion,6= eficienciaCritica, 
		# 7=caudalDise??o, 8=numeroUnidades,
		# 9= caudalUnidad,10=viscosidadCinematica,11=distanciaPlacas]

		

		listadeterminacionParametrosBasicosDiseno.append(round(longitudPlacas,3))
		anchoModulos=float(dimensionesTipoCeldaMaterial[dimensionesTipoCeldaMaterial.find('x')+2:])/1000.0
		listadeterminacionParametrosBasicosDiseno.append(round(anchoModulos,3))
		largoPlaca = float(dimensionesTipoCeldaMaterial[:dimensionesTipoCeldaMaterial.find('x')-1])/1000.0
		listadeterminacionParametrosBasicosDiseno.append(round(largoPlaca,3))
		cargaSuperficial = (listaSalidaDatosEntradaPrametrosBasicosCalculos[9]*86400.0)/(longitudPlacas*anchoModulos)
		listadeterminacionParametrosBasicosDiseno.append(round(cargaSuperficial,3))
		numeroConductosLargoUnidad= round(((longitudPlacas*sin(anguloInclinacion*(pi/180.0))) + (listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0))/((listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)+(listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0)),0)
		listadeterminacionParametrosBasicosDiseno.append(round(numeroConductosLargoUnidad,0))
		velocidadPromedioFlujoConductos = listaSalidaDatosEntradaPrametrosBasicosCalculos[9]/((numeroConductosLargoUnidad)*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)*(anchoModulos))
		
		listadeterminacionParametrosBasicosDiseno.append(round(velocidadPromedioFlujoConductos,4))
		longitudRelativaSedimentador =  largoPlaca/(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)
		listadeterminacionParametrosBasicosDiseno.append(round(longitudRelativaSedimentador,3))
		longitudRelativaRegionTransicion = (0.058*velocidadPromedioFlujoConductos*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0))/listaSalidaDatosEntradaPrametrosBasicosCalculos[10]
		
		listadeterminacionParametrosBasicosDiseno.append(round(longitudRelativaRegionTransicion,3))
		
		if longitudRelativaRegionTransicion<longitudRelativaSedimentador:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador-longitudRelativaRegionTransicion
		else:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador

		listadeterminacionParametrosBasicosDiseno.append(round(longitudRelativaRegionTransicionCorregida,2))
	
		velocidadSedimentacionCritica = ((listaSalidaDatosEntradaPrametrosBasicosCalculos[6])*(velocidadPromedioFlujoConductos*86400.0))/((sin(anguloInclinacion*pi*(1/180.0)))+(longitudRelativaRegionTransicionCorregida*cos(anguloInclinacion*pi*(1/180.0))))
		
		listadeterminacionParametrosBasicosDiseno.append(round(velocidadSedimentacionCritica,3))
		numeroReynolds = round(velocidadPromedioFlujoConductos*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100)*(1/listaSalidaDatosEntradaPrametrosBasicosCalculos[10]) ,0)
		listadeterminacionParametrosBasicosDiseno.append(numeroReynolds)
		tiempoRetencionCadaConjunto = (largoPlaca/velocidadPromedioFlujoConductos)/60.0
		listadeterminacionParametrosBasicosDiseno.append(round(tiempoRetencionCadaConjunto,3))

		if cargaSuperficial<120.0:
			revisaCargaSuperficial= "??Carga superficial baja,seleccione otra\nlongitud de tanque y/u otro n??mero de m??dulos!"
		elif cargaSuperficial>185.0:
			revisaCargaSuperficial= "??Carga superficial alta, seleccione otra\nlongitud de tanque y/u otro n??mero de m??dulos!"
		else:
			revisaCargaSuperficial= "Carga superficial dentro del rango aceptado"

		if velocidadPromedioFlujoConductos<0.002:
			revisaVelPromedioFlujo= "La velocidad promedio del flujo entre\n conductos es baja, ajuste datos de entrada"
		elif velocidadPromedioFlujoConductos>0.0025:
			revisaVelPromedioFlujo= "La velocidad promedio del flujo entre\n conductos es alta, ajuste datos de entrada"
		else:
			revisaVelPromedioFlujo= "La velocidad promedio del flujo entre\n conductos es adecuada"

		if longitudRelativaRegionTransicion>longitudRelativaRegionTransicionCorregida:
			revisaLongitudRelativaRegionTransicion="Aumente el valor de la longitud\n del sedimentador a un valor aproximado de 2??Lc??e"
		else: 
			revisaLongitudRelativaRegionTransicion="??Ok!"
		
		if tipoFloc == "Floc de alumbre":
			if velocidadSedimentacionCritica<12.0:
				revisaVelocidadSedimentacionCritica="La velocidad de sedimentaci??n cr??tica es baja,\n??Ajuste datos de entrada!"
			elif velocidadSedimentacionCritica>23.0:
				revisaVelocidadSedimentacionCritica="La velocidad de sedimentaci??n cr??tica es alta,\n??Ajuste datos de entrada!"
			else:
				revisaVelocidadSedimentacionCritica="La velocidad de sedimentaci??n cr??tica es\n adecuada."
		else:
			if velocidadSedimentacionCritica<16.0:
				revisaVelocidadSedimentacionCritica="La velocidad de sedimentaci??n cr??tica es baja,\n ??Ajuste datos de entrada!"
			elif velocidadSedimentacionCritica>29.0:
				revisaVelocidadSedimentacionCritica="La velocidad de sedimentaci??n cr??tica es alta,\n??Ajuste datos de entrada!"
			else:
				revisaVelocidadSedimentacionCritica="La velocidad de sedimentaci??n cr??tica es\n adecuada."
		if numeroReynolds<100.0:
			revisaNumeroReynolds="El valor del n??mero de Reynolds es bajo,\najuste los datos de entrada."
		else:
			revisaNumeroReynolds="El valor del n??mero de Reynolds es\nadecuado."
		if tipoCelda == "Conductos cuadrados":
			if tiempoRetencionCadaConjunto<6.0:
				revisaTiempoRetencion="El tiempo de retenci??n es bajo, ajuste datos\n de entrada!"
			elif tiempoRetencionCadaConjunto>10.0:
				revisaTiempoRetencion="El tiempo de retenci??n es alto, ajuste datos\n de entrada!"
			else:
				revisaTiempoRetencion="El tiempo de retenci??n es adecuado."
		else:
			if tiempoRetencionCadaConjunto<10.0:
				revisaTiempoRetencion="El tiempo de retenci??n es bajo, ajuste datos de entrada!"
			elif tiempoRetencionCadaConjunto>15.0:
				revisaTiempoRetencion="El tiempo de retenci??n es alto, ajuste datos de entrada!"
			else:
				revisaTiempoRetencion="El tiempo de retenci??n es adecuado."		


		

		listaAdicionales=[
			"",
			"",
			"",	
			revisaCargaSuperficial,
			"",
			revisaVelPromedioFlujo,
			"",
			"",
			revisaLongitudRelativaRegionTransicion, 
			revisaVelocidadSedimentacionCritica,	
		revisaNumeroReynolds, revisaTiempoRetencion]



		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listadeterminacionParametrosBasicosDiseno[i])
			listaTemp.append(unidadesLista[i])
			listaTemp.append(listaAdicionales[i])
			newDataTreeview(arboldeterminacionParametrosBasicosDiseno,listaTemp)
		
		PasarExcelDatos(".\\ResultadosSedimentador\\DeterminacionParametrosBasicosDiseno.xlsx",'Resultados',encabezadosLista,50, listadeterminacionParametrosBasicosDiseno, 15, unidadesLista, 15,False,listaAdicionales, 50)
		determinacionParametrosBasicosDisenoWindow.mainloop()
		

	def canaletasRecoleccionAgua(listaCanaletasRecoleccionAgua, tipoCelda):
		#ManejoEntradasCanaletasRecoleccionAgua
	

		if tipoCelda == "Seleccione el tipo de celda":
			messagebox.showwarning(title="Error", message=f"Hace falta seleccionar el tipo de celda")
			return None	

		#Verifica que no sean nulos.
		if tipoCelda == "Conductos cuadrados":
			labels=[ "distancia entre canaletas de recolecci??n","longitud ocupada por los m??dulos"]
		else: 
			labels=[ "distancia entre canaletas de recolecci??n","longitud ocupada por las placas"]

		for i in range(0, len(listaCanaletasRecoleccionAgua)):
			if listaCanaletasRecoleccionAgua[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor de la {labels[i]} ")	
				return None

		try:
			if float(listaCanaletasRecoleccionAgua[0].get())<0.9 or float(listaCanaletasRecoleccionAgua[0].get())>1.2:
				messagebox.showwarning(title="Error", message="La distancia entre canaletas de recolecci??n debe estar entre 0.9 y 1.2")	
				return None

			elif float(listaCanaletasRecoleccionAgua[1].get())<2 or float(listaCanaletasRecoleccionAgua[1].get())>12:
					if tipoCelda == "Conductos cuadrados":
						messagebox.showwarning(title="Error", message="La longitud ocupada por los m??dulos no puede ser menor que 2 ni mayor a 12")	
						return None
					else:
						messagebox.showwarning(title="Error", message="La longitud ocupada por las placas no puede ser menor que 2 ni mayor a 12")	
						return None
			else:
				distanciaCanaletasRecoleccion= float(listaCanaletasRecoleccionAgua[0].get())
				longitudPlacas = float(listaCanaletasRecoleccionAgua[1].get())
		except:
			messagebox.showwarning(title="Error", message="Alguno de los datos ingresados no es un n??mero.")
			return None	


		''' 
	listaCanaletasRecoleccionAgua = [distanciaCanaletasRecoleccion,longitudPlacas]

		'''
		canaletasRecoleccionAguaWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		canaletasRecoleccionAguaWindow.iconbitmap(bitmap=path)
		canaletasRecoleccionAguaWindow.geometry("500x180") 
		canaletasRecoleccionAguaWindow.resizable(0,0)	
		canaletasRecoleccionAguaWindow.configure(background="#9DC4AA")

		canaletasRecoleccionAguaFrame=LabelFrame(canaletasRecoleccionAguaWindow, text="Canaletas de recolecci??n de agua clarificada", font=("Yu Gothic bold", 11))
		canaletasRecoleccionAguaFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolcanaletasRecoleccionAgua_frame = Frame(canaletasRecoleccionAguaFrame)
		arbolcanaletasRecoleccionAgua_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolcanaletasRecoleccionAgua_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolcanaletasRecoleccionAgua_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolcanaletasRecoleccionAgua= ttk.Treeview(arbolcanaletasRecoleccionAgua_frame,selectmode=BROWSE, height=11,show="tree headings") #,yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arbolcanaletasRecoleccionAgua.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arbolcanaletasRecoleccionAgua.xview)
		#sedScrollY.configure(command=arbolcanaletasRecoleccionAgua.yview)
		#Define columnas.
		arbolcanaletasRecoleccionAgua["columns"]= (
		"Presione para ver excel","Valores","Unidades")

		#Headings
		arbolcanaletasRecoleccionAgua.heading("#0",text="ID", anchor=CENTER)


		

		for col in arbolcanaletasRecoleccionAgua["columns"]:
			arbolcanaletasRecoleccionAgua.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg("images\\Sed_CanaletasDeRecoleccion.png",780,125) )	
		
		
		arbolcanaletasRecoleccionAgua.column("#0",width=0, stretch=False)
		arbolcanaletasRecoleccionAgua.column("#1",width=300, stretch=False)
		arbolcanaletasRecoleccionAgua.column("#2",width=100, stretch=False)
		arbolcanaletasRecoleccionAgua.column("#3",width=100, stretch=False)
		


		#Striped row tags
		arbolcanaletasRecoleccionAgua.tag_configure("evenrow", background= "#1FCCDB")
		arbolcanaletasRecoleccionAgua.tag_configure("oddrow", background= "#9DC4AA")

		listacanaletasRecoleccionAgua=list()

		encabezadosLista=["Distancia entre canaletas de recolecci??n",
		"N??mero de canaletas de recolecci??n por m??dulo",
		"Distancia entre canaletas de recolecci??n (ajustado)"]
		unidadesLista=["m","und","m"]


		
		listacanaletasRecoleccionAgua.append(round(distanciaCanaletasRecoleccion,3))
		
		numeroCanaletasRecoleccionModulo= int(longitudPlacas/distanciaCanaletasRecoleccion)
		
		listacanaletasRecoleccionAgua.append(numeroCanaletasRecoleccionModulo)

		distanciaCanaletasRecoleccionAjustado = longitudPlacas/numeroCanaletasRecoleccionModulo
		
		listacanaletasRecoleccionAgua.append(round(distanciaCanaletasRecoleccionAjustado,3))
		
		
		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listacanaletasRecoleccionAgua[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolcanaletasRecoleccionAgua,listaTemp)
		PasarExcelDatos(".\\ResultadosSedimentador\\CanaletasRecoleccionAguaClarificada.xlsx",'Resultados',encabezadosLista,50, listacanaletasRecoleccionAgua, 15, unidadesLista, 15,False,[], 50)
		canaletasRecoleccionAguaWindow.mainloop()


	def tiempoRetencionTotalTanque(listaTiempoRetencionTotalTanque, tipoCelda):
		#manejoErroresTiempoRetencionTotalTanque
		'''
			listaEntradaParametrosBasicos=[0= tipoFloc, 1= tipoCelda, 2= materialTipoCelda, 3= dimensionesTipoCeldaMaterial,
			4= anguloInclinacion, 5= numeroUnidades,
			6=distanciaPlacas, 7= caudalMedioEntry, 8= factorMayoracionCaudalMD, 9= temperaturaEntry]
			listaDeterminacionParametrosBasicosDiseno() = listaEntradaParametrosBasicos + [10 = longitudPlacas] 
			listaCanaletasRecoleccionAgua = [distanciaCanaletasRecoleccion,longitudPlacas]
			listaTiempoRetencionTotalTanque = listaDeterminacionParametrosBasicosDiseno + [11 = distanciaVerticalDistribucionPlacas] + 12=distanciaCanaletasRecoleccion
		'''
		
		inicialesComboBox=["Seleccione el tipo de floc","Seleccione el tipo de celda",
		f"Seleccione el material de {tipoCelda}", f"Seleccione las dimensiones de {tipoCelda}", "Seleccione el n??mero de unidades","Seleccione la temperatura"]
		
		listaComboBox=[listaTiempoRetencionTotalTanque[0],listaTiempoRetencionTotalTanque[1],listaTiempoRetencionTotalTanque[2],
		listaTiempoRetencionTotalTanque[3],listaTiempoRetencionTotalTanque[5], listaTiempoRetencionTotalTanque[9]]

		listaSinComboBox=[listaTiempoRetencionTotalTanque[4],listaTiempoRetencionTotalTanque[6],
		listaTiempoRetencionTotalTanque[7],listaTiempoRetencionTotalTanque[8], listaTiempoRetencionTotalTanque[10], 
		listaTiempoRetencionTotalTanque[11], listaTiempoRetencionTotalTanque[12]]

		parametrosCombobox=list()

		for i in range(0,len(listaComboBox)):
			if listaComboBox[i].get()[0:10] == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta seleccionar {inicialesComboBox[i][10:].lower()}")
				return None	
			else:
				parametrosCombobox.append(listaComboBox[i].get())
		#Verifica que no sean nulos.

		if tipoCelda == "Conductos cuadrados":
			labels=["??ngulo de inclinaci??n", "lado interno de los conductos","caudal medio diario",
				"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por los m??dulos", 
				"distancia vertical de los orificios de distribuci??n a placas" 
				,"distancia entre canaletas de recolecci??n"]
		else: 

			labels=["??ngulo de inclinaci??n", "distancia entre placas","caudal medio diario",
			"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por las placas",
			"distancia vertical de los orificios de distribuci??n a placas","distancia entre canaletas de recolecci??n"]

		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None

		try:
			if float(listaTiempoRetencionTotalTanque[4].get()) != 60.0  :
				messagebox.showwarning(title="Error", message="El valor del ??ngulo de inclinaci??n solo puede ser 60??")	
				return None
			elif float(listaTiempoRetencionTotalTanque[6].get())>6.0 or float(listaTiempoRetencionTotalTanque[6].get())<5.0:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message=f"El valor del lado interno de los conductos cuadrados no puede ser menor que 5 ni mayor que 6.")	
					return None
				else: 
					messagebox.showwarning(title="Error", message=f"El valor de la distancia entre placas no puede ser menor que 5 ni mayor que 6.")	
					return None
			elif float(listaTiempoRetencionTotalTanque[7].get())<0.01 or float(listaTiempoRetencionTotalTanque[7].get())>0.2:
				messagebox.showwarning(title="Error", message="El valor del caudal medio diario debe estar entre 0.01 y 0.2")	
				return None
			elif float(listaTiempoRetencionTotalTanque[8].get())>1.3 or float(listaTiempoRetencionTotalTanque[8].get())<1:
				messagebox.showwarning(title="Error", message="El valor de factoraci??n de mayoraci??n del caudal m??ximo diario debe estar entre 1 y 1.3")	
				return None
			elif float(listaTiempoRetencionTotalTanque[10].get())<2 or float(listaTiempoRetencionTotalTanque[10].get())>12:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message="La longitud ocupada por los m??dulos no puede ser menor que 2 ni mayor a 12")	
					return None
				else:
					messagebox.showwarning(title="Error", message="La longitud ocupada por las placas no puede ser menor que 2 ni mayor a 12")	
					return None
			elif float(listaTiempoRetencionTotalTanque[11].get())<0.6 or float(listaTiempoRetencionTotalTanque[11].get())>0.9:
				messagebox.showwarning(title="Error", message="La distancia vertical de orificios de distribuci??n a placas debe estar entre 0.6 y 0.9")	
				return None

			elif float(listaTiempoRetencionTotalTanque[12].get())<0.9 or float(listaTiempoRetencionTotalTanque[12].get())>1.2:
				messagebox.showwarning(title="Error", message="La distancia entre canaletas de recolecci??n debe estar entre 0.9 y 1.2")	
				return None
		except:
			messagebox.showwarning(title="Error", message="Alguno de los datos ingresados no es un n??mero.")
			return None	

		anguloInclinacion = float(listaTiempoRetencionTotalTanque[4].get())
		distanciaPlacas = float(listaTiempoRetencionTotalTanque[6].get())
		caudalMedio = float(listaTiempoRetencionTotalTanque[7].get())
		factorMayoracionCaudalMD = float(listaTiempoRetencionTotalTanque[8].get())
		longitudPlacas = float(listaTiempoRetencionTotalTanque[10].get())
		distanciaVerticalDistribucionPlacas = float(listaTiempoRetencionTotalTanque[11].get())
		distanciaCanaletasRecoleccion= float(listaTiempoRetencionTotalTanque[12].get())


		tipoFloc = parametrosCombobox[0]
		tipoCelda = parametrosCombobox[1]
		materialTipoCelda = parametrosCombobox[2]
		dimensionesTipoCeldaMaterial = parametrosCombobox[3]
		numeroUnidades = parametrosCombobox[4]
		temperatura=  parametrosCombobox[5]


		
		tiempoRetencionTotalTanqueWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		tiempoRetencionTotalTanqueWindow.iconbitmap(bitmap=path)
		tiempoRetencionTotalTanqueWindow.geometry("540x300") 
		tiempoRetencionTotalTanqueWindow.resizable(0,0)	
		tiempoRetencionTotalTanqueWindow.configure(background="#9DC4AA")

		tiempoRetencionTotalTanqueFrame=LabelFrame(tiempoRetencionTotalTanqueWindow, text="Tiempo de retenci??n total en el tanque", font=("Yu Gothic bold", 11))
		tiempoRetencionTotalTanqueFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboltiempoRetencionTotalTanque_frame = Frame(tiempoRetencionTotalTanqueFrame)
		arboltiempoRetencionTotalTanque_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		#sedScrollX=Scrollbar(arboltiempoRetencionTotalTanque_frame,orient=HORIZONTAL)
		#sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arboltiempoRetencionTotalTanque_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboltiempoRetencionTotalTanque= ttk.Treeview(arboltiempoRetencionTotalTanque_frame,selectmode=BROWSE, height=11,show="tree headings")#,yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set,
		arboltiempoRetencionTotalTanque.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arboltiempoRetencionTotalTanque.xview)
		#sedScrollY.configure(command=arboltiempoRetencionTotalTanque.yview)
		#Define columnas.
		arboltiempoRetencionTotalTanque["columns"]= (
		"Presione para ver la excel","Valores","Unidades")

		#Headings
		arboltiempoRetencionTotalTanque.heading("#0",text="ID", anchor=CENTER)


		
		for col in arboltiempoRetencionTotalTanque["columns"]:
			arboltiempoRetencionTotalTanque.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg("images\\Sed_tiempoRetencionTotalTanque.png",782,193) )	

			
		arboltiempoRetencionTotalTanque.column("#0",width=0, stretch=False)
		arboltiempoRetencionTotalTanque.column("#1",width=340, stretch=False)
		arboltiempoRetencionTotalTanque.column("#2",width=100, stretch=False)
		arboltiempoRetencionTotalTanque.column("#3",width=100, stretch=False)

		#Striped row tags
		arboltiempoRetencionTotalTanque.tag_configure("evenrow", background= "#1FCCDB")
		arboltiempoRetencionTotalTanque.tag_configure("oddrow", background= "#9DC4AA")

		listatiempoRetencionTotalTanque=list()


		encabezadosLista=["Distancia vertical de orificios de distribuci??n a placas",
		"Altura de las placas",
		"Nivel del agua sobre las placas",
		"Altura de sedimentaci??n",
		"Volumen de sedimentaci??n de cada tanque",
		"Tiempo de retenci??n total en el tanque"]

		unidadesLista= ["m",
						"m",
						"m",
						"m",
						"m^3",
						"min"]

		
		#CalculosDeterminacionParametrosBasicos

		listaSalidaDatosEntradaPrametrosBasicosCalculos = datosEntradaParametrosBasicosCalculos(tipoFloc, tipoCelda, materialTipoCelda, dimensionesTipoCeldaMaterial, anguloInclinacion, numeroUnidades,distanciaPlacas, caudalMedio,factorMayoracionCaudalMD, temperatura)
				
		anchoModulos=float(dimensionesTipoCeldaMaterial[dimensionesTipoCeldaMaterial.find('x')+2:])/1000.0
		largoPlaca = float(dimensionesTipoCeldaMaterial[:dimensionesTipoCeldaMaterial.find('x')-1])/1000.0
		numeroConductosLargoUnidad= round(((longitudPlacas*sin(anguloInclinacion*(pi/180.0))) + (listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0))/((listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)+(listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0)),0)
		velocidadPromedioFlujoConductos = listaSalidaDatosEntradaPrametrosBasicosCalculos[9]/((numeroConductosLargoUnidad)*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)*(anchoModulos))
		longitudRelativaSedimentador =  largoPlaca/(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)
		longitudRelativaRegionTransicion = (0.058*velocidadPromedioFlujoConductos*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0))/listaSalidaDatosEntradaPrametrosBasicosCalculos[10]
		if longitudRelativaRegionTransicion<longitudRelativaSedimentador:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador-longitudRelativaRegionTransicion
		else:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador

	
		#CalculosCanaletasRecoleccion

		numeroCanaletasRecoleccionModulo= int(longitudPlacas/distanciaCanaletasRecoleccion)
		distanciaCanaletasRecoleccionAjustado = longitudPlacas/numeroCanaletasRecoleccionModulo		
		

		listatiempoRetencionTotalTanque.append(round(distanciaVerticalDistribucionPlacas,3))
		alturaPlacas = largoPlaca*sin(anguloInclinacion*pi*(1/180.0))
		listatiempoRetencionTotalTanque.append(round(alturaPlacas,3))	

		nivelAguaSobrePlacas = distanciaCanaletasRecoleccionAjustado*(velocidadPromedioFlujoConductos*86400.0)/432.0
		listatiempoRetencionTotalTanque.append(round(nivelAguaSobrePlacas,3))

		alturaSedimentacion = distanciaVerticalDistribucionPlacas+alturaPlacas+nivelAguaSobrePlacas
		listatiempoRetencionTotalTanque.append(round(alturaSedimentacion,3))
		
		volumenSedimentacionTanque = alturaSedimentacion*(longitudPlacas)*(anchoModulos) - ((numeroConductosLargoUnidad -1.0)*(largoPlaca)*(anchoModulos)*(listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0))
		listatiempoRetencionTotalTanque.append(round(volumenSedimentacionTanque,3))

		tiempoRetencionTotalResultado = volumenSedimentacionTanque/(60.0*listaSalidaDatosEntradaPrametrosBasicosCalculos[9])
		listatiempoRetencionTotalTanque.append(round(tiempoRetencionTotalResultado,3))


		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listatiempoRetencionTotalTanque[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arboltiempoRetencionTotalTanque,listaTemp)
		
		PasarExcelDatos(".\\ResultadosSedimentador\\TiempoRetencionTotalEnElTanque.xlsx",'Resultados',encabezadosLista,50, listatiempoRetencionTotalTanque, 15, unidadesLista, 15,False,[], 50)
		tiempoRetencionTotalTanqueWindow.mainloop()

	def dimensionesDelSedimentador(listaDimensionesDelSedimentador, tipoCelda):
		#ManejoErroresDimensionesDelSedimentador

		'''
			listaEntradaParametrosBasicos=[0= tipoFloc, 1= tipoCelda, 2= materialTipoCelda, 3= dimensionesTipoCeldaMaterial,
				4= anguloInclinacion, 5= numeroUnidades,
				6=distanciaPlacas, 7= caudalMedioEntry, 8= factorMayoracionCaudalMD, 9= temperaturaEntry]
				listaDeterminacionParametrosBasicosDiseno() = listaEntradaParametrosBasicos + [10 = longitudPlacas] 
				listaCanaletasRecoleccionAgua = [distanciaCanaletasRecoleccion,longitudPlacas]
				listaTiempoRetencionTotalTanque = listaDeterminacionParametrosBasicosDiseno + [11 = distanciaVerticalDistribucionPlacas] + 12=distanciaCanaletasRecoleccion
			listaDimensionesDelSedimentador = listaTiempoRetencionTotalTanque + [13= bordeLibre,
			14 = espesorMuros, 15 = pendienteTransversalTolva, 16 = anchoBasePlanaTolva] 
			
	
		'''
		
		inicialesComboBox=["Seleccione el tipo de floc","Seleccione el tipo de celda",
		f"Seleccione el material de {tipoCelda}", f"Seleccione las dimensiones de {tipoCelda}", "Seleccione el n??mero de unidades","Seleccione la temperatura"]
		
		listaComboBox=[listaDimensionesDelSedimentador[0],listaDimensionesDelSedimentador[1],listaDimensionesDelSedimentador[2],
		listaDimensionesDelSedimentador[3],listaDimensionesDelSedimentador[5], listaDimensionesDelSedimentador[9]]

		listaSinComboBox=[listaDimensionesDelSedimentador[4],listaDimensionesDelSedimentador[6],
		listaDimensionesDelSedimentador[7],listaDimensionesDelSedimentador[8], listaDimensionesDelSedimentador[10], 
		listaDimensionesDelSedimentador[11], listaDimensionesDelSedimentador[12], 
		
		listaDimensionesDelSedimentador[13],
		listaDimensionesDelSedimentador[14],listaDimensionesDelSedimentador[15],listaDimensionesDelSedimentador[16]]

		parametrosCombobox=list()

		for i in range(0,len(listaComboBox)):
			if listaComboBox[i].get()[0:10] == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta seleccionar {inicialesComboBox[i][10:].lower()}")
				return None	
			else:
				parametrosCombobox.append(listaComboBox[i].get())
		#Verifica que no sean nulos.

		if tipoCelda == "Conductos cuadrados":
			labels=["??ngulo de inclinaci??n", "lado interno de los conductos","caudal medio diario",
				"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por los m??dulos", 
				"distancia vertical de los orificios de distribuci??n a placas" 
				,"distancia entre canaletas de recolecci??n","borde libre", "espesor de muros de concreto",
				"pendiente transversal de la tolva de lodos", "ancho de la base plana de la tolva de lodos"]
		else: 

			labels=["??ngulo de inclinaci??n", "distancia entre placas","caudal medio diario",
			"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por las placas",
			"distancia vertical de los orificios de distribuci??n a placas","distancia entre canaletas de recolecci??n",
			"borde libre", "espesor de muros de concreto",
			"pendiente transversal de la tolva de lodos", "ancho de la base plana de la tolva de lodos"]

		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None

		try:
			if float(listaDimensionesDelSedimentador[4].get()) != 60.0  :
				messagebox.showwarning(title="Error", message="El valor del ??ngulo de inclinaci??n solo puede ser 60??")	
				return None
			elif float(listaDimensionesDelSedimentador[6].get())>6.0 or float(listaDimensionesDelSedimentador[6].get())<5.0:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message=f"El valor del lado interno de los conductos cuadrados no puede ser menor que 5 ni mayor que 6.")	
					return None
				else: 
					messagebox.showwarning(title="Error", message=f"El valor de la distancia entre placas no puede ser menor que 5 ni mayor que 6.")	
					return None
			elif float(listaDimensionesDelSedimentador[7].get())<0.01 or float(listaDimensionesDelSedimentador[7].get())>0.2:
				messagebox.showwarning(title="Error", message="El valor del caudal medio diario debe estar entre 0.01 y 0.2")	
				return None
			elif float(listaDimensionesDelSedimentador[8].get())>1.3 or float(listaDimensionesDelSedimentador[8].get())<1:
				messagebox.showwarning(title="Error", message="El valor de factoraci??n de mayoraci??n del caudal m??ximo diario debe estar entre 1 y 1.3")	
				return None
			elif float(listaDimensionesDelSedimentador[10].get())<2 or float(listaDimensionesDelSedimentador[10].get())>12:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message="La longitud ocupada por los m??dulos no puede ser menor que 2 ni mayor a 12")	
					return None
				else:
					messagebox.showwarning(title="Error", message="La longitud ocupada por las placas no puede ser menor que 2 ni mayor a 12")	
					return None
			elif float(listaDimensionesDelSedimentador[11].get())<0.6 or float(listaDimensionesDelSedimentador[11].get())>0.9:
				messagebox.showwarning(title="Error", message="La distancia vertical de orificios de distribuci??n a placas debe estar entre 0.6 y 0.9")	
				return None

			elif float(listaDimensionesDelSedimentador[12].get())<0.9 or float(listaDimensionesDelSedimentador[12].get())>1.2:
				messagebox.showwarning(title="Error", message="La distancia entre canaletas de recolecci??n debe estar entre 0.9 y 1.2")	
				return None
			
			elif float(listaDimensionesDelSedimentador[13].get())<0.3 or float(listaDimensionesDelSedimentador[13].get())>0.5:
				messagebox.showwarning(title="Error", message="El valor del borde libre debe estar entre 0.3 y 0.5")	
				return None
			
			elif float(listaDimensionesDelSedimentador[14].get())<0.3 or float(listaDimensionesDelSedimentador[14].get())>0.5:
				messagebox.showwarning(title="Error", message="El espesor de muros de concreto debe estar entre 0.3 y 0.5")	
				return None
			
			elif float(listaDimensionesDelSedimentador[15].get())<45.0 or float(listaDimensionesDelSedimentador[15].get())>60.0:
				messagebox.showwarning(title="Error", message="La pendiente transversal de la tolva de lodos debe estar entre 45?? y 60??")	
				return None
			
			elif float(listaDimensionesDelSedimentador[16].get())<0.1 or float(listaDimensionesDelSedimentador[16].get())>0.2:
				messagebox.showwarning(title="Error", message="El ancho de la base plana de la tolva de lodos debe estar entre 0.1 y 0.2")	
				return None
		except:
			messagebox.showwarning(title="Error", message="Alguno de los datos ingresados no es un n??mero.")
			return None	

		anguloInclinacion = float(listaDimensionesDelSedimentador[4].get())
		distanciaPlacas = float(listaDimensionesDelSedimentador[6].get())
		caudalMedio = float(listaDimensionesDelSedimentador[7].get())
		factorMayoracionCaudalMD = float(listaDimensionesDelSedimentador[8].get())
		longitudPlacas = float(listaDimensionesDelSedimentador[10].get())
		distanciaVerticalDistribucionPlacas = float(listaDimensionesDelSedimentador[11].get())
		distanciaCanaletasRecoleccion= float(listaDimensionesDelSedimentador[12].get())
		bordeLibre = float(listaDimensionesDelSedimentador[13].get())
		espesorMuros = float(listaDimensionesDelSedimentador[14].get())
		pendienteTransversalTolva = float(listaDimensionesDelSedimentador[15].get())
		anchoBasePlanaTolva = float(listaDimensionesDelSedimentador[16].get())

		tipoFloc = parametrosCombobox[0]
		tipoCelda = parametrosCombobox[1]
		materialTipoCelda = parametrosCombobox[2]
		dimensionesTipoCeldaMaterial = parametrosCombobox[3]
		numeroUnidades = parametrosCombobox[4]
		temperatura=  parametrosCombobox[5]





		


		#####
		dimensionesDelSedimentadorWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		dimensionesDelSedimentadorWindow.iconbitmap(bitmap=path)
		dimensionesDelSedimentadorWindow.geometry("520x400") 
		dimensionesDelSedimentadorWindow.resizable(0,0)	
		dimensionesDelSedimentadorWindow.configure(background="#9DC4AA")

		dimensionesDelSedimentadorFrame=LabelFrame(dimensionesDelSedimentadorWindow, text="Dimensiones del sedimentador", font=("Yu Gothic bold", 11))
		dimensionesDelSedimentadorFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboldimensionesDelSedimentador_frame = Frame(dimensionesDelSedimentadorFrame)
		arboldimensionesDelSedimentador_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arboldimensionesDelSedimentador_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldimensionesDelSedimentador_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldimensionesDelSedimentador= ttk.Treeview(arboldimensionesDelSedimentador_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arboldimensionesDelSedimentador.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arboldimensionesDelSedimentador.xview)
		sedScrollY.configure(command=arboldimensionesDelSedimentador.yview)
		#Define columnas.
		arboldimensionesDelSedimentador["columns"]= (
		"Presione para ver excel","Valores","Unidades")

		#Headings
		arboldimensionesDelSedimentador.heading("#0",text="ID", anchor=CENTER)




		for col in arboldimensionesDelSedimentador["columns"]:
			arboldimensionesDelSedimentador.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg("images\\Sed_DimensionesDelSedimentador.png",781,291) )	

		arboldimensionesDelSedimentador.column("#0",width=0, stretch=False)
		arboldimensionesDelSedimentador.column("#1",width=300, stretch=False)
		arboldimensionesDelSedimentador.column("#2",width=100, stretch=False)
		arboldimensionesDelSedimentador.column("#3",width=100, stretch=False)

		#Striped row tags
		arboldimensionesDelSedimentador.tag_configure("evenrow", background= "#1FCCDB")
		arboldimensionesDelSedimentador.tag_configure("oddrow", background= "#9DC4AA")




		listadimensionesDelSedimentador=list()


		encabezadosLista=["Borde libre",
				"Espesor de muros de concreto",
				"Pendiente tranversal de la tolva de lodos",
				"Ancho de la base plana de la tolva de lodos",
				"Relaci??n ancho / largo de cada tanque ",
				"Altura de la tolva de lodos",
				"Volumen de la tolva de lodos",
				"Largo total del sedimentador",
				"Ancho total del sedimentador",
				"Altura interna total del sedimentador"]
		unidadesLista = ["m",
						"m",
						"??",
						"m",
						"",
						"m",
						"m^3",
						"m",
						"m",
						"m"]
		
		##DatosDeterminacionParametrosBasicosDise??o
		listaSalidaDatosEntradaPrametrosBasicosCalculos = datosEntradaParametrosBasicosCalculos(tipoFloc, tipoCelda, materialTipoCelda, dimensionesTipoCeldaMaterial, anguloInclinacion, numeroUnidades,distanciaPlacas, caudalMedio,factorMayoracionCaudalMD, temperatura)
				
		anchoModulos=float(dimensionesTipoCeldaMaterial[dimensionesTipoCeldaMaterial.find('x')+2:])/1000.0
		largoPlaca = float(dimensionesTipoCeldaMaterial[:dimensionesTipoCeldaMaterial.find('x')-1])/1000.0
		cargaSuperficial = (listaSalidaDatosEntradaPrametrosBasicosCalculos[9]*86400.0)/(longitudPlacas*anchoModulos)
		numeroConductosLargoUnidad= round(((longitudPlacas*sin(anguloInclinacion*(pi/180.0))) + (listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0))/((listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)+(listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0)),0)
		velocidadPromedioFlujoConductos = listaSalidaDatosEntradaPrametrosBasicosCalculos[9]/((numeroConductosLargoUnidad)*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)*(anchoModulos))
		longitudRelativaSedimentador =  largoPlaca/(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)
		longitudRelativaRegionTransicion = (0.058*velocidadPromedioFlujoConductos*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0))/listaSalidaDatosEntradaPrametrosBasicosCalculos[10]
		if longitudRelativaRegionTransicion<longitudRelativaSedimentador:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador-longitudRelativaRegionTransicion
		else:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador


		##Tiempo retenci??n en el tanque

	
		#CalculosCanaletasRecoleccion

		numeroCanaletasRecoleccionModulo= int(longitudPlacas/distanciaCanaletasRecoleccion)
		distanciaCanaletasRecoleccionAjustado = longitudPlacas/numeroCanaletasRecoleccionModulo		
		

		alturaPlacas = largoPlaca*sin(anguloInclinacion*pi*(1/180.0))
	
		nivelAguaSobrePlacas = distanciaCanaletasRecoleccionAjustado*(velocidadPromedioFlujoConductos*86400.0)/432.0
		
		alturaSedimentacion = distanciaVerticalDistribucionPlacas+alturaPlacas+nivelAguaSobrePlacas
		
		volumenSedimentacionTanque = alturaSedimentacion*(longitudPlacas)*(anchoModulos) - ((numeroConductosLargoUnidad -1.0)*(largoPlaca)*(anchoModulos)*(listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0))
		
		




		##

		listadimensionesDelSedimentador.append(round(bordeLibre,3))
		listadimensionesDelSedimentador.append(round(espesorMuros,3))
		listadimensionesDelSedimentador.append(round(pendienteTransversalTolva,3))
		listadimensionesDelSedimentador.append(round(anchoBasePlanaTolva,3))
		relacionAnchoLargoTanque = round((longitudPlacas/anchoModulos),1)
		listadimensionesDelSedimentador.append(f"1:{relacionAnchoLargoTanque}")
		alturaTolvaLodos = ((anchoModulos-anchoBasePlanaTolva)/2.0)*tan(pendienteTransversalTolva*pi*(1/180.0))
		listadimensionesDelSedimentador.append(round(alturaTolvaLodos,3))
		volumenTolvaLodos = (longitudPlacas)*(alturaTolvaLodos)*( anchoBasePlanaTolva+((anchoModulos-anchoBasePlanaTolva)/2.0))
		listadimensionesDelSedimentador.append(round(volumenTolvaLodos,3))
		largoTotalSedimentador = (2*espesorMuros)+longitudPlacas
		listadimensionesDelSedimentador.append(round(largoTotalSedimentador,3))
		anchoTotalSedimentador = (anchoModulos+espesorMuros)*float(numeroUnidades)
		listadimensionesDelSedimentador.append(round(anchoTotalSedimentador,3))
		alturaInternaTotalSedimentador = espesorMuros+alturaTolvaLodos+bordeLibre+alturaSedimentacion 
		listadimensionesDelSedimentador.append(round(alturaInternaTotalSedimentador,3))
		


		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listadimensionesDelSedimentador[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arboldimensionesDelSedimentador,listaTemp)
		
		if volumenTolvaLodos < (0.1*(volumenTolvaLodos+volumenSedimentacionTanque)):
			messagebox.showinfo(title="Informaci??n", message="El volumen de la tolva de lodos es bajo en relaci??n al volumen total del tanque, ??Revise datos!")
		elif volumenTolvaLodos > (0.2*(volumenTolvaLodos+volumenSedimentacionTanque)):
			messagebox.showinfo(title="Informaci??n", message="El volumen de la tolva de lodos es alto en relaci??n al volumen total del tanque, ??Revise datos!")
			
		PasarExcelDatos(".\\ResultadosSedimentador\\DimensionesDelSedimentador.xlsx",'Resultados',encabezadosLista,50, listadimensionesDelSedimentador, 15, unidadesLista, 15,False,[], 50)

		dimensionesDelSedimentadorWindow.mainloop()

	def disenoSistemaEvacuacionLodos(listaDisenoSistemaEvacuacionLodos, tipoCelda):
		#ManejoErroresDisenoSistemaEvacuacionLodos
		
		'''
		
			listaEntradaParametrosBasicos=[0= tipoFloc, 1= tipoCelda, 2= materialTipoCelda, 3= dimensionesTipoCeldaMaterial,
				4= anguloInclinacion, 5= numeroUnidades,
				6=distanciaPlacas, 7= caudalMedioEntry, 8= factorMayoracionCaudalMD, 9= temperaturaEntry]
				listaDeterminacionParametrosBasicosDiseno() = listaEntradaParametrosBasicos + [10 = longitudPlacas] 
				listaCanaletasRecoleccionAgua = [distanciaCanaletasRecoleccion,longitudPlacas]
				listaTiempoRetencionTotalTanque = listaDeterminacionParametrosBasicosDiseno + [11 = distanciaVerticalDistribucionPlacas] + 12=distanciaCanaletasRecoleccion
			listaDimensionesDelSedimentador = listaTiempoRetencionTotalTanque + [13= bordeLibre,
			14 = espesorMuros, 15 = pendienteTransversalTolva, 16 = anchoBasePlanaTolva] 

			listaDisenoSistemaEvacuacionLodos = listaDimensionesDelSedimentador + [17 = velocidadMinimaArrastre, 18 = diametroNominalOrificionesMultipleDescarga]
			("Seleccione el di??metro nominal de los orificios del m??ltiple de descarga")
		'''

		

		inicialesComboBox=["Seleccione el tipo de floc","Seleccione el tipo de celda",
		f"Seleccione el material de {tipoCelda}", f"Seleccione las dimensiones de {tipoCelda}", "Seleccione el n??mero de unidades","Seleccione la temperatura",
		"Seleccione el di??metro nominal de los orificios del m??ltiple de descarga"]

		listaComboBox=[listaDisenoSistemaEvacuacionLodos[0],listaDisenoSistemaEvacuacionLodos[1],listaDisenoSistemaEvacuacionLodos[2],
		listaDisenoSistemaEvacuacionLodos[3],listaDisenoSistemaEvacuacionLodos[5], listaDisenoSistemaEvacuacionLodos[9], 
		listaDisenoSistemaEvacuacionLodos[18]]

		listaSinComboBox=[listaDisenoSistemaEvacuacionLodos[4],listaDisenoSistemaEvacuacionLodos[6],
		listaDisenoSistemaEvacuacionLodos[7],listaDisenoSistemaEvacuacionLodos[8], listaDisenoSistemaEvacuacionLodos[10], 
		listaDisenoSistemaEvacuacionLodos[11], listaDisenoSistemaEvacuacionLodos[12], 

		listaDisenoSistemaEvacuacionLodos[13],
		listaDisenoSistemaEvacuacionLodos[14],listaDisenoSistemaEvacuacionLodos[15],listaDisenoSistemaEvacuacionLodos[16],
		listaDisenoSistemaEvacuacionLodos[17]]

		parametrosCombobox=list()

		for i in range(0,len(listaComboBox)):
			if listaComboBox[i].get()[0:10] == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta seleccionar {inicialesComboBox[i][10:].lower()}")
				return None	
			else:
				parametrosCombobox.append(listaComboBox[i].get())
		#Verifica que no sean nulos.

		if tipoCelda == "Conductos cuadrados":
			labels=["??ngulo de inclinaci??n", "lado interno de los conductos","caudal medio diario",
				"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por los m??dulos", 
				"distancia vertical de los orificios de distribuci??n a placas" 
				,"distancia entre canaletas de recolecci??n","borde libre", "espesor de muros de concreto",
				"pendiente transversal de la tolva de lodos", "ancho de la base plana de la tolva de lodos",
				"velocidad m??nima de arrastre asignada"]
		else: 

			labels=["??ngulo de inclinaci??n", "distancia entre placas","caudal medio diario",
			"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por las placas",
			"distancia vertical de los orificios de distribuci??n a placas","distancia entre canaletas de recolecci??n",
			"borde libre", "espesor de muros de concreto",
			"pendiente transversal de la tolva de lodos", "ancho de la base plana de la tolva de lodos",
			"velocidad m??nima de arrastre asignada"]

		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None

		try:
			if float(listaDisenoSistemaEvacuacionLodos[4].get()) != 60.0  :
				messagebox.showwarning(title="Error", message="El valor del ??ngulo de inclinaci??n solo puede ser 60??")	
				return None
			elif float(listaDisenoSistemaEvacuacionLodos[6].get())>6.0 or float(listaDisenoSistemaEvacuacionLodos[6].get())<5.0:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message=f"El valor del lado interno de los conductos cuadrados no puede ser menor que 5 ni mayor que 6.")	
					return None
				else: 
					messagebox.showwarning(title="Error", message=f"El valor de la distancia entre placas no puede ser menor que 5 ni mayor que 6.")	
					return None
			elif float(listaDisenoSistemaEvacuacionLodos[7].get())<0.01 or float(listaDisenoSistemaEvacuacionLodos[7].get())>0.2:
				messagebox.showwarning(title="Error", message="El valor del caudal medio diario debe estar entre 0.01 y 0.2")	
				return None
			elif float(listaDisenoSistemaEvacuacionLodos[8].get())>1.3 or float(listaDisenoSistemaEvacuacionLodos[8].get())<1:
				messagebox.showwarning(title="Error", message="El valor de factoraci??n de mayoraci??n del caudal m??ximo diario debe estar entre 1 y 1.3")	
				return None
			elif float(listaDisenoSistemaEvacuacionLodos[10].get())<2 or float(listaDisenoSistemaEvacuacionLodos[10].get())>12:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message="La longitud ocupada por los m??dulos no puede ser menor que 2 ni mayor a 12")	
					return None
				else:
					messagebox.showwarning(title="Error", message="La longitud ocupada por las placas no puede ser menor que 2 ni mayor a 12")	
					return None
			elif float(listaDisenoSistemaEvacuacionLodos[11].get())<0.6 or float(listaDisenoSistemaEvacuacionLodos[11].get())>0.9:
				messagebox.showwarning(title="Error", message="La distancia vertical de orificios de distribuci??n a placas debe estar entre 0.6 y 0.9")	
				return None

			elif float(listaDisenoSistemaEvacuacionLodos[12].get())<0.9 or float(listaDisenoSistemaEvacuacionLodos[12].get())>1.2:
				messagebox.showwarning(title="Error", message="La distancia entre canaletas de recolecci??n debe estar entre 0.9 y 1.2")	
				return None
			
			elif float(listaDisenoSistemaEvacuacionLodos[13].get())<0.3 or float(listaDisenoSistemaEvacuacionLodos[13].get())>0.5:
				messagebox.showwarning(title="Error", message="El valor del borde libre debe estar entre 0.3 y 0.5")	
				return None
			
			elif float(listaDisenoSistemaEvacuacionLodos[14].get())<0.3 or float(listaDisenoSistemaEvacuacionLodos[14].get())>0.5:
				messagebox.showwarning(title="Error", message="El espesor de muros de concreto debe estar entre 0.3 y 0.5")	
				return None
			
			elif float(listaDisenoSistemaEvacuacionLodos[15].get())<45.0 or float(listaDisenoSistemaEvacuacionLodos[15].get())>60.0:
				messagebox.showwarning(title="Error", message="La pendiente transversal de la tolva de lodos debe estar entre 45?? y 60??")	
				return None
			
			elif float(listaDisenoSistemaEvacuacionLodos[16].get())<0.1 or float(listaDisenoSistemaEvacuacionLodos[16].get())>0.2:
				messagebox.showwarning(title="Error", message="El ancho de la base plana de la tolva de lodos debe estar entre 0.1 y 0.2")	
				return None
			
			elif float(listaDisenoSistemaEvacuacionLodos[17].get())<0.01 or float(listaDisenoSistemaEvacuacionLodos[17].get())>0.02:
				messagebox.showwarning(title="Error", message="La velocidad m??nima de arrastre asignada debe estar entre 0.01 y 0.02")	
				return None
		except:
			messagebox.showwarning(title="Error", message="Alguno de los datos ingresados no es un n??mero.")
			return None	

		anguloInclinacion = float(listaDisenoSistemaEvacuacionLodos[4].get())
		distanciaPlacas = float(listaDisenoSistemaEvacuacionLodos[6].get())
		caudalMedio = float(listaDisenoSistemaEvacuacionLodos[7].get())
		factorMayoracionCaudalMD = float(listaDisenoSistemaEvacuacionLodos[8].get())
		longitudPlacas = float(listaDisenoSistemaEvacuacionLodos[10].get())
		distanciaVerticalDistribucionPlacas = float(listaDisenoSistemaEvacuacionLodos[11].get())
		distanciaCanaletasRecoleccion= float(listaDisenoSistemaEvacuacionLodos[12].get())
		bordeLibre = float(listaDisenoSistemaEvacuacionLodos[13].get())
		espesorMuros = float(listaDisenoSistemaEvacuacionLodos[14].get())
		pendienteTransversalTolva = float(listaDisenoSistemaEvacuacionLodos[15].get())
		anchoBasePlanaTolva = float(listaDisenoSistemaEvacuacionLodos[16].get())
		velocidadMinimaArrastre = float(listaDisenoSistemaEvacuacionLodos[17].get())


		tipoFloc = parametrosCombobox[0]
		tipoCelda = parametrosCombobox[1]
		materialTipoCelda = parametrosCombobox[2]
		dimensionesTipoCeldaMaterial = parametrosCombobox[3]
		numeroUnidades = parametrosCombobox[4]
		temperatura=  parametrosCombobox[5]
		diametroNominalOrificionesMultipleDescarga = parametrosCombobox[6]





		###
		disenoSistemaEvacuacionLodosWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		disenoSistemaEvacuacionLodosWindow.iconbitmap(bitmap=path)
		disenoSistemaEvacuacionLodosWindow.geometry("520x400") 
		disenoSistemaEvacuacionLodosWindow.resizable(0,0)	
		disenoSistemaEvacuacionLodosWindow.configure(background="#9DC4AA")

		disenoSistemaEvacuacionLodosFrame=LabelFrame(disenoSistemaEvacuacionLodosWindow, text="Dise??o del sistema de evacuaci??n de lodos", font=("Yu Gothic bold", 11))
		disenoSistemaEvacuacionLodosFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboldisenoSistemaEvacuacionLodos_frame = Frame(disenoSistemaEvacuacionLodosFrame)
		arboldisenoSistemaEvacuacionLodos_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arboldisenoSistemaEvacuacionLodos_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldisenoSistemaEvacuacionLodos_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldisenoSistemaEvacuacionLodos= ttk.Treeview(arboldisenoSistemaEvacuacionLodos_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arboldisenoSistemaEvacuacionLodos.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arboldisenoSistemaEvacuacionLodos.xview)
		sedScrollY.configure(command=arboldisenoSistemaEvacuacionLodos.yview)
		#Define columnas.
		arboldisenoSistemaEvacuacionLodos["columns"]= (
		"Presione para ver excel","Valores","Unidades")

		#Headings
		arboldisenoSistemaEvacuacionLodos.heading("#0",text="ID", anchor=CENTER)


		for col in arboldisenoSistemaEvacuacionLodos["columns"]:
			arboldisenoSistemaEvacuacionLodos.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg("images\\Sed_disenoSistemaEvacuacionLodos.png",781,404) )	

		arboldisenoSistemaEvacuacionLodos.column("#0",width=0, stretch=False)
		arboldisenoSistemaEvacuacionLodos.column("#1",width=300, stretch=False)
		arboldisenoSistemaEvacuacionLodos.column("#2",width=100, stretch=False)
		arboldisenoSistemaEvacuacionLodos.column("#3",width=100, stretch=False)

		#Striped row tags
		arboldisenoSistemaEvacuacionLodos.tag_configure("evenrow", background= "#1FCCDB")
		arboldisenoSistemaEvacuacionLodos.tag_configure("oddrow", background= "#9DC4AA")




		listadisenoSistemaEvacuacionLodos=list()


		encabezadosLista= ["Velocidad m??nima de arrastre asignada",
					"Longitud del m??ltiple de descarga",
					"Tirante sobre los orificios del m??ltiple de descarga",
					"Di??metro nominal del m??ltiple de descarga",
					"Diametro interno del m??ltiple de descarga",
					"Di??metro nominal de los orificios del m??ltiple\nde descarga",
					"Di??metro interno de los orificios del m??ltiple\nde descarga",
					"Separaci??n entre orificios del m??ltiple (te??rica)",
					"N??mero de orificios del m??ltiple de descarga",
					"Cuadrado de la relaci??n entre el di??metro de orificios\ny el del m??ltiple por el n??mero de orificios",
					"Separaci??n entre orificios del m??ltiple (confirmada)"]


		unidadesLista= ["m/s",
					"m",
					"m",
					"pulg",
					"m",
					"pulg",
					"m",
					"m",
					"und",
					"",
					"m"]

		##CalculosDimensionesSedimentador
		##DatosDeterminacionParametrosBasicosDise??o
		listaSalidaDatosEntradaPrametrosBasicosCalculos = datosEntradaParametrosBasicosCalculos(tipoFloc, tipoCelda, materialTipoCelda, dimensionesTipoCeldaMaterial, anguloInclinacion, numeroUnidades,distanciaPlacas, caudalMedio,factorMayoracionCaudalMD, temperatura)
				
		anchoModulos=float(dimensionesTipoCeldaMaterial[dimensionesTipoCeldaMaterial.find('x')+2:])/1000.0
		largoPlaca = float(dimensionesTipoCeldaMaterial[:dimensionesTipoCeldaMaterial.find('x')-1])/1000.0

		numeroConductosLargoUnidad= round(((longitudPlacas*sin(anguloInclinacion*(pi/180.0))) + (listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0))/((listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)+(listaSalidaDatosEntradaPrametrosBasicosCalculos[4]/1000.0)),0)
		velocidadPromedioFlujoConductos = listaSalidaDatosEntradaPrametrosBasicosCalculos[9]/((numeroConductosLargoUnidad)*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)*(anchoModulos))
		longitudRelativaSedimentador =  largoPlaca/(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0)
		longitudRelativaRegionTransicion = (0.058*velocidadPromedioFlujoConductos*(listaSalidaDatosEntradaPrametrosBasicosCalculos[11]/100.0))/listaSalidaDatosEntradaPrametrosBasicosCalculos[10]
		if longitudRelativaRegionTransicion<longitudRelativaSedimentador:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador-longitudRelativaRegionTransicion
		else:
			longitudRelativaRegionTransicionCorregida= longitudRelativaSedimentador


		##Tiempo retenci??n en el tanque

		#CalculosCanaletasRecoleccion

		numeroCanaletasRecoleccionModulo= int(longitudPlacas/distanciaCanaletasRecoleccion)
		distanciaCanaletasRecoleccionAjustado = longitudPlacas/numeroCanaletasRecoleccionModulo		
		

		alturaPlacas = largoPlaca*sin(anguloInclinacion*pi*(1/180.0))
	
		nivelAguaSobrePlacas = distanciaCanaletasRecoleccionAjustado*(velocidadPromedioFlujoConductos*86400.0)/432.0
		
		alturaSedimentacion = distanciaVerticalDistribucionPlacas+alturaPlacas+nivelAguaSobrePlacas
		

		

		




		###

		
		alturaTolvaLodos = ((anchoModulos-anchoBasePlanaTolva)/2.0)*tan(pendienteTransversalTolva*pi*(1/180.0))
		


		##

		

		listadisenoSistemaEvacuacionLodos.append(round(velocidadMinimaArrastre,3))
		longitudMultipleDescarga = longitudPlacas
		listadisenoSistemaEvacuacionLodos.append(round(longitudMultipleDescarga,3))
		tiranteSobreOrificiosMultipleDescarga = alturaTolvaLodos+alturaSedimentacion
		listadisenoSistemaEvacuacionLodos.append(round(tiranteSobreOrificiosMultipleDescarga,3))
		
		if 2<=longitudMultipleDescarga<3.5:
			diametroNominalMutipleDescarga = "4(RDE 13.5)"
		elif 3.5<=longitudMultipleDescarga<6.5:
			diametroNominalMutipleDescarga = "6(RDE 13.5)"
		elif 6.5<=longitudMultipleDescarga<=12.0:
			diametroNominalMutipleDescarga = "8(RDE 13.5)"
		
		listadisenoSistemaEvacuacionLodos.append(diametroNominalMutipleDescarga)

		listaDiametroNominal= [
		"4(RDE 13.5)",
		"6(RDE 13.5)",
		"8(RDE 13.5)",
		]
		listaDiametroInterno = [0.09738,
		0.14334,
		0.18662
		]
		diamentroInternoDic=dict()

		for i in range(0, len(listaDiametroNominal)):
			diamentroInternoDic[listaDiametroNominal[i]]=listaDiametroInterno[i]

		diametroInterno= diamentroInternoDic[diametroNominalMutipleDescarga]
		listadisenoSistemaEvacuacionLodos.append(round(diametroInterno,3))
		listadisenoSistemaEvacuacionLodos.append(diametroNominalOrificionesMultipleDescarga)
		
		listaDiametroNominalOrificiosMultipleDescarga= [
		'1/2 (RDE 9)',
		'3/4 (RDE 11)',
		'3/4 (RDE 21)',
		'1 (RDE 13,5)',
		'1 (RDE 21)',
		'1 1/4 (RDE 21)',
		'1 1/2 (RDE 21)',
		'2 (RDE 21)'

		]
		listaDiametroInternoOrificiosMultipleDescarga = [
		0.01660,
		0.02181,
		0.02363,
		0.02848,
		0.03020,
		0.03814,
		0.04368,
		0.05458
		]

		diamentroInternoOrificiosMultipleDescargaDic=dict()

		for i in range(0, len(listaDiametroNominalOrificiosMultipleDescarga)):
			diamentroInternoOrificiosMultipleDescargaDic[listaDiametroNominalOrificiosMultipleDescarga[i]]=listaDiametroInternoOrificiosMultipleDescarga[i]		
		
		diametroInternoOrificiosMultipleDescarga= diamentroInternoOrificiosMultipleDescargaDic[diametroNominalOrificionesMultipleDescarga]

		listadisenoSistemaEvacuacionLodos.append(round(diametroInternoOrificiosMultipleDescarga,3))

		separacionOrificiosMultipleTeorica = 1.16*(diametroInternoOrificiosMultipleDescarga)*sqrt(((tiranteSobreOrificiosMultipleDescarga)**0.5)/(velocidadMinimaArrastre))

		listadisenoSistemaEvacuacionLodos.append(round(separacionOrificiosMultipleTeorica,3))
		numeroOrificiosMultipleDescarga = int(longitudMultipleDescarga/separacionOrificiosMultipleTeorica)+1
		listadisenoSistemaEvacuacionLodos.append(numeroOrificiosMultipleDescarga)

		cuadradoRelacionDiametroOrificiosYMultiplePorNumeroOrificios= ((diametroInternoOrificiosMultipleDescarga/diametroInterno)**2)*(numeroOrificiosMultipleDescarga)

		listadisenoSistemaEvacuacionLodos.append(round(cuadradoRelacionDiametroOrificiosYMultiplePorNumeroOrificios,3))

		separacionOrificiosMultipleConfirmada = longitudMultipleDescarga/numeroOrificiosMultipleDescarga

		listadisenoSistemaEvacuacionLodos.append(round(separacionOrificiosMultipleConfirmada,3))


		




		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listadisenoSistemaEvacuacionLodos[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arboldisenoSistemaEvacuacionLodos,listaTemp)
		if cuadradoRelacionDiametroOrificiosYMultiplePorNumeroOrificios<0.4:
			messagebox.showinfo(title="Informaci??n", message="??El Valor resultante del cuadrado de la relaci??n entre el di??metro de orificios y el del m??ltiple por el n??mero de orificios es bajo, revise datos de di??metros de orificios!")
		elif cuadradoRelacionDiametroOrificiosYMultiplePorNumeroOrificios>0.45:
			messagebox.showinfo(title="Informaci??n", message="??El Valor resultante del cuadrado de la relaci??n entre el di??metro de orificios y el del m??ltiple por el n??mero de orificios es alto, revise datos de di??metros de orificios!")
		
		PasarExcelDatos(".\\ResultadosSedimentador\\DisenoSistemaEvacuacionLodos.xlsx",'Resultados',encabezadosLista,50, listadisenoSistemaEvacuacionLodos, 15, unidadesLista, 15,False,[], 50)
		
		disenoSistemaEvacuacionLodosWindow.mainloop()
		
	

	def caudalesDeDise??o(listaCaudalesDise??o):
		
		# listaCaudalesDise??o = [factorMayoracionCaudalMD, factorMayoracionCaudalMH,caudalMedioEntry]
		
		
		# listaEntradaParametrosBasicos=[tipoFloc = 0 ,tipoCelda = 1, materialTipoCelda =2 , dimensionesTipoCeldaMaterial =3 
		# ,anguloInclinacion =4
		# ,numeroUnidades =5,
		# distanciaPlacas = 6, 
		# caudalMedioEntry = 7, 
		# factorMayoracionCaudalMD = 8,temperaturaEntry=  9]

		
		
		listaSinComboBox=[listaCaudalesDise??o[0],listaCaudalesDise??o[1],
		listaCaudalesDise??o[2]]	
		labels=["factoraci??n de mayoraci??n del caudal m??ximo diario","factor de mayoraci??n del caudal m??ximo horario", "caudal medio horario"]
		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None

		try:
			if float(listaCaudalesDise??o[2].get())<0.01 or float(listaCaudalesDise??o[2].get())>0.2:
				messagebox.showwarning(title="Error", message="El valor del caudal medio diario debe estar entre 0.01 y 0.2")	
				return None
			elif float(listaCaudalesDise??o[0].get())>1.3 or float(listaCaudalesDise??o[0].get())<1:
				messagebox.showwarning(title="Error", message="El valor de factoraci??n de mayoraci??n del caudal m??ximo diario debe estar entre 1 y 1.3")	
				return None
			elif float(listaCaudalesDise??o[1].get())>1.6 or float(listaCaudalesDise??o[1].get())<1:
				messagebox.showwarning(title="Error", message="El valor de factoraci??n de mayoraci??n del caudal m??ximo horario debe estar entre 1 y 1.6")	
				return None
		except:
			messagebox.showwarning(title="Error", message="Alguno de los datos ingresados no es un n??mero.")
			return None	
		
		caudalMedioDiario= float(listaCaudalesDise??o[2].get())
		factorMayoracionCaudalMD = float(listaCaudalesDise??o[0].get())
		factorMayoracionCaudalMH = float(listaCaudalesDise??o[1].get())
		
		
		
		CaudalesDise??oWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		CaudalesDise??oWindow.iconbitmap(bitmap=path)
		CaudalesDise??oWindow.geometry("500x300") 
		CaudalesDise??oWindow.resizable(0,0)	
		CaudalesDise??oWindow.configure(background="#9DC4AA")

		CaudalesDise??oFrame=LabelFrame(CaudalesDise??oWindow, text="Caudales de dise??o", font=("Yu Gothic bold", 11))
		CaudalesDise??oFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolCaudalesDise??o_frame = Frame(CaudalesDise??oFrame)
		arbolCaudalesDise??o_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolCaudalesDise??o_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolCaudalesDise??o_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCaudalesDise??o= ttk.Treeview(arbolCaudalesDise??o_frame,selectmode=BROWSE, height=11,show="tree headings")#,yscrollcommand=sedScrollY.set, xscrollcommand=sedScrollX.set)
		arbolCaudalesDise??o.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolCaudalesDise??o.xview)
		# sedScrollY.configure(command=arbolCaudalesDise??o.yview)
		#Define columnas.
		arbolCaudalesDise??o["columns"]= (
		"1","Valores","Unidades")

		

		#Headings
		arbolCaudalesDise??o.heading("#0",text="ID", anchor=CENTER)



		for col in arbolCaudalesDise??o["columns"]:
			arbolCaudalesDise??o.heading(col, text=col,anchor=CENTER)	

		arbolCaudalesDise??o.column("#1",width=300, stretch=False)
		arbolCaudalesDise??o.column("#2",width=100, stretch=False)
		arbolCaudalesDise??o.column("#3",width=100, stretch=False)
		


		arbolCaudalesDise??o.column("#0",width=0, stretch=False)
		
		

		#Striped row tags
		arbolCaudalesDise??o.tag_configure("evenrow", background= "#1FCCDB")
		arbolCaudalesDise??o.tag_configure("oddrow", background= "#9DC4AA")


		listaCaudalesDise??o=list()


		encabezadosLista=[
		"Factor de mayoraci??n del caudal m??ximo diario",
		"Factor de mayoraci??n del caudal m??ximo horario",
		"Caudal medio diario",			
		"Caudal m??ximo diario",			
		"Caudal m??ximo horario",			
		]
		unidadesLista=["",
		"",
		"(m^3)/s",
		"(m^3)/s",
		"(m^3)/s",
						]
		
		listaCaudalesDise??o.append(round(factorMayoracionCaudalMD,3))
		listaCaudalesDise??o.append(round(factorMayoracionCaudalMH,3))
		listaCaudalesDise??o.append(round(caudalMedioDiario,3))
		caudalMaximoDiario=caudalMedioDiario*factorMayoracionCaudalMD
		listaCaudalesDise??o.append(round(caudalMaximoDiario,3))
		caudalMaximoHorario=caudalMedioDiario*factorMayoracionCaudalMH
		listaCaudalesDise??o.append(round(caudalMaximoHorario,3))
		
		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listaCaudalesDise??o[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolCaudalesDise??o,listaTemp)

		PasarExcelDatos(".\\ResultadosSedimentador\\CaudalesDiseno.xlsx",'Resultados',encabezadosLista,50, listaCaudalesDise??o, 15, unidadesLista, 15,False,[], 50)
		CaudalesDise??oWindow.mainloop()

	def propiedadesFisicasAgua(temperaturaEntry):
		
		if temperaturaEntry.get()[0:10] == "Seleccione":
			messagebox.showwarning(title="Error", message=f"Hace falta seleccionar la temperatura del agua a tratar")
			return None	
		else:
			temperatura=float(temperaturaEntry.get())
		
		propiedadesFisicasAguaWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		propiedadesFisicasAguaWindow.iconbitmap(bitmap=path)
		propiedadesFisicasAguaWindow.geometry("500x250") 
		propiedadesFisicasAguaWindow.resizable(0,0)	
		propiedadesFisicasAguaWindow.configure(background="#9DC4AA")

		propiedadesFisicasAguaFrame=LabelFrame(propiedadesFisicasAguaWindow, text="Propiedades f??sicas de agua a tratar", font=("Yu Gothic bold", 11))
		propiedadesFisicasAguaFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolpropiedadesFisicasAgua_frame = Frame(propiedadesFisicasAguaFrame)
		arbolpropiedadesFisicasAgua_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolpropiedadesFisicasAgua_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolpropiedadesFisicasAgua_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolpropiedadesFisicasAgua= ttk.Treeview(arbolpropiedadesFisicasAgua_frame,selectmode=BROWSE, height=11,show="tree headings")#,yscrollcommand=sedScrollY.set, xscrollcommand=sedScrollX.set)
		arbolpropiedadesFisicasAgua.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolpropiedadesFisicasAgua.xview)
		# sedScrollY.configure(command=arbolpropiedadesFisicasAgua.yview)
		#Define columnas.
		arbolpropiedadesFisicasAgua["columns"]= (
		"1","Valores","Unidades")



		#Headings
		arbolpropiedadesFisicasAgua.heading("#0",text="ID", anchor=CENTER)




		for col in arbolpropiedadesFisicasAgua["columns"]:
			arbolpropiedadesFisicasAgua.heading(col, text=col,anchor=CENTER)	

		arbolpropiedadesFisicasAgua.column("#1",width=300, stretch=False)
		arbolpropiedadesFisicasAgua.column("#2",width=100, stretch=False)
		arbolpropiedadesFisicasAgua.column("#3",width=100, stretch=False)



		arbolpropiedadesFisicasAgua.column("#0",width=0, stretch=False)



		#Striped row tags
		arbolpropiedadesFisicasAgua.tag_configure("evenrow", background= "#1FCCDB")
		arbolpropiedadesFisicasAgua.tag_configure("oddrow", background= "#9DC4AA")


		listapropiedadesFisicasAgua=list()


		encabezadosLista=[
		"Temperatura del agua a tratar",
		f"Densidad del agua a {temperatura} ??C",
		f"Viscocidad din??mica del agua a {temperatura} ??C",
		f"Viscocidad cinem??tica del agua a {temperatura} ??C",

		]
		unidadesLista=[
		"??C",
		"kg/(m^3)",
		"(N.s)/(m^2)",
		"(m^2)/s",
						]
		
		valorTemperaturas=list()

		tablaTemperaturaViscocidadCinematica=dict()
		viscosidadDinamicaDic=dict()
		tablaTemperaturaDensidad=dict()

		for i in range(0,36):    
			valorTemperaturas.append(i)
					
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		viscosidadDinamicaValor = [0.001792, 0.001731, 
		0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 
		0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 
		0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 
		0.001083, 0.001056, 0.00103, 0.001005, 0.000981, 
		0.000958, 0.000936, 0.000914, 0.000894, 0.000874,
		0.000855, 0.000836, 0.000818, 0.000801, 0.000784,
		0.000768, 0.000752, 0.000737, 0.000723]

	
		valorDensidad= [999.82, 999.89, 999.94, 999.98, 1000.0, 1000.0, 999.99, 999.96, 999.91, 999.85, 999.77, 999.68, 999.58, 999.46, 999.33, 999.19, 999.03, 998.86, 998.68, 998.49, 998.29, 998.08, 997.86, 997.62, 997.38, 997.13, 
			996.86, 996.59, 996.31, 996.02, 995.71, 995.41, 995.09, 994.76, 994.43, 994.08]
	
		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaDensidad[valorTemperaturas[ind]]= valorDensidad[ind]
			tablaTemperaturaViscocidadCinematica[valorTemperaturas[ind]]=valorViscocidad[ind]
			viscosidadDinamicaDic[valorTemperaturas[ind]]=viscosidadDinamicaValor[ind]

		valorDensidadAgua = tablaTemperaturaDensidad[temperatura]
		viscosidadDinamica = viscosidadDinamicaDic[temperatura]
		viscosidadCinematica = tablaTemperaturaViscocidadCinematica[temperatura]


		listapropiedadesFisicasAgua.append(round(temperatura))
		listapropiedadesFisicasAgua.append(round(valorDensidadAgua,2))
		listapropiedadesFisicasAgua.append(round(viscosidadDinamica,9))
		listapropiedadesFisicasAgua.append(round(viscosidadCinematica,9))


		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listapropiedadesFisicasAgua[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolpropiedadesFisicasAgua,listaTemp)
		PasarExcelDatos(".\\ResultadosSedimentador\\PropiedadesFisicasDelAgua.xlsx",'Resultados',encabezadosLista,50, listapropiedadesFisicasAgua, 15, unidadesLista, 15,False,[], 50)
		propiedadesFisicasAguaWindow.mainloop()


	def verDatosParametrosEntrada(listaVerDatosParametrosEntrada,tipoCelda):
		
		'''
		listaEntradaParametrosBasicos=[tipoFloc = 0 ,tipoCelda = 1, materialTipoCelda =2 , dimensionesTipoCeldaMaterial =3 
		,anguloInclinacion =4
		,numeroUnidades =5,
		distanciaPlacas = 6, 
		caudalMedioEntry = 7, 
		factorMayoracionCaudalMD = 8,temperaturaEntry=  9]

		listaVerDatosParametrosEntrada = listaEntradaParametrosBasicos + [longitudPlacas = 10]

		listaCanaletasRecoleccionAgua = [distanciaCanaletasRecoleccion,longitudPlacas]
		listaTiempoRetencionTotalTanque = listaVerDatosParametrosEntrada + [distanciaVerticalDistribucionPlacas] + listaCanaletasRecoleccionAgua
		listaDimensionesDelSedimentador = listaTiempoRetencionTotalTanque + [bordeLibre,espesorMuros,pendienteTransversalTolva,anchoBasePlanaTolva] 
		listaDisenoSistemaEvacuacionLodos = listaDimensionesDelSedimentador + [velocidadMinimaArrastre,longitudPlacas, diametroNominalOrificionesMultipleDescarga]
		'''

		inicialesComboBox=["Seleccione el tipo de floc","Seleccione el tipo de celda",
		f"Seleccione el material de {tipoCelda}", f"Seleccione las dimensiones de {tipoCelda}", "Seleccione el n??mero de unidades","Seleccione la temperatura"]

		listaComboBox=[listaVerDatosParametrosEntrada[0],listaVerDatosParametrosEntrada[1],listaVerDatosParametrosEntrada[2],
		listaVerDatosParametrosEntrada[3],listaVerDatosParametrosEntrada[5], listaVerDatosParametrosEntrada[9]]
		listaSinComboBox=[listaVerDatosParametrosEntrada[4],listaVerDatosParametrosEntrada[6],
		listaVerDatosParametrosEntrada[7],listaVerDatosParametrosEntrada[8], listaVerDatosParametrosEntrada[10]]

		parametrosCombobox=list()

		for i in range(0,len(listaComboBox)):
			if listaComboBox[i].get()[0:10] == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta seleccionar {inicialesComboBox[i][10:].lower()}")
				return None	
			else:
				parametrosCombobox.append(listaComboBox[i].get())
		#Verifica que no sean nulos.
		if tipoCelda == "Conductos cuadrados":
			labels=["??ngulo de inclinaci??n", "lado interno de los conductos","caudal medio diario",
			"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por los m??dulos"]
		else: 

			labels=["??ngulo de inclinaci??n", "distancia entre placas","caudal medio diario",
			"factor de mayoraci??n del caudal m??ximo diario", "longitud ocupada por las placas"]


		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None

		try:
			if float(listaVerDatosParametrosEntrada[4].get()) != 60.0  :
				messagebox.showwarning(title="Error", message="El valor del ??ngulo de inclinaci??n solo puede ser 60??")	
				return None
			elif float(listaVerDatosParametrosEntrada[6].get())>6.0 or float(listaVerDatosParametrosEntrada[6].get())<5.0:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message=f"El valor del lado interno de los conductos cuadrados no puede ser menor que 5 ni mayor que 6.")	
					return None
				else: 
					messagebox.showwarning(title="Error", message=f"El valor de la distancia entre placas no puede ser menor que 5 ni mayor que 6.")	
					return None
			elif float(listaVerDatosParametrosEntrada[7].get())<0.01 or float(listaVerDatosParametrosEntrada[7].get())>0.2:
				messagebox.showwarning(title="Error", message="El valor del caudal medio diario debe estar entre 0.01 y 0.2")	
				return None
			elif float(listaVerDatosParametrosEntrada[8].get())>1.3 or float(listaVerDatosParametrosEntrada[8].get())<1:
				messagebox.showwarning(title="Error", message="El valor de factoraci??n de mayoraci??n del caudal m??ximo diario debe estar entre 1 y 1.3")	
				return None
			elif float(listaVerDatosParametrosEntrada[10].get())<2 or float(listaVerDatosParametrosEntrada[10].get())>12:
				if tipoCelda == "Conductos cuadrados":
					messagebox.showwarning(title="Error", message="La longitud ocupada por los m??dulos no puede ser menor que 2 ni mayor a 12")	
					return None
				else:
					messagebox.showwarning(title="Error", message="La longitud ocupada por las placas no puede ser menor que 2 ni mayor a 12")	
					return None
		except:
			messagebox.showwarning(title="Error", message="Alguno de los datos ingresados no es un n??mero.")
			return None	

		anguloInclinacion = float(listaVerDatosParametrosEntrada[4].get())
		distanciaPlacas = float(listaVerDatosParametrosEntrada[6].get())
		caudalMedio = float(listaVerDatosParametrosEntrada[7].get())
		factorMayoracionCaudalMD = float(listaVerDatosParametrosEntrada[8].get())
		longitudPlacas = float(listaVerDatosParametrosEntrada[10].get())

		tipoFloc = parametrosCombobox[0]
		tipoCelda = parametrosCombobox[1]
		materialTipoCelda = parametrosCombobox[2]
		dimensionesTipoCeldaMaterial = parametrosCombobox[3]
		numeroUnidades = parametrosCombobox[4]
		temperatura=  parametrosCombobox[5]






		VerDatosParametrosEntradaWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		VerDatosParametrosEntradaWindow.iconbitmap(bitmap=path)
		VerDatosParametrosEntradaWindow.geometry("725x420") 
		VerDatosParametrosEntradaWindow.resizable(0,0)	
		VerDatosParametrosEntradaWindow.configure(background="#9DC4AA")

		VerDatosParametrosEntradaFrame=LabelFrame(VerDatosParametrosEntradaWindow, text="Datos de entrada para par??metros b??sicos", font=("Yu Gothic bold", 11))
		VerDatosParametrosEntradaFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolVerDatosParametrosEntrada_frame = Frame(VerDatosParametrosEntradaFrame)
		arbolVerDatosParametrosEntrada_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolVerDatosParametrosEntrada_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolVerDatosParametrosEntrada_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolVerDatosParametrosEntrada= ttk.Treeview(arbolVerDatosParametrosEntrada_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set) #,xscrollcommand=sedScrollX.set)
		arbolVerDatosParametrosEntrada.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arbolVerDatosParametrosEntrada.xview)
		sedScrollY.configure(command=arbolVerDatosParametrosEntrada.yview)
		#Define columnas.
		arbolVerDatosParametrosEntrada["columns"]= (
		"1","Valores","Unidades")



		#Headings
		arbolVerDatosParametrosEntrada.heading("#0",text="ID", anchor=CENTER)



		for col in arbolVerDatosParametrosEntrada["columns"]:
			arbolVerDatosParametrosEntrada.heading(col, text=col,anchor=CENTER)	

		arbolVerDatosParametrosEntrada.column("#1",width=400, stretch=False)
		arbolVerDatosParametrosEntrada.column("#2",width=200, stretch=False)
		arbolVerDatosParametrosEntrada.column("#3",width=100, stretch=False)
		


		arbolVerDatosParametrosEntrada.column("#0",width=0, stretch=False)



		#Striped row tags
		arbolVerDatosParametrosEntrada.tag_configure("evenrow", background= "#1FCCDB")
		arbolVerDatosParametrosEntrada.tag_configure("oddrow", background= "#9DC4AA")


		listaVerDatosParametrosEntrada=list()


		if tipoCelda == "Conductos cuadrados":
			encabezadosLista=["Tipo de floc",
				"Tipo de celda",
				"Material de m??dulos de Conductos cuadrados",
				"Secci??n tranversal inclinada de m??dulos de Conductos cuadrados",
				"Espesor de pared de Conductos cuadrados",
				"??ngulo de inclinaci??n de Conductos cuadrados",
				"Eficiencia cr??tica para Conductos cuadrados",
				"Caudal de dise??o (QMD)",
				"N??mero de unidades",
				"Caudal por unidad",
				"Viscosidad cinem??tica",
				"Lado interno de Conductos cuadrados",
					]

		else:
			encabezadosLista=[
				"Tipo de floc",
				"Tipo de celda",
				"Material de Placas",
				"Dimensiones de Placas",
				"Espesor de Placas",
				"??ngulo de inclinaci??n de Placas",
				"Eficiencia cr??tica para Placas",
				"Caudal de dise??o (QMD)",
				"N??mero de unidades",
				"Caudal por unidad",
				"Viscosidad cinem??tica",
				"Distancia entre placas",
			]
		unidadesLista=[
			"",
			"",
			"",
			"mm x mm",
			"mm",
			"??",
			"",
			"m3/s",
			"und",
			"m3/s",
			"m2/s",
			"cm",
		]


		listaSalidaDatosEntradaPrametrosBasicosCalculos = datosEntradaParametrosBasicosCalculos(tipoFloc, tipoCelda, materialTipoCelda, dimensionesTipoCeldaMaterial, anguloInclinacion, numeroUnidades,distanciaPlacas, caudalMedio,factorMayoracionCaudalMD, temperatura)
		# listaSalida=[0 = tipoFloc,1 = tipoCelda,
		# 2= materialCelda, 3= dimensiones,
		# 4= espesor,5= anguloInclinacion,6= eficienciaCritica, 
		# 7=caudalDise??o, 8=numeroUnidades,
		# 9= caudalUnidad,10=viscosidadCinematica,11=distanciaPlacas]


	
		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			if i==10:
				listaTemp.append(round(listaSalidaDatosEntradaPrametrosBasicosCalculos[i],7))
			else:
				try:
					listaTemp.append(round(listaSalidaDatosEntradaPrametrosBasicosCalculos[i],3))
				except:
					listaTemp.append(listaSalidaDatosEntradaPrametrosBasicosCalculos[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolVerDatosParametrosEntrada,listaTemp)

		PasarExcelDatos(".\\ResultadosSedimentador\\VerParametrosEntrada.xlsx",'Resultados',encabezadosLista,50, listaSalidaDatosEntradaPrametrosBasicosCalculos, 15, unidadesLista, 15,False,[], 50)
		VerDatosParametrosEntradaWindow.mainloop()

	mainWindow.withdraw()
	sedWindow= tk.Toplevel()
	sedWindow.protocol("WM_DELETE_WINDOW", on_closing)
	path=resource_path('icons\\agua.ico')
	sedWindow.iconbitmap(bitmap=path)
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
	panel.add(frameSed, text="C??lculos")
	

	
	factorMayoracionCaudalMD = Entry(frameSed, width="15")
	factorMayoracionCaudalMD.focus()
	factorMayoracionCaudalMH = Entry(frameSed,width="15")
	caudalMedioEntry = Entry(frameSed,width="15")
	
	listaValoresTemp=list()
	for i in range(0,36):
		listaValoresTemp.append(f"{i}")
	
	temperaturaEntry = ttk.Combobox(frameSed, width="30", state="readonly",values=listaValoresTemp)
	temperaturaEntry.set("Seleccione la temperatura")
	
	
	


	oP1=["Floc de alumbre", "Floc con alumbre y polielectrolitos"]
	tipoFloc = ttk.Combobox(frameSed, width="51", state="readonly", values=oP1)
	tipoFloc.set("Seleccione el tipo de floc")
	oP2 = {
	"Placas planas paralelas": ("Acero inoxidable AISI 316","Polietileno alta densidad (HDPE)","Poliestireno de alto impacto(HIPS)") , 
	"Placas onduladas paralelas":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)"),
	"Conductos cuadrados":("Acrilonitrilo butadieno estireno (ABS)","Polipropileno (PP)")}
	
	
	#Cambiar "Seleccione el material del tipo de celda"

	def onComboboxSelect1(event):
		
		if tipoCelda.get() == "Conductos cuadrados":	
			materialTipoCelda.set(f"Seleccione el material de los {tipoCelda.get().lower()}")
			materialTipoCelda.config(values=oP2[tipoCelda.get()])
			anguloInclinacionLabel.config(text=f"??ngulo de inclinaci??n de {tipoCelda.get().lower()} [??]:")
			distanciaPlacasLabel.config(text=f"Lado interno de {tipoCelda.get().lower()} [5cm - 6cm]:")
			longitudPlacasLabel.config(text="Longitud ocupada por los m??dulos [2m - 12m]:")
			materialTipoCeldaLabel.config(text=f"Seleccione el material los {tipoCelda.get().lower()}:")	
			dimensionesCeldaLabel.config(text=f"Seleccione las dimensiones de la secci??n tranversal inclinada [mm x mm]:", font=("Yu Gothic",7))	
			dimensionesTipoCeldaMaterial.set(f"Seleccione las dimensiones del {tipoCelda.get().lower()}")



		else:
			materialTipoCelda.set(f"Seleccione el material de las {tipoCelda.get().lower()}")
			materialTipoCelda.config(values=oP2[tipoCelda.get()])
			anguloInclinacionLabel.config(text=f"??ngulo de inclinaci??n {tipoCelda.get().lower()} [??]:")
			distanciaPlacasLabel.config(text="Distancia entre placas [5cm - 6cm]:")
			longitudPlacasLabel.config(text="Longitud ocupada por las placas [2m - 12m]:")
			materialTipoCeldaLabel.config(text=f"Seleccione el material de las {tipoCelda.get().lower()}:")	
			dimensionesCeldaLabel.config(text=f"Seleccione las dimensiones de las {tipoCelda.get().lower()} [mm x mm]:",font=("Yu Gothic",7)) 
			dimensionesTipoCeldaMaterial.set(f"Seleccione las dimensiones del {tipoCelda.get().lower()}")
			
		

	def onComboboxSelect2(event):
		dimensionesTipoCeldaMaterial.set(f"Seleccione las dimensiones del {tipoCelda.get().lower()}")
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
			dimensionesTipoCeldaMaterial.set("Seleccione las dimensiones")
		for i in range(0,len(combinacionesTipoCeldaMaterial)):
			if ((tipoCelda.get(),materialTipoCelda.get())== combinacionesTipoCeldaMaterial[i]):
				dimensionesTipoCeldaMaterial.config(values=dimensiones[i])
		

	tipoCelda = ttk.Combobox(frameSed, width="51", state="readonly",values=tuple(oP2.keys()))
	tipoCelda.bind("<<ComboboxSelected>>", onComboboxSelect1)
	tipoCelda.set("Seleccione el tipo de celda")
	

	materialTipoCelda = ttk.Combobox(frameSed, width="51", state="readonly")
	materialTipoCelda.bind("<<ComboboxSelected>>", onComboboxSelect2)
	materialTipoCelda.set("Seleccione el material del tipo de celda")
	
	dimensionesTipoCeldaMaterial = ttk.Combobox(frameSed, width="51", state="readonly")
	dimensionesTipoCeldaMaterial.set("Seleccione las dimensiones")
	

	
	
	anguloInclinacion = Entry(frameSed, width=6)
	numeroUnidades = ttk.Combobox(frameSed, width="51", state="readonly",values=["2","3","4","5","6","7","8"])
	numeroUnidades.set("Seleccione el n??mero de unidades")
	distanciaPlacas = Entry(frameSed, width=6)
	longitudPlacas = Entry(frameSed,width=6)
	distanciaCanaletasRecoleccion = Entry(frameSed,width=15)
	distanciaVerticalDistribucionPlacas = Entry(frameSed,width=15)
	bordeLibre = Entry(frameSed,width=15)
	espesorMuros = Entry(frameSed,width=15)
	pendienteTransversalTolva = Entry(frameSed,width=15)
	anchoBasePlanaTolva = Entry(frameSed,width=15)
	velocidadMinimaArrastre = Entry(frameSed, width=15)

	diametroNominalLista= ['1/2 (RDE 9)',
		'3/4 (RDE 11)',
		'3/4 (RDE 21)',
		'1 (RDE 13,5)',
		'1 (RDE 21)',
		'1 1/4 (RDE 21)',
		'1 1/2 (RDE 21)',
		'2 (RDE 21)']
	
	diametroNominalOrificionesMultipleDescarga = ttk.Combobox(frameSed, width="65", state="readonly",values= diametroNominalLista)
	diametroNominalOrificionesMultipleDescarga.set("Seleccione el di??metro nominal de los orificios del m??ltiple de descarga")
	
	

	lista_entradas=[factorMayoracionCaudalMD,
	factorMayoracionCaudalMH,caudalMedioEntry,
	temperaturaEntry, 
	tipoFloc,
	tipoCelda,
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

	#BorrarSed
	# listaTemporalEntradas= ["1.3",
	# 		"1.6",
	# 		"0.04404",
	# 		"3",
	# 		"Floc de alumbre",
	# 		"Conductos cuadrados",
	# 		"Polipropileno (PP)",
	# 		"1200 x 3000",
	# 		"60.00",
	# 		"7",
	# 		"5.00",
	# 		"5.857",
	# 		"0.900",
	# 		"0.600",
	# 		"0.300",
	# 		"0.300",
	# 		"55",
	# 		"0.10",
	# 		"0.01",
	# 		"3/4 (RDE 11)"]
		
	# for i in range(0,len(lista_entradas)):
	# 	try:
	# 		lista_entradas[i].set(listaTemporalEntradas[i])
	# 	except:
	# 		lista_entradas[i].insert(0, listaTemporalEntradas[i])
			

	
	
	labelIntroduccion = Label(frameSed, text="Datos de entrada para par??metros b??sicos: ",font=("Yu Gothic bold",10))
	caudalDise??oLabel = Label(frameSed, text="Caudales de dise??o:", font =("Yu Gothic bold",8))
	factorMayoracionCaudalMDLabel = Label(frameSed, text="Factor de mayoraci??n del caudal m??ximo diario [1 - 1.3] m^3/s:", font =("Yu Gothic",8))
	factorMayoracionCaudalMHLabel = Label(frameSed, text="Factor mayoraci??n del caudal m??ximo horario [0.01 - 0.2] m^3/s:", font =("Yu Gothic",8))
	caudalEntryLabel = Label(frameSed, text="Caudal de dise??o [[0.01 - 0.2]m^3/s]: ", font =("Yu Gothic",9))
	propiedadesFisicasAguaLabel = Label(frameSed, text="Propiedades f??sicas del agua a tratar.\nSeleccione la temperatura del agua:", font =("Yu Gothic bold",10))
	datosEntradaParametrosBasicosLabel = Label(frameSed, text="Datos de entrada para par??metros b??sicos.", font =("Yu Gothic bold",10))
	anguloInclinacionLabel = Label(frameSed, text="??ngulo de inclinaci??n [??]:", font =("Yu Gothic",8))
	distanciaPlacasLabel = Label(frameSed, text="Distancia del tipo de celda [5cm - 6cm]:", font =("Yu Gothic",8))
	longitudPlacasLabel = Label(frameSed, text="Longitud del tipo de celda [2m - 12m]:", font =("Yu Gothic",8))
	distanciaCanaletasRecoleccionLabel = Label(frameSed, text="Distancia entre las canaletas de recolecci??n [0.9m - 1.2m]: ", font =("Yu Gothic",8))
	distanciaVerticalDistribucionPlacasLabel = Label(frameSed, text="Distancia vertical de orificios de distribuci??n [0.6m y 0.9m]:", font =("Yu Gothic",8))	
	bordeLibreLabel= Label(frameSed, text="Borde libre [0.3m - 0.5m]:", font =("Yu Gothic",8))	
	espesorMurosLabel = Label(frameSed, text="Espesor de muros de concreto [0.3m - 0.5m]:", font =("Yu Gothic",8))	
	pendienteTransversalTolvaLabel = Label(frameSed, text="Pendiente transversal de la tolva de lodos [45?? - 60??]:", font =("Yu Gothic",8))	
	anchoBasePlanaTolvaLabel = Label(frameSed, text="Ancho de la base plana de la tolva de lodos [0.1m - 0.2m]:", font =("Yu Gothic",8))	
	velocidadMinimaArrastreLabel = Label(frameSed, text="Velocidad m??nima de arrastre asignada [0.01 m/s - 0.02 m/s]", font =("Yu Gothic",8))	

	
	tipoFlocLabel = Label(frameSed, text="Seleccione el tipo de floc:", font =("Yu Gothic",8))	
	tipoCeldaLabel = Label(frameSed, text="Seleccione el tipo de celda:", font =("Yu Gothic",8))	
	materialTipoCeldaLabel= Label(frameSed, text="Seleccione el material del tipo de celda:", font =("Yu Gothic",8))	
	dimensionesCeldaLabel= Label(frameSed, text="Seleccione las dimensiones del tipo de celda [mm x mm]:", font =("Yu Gothic",8))	
	numeroUnidadesLabel= Label(frameSed, text="Seleccione el n??mero de unidades [und]:", font =("Yu Gothic",8))	
	diametroNominalOrificionesMultipleDescargaLabel = Label(frameSed, text="Seleccione el di??metro nominal de los orificios del m??ltiple de descarga [pulg]:", font =("Yu Gothic",8))	

	listaLabelAdicionales=[tipoFlocLabel, tipoCeldaLabel, materialTipoCeldaLabel,
	dimensionesCeldaLabel,numeroUnidadesLabel, diametroNominalOrificionesMultipleDescargaLabel]
	
	listaLabels=[labelIntroduccion,
	caudalDise??oLabel,
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
	
	#voler
	listaLabelReiniciar =[anguloInclinacionLabel, distanciaPlacasLabel, longitudPlacasLabel, materialTipoCeldaLabel,dimensionesCeldaLabel]
	
	
	#ListasEntradasBotonesSed

	listaEntradaParametrosBasicos=[tipoFloc,tipoCelda, materialTipoCelda, dimensionesTipoCeldaMaterial,anguloInclinacion,numeroUnidades,
	distanciaPlacas, caudalMedioEntry, factorMayoracionCaudalMD,temperaturaEntry]
	listaDeterminacionParametrosBasicosDiseno = listaEntradaParametrosBasicos + [longitudPlacas] 
	listaCanaletasRecoleccionAgua = [distanciaCanaletasRecoleccion,longitudPlacas]
	listaTiempoRetencionTotalTanque = listaDeterminacionParametrosBasicosDiseno + [distanciaVerticalDistribucionPlacas] + [distanciaCanaletasRecoleccion]
	listaDimensionesDelSedimentador = listaTiempoRetencionTotalTanque + [bordeLibre,espesorMuros,pendienteTransversalTolva,anchoBasePlanaTolva] 
	listaDisenoSistemaEvacuacionLodos = listaDimensionesDelSedimentador + [velocidadMinimaArrastre, diametroNominalOrificionesMultipleDescarga]  
	listaCaudalesDise??o = [factorMayoracionCaudalMD, factorMayoracionCaudalMH,caudalMedioEntry]
	

	pathAtras= resource_path('images\\atras.png')
	imageAtras= PhotoImage(file=pathAtras)
	#BotonesSed.
	botonAtras= HoverButton(frameSed, image=imageAtras, width=100, height=40, bg= None, command=lambda: returnMainWindow(sedWindow))
	botonAtras.place(x=0,y=10)
	
	botonParametrosDeDise??oSedimentadorAltaTasa = HoverButton(frameSed, text="Par??metros de dise??o de sedimentadores de alta tasa", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: parametrosDeDise??oSedimentadorAltaTasa())
	botonDeterminacionParametrosBasicosDiseno = HoverButton(frameSed, text="Determinaci??n de par??metros b??sicos de dise??o", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: determinacionParametrosBasicosDiseno(listaDeterminacionParametrosBasicosDiseno, tipoCelda.get()))
	botonCanaletasRecoleccionAgua = HoverButton(frameSed, text="Canaletas de recolecci??n de agua clarificada", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: canaletasRecoleccionAgua(listaCanaletasRecoleccionAgua,tipoCelda.get()))
	botonTiempoRetencionTotalTanque = HoverButton(frameSed, text="Tiempo de retenci??n total en el tanque", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: tiempoRetencionTotalTanque(listaTiempoRetencionTotalTanque,tipoCelda.get()))
	botonDimensionesDelSedimentador = HoverButton(frameSed, text="Dimensiones del sedimentador", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: dimensionesDelSedimentador(listaDimensionesDelSedimentador, tipoCelda.get()))
	botonDisenoSistemaEvacuacionLodos = HoverButton(frameSed, text="Dise??o del sistema de evacuaci??n de lodos", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: disenoSistemaEvacuacionLodos(listaDisenoSistemaEvacuacionLodos,tipoCelda.get()))
	
	botonAyudaVisualSed = HoverButton(frameSed, text="Ayuda visual-\nGeometr??a del sedimentador", activebackground="#9DC4AA", width=40, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: proyectarImg("images\\VistaSedimentador.png",802,625))
	
	botonCaudalesDeDise??o = HoverButton(frameSed, text="Caudales de dise??o", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: caudalesDeDise??o(listaCaudalesDise??o))
	botonPropiedadesFisicasAgua = HoverButton(frameSed, text="Propiedades f??sica del agua a tratar", activebackground="#9DC4AA", width=60, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: propiedadesFisicasAgua(temperaturaEntry))
	botonVerDatosEntradaParametrosBasicos = HoverButton(frameSed, text="Ver datos de entrada\npara par??metros b??sicos", activebackground="#9DC4AA", width=40, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: verDatosParametrosEntrada(listaDeterminacionParametrosBasicosDiseno,tipoCelda.get()))

	botonLimpiarEntradas = HoverButton(frameSed, text="Limpiar entradas", activebackground="#9DC4AA", width=40, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntrySed(lista_entradas,listaLabelReiniciar))



	listaBotones=[
	botonCaudalesDeDise??o,
	botonParametrosDeDise??oSedimentadorAltaTasa,
	botonPropiedadesFisicasAgua,
	botonVerDatosEntradaParametrosBasicos,
	botonDeterminacionParametrosBasicosDiseno,
	botonCanaletasRecoleccionAgua,
	botonTiempoRetencionTotalTanque, 
	botonDimensionesDelSedimentador,
	botonDisenoSistemaEvacuacionLodos, 
	botonLimpiarEntradas,
	botonAyudaVisualSed]

	
	#UbicacionElementos


	yInicial= 60
	yInicial2=50
	yInicial3=50
	#0,1,5,7
	j=0
	m=0
	for i in range(0, len(listaLabels)):
		if i<7:

			if i==0 or i==1 or i==5:
				listaLabels[i].place(x=0, y=yInicial)
				yInicial=yInicial + 40
			else:
				lista_entradas[j].place(x=330, y=yInicial)
				listaLabels[i].place(x=0, y=yInicial)
				yInicial=yInicial + 40
				j=j+1
		
		elif 7<=i<16 :
			if i==7:
				yInicial2= yInicial2 - 50 
				listaLabels[i].place(x=450, y=yInicial2)
				yInicial2=yInicial2 + 40
			else:
				if i==11 or i==13 or i==14:
					if m<=4:
						listaLabelAdicionales[m].place(x=450, y=yInicial2-20)
						m=m+1
					lista_entradas[j].place(x=730, y=yInicial2)
					listaLabels[i].place(x=450, y=yInicial2)
					yInicial2=yInicial2 + 25
					j=j+1
				else:
					if m<=4:
						if m==4:
							pass
						else:
							listaLabelAdicionales[m].place(x=450, y=yInicial2-20)
							m=m+1
					lista_entradas[j].place(x=730, y=yInicial2)
					listaLabels[i].place(x=450, y=yInicial2)
					yInicial2=yInicial2 + 45
					j=j+1
					
		else:
				if i == (len(listaLabels)-1):
					listaLabelAdicionales[m].place(x=800, y= yInicial3)
					listaLabels[i].place(x=800, y=yInicial3+30)
					yInicial3=yInicial3 + 30
				else:
					lista_entradas[j].place(x=1123, y=yInicial3)
					listaLabels[i].place(x=800, y=yInicial3)
					yInicial3=yInicial3 + 30
				
				j=j+1
		i=i+1


		varX= [0, 450, 800]
		yBotones=yInicial
		yBotones1=yInicial

		# listaBotones=[
		# 	botonCaudalesDeDise??o,
		# 	botonParametrosDeDise??oSedimentadorAltaTasa,
		# 	botonPropiedadesFisicasAgua,
		# 	botonVerDatosEntradaParametrosBasicos,
		# 	botonDeterminacionParametrosBasicosDiseno,
		# 	botonCanaletasRecoleccionAgua,
		# 	botonTiempoRetencionTotalTanque, 
		# 	botonDimensionesDelSedimentador,
		# 	botonDisenoSistemaEvacuacionLodos, 
		# 	botonLimpiarEntradas]
		listaBotones=[
		botonCaudalesDeDise??o,
		botonParametrosDeDise??oSedimentadorAltaTasa,
		botonPropiedadesFisicasAgua,
		botonDeterminacionParametrosBasicosDiseno,
		botonCanaletasRecoleccionAgua,
		botonTiempoRetencionTotalTanque, 
		botonDimensionesDelSedimentador,
		botonDisenoSistemaEvacuacionLodos, 
		botonAyudaVisualSed,
		botonLimpiarEntradas,
		botonVerDatosEntradaParametrosBasicos,]
		listaBotones[8].place(x=470,y=yBotones)
		listaBotones[9].place(x=470,y=yBotones+50)
		listaBotones[10].place(x=470,y=yBotones+100)
		for i in range(0,8):
			if i<4:
				listaBotones[i].place(x=varX[0],y=yBotones)
				yBotones=yBotones+50
			else:
				listaBotones[i].place(x=varX[2],y=yBotones1)
				yBotones1=yBotones1+50

	
	##CalculosAdicionalesDatosEntradaB??sicos


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
		path=resource_path('icons\\agua.ico')
		caracFiltroWindow.iconbitmap(bitmap=path)
		caracFiltroWindow.geometry("400x500") 
		caracFiltroWindow.resizable(0,0)	
		caracFiltroWindow.configure(background="#9DC4AA")
		
		#Frame Treeview
		arbolCaracFiltro_frame = LabelFrame(caracFiltroWindow, text="Principales caracter??siticas del filtro", font=("Yu Gothic bold", 11))
		arbolCaracFiltro_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolCaracFiltro_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolCaracFiltro_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCaracFiltro= ttk.Treeview(arbolCaracFiltro_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set)#,xscrollcommand=sedScrollX.set
		arbolCaracFiltro.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arbolCaracFiltro.xview)
		sedScrollY.configure(command=arbolCaracFiltro.yview)
		#Define columnas.
		arbolCaracFiltro["columns"]= (
		"Denominaci??n","Valor"
		)

		#Headings
		arbolCaracFiltro.heading("#0",text="ID", anchor=CENTER)
		
		for col in arbolCaracFiltro["columns"]:
			arbolCaracFiltro.heading(col, text=col,anchor=CENTER)

		
	
		arbolCaracFiltro.column("#2",width=200, stretch=False)
		arbolCaracFiltro.column("#1",width=200, stretch=False)
		arbolCaracFiltro.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolCaracFiltro.tag_configure("oddrow", background= "#1FCCDB")
		arbolCaracFiltro.tag_configure("evenrow", background= "#9DC4AA")

		col1=["Tipo de filtro","Medio filtrante","Distribuci??n del medio","Tasa media de filtraci??n","Tasa m??xima de filtraci??n","Duraci??n de carrera","P??rdida de carga inicial","P??rdida de carga final","Uso de agua tratada en lavado","Profundida del medio","Profundidad de grava","Drenaje"]
		col2=["Filtro r??pido de arena","Arena","Estratigicado de fino a grueso","120 m/d","150 m/d","12 - 36 horas", "0,3 m","2,4 - 3,0 m","2-4%","0,60-0,75 m","0,30-0,45 m","Tuber??a Perforada"]

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
		# Pediente
		colsDatos=[col1,col2]

		pasarTreeViewExcel(colsDatos,arbolCaracFiltro,'.\\ResultadosFiltro\\VerPrincipalesCaracteristicasDelFiltro.xlsx')
		
		
		
		caracFiltroWindow.mainloop()

	def granulometria(lista1,lista2):
		
		def buscarEnTabla(NumTamiz,tablaDic):
			return tablaDic[NumTamiz]

		listaNTamizTemp=lista1.copy()
		listaARetenidaTemp=lista2.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de los n??meros de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de la arena retenida.")
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
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores est??ndar para n??mero de tamiz. Pulse el bot??n para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de n??mero de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None

		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de n??mero de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento

			
		

		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None
	


	

		granulometriaWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		granulometriaWindow.iconbitmap(bitmap=path)
		granulometriaWindow.geometry("1000x500") 
		granulometriaWindow.resizable(0,0)	
		granulometriaWindow.configure(background="#9DC4AA")
		
		#Frame principal
		granulometriaFrame=LabelFrame(granulometriaWindow, text="Granulometr??a del medio filtrante de arena", font=("Yu Gothic bold", 11))
		granulometriaFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolgranulometria_frame = LabelFrame(granulometriaFrame, text="Principales caracter??siticas del filtro", font=("Yu Gothic bold", 11))
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
		"N??mero de tamiz",
		"Arena retenida [%]", 
		"Tamiz que retiene", 
		"Tama??o de abertura del tamiz [mm] (OD)", 
		"Acumulado de arena que pasa [%] (OD)", 
		"Tama??o de abertura del tamiz [mm] (OA)", 
		"Acumulado de arena que pasa [%](OA)" 
		)
		
		
		#Headings
		arbolGranulometria.heading("#0",text="ID", anchor=CENTER)
		
		for col in arbolGranulometria["columns"]:
			arbolGranulometria.heading(col, text=col,anchor=CENTER)

		listaLargoFila=[0,200,200,200,400,400,400,400]
		for i in range(1,len(arbolGranulometria["columns"])+1):
				arbolGranulometria.column(f"#{i}",width=listaLargoFila[i], stretch=False)	
		

		
		
	
		arbolGranulometria.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolGranulometria.tag_configure("oddrow", background= "#1FCCDB")
		arbolGranulometria.tag_configure("evenrow", background= "#9DC4AA")


		#Insersi??n datos.
		global contadorFiltro
		contadorFiltro = 0

		listaEntradaTemp=list()
		datosSalida=list()
		
		
		
		
		#Tabla Tama??o Abertura Tamiz
		Tama??oTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
		Tama??oAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
		tablaTama??oAberturaTamiz=dict()
		for ind in range(0, len(Tama??oTamiz)):
			tablaTama??oAberturaTamiz[Tama??oTamiz[ind]] = Tama??oAbertura[ind]

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
	
		col1=list()
		col2=list()
		col3=list()
		col4=list()
		col5=list()
		col6=list()
		col7=list()


		longListaARetenida=len(listaARetenida)-1
		for ind in range(0, len(listaARetenida)):
			listaEntradaTemp.clear()
			
			listaEntradaTemp.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
			col1.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
			extremoDerecho=listaNTamizExtremo[ind]
			listaEntradaTemp.append(listaARetenida[ind])
			col2.append(listaARetenida[ind])
			listaEntradaTemp.append(extremoDerecho)
			col3.append(extremoDerecho)
			listaEntradaTemp.append(tablaTama??oAberturaTamiz[extremoDerecho])
			col4.append(tablaTama??oAberturaTamiz[extremoDerecho])
			listaEntradaTemp.append(round(listaAcumuladoArenaDescendente[ind],3))
			col5.append(round(listaAcumuladoArenaDescendente[ind],3))
			listaEntradaTemp.append(round(tablaTama??oAberturaTamiz[listaNTamizExtremo[longListaARetenida-ind]],3))
			col6.append(round(tablaTama??oAberturaTamiz[listaNTamizExtremo[longListaARetenida-ind]],3))
			listaEntradaTemp.append(round(listaAcumuladoArenaAscendente[ind],3))
			col7.append(round(listaAcumuladoArenaAscendente[ind],3))
			listaIntermedia = listaEntradaTemp.copy()
			datosSalida.append(listaIntermedia)
			newDataTreeview(arbolGranulometria, listaEntradaTemp)
		
		colsDatos=[col1,col2,col3,col4,col5,col6,col7]
		#volver
		pasarTreeViewExcel(colsDatos,arbolGranulometria,'.\\ResultadosFiltro\\GranulometriaMedioFiltranteArena.xlsx')

		

		
		granulometriaWindow.mainloop()

	def coeficienteDeUniformidad(lista1,lista2):

		def buscarEnTabla(NumTamiz,tablaDic):
			return tablaDic[NumTamiz]

		listaNTamizTemp=lista1.copy()
		listaARetenidaTemp=lista2.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de los n??meros de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de la arena retenida.")
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
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores est??ndar para n??mero de tamiz. Pulse el bot??n para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de n??mero de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de n??mero de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento
		
		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None
	

		coeficienteDUWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		coeficienteDUWindow.iconbitmap(bitmap=path)
		coeficienteDUWindow.geometry("600x120") 
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
		# sedScrollY=Scrollbar(arbolCoeficienteDU_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCoeficienteDU= ttk.Treeview(arbolCoeficienteDU_frame,selectmode=BROWSE, height=2,show="tree headings",xscrollcommand=sedScrollX.set)#,yscrollcommand=sedScrollY.set)
		arbolCoeficienteDU.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolCoeficienteDU.xview)
		#sedScrollY.configure(command=arbolCoeficienteDU.yview)
		#Define columnas.
		arbolCoeficienteDU["columns"]= (
		"Tama??o Efectivo d{} [mm]".format(getSub("10")),
        "Tama??o Efectivo d{} [mm]".format(getSub("60")),
        "Coeficiente de uniformidad. CU= d{}/d{}".format(getSub("60"),getSub("10"))
		)
		

		

		#Headings
		arbolCoeficienteDU.heading("#0",text="ID", anchor=CENTER)
		
		arbolCoeficienteDU.heading("#1", text="Tama??o Efectivo d{} [mm]".format(getSub("10")), anchor=CENTER, command= lambda: tama??od(x1,y1,x2,y2,10))
		arbolCoeficienteDU.heading("#2", text="Tama??o Efectivo d{} [mm]".format(getSub("60")), anchor=CENTER, command= lambda: tama??od(X1,Y1,X2,Y2,60))
		arbolCoeficienteDU.heading("#3", text="Coeficiente de uniformidad. CU = d{}/d{}".format(getSub("60"),getSub("10")), anchor=CENTER)

		"""for col in arbolCoeficienteDU["columns"]:
			arbolCoeficienteDU.heading(col, text=col,anchor=CENTER)"""
		


		
		for i in range(0,len(arbolCoeficienteDU["columns"])+1) :
				arbolCoeficienteDU.column(f"#{i}",width=300, stretch=False)	
	
		arbolCoeficienteDU.column("#0",width=0, stretch=False)
		arbolCoeficienteDU.column("#3",width=400, stretch=False)

		#Striped row tags
		arbolCoeficienteDU.tag_configure("oddrow", background= "#1FCCDB")
		arbolCoeficienteDU.tag_configure("evenrow", background= "#1FCCDB")
		# arbolCoeficienteDU.tag_configure("evenrow", background= "#9DC4AA")


		#Insersi??n datos.
		global contadorFiltro
		contadorFiltro = 0

		listaEntradaTemp=list()
		datosSalida=list()
		

		
		
		#Tabla Tama??o Abertura Tamiz
		Tama??oTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
		Tama??oAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
		tablaTama??oAberturaTamiz=dict()
		for ind in range(0, len(Tama??oTamiz)):
			tablaTama??oAberturaTamiz[Tama??oTamiz[ind]] = Tama??oAbertura[ind]

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
			listaEntradaTemp.append(tablaTama??oAberturaTamiz[extremoDerecho])
			listaEntradaTemp.append(listaAcumuladoArenaDescendente[ind])
			listaEntradaTemp.append(tablaTama??oAberturaTamiz[listaNTamizExtremo[longListaARetenida-ind]])
			listaEntradaTemp.append(listaAcumuladoArenaAscendente[ind])
			listaIntermedia = listaEntradaTemp.copy()
			datosSalida.append(listaIntermedia)
		
		abAcDic= dict()
		for ind in range(0,len(datosSalida)):
			abAcDic[datosSalida[ind][6]]=datosSalida[ind][5]
		
		

		def tama??oEfectivod1(numero,dic):
			elementoAnterior=dic[0]
			for elemento in dic:
				if elemento <= numero and elemento>=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda

		def tama??oEfectivod2(numero,dic):
			elementoAnterior=100
			for elemento in dic:
				if elemento >= numero and elemento<=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda
		def tama??oEfectivod(numero,dic):
			return[tama??oEfectivod1(numero,dic), tama??oEfectivod2(numero,dic)]

		def calculo1CU(numero,x1,y1,x2,y2):
			return(log10(x1)+(((numero-y1)/(y2-y1))*log10(x2/x1)))
		def calculo2CU(numero,x1,y1,x2,y2):
			return (10**(calculo1CU(numero,x1,y1,x2,y2)))
		
		#Calculo Tama??o Efectivo d10:
		listaAcumuladoCU10=tama??oEfectivod(10,abAcDic)
		y1=listaAcumuladoCU10[0]
		y2=listaAcumuladoCU10[1]
		x1=abAcDic[y1]
		x2=abAcDic[y2]
		d10= calculo2CU(10,x1,y1,x2,y2)
		listaAcumuladoCU60=tama??oEfectivod(60,abAcDic)
		Y1= listaAcumuladoCU60[0]
		Y2= listaAcumuladoCU60[1]
		X1= abAcDic[Y1]
		X2=	abAcDic[Y2]
		d60= calculo2CU(60,X1,Y1,X2,Y2)
		CU=d60/d10
		listaIngreso=[round(d10,3),round(d60,3),round(CU,3)]
		
		newDataTreeview(arbolCoeficienteDU,listaIngreso)

		
		col1=[round(d10,3)]
		col2=[round(d60,3)]
		col3=[round(CU,3)]
		DatosCols=[col1,col2,col3]
		pasarTreeViewExcel(DatosCols,arbolCoeficienteDU,'.\\ResultadosFiltro\\CoeficienteDeUniformidad.xlsx')

		def tama??od(x1,y1,x2,y2,numero):
			tama??oD10Window = tk.Toplevel()
			path=resource_path('icons\\agua.ico')
			tama??oD10Window.iconbitmap(bitmap=path)
			tama??oD10Window.geometry("1200x220") 
			tama??oD10Window.resizable(0,0)	
			tama??oD10Window.configure(background="#9DC4AA")
			coeficienteDUFrame10=LabelFrame(tama??oD10Window, text="Tama??o Efectio d{} del medio filtrante".format(getSub(f"{numero}")), font=("Yu Gothic bold", 11))
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
			"Tama??o de abertura del tamiz [mm]",
			"Acumulado de arena que pasa [%]",
			"Tama??o d{} [mm]".format(getSub(f"{numero}"))
			)

			#Headings
			arbolCoeficienteDU10.heading("#0",text="ID", anchor=CENTER)
			for col in arbolCoeficienteDU10["columns"]:
				arbolCoeficienteDU10.heading(col, text=col,anchor=CENTER)
		
			listaAnchos=[0,250,300,350,150]
			for i in range(0,len(arbolCoeficienteDU10["columns"])):
					arbolCoeficienteDU10.column(f"#{i}",width=listaAnchos[i], stretch=False)		
			arbolCoeficienteDU10.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolCoeficienteDU10.tag_configure("oddrow", background= "#1FCCDB")
			arbolCoeficienteDU10.tag_configure("evenrow", background= "#9DC4AA")

			lista1=list()
			lista2=list()
			lista1.append("(x1,y1)")
			lista1.append(round(x1,3))
			lista1.append(round(y1,3))
			lista1.append(round((calculo2CU(numero,x1,y1,x2,y2)),3))
			lista2.append("(x2,y2)")
			lista2.append(round(x2,3))
			lista2.append(round(y2,3))
			lista2.append(round((calculo2CU(numero,x1,y1,x2,y2)),3))
			listaInsertar=[lista1,lista2]
			
			
			# for i in range(len(listaEncabezados)):
			# 	listaTemp=list()
			# 	listaTemp.append(listaEncabezados[i])
			# 	listaTemp.append(lista1[i])
			# 	listaTemp.append(lista2[i])
			for i in range(0, len(listaInsertar)):
				newDataTreeview(arbolCoeficienteDU10,listaInsertar[i])



		coeficienteDUWindow.mainloop()

	def calcularPEArena(listaNTamiz,listaARetenida,listaE,valorTemperatura):
		listaEU=list()
		

		
		i=0
		listaLabels=["Error con el tipo de grano","profundidad del lecho fijo de arena","densidad relativa de la arena",
		"porosidad del lecho fijo","constante de filtraci??n","Error en tasa filtraci??n"]
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
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None
			
		listaEU.append(float(valorTemperatura))

		# listaEntradas=[TipoGranoArena, profundidadLechoFijoArena, densidadRelativaArena,
		# porosidadLechoFijo,constanteFiltracionFH,Tasa]
		

		profundidadLechoFijo = listaEU[1]
		densidadRelativaArena= listaEU[2]
		porosidadLechoFijo= listaEU[3]
		constanteFiltracionFH = listaEU[4]

		listaRestricciones= [profundidadLechoFijo, densidadRelativaArena, porosidadLechoFijo,constanteFiltracionFH]
		listaLabelsRestricciones=["profundidad del lecho fijo de arena",
		"densidad relativa de la arena","porosidad del lecho fijo",]
		restriccionesCarac=["0.60 y 0.75","2.50 y 2.70","0.40 y 0.48"]

		for i in range(0, len(listaLabelsRestricciones)):
			inf= float(restriccionesCarac[i][0:4])
			sup= float(restriccionesCarac[i][7:])
			if listaRestricciones[i]< inf or  listaRestricciones[i]> sup:
				messagebox.showwarning(title="Error", message=f"El valor de la {listaLabelsRestricciones[i]} debe estar entre {inf} y {sup}")
				return None
				
		if constanteFiltracionFH != 5:
			messagebox.showwarning(title="Error", message=f"El valor de la constante de filtraci??n (Fair - Hatch) debe ser 5")
			return None
		
		

		

		estimacionPerdidaArenaCalculoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		estimacionPerdidaArenaCalculoWindow.iconbitmap(bitmap=path)
		estimacionPerdidaArenaCalculoWindow.geometry("1000x500") 
		estimacionPerdidaArenaCalculoWindow.resizable(0,0)	
		estimacionPerdidaArenaCalculoWindow.configure(background="#9DC4AA")
		global contadorFiltro

		if listaEU[0] != "Afilada":

			##Panel:
			panelFiltro = ttk.Notebook(estimacionPerdidaArenaCalculoWindow)
			panelFiltro.pack(fill=BOTH, expand=TRUE)
			###########Frame Principal1
			estimacionPerdidaArenaFHFrame=LabelFrame(panelFiltro, text=f"Estimaci??n de la p??rdida de energ??a en le lecho filtrante de arena limpio a {TasaCopy.lower()}.", font=("Yu Gothic bold", 11))
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
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"arena retenida/tama??o promedio geom??trico[1/(m^2)]",
			"Fair-Hatch"
			)

			#Headings
			arbolEstimacionPerdidaArenaFH.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaFH["columns"]:
				arbolEstimacionPerdidaArenaFH.heading(col, text=col,anchor=CENTER)	

			listaLargoFila=[0,200,200,430,430,350,500,200]
			for i in range(1,len(arbolEstimacionPerdidaArenaFH["columns"])+1):
					arbolEstimacionPerdidaArenaFH.column(f"#{i}",width=listaLargoFila[i], stretch=False)	

			
			arbolEstimacionPerdidaArenaFH.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolEstimacionPerdidaArenaFH.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaFH.tag_configure("evenrow", background= "#9DC4AA")
			
			################Frame principal2
			estimacionPerdidaArenaCKFrame=LabelFrame(panelFiltro, text="Estimaci??n de la p??rdida de energ??a en le lecho filtrante de arena limpio.", font=("Yu Gothic bold", 11))
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
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"N??mero de Reynolds", 
			"Factor de fricci??n",
			"[p/(d{})^2]".format(getSub("g")),
			"P??rdida de cabeza hidr??ulica total",
			"p/d{}".format(getSub("g")),
			"Coeficiente de permeabilidad",
			)

			#Headings
			arbolEstimacionPerdidaArenaCK.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaCK["columns"]:
				arbolEstimacionPerdidaArenaCK.heading(col, text=col,anchor=CENTER)	

			listaLargoFila=[0,200,200,430,430,350,200,200,100,300,100,300]
			for i in range(1,len(arbolEstimacionPerdidaArenaCK["columns"])+1):
					arbolEstimacionPerdidaArenaCK.column(f"#{i}",width=listaLargoFila[i], stretch=False)		

			arbolEstimacionPerdidaArenaCK.column("#0",width=0, stretch=False)


			#Striped row tags
			arbolEstimacionPerdidaArenaCK.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaCK.tag_configure("evenrow", background= "#9DC4AA")

			##########Frame principal3
			estimacionPerdidaArenaRFrame=LabelFrame(panelFiltro, text="Estimaci??n de la p??rdida de energ??a en le lecho filtrante de arena limpio.", font=("Yu Gothic bold", 11))
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
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"N??mero de Reynolds",
			"C{}".format(getSub("d")),
			"(C{}*p)/d{}".format(getSub("d"),getSub("g")),
			"h{}".format(getSub("L")),
			)

			#Headings
			arbolEstimacionPerdidaArenaR.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaR["columns"]:
				arbolEstimacionPerdidaArenaR.heading(col, text=col,anchor=CENTER)	

			
			listaLargoFila=[0,200,200,430,430,350,200,100,100,100]
			for i in range(1,len(arbolEstimacionPerdidaArenaR["columns"])+1):
					arbolEstimacionPerdidaArenaR.column(f"#{i}",width=listaLargoFila[i], stretch=False)		


			arbolEstimacionPerdidaArenaR.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolEstimacionPerdidaArenaR.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaR.tag_configure("evenrow", background= "#9DC4AA")

			

			############Insersi??n datos.

			
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

			elif listaEU[0] == "Esf??rica":
				listaEU.append(1)
				listaEU.append(1)
				listaEU.append(6)
				listaEU.append(6)

			
			
				

			#Tabla Tama??o Abertura Tamiz
			Tama??oTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
			Tama??oAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
			tablaTama??oAberturaTamiz=dict()
			for ind in range(0, len(Tama??oTamiz)):
				tablaTama??oAberturaTamiz[Tama??oTamiz[ind]] = Tama??oAbertura[ind]

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
			elif listaEU[10] == "Tasa m??xima":
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
			#Lista sin repetici??n.
			guardado=listaNTamiz[0]
			listaNTamizSinRepeticion.append(guardado)
			for elemento in listaNTamiz:
				if elemento != guardado:
					listaNTamizSinRepeticion.append(elemento)
					guardado=elemento


			
			def tama??oPromedioGeometrico(d1,d2):
				return sqrt(d1*d2)

			

			"""	 
			#ListaOrden
			listaEU=[0 = TipoGranoArena, 1 = profundidadLechoFijoArena, 2 = densidadRelativaArena,
			3 = porosidadLechoFijo,4 = constanteFiltracionFH, 5 = temperatura, 6 = Coeficiente de filtraci??n,
			7 = Factor de esfericidad (FH - CK), 8 = Factor de forma (FH), 9 = Factor de forma (Rose)]

			"""

			#############DATOS

			#DatosPara1

			'''(
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"arena retenida/tama??o promedio geom??trico [1/(m^2)]",
			"Fair-Hatch"
			)
			'''
			sumaFH=0
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp1.clear()
				
				arenaRenetinda=listaARetenida[ind]
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				valorEnSuma= (arenaRenetinda/100)/((tama??oPromedioGeo/1000)**2)
				sumaFH=sumaFH+valorEnSuma
			
			

			contadorFiltro=0

			valorFH= (listaEU[4]*listaEU[5])*((1-listaEU[3])**2)*listaEU[1]*(listaEU[10]/86400.0)*((6/listaEU[6])**2)*(1/9.806)*((1/listaEU[3])**3)*sumaFH
			
			colFH1=list()
			colFH2=list()
			colFH3=list()
			colFH4=list()
			colFH5=list()
			colFH6=list()
			colFH7=list()
			
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp1.clear()
				listaEntradaTemp1.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				colFH1.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp1.append(arenaRenetinda)
				colFH2.append(arenaRenetinda)
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				listaEntradaTemp1.append(tama??oSuperior)
				colFH3.append(tama??oSuperior)
				listaEntradaTemp1.append(tama??oInferior)
				colFH4.append(tama??oInferior)
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				listaEntradaTemp1.append(round(tama??oPromedioGeo,3))
				colFH5.append(round(tama??oPromedioGeo,3))
				valorEnSuma= (arenaRenetinda/100)/((tama??oPromedioGeo/1000)**2)
				listaEntradaTemp1.append(round(valorEnSuma,3))
				colFH6.append(round(valorEnSuma,3))
				listaEntradaTemp1.append(round(valorFH,3))
				colFH7.append(round(valorFH,3))
				newDataTreeview(arbolEstimacionPerdidaArenaFH, listaEntradaTemp1)
			
			colsDatos=[colFH1,colFH2,colFH3,colFH4,colFH5,colFH6,colFH7]
			pasarTreeViewExcel(colsDatos,arbolEstimacionPerdidaArenaFH,'.\\ResultadosFiltro\\FH_EstimacionPerdidaDeEnergiaEnLechoFiltranteArena.xlsx')
				
			
			#DatosPara2
			'''(
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"N??mero de Reynolds", 
			"Factor de fricci??n",
			#Pendiente
			"NOMBREPREG",
			"P??rdida de cabeza hidr??ulica total",
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
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				Reynolds2=listaEU[6]*(tama??oPromedioGeo/1000)*(listaEU[10]/86400)*(1/listaEU[5])
				friccion2=150*((1-listaEU[3])/Reynolds2)+1.75
				valorSuma2A= friccion2*(arenaRenetinda/100)*(1/(tama??oPromedioGeo/1000))
				sumaCK=sumaCK+valorSuma2A
			
			valorCK=(1/listaEU[6])*(1-listaEU[3])*((1/listaEU[3])**3)*listaEU[1]*((listaEU[10]/86400)**2)*(1/9.806)*sumaCK
		
			
			sumaCKsinF=0
			
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp2.clear()
				arenaRenetinda=listaARetenida[ind]
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				Reynolds2_2=listaEU[6]*(tama??oPromedioGeo/1000)*(listaEU[10]/86400)*(1/listaEU[5])
				valorSuma2_2= (arenaRenetinda/100)*(1/(tama??oPromedioGeo/1000))
				sumaCKsinF=sumaCKsinF+valorSuma2_2
			
			
			
			valorCoefPermeabilidad = (tablaTemperaturaDensidad[valorTemperatura]*9.806)*(1/tablaTemperaturaViscosidadDinamica[valorTemperatura])*(1/listaEU[4])*((1/listaEU[8])**2)*(listaEU[3]**3)*(1/(1-listaEU[3]))*(sumaCKsinF**(-2))
			ColCK1 =list()
			ColCK2 =list()
			ColCK3 =list()
			ColCK4 =list()
			ColCK5 =list()
			ColCK6 =list()
			ColCK7 =list()
			ColCK8 =list()
			ColCK9 =list()
			ColCK10 =list()
			ColCK11 =list()

			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp2.clear()
				listaEntradaTemp2.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				ColCK1.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")

				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp2.append(arenaRenetinda)
				ColCK2.append(arenaRenetinda)
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				listaEntradaTemp2.append(tama??oSuperior)
				ColCK3.append(tama??oSuperior)
				listaEntradaTemp2.append(tama??oInferior)
				ColCK4.append(tama??oInferior)
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				listaEntradaTemp2.append(round(tama??oPromedioGeo,3))
				ColCK5.append(round(tama??oPromedioGeo,3))
				Reynolds2=listaEU[6]*(tama??oPromedioGeo/1000)*(listaEU[10]/86400)*(1/listaEU[5])
				listaEntradaTemp2.append(round(Reynolds2,3))
				ColCK6.append(round(Reynolds2,3))
				friccion2=150*((1-listaEU[3])/Reynolds2)+1.75
				listaEntradaTemp2.append(round(friccion2,6))
				ColCK7.append(round(friccion2,6))
				valorSuma2= friccion2*(arenaRenetinda/100)*(1/(tama??oPromedioGeo/1000))
				listaEntradaTemp2.append(round(valorSuma2,3))
				ColCK8.append(round(valorSuma2,3))
				listaEntradaTemp2.append(round(valorCK,3))
				ColCK9.append(round(valorCK,3))
				valorSuma2_2= (arenaRenetinda/100)*(1/(tama??oPromedioGeo/1000))
				listaEntradaTemp2.append(round(valorSuma2_2,3))
				ColCK10.append(round(valorSuma2_2,3))
				listaEntradaTemp2.append(round(valorCoefPermeabilidad,3))
				ColCK11.append(round(valorCoefPermeabilidad,3))
				newDataTreeview(arbolEstimacionPerdidaArenaCK, listaEntradaTemp2)
			
			colsDatos= [ColCK1,ColCK2,ColCK3,ColCK4,ColCK5,ColCK6,ColCK7,ColCK8,ColCK9,ColCK10,ColCK11]
			pasarTreeViewExcel(colsDatos,arbolEstimacionPerdidaArenaCK,'.\\ResultadosFiltro\\CK_EstimacionPerdidaDeEnergiaEnLechoFiltranteArena.xlsx')
			#DatosPara3

			'''(
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"N??mero de Reynolds",
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
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				Reynolds3= (tama??oPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				Suma3=Cd*(arenaRenetinda/100)*(1000/tama??oPromedioGeo)
				sumaR= sumaR + Suma3
			

			valorR= 1.067*((listaEU[10]/86400.0)**2)*listaEU[1]*(1/9.806)*((1/listaEU[3])**4)*(1/listaEU[7])*sumaR

			colR1=list()
			colR2=list()
			colR3=list()
			colR4=list()
			colR5=list()
			colR6=list()
			colR7=list()
			colR8=list()
			colR9=list()
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp3.clear()
				listaEntradaTemp3.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				colR1.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp3.append(arenaRenetinda)
				colR2.append(arenaRenetinda)
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				listaEntradaTemp3.append(tama??oSuperior)
				colR3.append(tama??oSuperior)
				listaEntradaTemp3.append(tama??oInferior)
				colR4.append(tama??oInferior)
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				listaEntradaTemp3.append(round(tama??oPromedioGeo,3))
				colR5.append(round(tama??oPromedioGeo,3))
				Reynolds3= (tama??oPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				listaEntradaTemp3.append(round(Reynolds3,3))
				colR6.append(round(Reynolds3,3))
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				listaEntradaTemp3.append(round(Cd,3))
				colR7.append(round(Cd,3))
				Suma3=Cd*(arenaRenetinda/100)*(1000/tama??oPromedioGeo)
				listaEntradaTemp3.append(round(Suma3,3))
				colR8.append(round(Suma3,3))
				listaEntradaTemp3.append(round(valorR,3))
				colR9.append(round(valorR,3))
				newDataTreeview(arbolEstimacionPerdidaArenaR, listaEntradaTemp3)
			colsDatos=[colR1,colR2,colR3,colR4,colR5,colR6,colR7,colR8,colR9]
			pasarTreeViewExcel(colsDatos,arbolEstimacionPerdidaArenaR,'.\\ResultadosFiltro\\Rose_EstimacionPerdidaDeEnergiaEnLechoFiltranteArena.xlsx')
			estimacionPerdidaArenaCalculoWindow.mainloop()

			
		else: #Inicio
			
			
			
			
			##Panel:
			panelFiltro = ttk.Notebook(estimacionPerdidaArenaCalculoWindow)
			panelFiltro.pack(fill=BOTH, expand=TRUE)
			
			##########Frame principal3
			estimacionPerdidaArenaRFrame=LabelFrame(panelFiltro, text="Estimaci??n de la p??rdida de energ??a en le lecho filtrante de arena limpio.", font=("Yu Gothic bold", 11))
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
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"N??mero de Reynolds",
			"C{}".format(getSub("d")),
			"(C{}*p)/d{}".format(getSub("d"),getSub("g")),
			"h{}".format(getSub("L")),
			)

			#Headings
			arbolEstimacionPerdidaArenaR.heading("#0",text="ID", anchor=CENTER)

			for col in arbolEstimacionPerdidaArenaR["columns"]:
				arbolEstimacionPerdidaArenaR.heading(col, text=col,anchor=CENTER)	

			listaLargoFila=[0,200,200,430,430,350,200,100,100,100]
			for i in range(1,len(arbolEstimacionPerdidaArenaR["columns"])+1):
					arbolEstimacionPerdidaArenaR.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
			arbolEstimacionPerdidaArenaR.column("#0",width=0, stretch=False)

			#Striped row tags
			arbolEstimacionPerdidaArenaR.tag_configure("oddrow", background= "#1FCCDB")
			arbolEstimacionPerdidaArenaR.tag_configure("evenrow", background= "#9DC4AA")

			

			############Insersi??n datos.

			
			contadorFiltro = 0
			
			
			listaEntradaTemp3=list()
			datosSalida=list()
			
					
			


			if listaEU[0] == "Afilada":
				listaEU.append(0)
				listaEU.append(0.85)
				listaEU.append(0)
				listaEU.append(6.2)
			
			
				

			#Tabla Tama??o Abertura Tamiz
			Tama??oTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
			Tama??oAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
			tablaTama??oAberturaTamiz=dict()
			for ind in range(0, len(Tama??oTamiz)):
				tablaTama??oAberturaTamiz[Tama??oTamiz[ind]] = Tama??oAbertura[ind]

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
			elif listaEU[10] == "Tasa m??xima":
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
			#Lista sin repetici??n.
			guardado=listaNTamiz[0]
			listaNTamizSinRepeticion.append(guardado)
			for elemento in listaNTamiz:
				if elemento != guardado:
					listaNTamizSinRepeticion.append(elemento)
					guardado=elemento


			
			def tama??oPromedioGeometrico(d1,d2):
				return sqrt(d1*d2)

	
				
			#DatosPara3

			'''(
			"N??mero de tamiz",
			"Arena retenida [%]", 
			"Tama??o de abertura del tamiz superior [mm]", 
			"Tama??o de abertura del tamiz inferior [mm]",
			"Tama??o promedio geom??trico [mm]",
			"N??mero de Reynolds",
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
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				Reynolds3= (tama??oPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				Suma3=Cd*(arenaRenetinda/100)*(1000/tama??oPromedioGeo)
				sumaR= sumaR + Suma3
			
			
			
			valorR= 1.067*((listaEU[10]/86400.0)**2)*listaEU[1]*(1/9.806)*(1/((listaEU[3])**4))*(1/listaEU[7])*sumaR
			colR1=list()
			colR2=list()
			colR3=list()
			colR4=list()
			colR5=list()
			colR6=list()
			colR7=list()
			colR8=list()
			colR9=list()
			
			for ind in range(0, len(listaARetenida)):
				listaEntradaTemp3.clear()
				listaEntradaTemp3.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				colR1.append(f"{listaNTamizSinRepeticion[ind]} - {listaNTamizSinRepeticion[ind+1]}")
				arenaRenetinda=listaARetenida[ind]
				listaEntradaTemp3.append(arenaRenetinda)
				colR2.append(arenaRenetinda)
				extremoDerecho=listaNTamizExtremoD[ind]
				extremoIzquierdo=listaNTamizExtremoI[ind]
				tama??oSuperior= tablaTama??oAberturaTamiz[extremoIzquierdo]
				tama??oInferior= tablaTama??oAberturaTamiz[extremoDerecho]
				listaEntradaTemp3.append(tama??oSuperior)
				colR3.append(tama??oSuperior)
				listaEntradaTemp3.append(tama??oInferior)
				colR4.append(tama??oInferior)
				tama??oPromedioGeo = tama??oPromedioGeometrico(tama??oSuperior,tama??oInferior)
				listaEntradaTemp3.append(round(tama??oPromedioGeo,3))
				colR5.append(round(tama??oPromedioGeo,3))
				Reynolds3= (tama??oPromedioGeo/1000)*(listaEU[10]/86400.0)/listaEU[5]
				listaEntradaTemp3.append(round(Reynolds3,3))
				colR6.append(round(Reynolds3,3))
				Cd=24/Reynolds3 + 3/sqrt(Reynolds3)+0.34
				listaEntradaTemp3.append(round(Cd,3))
				colR7.append(round(Cd,3))
				Suma3=Cd*(arenaRenetinda/100)*(1000/tama??oPromedioGeo)
				listaEntradaTemp3.append(round(Suma3,3))
				colR8.append(round(Suma3,3))
				listaEntradaTemp3.append(round(valorR,3))
				colR9.append(round(valorR,3))
				newDataTreeview(arbolEstimacionPerdidaArenaR, listaEntradaTemp3)
			
			colsDatos=[colR1,colR2,colR3,colR4,colR5,colR6,colR7,colR8,colR9]
			pasarTreeViewExcel(colsDatos,arbolEstimacionPerdidaArenaR,'.\\ResultadosFiltro\\Rose_EstimacionPerdidaDeEnergiaEnLechoFiltranteArena.xlsx')
			estimacionPerdidaArenaCalculoWindow.mainloop()

				
			







	def estimacionPerdidaEnergiaArena(lista1,lista2,optnValue):
		listaNTamizTemp=lista1.copy()
		listaARetenidaTemp=lista2.copy()
		listaNTamiz=list()
		listaARetenida=list()
		
		
		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de los n??meros de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de la arena retenida.")
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
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores est??ndar para n??mero de tamiz. Pulse el bot??n para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de n??mero de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None


		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de n??mero de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None


		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento


		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None

		estimacionPerdidaArenaWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		estimacionPerdidaArenaWindow.iconbitmap(bitmap=path)
		estimacionPerdidaArenaWindow.geometry("800x600") 
		estimacionPerdidaArenaWindow.resizable(0,0)	
		estimacionPerdidaArenaWindow.configure(background="#9DC4AA")

		frameEstimacionPerdidaArena= LabelFrame(estimacionPerdidaArenaWindow, text="Estimaci??n de la p??rdida de energ??a en el lecho filtrante de arena limpio",font=("Yu Gothic bold", 11))
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
		lista_inputs=["Tasa m??xima de filtraci??n [m/d]",
		"Profundidad del lecho fijo de arena",
		"Densidad relativa de la arena",
		"Porosidad del lecho fijo",
		"Constante de filtraci??n (Fair-Hatch)",
		"Factor de forma (Fair-Hatch)",
		"Factor de forma (Carmen -Kozeny)",
		"Factor de forma (Rose)"
					]
	
		inicialLabel=Label(frameEstimacionPerdidaArena, text="Caracter??sticas del lecho filtrante de arena: ",font=("Yu Gothic bold",10))

		
		
		
		TipoGranoArena = StringVar()
		TipoGranoArena.set("Seleccione el tipo de grano de arena")
		listaValoresTemp=["Angular", "Afilada", "Erosionada", "Redondeada", "Esf??rica"]
		TipoGranoArenaName = OptionMenu(frameEstimacionPerdidaArena, TipoGranoArena, *listaValoresTemp)

		Tasa = StringVar()
		Tasa.set("Seleccione la tasa para calcular")
		listaValoresTemp1=["Tasa media", "Tasa m??xima"]
		TasaName = OptionMenu(frameEstimacionPerdidaArena, Tasa, *listaValoresTemp1)
		


		profundidadLechoFijoArenaLabel = Label(frameEstimacionPerdidaArena, text="L = Profundidad del lecho fijo de arena [0.6m - 0.75m]:", font =("Yu Gothic",9))
		
		densidadRelativaArenaLabel = Label(frameEstimacionPerdidaArena, text="S{} = Densidad relativa de la arena [2.5 - 2.7]:".format(getSub("s")), font =("Yu Gothic",9))
		porosidadLechoFijoLabel = Label(frameEstimacionPerdidaArena, text=u"\u03B5 ,e = Porosidad del lecho fijo [0.4 - 0.48]:", font =("Yu Gothic",9))
		constanteFiltracionFHLabel = Label(frameEstimacionPerdidaArena, text=u"\u03BA = Constante de Filtraci??n (Fair-Hatch) []:", font =("Yu Gothic",9))
		
		
		

		profundidadLechoFijoArena = Entry(frameEstimacionPerdidaArena)
		densidadRelativaArena = Entry(frameEstimacionPerdidaArena)
		porosidadLechoFijo = Entry(frameEstimacionPerdidaArena)
		constanteFiltracionFH = Entry(frameEstimacionPerdidaArena)
		
		#Borrar

		# profundidadLechoFijoArena.insert(0,"0.64")
		# densidadRelativaArena.insert(0,"2.65")
		# porosidadLechoFijo.insert(0,"0.45")
		# constanteFiltracionFH.insert(0,"5")
		# TipoGranoArena.set("Erosionada")
		# Tasa.set("Tasa media")
	

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
		botonCalcular = HoverButton(frameEstimacionPerdidaArena, text="Calcular la estimaci??n de la p??rdida de energ??a en el lecho filtrante de arena limpio.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularPEArena(listaNTamiz,listaARetenida,listaEntradas,valorTemperatura) )
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
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de los n??meros de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de la arena retenida.")
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
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores est??ndar para n??mero de tamiz. Pulse el bot??n para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de n??mero de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de n??mero de tamiz no coincide con la cantidad de datos de arena retendia.")
			return None
		
		
		sumaPorcentajes=0
		for elemento in listaARetenida:
			sumaPorcentajes= sumaPorcentajes + elemento
		
		
		if round(sumaPorcentajes,4) != 100.0:
			messagebox.showwarning(title="Error", message="La suma de porcentajes de arena retenida es diferente de 100.")
			return None

		listaEntradaTemp=list()
		datosSalida=list()
		
		
		
		#Tabla Tama??o Abertura Tamiz
		Tama??oTamiz= [4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140]
		Tama??oAbertura= [4.76, 3.35, 2.38, 1.68, 1.41, 1.0, 0.841, 0.707, 0.595, 0.5, 0.4, 0.354, 0.297, 0.25, 0.21, 0.177, 0.149, 0.105]
		tablaTama??oAberturaTamiz=dict()
		for ind in range(0, len(Tama??oTamiz)):
			tablaTama??oAberturaTamiz[Tama??oTamiz[ind]] = Tama??oAbertura[ind]

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
			listaEntradaTemp.append(tablaTama??oAberturaTamiz[extremoDerecho])
			listaEntradaTemp.append(listaAcumuladoArenaDescendente[ind])
			listaEntradaTemp.append(tablaTama??oAberturaTamiz[listaNTamizExtremo[longListaARetenida-ind]])
			listaEntradaTemp.append(listaAcumuladoArenaAscendente[ind])
			listaIntermedia = listaEntradaTemp.copy()
			datosSalida.append(listaIntermedia)
		
		
		abAcDic= dict()
		for ind in range(0,len(datosSalida)):
			abAcDic[datosSalida[ind][6]]=datosSalida[ind][5]
		
		
		def tama??oEfectivod1(numero,dic):
			elementoAnterior=dic[0]
			
			for elemento in dic:
	
				if elemento <= numero and elemento>=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda
			
			
		def tama??oEfectivod2(numero,dic):
			elementoAnterior=100
			for elemento in dic:
				if elemento >= numero and elemento<=elementoAnterior:
					variableGuarda=elemento
					elementoAnterior=elemento
			return variableGuarda
			

		def tama??oEfectivod(numero,dic):
			return[tama??oEfectivod1(numero,dic), tama??oEfectivod2(numero,dic)]

		def calculo1CU(numero,x1,y1,x2,y2):
			return(log10(x1)+(((numero-y1)/(y2-y1))*log10(x2/x1)))
		def calculo2CU(numero,x1,y1,x2,y2):
			return (10**(calculo1CU(numero,x1,y1,x2,y2)))
		
		#Calculo Tama??o Efectivo d10:
		listaAcumuladoCU10=tama??oEfectivod(10,abAcDic)
		y1=listaAcumuladoCU10[0]
		y2=listaAcumuladoCU10[1]
		x1=abAcDic[y1]
		x2=abAcDic[y2]
		d10= calculo2CU(10,x1,y1,x2,y2)
		listaAcumuladoCU60=tama??oEfectivod(60,abAcDic)
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
				messagebox.showwarning(title="Error", message="Todos los valores ingresados deben ser n??meros.")
				return None
	
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.iconbitmap(bitmap=path)
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.geometry("1000x200") 
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.resizable(0,0)	
		estimacionPerdidaGravaYPredimensionamientoCalculoWindow.configure(background="#9DC4AA")

		##Panel:
		panelGravaDimension = ttk.Notebook(estimacionPerdidaGravaYPredimensionamientoCalculoWindow)
		panelGravaDimension.pack(fill=BOTH, expand=TRUE)
		###########Frame Principal1
		estimacionPerdidaGravaFrame=LabelFrame(panelGravaDimension, text="Estimaci??n de la p??rdida de energ??a en le lecho de grava.", font=("Yu Gothic bold", 11))
		estimacionPerdidaGravaFrame.pack(side=TOP, fill=BOTH,expand=True)
		panelGravaDimension.add(estimacionPerdidaGravaFrame,text="P??rdida energ??a en el lecho de grava")
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
		"V{} = Tasa de filtraci??n [m/d]".format(getSub("f")),
		"L{} = Profundidad del lecho de grava [m]".format(getSub("g")),
		"h{} = P??rdida de energ??a en lecho de grava durante la filtraci??n [m]".format(getSub("g"))
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
		PerdidaCargaGravaFrame=LabelFrame(panelGravaDimension, text="P??rdida de carga a trav??s del lecho de grava", font=("Yu Gothic bold", 11))
		PerdidaCargaGravaFrame.pack(side=TOP, fill=BOTH,expand=True)
		panelGravaDimension.add(PerdidaCargaGravaFrame,text="P??rdida de carga a trav??s del lecho de grava")
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
		"h{} = P??rdida de energ??a en el lecho de grava durante el lavado [m]".format(getSub("2"))
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

		############Insersi??n datos.
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
		path=resource_path('icons\\agua.ico')
		estimacionPerdidaGravaYPredimensionamientoWindow.iconbitmap(bitmap=path)
		estimacionPerdidaGravaYPredimensionamientoWindow.geometry("800x600") 
		estimacionPerdidaGravaYPredimensionamientoWindow.resizable(0,0)	
		estimacionPerdidaGravaYPredimensionamientoWindow.configure(background="#9DC4AA")
		frameEstimacionPerdidaGravaYPredimensionamiento= LabelFrame(estimacionPerdidaGravaYPredimensionamientoWindow, text="Estimaci??n de la p??rdida de energ??a en el lecho de grava y predimensionamiento de los filtros",font=("Yu Gothic bold", 11))
		frameEstimacionPerdidaGravaYPredimensionamiento.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				elemento.delete(0, END)


		#Input
		lista_inputs=[]

		inicialLabel=Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Caracter??sticas del lecho de grava para drenaje por tuber??as: ",font=("Yu Gothic bold",10))
		segundoLabel= Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Caudales de dise??o",font=("Yu Gothic bold",10))

		NumeroCapaLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="N??mero de capa",font=("Yu Gothic bold",10))
		tama??oAberturaMallaPasandoLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Tama??o de abertura\nde malla pasando [pulg]",font=("Yu Gothic bold",10))
		tama??oAberturaMallaRetenidaLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Tama??o de abertura\nde malla retenida [pulg]",font=("Yu Gothic bold",10))
		profundidadCapaLabel = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="Profundidad de la capa [m]",font=("Yu Gothic bold",10))
		NumeroCapaLabel1Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="1",font=("Yu Gothic bold",10))
		NumeroCapaLabel2Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="2",font=("Yu Gothic bold",10))
		NumeroCapaLabel3Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="3",font=("Yu Gothic bold",10))
		NumeroCapaLabel4Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="4",font=("Yu Gothic bold",10))
		NumeroCapaLabel5Label = Label(frameEstimacionPerdidaGravaYPredimensionamiento, text="5",font=("Yu Gothic bold",10))

		

		tama??oAberturaMallaPasando1 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaPasando1.focus()
		tama??oAberturaMallaPasando2 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaPasando3 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaPasando4 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaPasando5 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)

		tama??oAberturaMallaRetenida1 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaRetenida2 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaRetenida3 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaRetenida4 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		tama??oAberturaMallaRetenida5 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)

		profundidadCapa1 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa2 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa3 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa4 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)
		profundidadCapa5 = Entry(frameEstimacionPerdidaGravaYPredimensionamiento)

		

		listaTitulosTabla=[NumeroCapaLabel,tama??oAberturaMallaPasandoLabel, tama??oAberturaMallaRetenidaLabel, profundidadCapaLabel]

		listaColumna1=[NumeroCapaLabel1Label,NumeroCapaLabel2Label,NumeroCapaLabel3Label,NumeroCapaLabel4Label,NumeroCapaLabel5Label]
		listaColumna2=[tama??oAberturaMallaPasando1,tama??oAberturaMallaPasando2,tama??oAberturaMallaPasando3,tama??oAberturaMallaPasando4,tama??oAberturaMallaPasando5]
		listaColumna3=[tama??oAberturaMallaRetenida1,tama??oAberturaMallaRetenida2,tama??oAberturaMallaRetenida3,tama??oAberturaMallaRetenida4,tama??oAberturaMallaRetenida5]
		listaColumna4=[profundidadCapa1,profundidadCapa2,profundidadCapa3,profundidadCapa4,profundidadCapa5]
		
		listaEntradas = [tama??oAberturaMallaPasando1,tama??oAberturaMallaPasando2,tama??oAberturaMallaPasando3,tama??oAberturaMallaPasando4,tama??oAberturaMallaPasando5,
		tama??oAberturaMallaRetenida1,tama??oAberturaMallaRetenida2,tama??oAberturaMallaRetenida3,tama??oAberturaMallaRetenida4,tama??oAberturaMallaRetenida5,
		profundidadCapa1,profundidadCapa2,profundidadCapa3,profundidadCapa4,profundidadCapa5]
		
		#Organizaci??n tabla.
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
		botonCalcular = HoverButton(frameEstimacionPerdidaGravaYPredimensionamiento, text="Calcular la estimaci??n de la p??rdida de energ??a en el lecho de grava.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularPEGravaYPredimensionamiento(listaEntradas,lista1, lista2,temp) )
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
				messagebox.showwarning(title="Error",message="Uno o varios de los valores ingresados no son n??meros.")
				return None
		perdidaLechoExpandidoCWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaLechoExpandidoCWindow.iconbitmap(bitmap=path)
		perdidaLechoExpandidoCWindow.geometry("1000x500") 
		perdidaLechoExpandidoCWindow.resizable(0,0)	
		perdidaLechoExpandidoCWindow.configure(background="#9DC4AA")

		#Frame principal
		perdidaLechoExpandidoCFrame=LabelFrame(perdidaLechoExpandidoCWindow, text="P??rdida de carga a trav??s del lecho expandido", font=("Yu Gothic bold", 11))
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
		"h{} = P??rdida de carga a trav??s del lecho expandido [m]".format(getSub("1"))
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


		#Insersi??n datos.
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
		path=resource_path('icons\\agua.ico')
		perdidaCargaLechoExpandidoWindow.iconbitmap(bitmap=path)
		perdidaCargaLechoExpandidoWindow.geometry("600x400") 
		perdidaCargaLechoExpandidoWindow.resizable(0,0)	
		perdidaCargaLechoExpandidoWindow.configure(background="#9DC4AA")

		framePerdidaCargaLechoExpandido= LabelFrame(perdidaCargaLechoExpandidoWindow, text="P??rdida de carga a trav??s del lecho expandido",font=("Yu Gothic bold", 11))
		framePerdidaCargaLechoExpandido.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista):
			for elemento in lista:
				elemento.delete(0, END)


		#Input
		lista_inputs=[]

		inicialLabel=Label(framePerdidaCargaLechoExpandido, text="Caracter??sticas del lecho filtrante de arena: ",font=("Yu Gothic bold",10))



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
		botonCalcular = HoverButton(framePerdidaCargaLechoExpandido, text="Calcular la p??rdida de carga a trav??s del lecho expandido.", activebackground="#9DC4AA", width=70, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: calcularPerdidadLechoExpandido(listaEntradas) )
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
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero.")
			return None

		if caudalMedio<0.01 or caudalMedio>0.2:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero entre 0.01 y 0.2")
			return None
		
		predimensionamientoFiltrosWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		predimensionamientoFiltrosWindow.iconbitmap(bitmap=path)
		predimensionamientoFiltrosWindow.geometry("620x500") 
		predimensionamientoFiltrosWindow.resizable(0,0)	
		predimensionamientoFiltrosWindow.configure(background="#9DC4AA")

		PredimensionamientoFiltrosFrame=LabelFrame(predimensionamientoFiltrosWindow, text="Predimensionamiento de los filtros", font=("Yu Gothic bold", 11))
		PredimensionamientoFiltrosFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolPredimensionamientoFiltros_frame = Frame(PredimensionamientoFiltrosFrame)
		arbolPredimensionamientoFiltros_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolPredimensionamientoFiltros_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPredimensionamientoFiltros_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPredimensionamientoFiltros= ttk.Treeview(arbolPredimensionamientoFiltros_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arbolPredimensionamientoFiltros.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolPredimensionamientoFiltros.xview)
		sedScrollY.configure(command=arbolPredimensionamientoFiltros.yview)
		#Define columnas.
		arbolPredimensionamientoFiltros["columns"]= (
		"Presione para ver hoja de Excel","2", "Unidades")
		
		'''
		"Q = Caudal de dise??o (QMD)  ",
		"V{} = Tasa de filtraci??n en operaci??n normal [m/d??a]".format(getSub("f")),
		"V{} = Tasa de filtraci??n con un filtro fuera de servicio por lavado".format(getSub("max")),
		"A{} = ??rea de filtraci??n en operaci??n normal".format(getSub("T")),
		"A{} = ??rea de filtraci??n con un filtros fuera de servicio por lavado".format(getSub("t")),
		"??rea de filtraci??n fuera de servicio por lavado de filtros",
		"N{} = N??mero m??nimo de filtros [und]".format(getSub("f")),
		"N{} = N??mero de filtros [und]".format(getSub("f")),
		"A{} = ??rea de cada filtro".format(getSub("f")),
		"L{} = Lado de cada filtro".format(getSub("f"))'''
		

		#Headings
		arbolPredimensionamientoFiltros.heading("#0",text="ID", anchor=CENTER)


		

		for col in arbolPredimensionamientoFiltros["columns"]:																				
			arbolPredimensionamientoFiltros.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg('images\\Filtro_predimensionamientoFiltros.png',1004,383))	

		
		arbolPredimensionamientoFiltros.column("#0",width=0, stretch=False)
		arbolPredimensionamientoFiltros.column("#1",width=400, stretch=False)
		arbolPredimensionamientoFiltros.column("#2",width=100, stretch=False)
		arbolPredimensionamientoFiltros.column("#3",width=100, stretch=False)
		#Striped row tags
		arbolPredimensionamientoFiltros.tag_configure("evenrow", background= "#1FCCDB")
		arbolPredimensionamientoFiltros.tag_configure("oddrow", background= "#9DC4AA")

		
		contadorFiltro = 0

		listaArbolCaudal=list()
		caudal=caudalMedio*(1.30)
		listaArbolCaudal.append(round(caudal,3))
		Vf=120
		Vmax=150
		listaArbolCaudal.append(round(Vf,3))
		listaArbolCaudal.append(round(Vmax,3))
		arenaFilOpNormal=caudal*86400*(1/Vf)
		listaArbolCaudal.append(round(arenaFilOpNormal,3))
		arenaFilFueraServ=caudal*86400*(1/Vmax)
		listaArbolCaudal.append(round(arenaFilFueraServ,3))
		arenaFilFueraServ2 = arenaFilOpNormal - arenaFilFueraServ
		listaArbolCaudal.append(round(arenaFilFueraServ2,3))

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
		listaArbolCaudal.append(round(areaFiltro,3))

		ladoFiltro= sqrt(round(areaFiltro,3))
		listaArbolCaudal.append(round(ladoFiltro,3))
		
		encabezadosLista=["Q = Caudal de dise??o (QMD)  [(m^3)/s]",
		"V{} = Tasa de filtraci??n en operaci??n normal [m/d??a]".format(getSub("f")),
		"V{} = Tasa de filtraci??n con un filtro fuera de servicio por lavado".format(getSub("max")),
		"A{} = ??rea de filtraci??n en operaci??n normal".format(getSub("T")),
		"A{} = ??rea de filtraci??n con un filtros fuera de servicio por lavado".format(getSub("t")),
		"??rea de filtraci??n fuera de servicio por lavado de filtros",
		"N{} = N??mero m??nimo de filtros [und]".format(getSub("f")),
		"N{} = N??mero de filtros [und]".format(getSub("f")),
		"A{} = ??rea de cada filtro".format(getSub("f")),
		"L{} = Lado de cada filtro".format(getSub("f"))]
		
		listaUnidades=[
		"(m^3)/s",
		"m/d??a",
		"m/d??a",
		"m^2",
		"m^2",
		"m^2",
		"",
		"",
		"m^2",
		"m"
		]

		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listaArbolCaudal[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arbolPredimensionamientoFiltros,listaTemp)
		#newDataTreeview(arbolPredimensionamientoFiltros,listaArbolCaudal)
		
		
		
		PasarExcelDatos(".\\ResultadosFiltro\\PredimensionamientoFiltros.xlsx",'Resultados',encabezadosLista,50, listaArbolCaudal, 15, listaUnidades, 15,False,[], 50)

		predimensionamientoFiltrosWindow.mainloop()
	
	def ValuepredimensionamientoFiltros(listaET):
	
			
		try: 
			caudalMedio=float(listaET[0].get())
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero.")
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
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])
			diametroOrificios2= f"{listaEntradaDrenaje[0].get()[0]}/{listaEntradaDrenaje[0].get()[2]}"
		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())
		
		
		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()
		
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())
	

		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()
		
		
	
			
		drenajeFiltrosWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		drenajeFiltrosWindow.iconbitmap(bitmap=path)
		drenajeFiltrosWindow.geometry("770x350") 
		drenajeFiltrosWindow.resizable(0,0)	
		drenajeFiltrosWindow.configure(background="#9DC4AA")

		drenajeFiltrosFrame=LabelFrame(drenajeFiltrosWindow, text="Drenaje calculo", font=("Yu Gothic bold", 11))
		drenajeFiltrosFrame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolDrenajeFiltros_frame = Frame(drenajeFiltrosFrame)
		arbolDrenajeFiltros_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolDrenajeFiltros_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolDrenajeFiltros_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolDrenajeFiltros= ttk.Treeview(arbolDrenajeFiltros_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arbolDrenajeFiltros.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arbolDrenajeFiltros.xview)
		sedScrollY.configure(command=arbolDrenajeFiltros.yview)
		#Define columnas.
		arbolDrenajeFiltros["columns"]= (
		"Presione para ver Excel","Valores","Unidades","Adicional"
		)

		#Headings
		arbolDrenajeFiltros.heading("#0",text="ID", anchor=CENTER)

		for col in arbolDrenajeFiltros["columns"]:
			arbolDrenajeFiltros.heading(col, text=col,anchor=CENTER, command= lambda: proyectarImg('images\\Filtro_drenajeFiltroTuberiasPerforadas.png',901,412))	

		
		listaLargoFila=[0,250,100,100,300]
		for i in range(1,len(arbolDrenajeFiltros["columns"])+1):
			arbolDrenajeFiltros.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
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

		#Obtenci??n de Lf
		
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

		listaArbolDreanejFiltros.append(diametroOrificios2)
		listaArbolDreanejFiltros.append(distanciaOrificios)
		listaArbolDreanejFiltros.append(seccionTransvMultiple)


		

		anchoMultiple= anchoSeccion[seccionTransvMultiple]
		listaArbolDreanejFiltros.append(round(anchoMultiple,3))


		longitudLaterales= round(((ladoFiltro/2) - (anchoMultiple/2) -0.05),2)
		listaArbolDreanejFiltros.append(round(longitudLaterales,3))
		
		listaArbolDreanejFiltros.append(distanciaLaterales)
		listaArbolDreanejFiltros.append(diametroLaterales)
		
		numLatPUDF= 2*round((ladoFiltro/distanciaLaterales),0)
		listaArbolDreanejFiltros.append(numLatPUDF)

		numOrif= 2*(int(longitudLaterales/distanciaOrificios)+1)
		listaArbolDreanejFiltros.append(numOrif)

		

		numOrifPUDF=numLatPUDF*numOrif
		listaArbolDreanejFiltros.append(numOrifPUDF)

	


		areaTotalOrificios= round((float(numOrifPUDF)*areaOrificiosDic[diametroOrificios]*(1.0/areaFiltro)),4)
		listaArbolDreanejFiltros.append(round(areaTotalOrificios,3))



		areaTransversalDelLateral= round((areaLateralesDic[diametroLaterales]/(areaOrificiosDic[diametroOrificios]*numOrif)),2)
		listaArbolDreanejFiltros.append(round(areaTransversalDelLateral,3))


		areaTransversalDelMultiple=	round((anchoSeccion2[seccionTransvMultiple]/(numLatPUDF*areaLateralesDic[diametroLaterales])),2)
		listaArbolDreanejFiltros.append(round(areaTransversalDelMultiple,3))
			

		#diametroLateralesA n??mero:

		if diametroLaterales=="1 1/2":
			diametroLaterales= 1.0 + (1/2)
		elif diametroLaterales=="2 1/2":
			diametroLaterales=2.0 + (1/2)
		else:
			diametroLaterales=float(diametroLaterales)

		longitudLateral= longitudLaterales/(diametroLaterales*0.0254)
		listaArbolDreanejFiltros.append(round(longitudLateral,3))

		
		listaEncabezados = [
		u"\u03D5{} = Di??metro de los orificios".format(getSub('ori')),
		"X{} = Distancia entre los orificios".format(getSub('ori')),
		"S{} = Secci??n transversal comercial del\nm??ltiple".format(getSub('mul')),
		"B{} = Ancho del m??ltiple".format(getSub("mul")),
		"L{} = Longitud de los laterales".format(getSub("lat")),
		"X{} = Distancia entre los laterales".format(getSub('Lat')),
		u"\u03D5{} = Di??metro de los laterales".format(getSub('Lat')),
		"N{} = N??mero de laterales por\nunidad de filtraci??n".format(getSub("lat")),
		" = N??mero de orificios por lateral",
		"N{} = N??mero de orificios por\nunidad de filtraci??n".format(getSub("ori")),
		"??rea total de orificios/\n??rea filtrante",
		"??rea transversal del lateral/\n??rea de orificios del lateral",
		"??rea transversal del m??ltiple/\n??rea transversal de laterales",
		"Longitud de lateral/\ndi??metro de lateral",]

		listaUnidades = ["pulgadas",
		"m",
		"pulgadas^2",
		"m",
		"m",
		"m",
		"pulgadas",
		"",
		"",
		"",
		"",
		"",
		"",
		""]
		

		if areaTotalOrificios>0.0015 and areaTotalOrificios<0.005:
			areaTotalOrificiosInfo = "El area total de orificios es adecuada"
		else:
			areaTotalOrificiosInfo = "??Error, revise cantidades, di??metros y distancias\nen orificios!"
		
		if areaTransversalDelLateral>2.0 and areaTransversalDelLateral<4.0:
			areaTransversalDelLateralInfo = "El ??rea transversal del lateral es adecuada"
		else:
			areaTransversalDelLateralInfo = "??Error, revise los di??metros y distancias en los laterales\ny orificios, adem??s, las velocidad asociadas!"

		if areaTransversalDelMultiple>1.5 and areaTransversalDelMultiple<3.0:
			areaTransversalDelMultipleInfo= "El ??rea transversal del m??ltiple es adecuada"
		else:
			areaTransversalDelMultipleInfo = " ??Error, revise dimensiones de m??ltiple y laterales, tenga\nen cuenta velocidad de flujo en el m??ltiple y laterales!"
		
		if longitudLateral<60.0:
			longitudLateralInfo="La longitud lateral es adecuada"
		else:
			longitudLateralInfo="??Error, revise di??metros de laterales!"

		listaAdicional=[
		"",
		"",
		"",
		"",
		"",
		"",
		"",
		"",
		"",
		"",
		areaTotalOrificiosInfo,
		areaTransversalDelLateralInfo,
		areaTransversalDelMultipleInfo,
		longitudLateralInfo
		]
		

		
		for i in range(0, len(listaEncabezados)):
			listaTemp= list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaArbolDreanejFiltros[i])
			listaTemp.append(listaUnidades[i])
			listaTemp.append(listaAdicional[i])
			newDataTreeview(arbolDrenajeFiltros,listaTemp)
		
		PasarExcelDatos(".\\ResultadosFiltro\\DrenajeFiltro_TuberiasPerforadas.xlsx",'Resultados',listaEncabezados,50, listaArbolDreanejFiltros, 15, listaUnidades, 15,True,listaAdicional, 50)

		drenajeFiltrosWindow.mainloop()
	
	def ValueDrenajeFiltro2(caudal,listaEntradaDrenaje):
			
		
		'''
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]

		'''

		
		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())
		
		
		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()
		
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())
	

		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
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

		#Obtenci??n de Lf
		
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
			

		#diametroLateralesA n??mero:

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
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero.")
			return None

		if caudalMedio<0.01 or caudalMedio>0.2:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero entre 0.01 y 0.2")
			return None

		drenajeFiltrosMainWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		drenajeFiltrosMainWindow.iconbitmap(bitmap=path)
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
		diametroOrificiosLabel= Label(drenajeFiltrosMainWindow, text="Seleccione el di??metro de los orificios [pulgadas]:", font=("Yu Gothic bold", 11))
		

		
		distanciaOrificios = StringVar()
		distanciaOrificios.set("Distancia entre los orificios")
		listaValoresTempDistanciaOrificios=list()
		listaValoresTempDistanciaOrificios.append("0.750")
		listaValoresTempDistanciaOrificios.append("0.100")
		listaValoresTempDistanciaOrificios.append("0.125")
		listaValoresTempDistanciaOrificios.append("0.150")
		distanciaOrificiosName = OptionMenu(drenajeFiltrosMainFrame, distanciaOrificios, *listaValoresTempDistanciaOrificios)
		distanciaOrificiosLabel= Label(drenajeFiltrosMainWindow, text="Seleccione la distancia entre orificios [m]:", font=("Yu Gothic bold", 11))


		seccionTransversal = StringVar()
		seccionTransversal.set("Secci??n transversal")
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
		seccionTransversalLabel= Label(drenajeFiltrosMainWindow, text="Seleccione la secci??n transversal comercial del m??ltiple [pulgadas^2]:", font=("Yu Gothic bold", 11))


		distanciaLaterales = StringVar()
		distanciaLaterales.set("Distancia entre laterales")
		listaValoresTempDistanciaLaterales=list()
		listaValoresTempDistanciaLaterales.append("0.20")
		listaValoresTempDistanciaLaterales.append("0.25")
		listaValoresTempDistanciaLaterales.append("0.30")
		distanciaLateralesName = OptionMenu(drenajeFiltrosMainFrame, distanciaLaterales, *listaValoresTempDistanciaLaterales)
		distanciaLateralesLabel= Label(drenajeFiltrosMainWindow, text="Seleccione la distancia entre laterales [m]:", font=("Yu Gothic bold", 11))
		

		
		diametroEntreLaterales = StringVar()
		diametroEntreLaterales.set("Di??metro de los laterales")
		listaValoresTempDiametroEntreLaterales=list()
		listaValoresTempDiametroEntreLaterales.append("1 1/2")
		listaValoresTempDiametroEntreLaterales.append("2")
		listaValoresTempDiametroEntreLaterales.append("2 1/2")
		listaValoresTempDiametroEntreLaterales.append("3")
		diametroEntreLateralesName = OptionMenu(drenajeFiltrosMainFrame, diametroEntreLaterales, *listaValoresTempDiametroEntreLaterales)
		diametroEntreLateralesLabel= Label(drenajeFiltrosMainWindow, text="Seleccione el di??metro de los laterales [pulgadas]:", font=("Yu Gothic bold", 11))


		
		listaEntradaDrenaje2=[diametroOrificiosName,distanciaOrificiosName,seccionTransversalName,distanciaLateralesName, diametroEntreLateralesName]
		listaLabel= [diametroOrificiosLabel,distanciaOrificiosLabel, seccionTransversalLabel, distanciaLateralesLabel, diametroEntreLateralesLabel]
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]
		
		#Borrar

		# diametroOrificios.set("1/4")
		# distanciaOrificios.set("0.100")
		# seccionTransversal.set("14 X 14")
		# distanciaLaterales.set("0.25")
		# diametroEntreLaterales.set("1 1/2")


		
	
		altIn= 30
		for ind in range(0,len(listaLabel)):
			listaLabel[ind].place(x=0,y=altIn)
			listaEntradaDrenaje2[ind].place(x=0, y= altIn+20)
			altIn=altIn+80
		
		botonCalculoDrenaje = HoverButton(drenajeFiltrosMainFrame, text="C??lculos para el drenaje del filtro", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: drenajeFiltro2(caudalMedio,listaEntradaDrenaje))
		botonCalculoDrenaje.place(x=0, y=altIn)
		
		
		def newEntryFiltroDrenaje(lista): 
			lista2= [
						"Diametro de los orificios",
						"Distancia entre los orificios",
						"Secci??n transversal",
						"Distancia entre laterales",
						"Di??metro de los laterales"]

			for i in range(0, len(lista)):
					lista[i].set(lista2[i])



		botonLimpiarEntradasDrenaje = HoverButton(drenajeFiltrosMainFrame, text="Limpiar entradas", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: newEntryFiltroDrenaje(listaEntradaDrenaje))
		botonLimpiarEntradasDrenaje.place(x=0, y=altIn+80)		
		
	
		
		
		drenajeFiltrosMainWindow.mainloop()
	
	def velocidadLavadoExpansionLechoFiltrante(tempValue,d60,porosidadEntry,profundidadEntry):
		

		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None
		
		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None

		velocidadLavadoExpansionLechoFiltranteWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		velocidadLavadoExpansionLechoFiltranteWindow.iconbitmap(bitmap=path)
		velocidadLavadoExpansionLechoFiltranteWindow.geometry("520x400") 
		velocidadLavadoExpansionLechoFiltranteWindow.resizable(0,0)	
		velocidadLavadoExpansionLechoFiltranteWindow.configure(background="#9DC4AA")

		velocidadLavadoExpansionLechoFiltranteFrame=LabelFrame(velocidadLavadoExpansionLechoFiltranteWindow, text="C??lculos para la velocidad de expansi??n del lecho filtrante", font=("Yu Gothic bold", 11))
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
		"Pulse para ver f??rmulas","Valores","Unidades","Adicional"
		)

		#Headings
		arbolvelocidadLavadoExpansionLechoFiltrante.heading("#0",text="ID", anchor=CENTER)

		for col in arbolvelocidadLavadoExpansionLechoFiltrante["columns"]:
			arbolvelocidadLavadoExpansionLechoFiltrante.heading(col, text=col,anchor=CENTER, command= lambda: proyectarImg('images\Hidraulica_VelocidadLavadoYExpansionLechoFiltrante.png',1007,387))	

		listaLargoFila=[0,300,100,100,181]
		for i in range(1,len(arbolvelocidadLavadoExpansionLechoFiltrante["columns"])+1):
			arbolvelocidadLavadoExpansionLechoFiltrante.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolvelocidadLavadoExpansionLechoFiltrante.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolvelocidadLavadoExpansionLechoFiltrante.tag_configure("evenrow", background= "#1FCCDB")
		arbolvelocidadLavadoExpansionLechoFiltrante.tag_configure("oddrow", background= "#9DC4AA")    

		listavelocidadLavadoExpansionLechoFiltrante=list()
	
		
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
		
		listavelocidadLavadoExpansionLechoFiltrante.append(round(viscosidadDinamica,6))

		D60=d60

		listavelocidadLavadoExpansionLechoFiltrante.append(round(D60,3))

		velocidadAsentamientoMedioFiltrante20 = D60*10
		
		listavelocidadLavadoExpansionLechoFiltrante.append(round(velocidadAsentamientoMedioFiltrante20,3))

		velocidadAsentamientoMedioFiltrante3= velocidadAsentamientoMedioFiltrante20*(viscosidadDinamica**(-1/3))

		listavelocidadLavadoExpansionLechoFiltrante.append(round(velocidadAsentamientoMedioFiltrante3,3))

		velocidadFluidizacion3 = velocidadAsentamientoMedioFiltrante3*(porosidad**(4.5))

		listavelocidadLavadoExpansionLechoFiltrante.append(round(velocidadFluidizacion3,3))

		velocidadOptimaLavado3= velocidadAsentamientoMedioFiltrante3*0.1

		listavelocidadLavadoExpansionLechoFiltrante.append(round(velocidadOptimaLavado3,3))

		
		porosidadLechoExpandido = (velocidadOptimaLavado3/velocidadAsentamientoMedioFiltrante3)**(0.22)

		listavelocidadLavadoExpansionLechoFiltrante.append(round(porosidadLechoExpandido,3))

	

		listavelocidadLavadoExpansionLechoFiltrante.append(round(profundidadLechoFijo,3))

		profundidadLechoExpandido= profundidadLechoFijo*((1-porosidad)/(1- porosidadLechoExpandido))

		listavelocidadLavadoExpansionLechoFiltrante.append(round(profundidadLechoExpandido,3))

		relacionExpansion = ((porosidadLechoExpandido-porosidad)/(1-porosidadLechoExpandido))*100

		listavelocidadLavadoExpansionLechoFiltrante.append(round(relacionExpansion,3))
		
		listaEncabezados=[
		"Porosidad del lecho fijo", "Viscosidad din??mica del agua",
		"Percentil 60 del an??lisis granulom??trico", "Velocidad de asentamiento del medio filtrante a 20 ??C",
		f"Velocidad de asentamiento del medio filtrante a {tempValue} ??C",
		f"Velocidad de fluidizaci??n del medio filtrante a {tempValue} ??C",
		f"Velocidad ??ptima de lavado a {tempValue} ??C",
		"Porosidad del lecho expandido",
		"Profundidad del lecho fijo",
		"Profundidad del lecho expandido",
		"Relaci??n de expansi??n",
		]
		listaUnidades=[
			
			"",
			"cP",
			"mm",
			"m/min",
			"m/min",
			"m/min",
			"m/min",
			"",
			"m",
			"m",
			"%",
			]
		
		if velocidadOptimaLavado3<0.3:
			velocidadOptimaLavado3Info="??Error, velocidad de lavado baja!"
		elif velocidadOptimaLavado3<0.84:
			velocidadOptimaLavado3Info="??Error, velocidad de lavado alta!"
		else:
			velocidadOptimaLavado3Info="Velocidad de lavado adecuada"
		
		if relacionExpansion<35:
			relacionExpansionInfo="??Error, relaci??n de expansi??n baja!"
		if relacionExpansion<41:
			relacionExpansionInfo="??Error, relaci??n de expansi??n alta!"
		else:
			relacionExpansionInfo= "Relaci??n de expansi??n adecuada"
				
		
		
		
		listaAdicional=[
			"",
			"",
			"",
			"",
			"",
			"",
			velocidadOptimaLavado3Info,
			"",
			"",
			"",
			relacionExpansionInfo,
			]

		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listavelocidadLavadoExpansionLechoFiltrante[i])
			listaTemp.append(listaUnidades[i])
			listaTemp.append(listaAdicional[i])	
			newDataTreeview(arbolvelocidadLavadoExpansionLechoFiltrante,listaTemp)
		PasarExcelDatos(".\\ResultadosFiltro\\VelocidadDeLavadoYExpansionDelLechoFiltrante.xlsx",'Resultados',listaEncabezados,50, listavelocidadLavadoExpansionLechoFiltrante, 15, listaUnidades, 15,True,listaAdicional, 50)
		velocidadLavadoExpansionLechoFiltranteWindow.mainloop()
	
	def ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60,porosidad,profundidadLechoFijo):
		

		listavelocidadLavadoExpansionLechoFiltrante=list()
	

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

		listavelocidadLavadoExpansionLechoFiltrante.append(porosidadLechoExpandido)

		

		listavelocidadLavadoExpansionLechoFiltrante.append(profundidadLechoFijo)

		profundidadLechoExpandido= profundidadLechoFijo*((1-porosidad)/(1- porosidadLechoExpandido))

		listavelocidadLavadoExpansionLechoFiltrante.append(profundidadLechoExpandido)

		relacionExpansion = ((porosidadLechoExpandido-porosidad)/(1-porosidadLechoExpandido))*100

		listavelocidadLavadoExpansionLechoFiltrante.append(relacionExpansion)
		
		return(listavelocidadLavadoExpansionLechoFiltrante)
		


	def ValueConsumoAguaLavado(listaE,tempValue,d60,caudalLista,porosidad,profundidad):
		

	
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		else:
			tiempoRetrolavado = float(listaE[0].get())

		listaconsumoAguaLavado2=list()

		listaVelocidadVelocidadLavadoExpansion = ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60,porosidad,profundidad)

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


	def consumoAguaLavado(listaE,tempValue,d60,caudalLista,porosidadEntry,profundidadEntry):
		
		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None
	
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		else:
			tiempoRetrolavado = float(listaE[0].get())

		try: 
			caudalMedio=float(caudalLista[0].get())
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero.")
			return None

		if caudalMedio<0.01 or caudalMedio>0.2:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero entre 0.01 y 0.2")
			return None

		

		consumoAguaLavado2Window = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		consumoAguaLavado2Window.iconbitmap(bitmap=path)
		consumoAguaLavado2Window.geometry("450x420") 
		consumoAguaLavado2Window.resizable(0,0)	
		consumoAguaLavado2Window.configure(background="#9DC4AA")

		consumoAguaLavado2Frame=LabelFrame(consumoAguaLavado2Window, text="C??lculos para el consumo de agua de lavado", font=("Yu Gothic bold", 11))
		consumoAguaLavado2Frame.pack(side=TOP, fill=BOTH,expand=True)
		
		#Frame Treeview
		arbolconsumoAguaLavado2_frame = Frame(consumoAguaLavado2Frame)
		arbolconsumoAguaLavado2_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolconsumoAguaLavado2_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolconsumoAguaLavado2_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolconsumoAguaLavado2= ttk.Treeview(arbolconsumoAguaLavado2_frame,selectmode=BROWSE, height=11,show="tree headings")#,yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arbolconsumoAguaLavado2.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolconsumoAguaLavado2.xview)
		# sedScrollY.configure(command=arbolconsumoAguaLavado2.yview)
		#Define columnas.
		arbolconsumoAguaLavado2["columns"]= (
		"Pulse para ver f??rmulas","Valores","Unidades"
		)

		#Headings
		arbolconsumoAguaLavado2.heading("#0",text="ID", anchor=CENTER)
		
		for col in arbolconsumoAguaLavado2["columns"]:
			arbolconsumoAguaLavado2.heading(col, text=col,anchor=CENTER, command= lambda: proyectarImg('images\\Hidraulica_ConsumoAguaLavado.png',1005,259))	

		listaLargoFila=[0,250,100,100]
		for i in range(1,len(arbolconsumoAguaLavado2["columns"])+1):
			arbolconsumoAguaLavado2.column(f"#{i}",width=listaLargoFila[i], stretch=False)	
		arbolconsumoAguaLavado2.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolconsumoAguaLavado2.tag_configure("evenrow", background= "#1FCCDB")
		arbolconsumoAguaLavado2.tag_configure("oddrow", background= "#9DC4AA")    


		listaconsumoAguaLavado2=list()

		listaVelocidadVelocidadLavadoExpansion = ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60,porosidad,profundidadLechoFijo)

		listaconsumoAguaLavado2.append(round(tiempoRetrolavado,3))

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

		listaconsumoAguaLavado2.append(round(porcentajeAguaFiltrada,3))

		listaEncabezados=[

		"Tiempo de retrolavado",
		"Carrera de filtraci??n normal o duraci??n del\nciclo",
		"Velocidad de lavado",
		"Tasa de filtraci??n en operaci??n normal",
		"??rea de un filtro",
		"Caudal de lavado",
		"Consumo de agua para lavado de un filtro\n(Volumen del tanque)",
		"Agua producida por un filtro en cada ciclo",
		"Porcentaje de agua filtrada usada en el lavado\nde un filtro",
		]

		listaUnidades= ["min",
		"horas",
		"m/min",
		"m/d??a",
		"m2",
		"m3/s",
		"m3/ciclo",
		"m3/ciclo",
		"%"
		]
		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaconsumoAguaLavado2[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arbolconsumoAguaLavado2,listaTemp)  

		PasarExcelDatos(".\\ResultadosFiltro\\ConsumoAguaDuranteLavado.xlsx",'Resultados',listaEncabezados,50, listaconsumoAguaLavado2, 15, listaUnidades, 15,False,[], 50)
		consumoAguaLavado2Window.mainloop()




	def valuePerdidaCargaLechoExpandido(porosidadLechoFijo,profundidadLechoFijo,densidadRelativaArena):
		
		listaperdidaCargaLechoExpandido=list()
		
		
		listaperdidaCargaLechoExpandido.append(profundidadLechoFijo)

		listaperdidaCargaLechoExpandido.append(porosidadLechoFijo)

		listaperdidaCargaLechoExpandido.append(densidadRelativaArena)

		perdidaCargaALechoExpandido= profundidadLechoFijo*(1-porosidadLechoFijo)*(densidadRelativaArena-1)
		listaperdidaCargaLechoExpandido.append(perdidaCargaALechoExpandido)

		return listaperdidaCargaLechoExpandido


	def perdidaCargaLechoExpandido(porosidadEntry,profundidadEntry,densidadEntry):
		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None


		if densidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la densidad relativa de arena")
			return None
		try:
			densidadRelativaArena= float(densidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la densidad relativa de arena debe ser un n??mero")
			return None
		
		if densidadRelativaArena <2.5 or densidadRelativaArena >2.7:
			messagebox.showwarning(title="Error", message="El valor de la densidad relativa de arena debe estar entre 2.5 y 2.7")
			return None


		perdidaCargaLechoExpandidoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaLechoExpandidoWindow.iconbitmap(bitmap=path)
		perdidaCargaLechoExpandidoWindow.geometry("360x250") 
		perdidaCargaLechoExpandidoWindow.resizable(0,0)	
		perdidaCargaLechoExpandidoWindow.configure(background="#9DC4AA")

		perdidaCargaLechoExpandidoFrame=LabelFrame(perdidaCargaLechoExpandidoWindow, text="P??rdida de carga a trav??s del lecho expandido", font=("Yu Gothic bold", 8))
		perdidaCargaLechoExpandidoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaLechoExpandido_frame = Frame(perdidaCargaLechoExpandidoFrame)
		arbolperdidaCargaLechoExpandido_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolperdidaCargaLechoExpandido_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidaCargaLechoExpandido_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaLechoExpandido= ttk.Treeview(arbolperdidaCargaLechoExpandido_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaLechoExpandido.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolperdidaCargaLechoExpandido.xview)
		# sedScrollY.configure(command=arbolperdidaCargaLechoExpandido.yview)
		#Define columnas.
		arbolperdidaCargaLechoExpandido["columns"]= (
		"Ver f??rmulas","Valores","Unidades"
		)

		#Headings
		arbolperdidaCargaLechoExpandido.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaLechoExpandido["columns"]:
			arbolperdidaCargaLechoExpandido.heading(col, text=col,anchor=CENTER, command= lambda: proyectarImg('images\\Hidraulica_PerdidaCargaLechoExpandido.png',1004,123))	

		listaLargoFila=[0,200,60,100]
		for i in range(1,len(arbolperdidaCargaLechoExpandido["columns"])+1):
		    arbolperdidaCargaLechoExpandido.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidaCargaLechoExpandido.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaLechoExpandido.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaLechoExpandido.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaLechoExpandido=list()
		

		listaperdidaCargaLechoExpandido.append(profundidadLechoFijo)
		
		listaperdidaCargaLechoExpandido.append(porosidad)

		listaperdidaCargaLechoExpandido.append(densidadRelativaArena)

		perdidaCargaALechoExpandido= profundidadLechoFijo*(1-porosidad)*(densidadRelativaArena-1)
		listaperdidaCargaLechoExpandido.append(round(perdidaCargaALechoExpandido,3))

		listaEncabezados= ["Profundidad del lecho fijo", 
		"Porosidad del lecho fijo",
		"Densidad relativa de la arena",
		"P??rdida de carga a trav??s del lecho\nexpandido"]
		listaUnidades=[
		"m",
		"",
		"",
		"m"
		]
		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaperdidaCargaLechoExpandido[i])
			listaTemp.append(listaUnidades[i])
			
			newDataTreeview(arbolperdidaCargaLechoExpandido,listaTemp)  

		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaCargaATravezLechoExpandido.xlsx",'Resultados',listaEncabezados,50, listaperdidaCargaLechoExpandido, 15, listaUnidades, 15,False,[], 50)
		
		perdidaCargaLechoExpandidoWindow.mainloop()



		
	def valuePerdidacargaLechoGravaLavado(tempValue,d60,porosidad,profundidad):
		
		listaperdidacargaLechoGravaLavado=list()
		
		velocidadLavado= ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60,porosidad,profundidad)[6]
		listaperdidacargaLechoGravaLavado.append(velocidadLavado)

		profundidadLechoGrava= 0.100+0.075+0.075+0.100+0.100

		listaperdidacargaLechoGravaLavado.append(profundidadLechoGrava)

		perdidaLechoGrava= velocidadLavado*profundidadLechoGrava*(1/3)

		listaperdidacargaLechoGravaLavado.append(perdidaLechoGrava)

		return listaperdidacargaLechoGravaLavado


	def perdidacargaLechoGravaLavado(tempValue,d60,porosidadEntry,profundidadEntry):
		
		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None
		
		
		
		perdidacargaLechoGravaLavadoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidacargaLechoGravaLavadoWindow.iconbitmap(bitmap=path)
		perdidacargaLechoGravaLavadoWindow.geometry("400x200") 
		perdidacargaLechoGravaLavadoWindow.resizable(0,0)	
		perdidacargaLechoGravaLavadoWindow.configure(background="#9DC4AA")

		perdidacargaLechoGravaLavadoFrame=LabelFrame(perdidacargaLechoGravaLavadoWindow, text="C??lculos para la p??rdida de carga a trav??s del lecho de grava", font=("Yu Gothic bold", 8))
		perdidacargaLechoGravaLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidacargaLechoGravaLavado_frame = Frame(perdidacargaLechoGravaLavadoFrame)
		arbolperdidacargaLechoGravaLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidacargaLechoGravaLavado= ttk.Treeview(arbolperdidacargaLechoGravaLavado_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidacargaLechoGravaLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolperdidacargaLechoGravaLavado.xview)
		# sedScrollY.configure(command=arbolperdidacargaLechoGravaLavado.yview)
		#Define columnas.
		arbolperdidacargaLechoGravaLavado["columns"]= (
		"Ver f??rmulas","2", "Unidades"
		)

		#Headings
		arbolperdidacargaLechoGravaLavado.heading("#0",text="ID", anchor=CENTER)
		
		
		for col in arbolperdidacargaLechoGravaLavado["columns"]:
			arbolperdidacargaLechoGravaLavado.heading(col, text=col,anchor=CENTER, command= lambda: proyectarImg('images\\Hidraulica_PerdidaCargaATravesLechoGravaDixon.png',1006,126)) 

		listaLargoFila=[0,200,100,100]
		for i in range(1,len(arbolperdidacargaLechoGravaLavado["columns"])+1):
			arbolperdidacargaLechoGravaLavado.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidacargaLechoGravaLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidacargaLechoGravaLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidacargaLechoGravaLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidacargaLechoGravaLavado=list()
		
		velocidadLavado= ValuevelocidadLavadoExpansionLechoFiltrante(tempValue,d60,porosidad,profundidadLechoFijo)[6]
		listaperdidacargaLechoGravaLavado.append(round(velocidadLavado,3))

		profundidadLechoGrava= 0.100+0.075+0.075+0.100+0.100

		listaperdidacargaLechoGravaLavado.append(round(profundidadLechoGrava,3))

		perdidaLechoGrava= velocidadLavado*profundidadLechoGrava*(1/3)

		listaperdidacargaLechoGravaLavado.append(round(perdidaLechoGrava,3))

		listaEncabezados=[
		"Velocidad de lavado", 
		"Profundidad del lecho de grava",
		"P??rdida de carga a trav??s\ndel lecho de grava",
		]
		listaUnidades=[
		"m/min",
		"m",
		"m"
		]
		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaperdidacargaLechoGravaLavado[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arbolperdidacargaLechoGravaLavado,listaTemp)  

		PasarExcelDatos(".\\ResultadosFiltro\\perdidaCargaAtravesLechoGrava.xlsx",'Resultados',listaEncabezados,50, listaperdidacargaLechoGravaLavado, 15, listaUnidades, 15,False,[], 50)

		perdidacargaLechoGravaLavadoWindow.mainloop()



	def valuePerdidacargaLechoGravaLavado_2(tempValue,d60,tasa):

		listaperdidacargaLechoGravaLavado=list()
		if tasa == "Tasa media":
			velocidadLavado= 120/(24*60)
		elif tasa == "Tasa m??xima":
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
		path=resource_path('icons\\agua.ico')
		perdidacargaLechoGravaLavadoWindow.iconbitmap(bitmap=path)
		perdidacargaLechoGravaLavadoWindow.geometry("400x200") 
		perdidacargaLechoGravaLavadoWindow.resizable(0,0)	
		perdidacargaLechoGravaLavadoWindow.configure(background="#9DC4AA")

		perdidacargaLechoGravaLavadoFrame=LabelFrame(perdidacargaLechoGravaLavadoWindow, text=f"C??lculos para la p??rdida de energ??a en el lecho de grava a {tasa.lower()}\nde filtraci??n (Dixon)", font=("Yu Gothic bold",8 ))
		perdidacargaLechoGravaLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidacargaLechoGravaLavado_frame = Frame(perdidacargaLechoGravaLavadoFrame)
		arbolperdidacargaLechoGravaLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidacargaLechoGravaLavado_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidacargaLechoGravaLavado= ttk.Treeview(arbolperdidacargaLechoGravaLavado_frame,selectmode=BROWSE, height=11,show="tree headings") #,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidacargaLechoGravaLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolperdidacargaLechoGravaLavado.xview)
		# sedScrollY.configure(command=arbolperdidacargaLechoGravaLavado.yview)
		#Define columnas.
		arbolperdidacargaLechoGravaLavado["columns"]= (
		"Ver f??rmulas","Valores","Unidades"
		)

		#Headings
		arbolperdidacargaLechoGravaLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidacargaLechoGravaLavado["columns"]:
			arbolperdidacargaLechoGravaLavado.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg('images\\PerdidaLechoLimpio_PerdidaEnergiaLechoGrava.png',1007,131))	

		listaLargoFila=[0,200,100,100]
		for i in range(1,len(arbolperdidacargaLechoGravaLavado["columns"])+1):
			arbolperdidacargaLechoGravaLavado.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidacargaLechoGravaLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidacargaLechoGravaLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidacargaLechoGravaLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidacargaLechoGravaLavado=list()
		if tasa == "Tasa media":
			velocidadLavado= 120/(24*60)
		elif tasa == "Tasa m??xima":
			velocidadLavado= 150/(24*60)
		
		listaperdidacargaLechoGravaLavado.append(round(velocidadLavado,3))

		profundidadLechoGrava= 0.100+0.075+0.075+0.100+0.100

		listaperdidacargaLechoGravaLavado.append(round(profundidadLechoGrava,3))

		perdidaLechoGrava= velocidadLavado*profundidadLechoGrava*(1/3)

		listaperdidacargaLechoGravaLavado.append(round(perdidaLechoGrava,3))


		listaEncabezados=[	"Tasa de filtraci??n", 
		"Profundidad del lecho de grava",
		"P??rdida de carga a trav??s\ndel lecho de grava",]
		
		listaUnidades=[
		"m/min",
		"m",
		"m"
		]

		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaperdidacargaLechoGravaLavado[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arbolperdidacargaLechoGravaLavado,listaTemp) 

		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaEnergiaLechoGravaDuranteFiltradoLechoLimpio.xlsx",'Resultados',listaEncabezados,50, listaperdidacargaLechoGravaLavado, 15, listaUnidades, 15,False,[], 50)
		perdidacargaLechoGravaLavadoWindow.mainloop()

	def valuePerdidaCargaSistemaDrenajeLavado(tempValue,d60, caudal,listaEntradaDrenaje,porosidad,profundidad):
		
		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		velocidadDeLavado= round(ValuevelocidadLavadoExpansionLechoFiltrante(tempValue, d60,porosidad,profundidad)[6]*(1/60.0),4)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(velocidadDeLavado)

		coeficienteDeOrificio=0.6
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(coeficienteDeOrificio)

		areaTotalOrificios=round(ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[5],4)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(areaTotalOrificios)

		

		perdidaCargaSistemaDrenaje= (1/(2.0*9.806))*((velocidadDeLavado/(coeficienteDeOrificio*areaTotalOrificios))**2)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(perdidaCargaSistemaDrenaje)

		return listaperdidaCargaSistemaDrenajeLavadoLavado

		

		



	def perdidaCargaSistemaDrenajeLavado(tempValue,d60, caudal,listaEntradaDrenaje,porosidadEntry,profundidadEntry):
		
		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None
		
		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None
	

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		
		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
	
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		
	

		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
		

		
		
		
		perdidaCargaSistemaDrenajeLavadoLavadoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.iconbitmap(bitmap=path)
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.geometry("400x240") 
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.resizable(0,0)	
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaSistemaDrenajeLavadoLavadoFrame=LabelFrame(perdidaCargaSistemaDrenajeLavadoLavadoWindow, text="C??lculos para la p??rdida de carga a trav??s\ndel sistema de drenaje durante el lavado", font=("Yu Gothic bold", 8))
		perdidaCargaSistemaDrenajeLavadoLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame = Frame(perdidaCargaSistemaDrenajeLavadoLavadoFrame)
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado= ttk.Treeview(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaSistemaDrenajeLavadoLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.xview)
		# sedScrollY.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.yview)
		#Define columnas.
		arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]= (
		"Ver las f??rmulas","Valores","Unidades"
		)

		#Headings
		arbolperdidaCargaSistemaDrenajeLavadoLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]:
			arbolperdidaCargaSistemaDrenajeLavadoLavado.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg('images\\Hidraulica_PeridaCargaATravezDrenajeLavado.png',1003,155))	

		listaLargoFila=[0,200,100,100]
		for i in range(1,len(arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"])+1):
			arbolperdidaCargaSistemaDrenajeLavadoLavado.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidaCargaSistemaDrenajeLavadoLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		velocidadDeLavado= round(ValuevelocidadLavadoExpansionLechoFiltrante(tempValue, d60,porosidad,profundidadLechoFijo)[6]*(1/60.0),4)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(velocidadDeLavado)

		coeficienteDeOrificio=0.6
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(coeficienteDeOrificio)

		areaTotalOrificios=(ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[5])
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(round(areaTotalOrificios,3))

	
	
		perdidaCargaSistemaDrenaje= (1.0/(2.0*9.806))*((velocidadDeLavado/(coeficienteDeOrificio*areaTotalOrificios))**2)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(round(perdidaCargaSistemaDrenaje,3))

		listaEncabezados=["Velocidad de lavado",
		"Coeficiente de orificio",
		"??rea total de orificios\n/??rea filtrante",
		"P??rdida de carga a trav??s\ndel sistema de drenaje"]
		listaUnidades=[
		"m/s",
		"",
		"",
		"m"
		]
		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaperdidaCargaSistemaDrenajeLavadoLavado[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arbolperdidaCargaSistemaDrenajeLavadoLavado,listaTemp)  

		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaCargaAtravezSistemaDrenajeDuranteLavado.xlsx",'Resultados',listaEncabezados,50, listaperdidaCargaSistemaDrenajeLavadoLavado, 15, listaUnidades, 15,False,[], 50)


		perdidaCargaSistemaDrenajeLavadoLavadoWindow.mainloop()


	def valuePerdidaCargaSistemaDrenajeLavado_2(tempValue,d60, caudal,listaEntradaDrenaje, tasa):

		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		if tasa == "Tasa media":
			velocidadDeLavado= 120.0/86400.0
		elif tasa == "Tasa m??xima":
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
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())


		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())


		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()

		perdidaCargaSistemaDrenajeLavadoLavadoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.iconbitmap(bitmap=path)
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.geometry("400x240") 
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.resizable(0,0)	
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaSistemaDrenajeLavadoLavadoFrame=LabelFrame(perdidaCargaSistemaDrenajeLavadoLavadoWindow, text=f"C??lculos para la p??rdida de energ??a en el sistema de drenaje\na {tasa.lower()} de filtraci??n.", font=("Yu Gothic bold", 8))
		perdidaCargaSistemaDrenajeLavadoLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame = Frame(perdidaCargaSistemaDrenajeLavadoLavadoFrame)
		arbolperdidaCargaSistemaDrenajeLavadoLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaSistemaDrenajeLavadoLavado= ttk.Treeview(arbolperdidaCargaSistemaDrenajeLavadoLavado_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaSistemaDrenajeLavadoLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.xview)
		# sedScrollY.configure(command=arbolperdidaCargaSistemaDrenajeLavadoLavado.yview)
		#Define columnas.
		arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]= (
		"Ver f??rmulas","Valores","Unidades"
		)

		#Headings
		arbolperdidaCargaSistemaDrenajeLavadoLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"]:
			arbolperdidaCargaSistemaDrenajeLavadoLavado.heading(col, text=col,anchor=CENTER,command=lambda: proyectarImg('images\\PerdidaLechoLimpio_PerdidaEnergiaDrenaje.png',1004,155))	

		listaLargoFila=[0,200,100,100]
		for i in range(1,len(arbolperdidaCargaSistemaDrenajeLavadoLavado["columns"])+1):
			arbolperdidaCargaSistemaDrenajeLavadoLavado.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidaCargaSistemaDrenajeLavadoLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaSistemaDrenajeLavadoLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaSistemaDrenajeLavadoLavado=list()
		
		if tasa == "Tasa media":
			velocidadDeLavado= 120.0/86400.0
		elif tasa == "Tasa m??xima":
			velocidadDeLavado= 150.0/86400.0
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(round(velocidadDeLavado,3))

		coeficienteDeOrificio=0.6
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(round(coeficienteDeOrificio,3))

		areaTotalOrificios=(ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[5])
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(round(areaTotalOrificios,3))

	

		perdidaCargaSistemaDrenaje= (1.0/(2.0*9.806))*((velocidadDeLavado/(coeficienteDeOrificio*areaTotalOrificios))**2)
		listaperdidaCargaSistemaDrenajeLavadoLavado.append(round(perdidaCargaSistemaDrenaje,3))
		
		listaEncabezados= ["Tasa de filtraci??n",
		"Coeficiente de orificio",
		"??rea total de orificios\n/??rea filtrante",
		"P??rdida de carga a trav??s\ndelsistema de drenaje",
		]
		listaUnidades=[
		"m/s",
		"",
		"",
		"m"
		]

		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaperdidaCargaSistemaDrenajeLavadoLavado[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arbolperdidaCargaSistemaDrenajeLavadoLavado,listaTemp)  

		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaEnergiaEnSistemaDrenajeFiltradoLechoLimpio.xlsx",'Resultados',listaEncabezados,50, listaperdidaCargaSistemaDrenajeLavadoLavado, 15, listaUnidades, 15,False,[], 50)
		perdidaCargaSistemaDrenajeLavadoLavadoWindow.mainloop()

	
	def ValuePerdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista,porosidad,profundidad):
		
		

		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None

					elif elemento.get() == "Codo 90?? radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90?? radio")
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
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None
			
		listaEU.append(temperatureValue)
		
		
		

		listaEntradaTemp1=list()
		listaEntradaTemp2=list()
		listaEntradaTemp3=list()
		

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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

		caudalLavado = ValueConsumoAguaLavado(listaE1,temperatureValue,d60,caudalLista,porosidad,profundidad)[5]
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


		
		
		
		accesoriosLista = ["V??lvula de compuerta\ncompletamente abierta",
		"Codo 90?? radio corto (r/d 1)",
		"Codo 90?? radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Uni??n",
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


		accesoriosListaEntrada= ["V??lvula de compuerta\ncompletamente abierta",
		f"{listaEU[4]}",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Uni??n",
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



	def perdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista,unidadesDiametro,porosidad,profundidad):
		
		

		
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None

					elif elemento.get() == "Codo 90?? radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90?? radio")
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
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None
			
		listaEU.append(temperatureValue)
		


		perdidaCargaTuberiaLavado_DW_HW2Window = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HW2Window.iconbitmap(bitmap=path)
		perdidaCargaTuberiaLavado_DW_HW2Window.geometry("675x470") 
		perdidaCargaTuberiaLavado_DW_HW2Window.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HW2Window.configure(background="#9DC4AA")




		##Panel:
		PanelPerdidaCargaTuberiaLavado = ttk.Notebook(perdidaCargaTuberiaLavado_DW_HW2Window)
		PanelPerdidaCargaTuberiaLavado.pack(fill=BOTH, expand=TRUE)
		###########Frame Principal1
		PerdidaCargaTuberiaLavado_DWFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimaci??n de la p??rdida de carga en la tuber??a de lavado", font=("Yu Gothic bold", 11))
		PerdidaCargaTuberiaLavado_DWFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(PerdidaCargaTuberiaLavado_DWFrame,text="Darcy - Weisbach")
		#Frame Treeview
		arbolPerdidaCargaTuberiaLavado_DW_frame = LabelFrame(PerdidaCargaTuberiaLavado_DWFrame, text="Darcy - Weisbach", font=("Yu Gothic bold", 11))
		arbolPerdidaCargaTuberiaLavado_DW_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaCargaTuberiaLavado_DW= ttk.Treeview(arbolPerdidaCargaTuberiaLavado_DW_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set)#xscrollcommand=sedScrollX.set,
		arbolPerdidaCargaTuberiaLavado_DW.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolPerdidaCargaTuberiaLavado_DW.xview)
		sedScrollY.configure(command=arbolPerdidaCargaTuberiaLavado_DW.yview)
		#Define columnas.
		arbolPerdidaCargaTuberiaLavado_DW["columns"]= (
		"Ver las f??rmulas","Valores","Unidades"
		)
		
		#Headings
		
		
		arbolPerdidaCargaTuberiaLavado_DW.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaCargaTuberiaLavado_DW["columns"]:
			arbolPerdidaCargaTuberiaLavado_DW.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg('images\\Hidraulica_PeridaCargaTuberaDW.png',807,434))	

		listaLargoFila1=[0,250,300,100]
		for i in range(1,len(arbolPerdidaCargaTuberiaLavado_DW["columns"])+1):
			arbolPerdidaCargaTuberiaLavado_DW.column(f"#{i}",width=listaLargoFila1[i], stretch=False)		
		arbolPerdidaCargaTuberiaLavado_DW.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("oddrow", background= "#1FCCDB")
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("evenrow", background= "#9DC4AA")

		################Frame principal2
		PerdidaCargaTuberiaLavado_HWFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimaci??n de la p??rdida de carga en la tuber??a de lavado", font=("Yu Gothic bold", 11))
		PerdidaCargaTuberiaLavado_HWFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(PerdidaCargaTuberiaLavado_HWFrame,text="Hazen - Williams")
		#Frame Treeview
		arbolPerdidaCargaTuberiaLavado_HW_frame = LabelFrame(PerdidaCargaTuberiaLavado_HWFrame, text="Hazen - Williams", font=("Yu Gothic bold", 11))
		arbolPerdidaCargaTuberiaLavado_HW_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolPerdidaCargaTuberiaLavado_HW_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolPerdidaCargaTuberiaLavado_HW_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaCargaTuberiaLavado_HW= ttk.Treeview(arbolPerdidaCargaTuberiaLavado_HW_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolPerdidaCargaTuberiaLavado_HW.pack(side=TOP, fill=BOTH, expand=TRUE)
		
		# sedScrollX.configure(command=arbolPerdidaCargaTuberiaLavado_HW.xview)
		# sedScrollY.configure(command=arbolPerdidaCargaTuberiaLavado_HW.yview)
		#Define columnas.
		arbolPerdidaCargaTuberiaLavado_HW["columns"]= (
		"Ver las f??rmulas","Valores","Unidades"
		)

		#Headings
		arbolPerdidaCargaTuberiaLavado_HW.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaCargaTuberiaLavado_HW["columns"]:
			arbolPerdidaCargaTuberiaLavado_HW.heading(col, text=col,anchor=CENTER, command= lambda: proyectarImg('images\\Hidraulica_PeridaCargaTuberiaHZ.png',1003,253))	

		listaLargoFila2=[0,250,300,120]
		for i in range(1,len(arbolPerdidaCargaTuberiaLavado_HW["columns"])+1):
			arbolPerdidaCargaTuberiaLavado_HW.column(f"#{i}",width=listaLargoFila2[i], stretch=False)		
		arbolPerdidaCargaTuberiaLavado_HW.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPerdidaCargaTuberiaLavado_HW.tag_configure("oddrow", background= "#1FCCDB")
		arbolPerdidaCargaTuberiaLavado_HW.tag_configure("evenrow", background= "#9DC4AA")

		##########Frame principal3
		perdidaCargaTuberiaLavado_ACFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimaci??n de la p??rdida de carga en la tuber??a de lavado por accesorios", font=("Yu Gothic bold", 8))
		perdidaCargaTuberiaLavado_ACFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(perdidaCargaTuberiaLavado_ACFrame,text="Accesorios")
		#Frame Treeview
		arbolperdidaCargaTuberiaLavado_AC_frame = LabelFrame(perdidaCargaTuberiaLavado_ACFrame, text="Accesorios", font=("Yu Gothic bold", 11))
		arbolperdidaCargaTuberiaLavado_AC_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)
		
		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		#sedScrollY=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTuberiaLavado_AC= ttk.Treeview(arbolperdidaCargaTuberiaLavado_AC_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set) #,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTuberiaLavado_AC.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaTuberiaLavado_AC.xview)
		#sedScrollY.configure(command=arbolperdidaCargaTuberiaLavado_AC.yview)
		#Define columnas.
		arbolperdidaCargaTuberiaLavado_AC["columns"]= (
		"Accesorio",
		"Di??metro nominal",
		"Cantidad",
		"Coeficiente de p??rdida menor",
		"Sumatoria de coeficientes de p??rdida menor",
		"P??rdida de carga en la tuber??a de lavado por accesorios"
		)

		#Headings
		arbolperdidaCargaTuberiaLavado_AC.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTuberiaLavado_AC["columns"]:
			arbolperdidaCargaTuberiaLavado_AC.heading(col, text=col,anchor=CENTER)	

		listaLargoFila=[0,200,200,200,300,450,560]
		for i in range(1,len(arbolperdidaCargaTuberiaLavado_AC["columns"])+1):
			arbolperdidaCargaTuberiaLavado_AC.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidaCargaTuberiaLavado_AC.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("oddrow", background= "#1FCCDB")
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("evenrow", background= "#9DC4AA")



		############Insersi??n datos.
	
		
		contadorFiltro = 0

		listaEntradaTemp1=list()
		listaEntradaTemp2=list()
		listaEntradaTemp3=list()
		

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]
		
		rugosidadLista=[0.1500, 0.1500, 0.2500,0.2500,0.0070,0.0070,0.0015,0.0015]

		
		rugosidadDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadDic[MaterialTuberiaLista[i]] = rugosidadLista[i]
		
		rugosidadAbsoluta= rugosidadDic[listaEU[0]]
		
		listaEntradaTemp1.append(listaE[0].get())

		listaEntradaTemp1.append(round(rugosidadAbsoluta,3))

		

		listaEntradaTemp1.append(listaE[2].get())
		listaEntradaTemp1.append(listaE[1].get())

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
		listaEntradaTemp1.append(round(diametroInternoTuberiaLavado,3))

		caudalLavado = ValueConsumoAguaLavado(listaE1,temperatureValue,d60,caudalLista,porosidad,profundidad)[5]
		velocidadFlujoTuberiaLavado = (4.0*caudalLavado)*(1.0/(pi*(diametroInternoTuberiaLavado**2)))
		listaEntradaTemp1.append(round(velocidadFlujoTuberiaLavado,3))
		
		cabezaVelocidad = (velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))
		listaEntradaTemp1.append(round(cabezaVelocidad,3))

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

		listaEntradaTemp1.append(round(viscocidadCinematica,7))

		numeroReynolds= velocidadFlujoTuberiaLavado*diametroInternoTuberiaLavado*(1/viscocidadCinematica)
		listaEntradaTemp1.append(round(numeroReynolds,2))

		factorFriccionInicial = listaEU[3]
		
		listaEntradaTemp1.append(round(factorFriccionInicial,7))
		
		factorFriccion=listaEU[3]

		for i in range(0,5):
			factorFriccion= (1/(-2*log10(((rugosidadAbsoluta/1000)*(1/(3.7*diametroInternoTuberiaLavado)))+(2.51*(1/(numeroReynolds*sqrt(factorFriccion)))))))**2
		
		listaEntradaTemp1.append(round(factorFriccion,7))

		perdidaCargaTuberiaLavadoDW= factorFriccion*(listaEU[2]/diametroInternoTuberiaLavado)*(velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))

		listaEntradaTemp1.append(round(perdidaCargaTuberiaLavadoDW,3))
		
		listaEncabezados1=[
		"Material de la tuber??a de lavado",
		"Rugosidad absoluta de la tuber??a",
		"Longitud de la tuber??a de lavado",
		"Di??metro nominal de la tuber??a de lavado",
		"Di??metro interno de la tuber??a de lavado",
		"Velocidad de flujo en la tuber??a de lavado",
		"Cabeza de velocidad",
		f"Viscosidad cinem??tica del agua a {temperatureValue} ??C ",
		"N??mero de Reynolds",
		"Factor de fricci??n (Asumido)",
		"Factor de fricci??n (Iteraci??n 4)",
		"P??rdida de carga en la tuber??a de lavado\n(Sin accesorios)", ]
		
		listaUnidades1=[
			"",
			"mm",
			"m",
			unidadesDiametro,
			"m",
			"m/s",
			"m",
			"(m^2)/s",
			"",
			"",
			"",
			"m"]
		
		for i in range(0, len(listaEncabezados1)):
			listaTemp=list()
			listaTemp.append(listaEncabezados1[i])
			listaTemp.append(listaEntradaTemp1[i])
			listaTemp.append(listaUnidades1[i])	
			newDataTreeview(arbolPerdidaCargaTuberiaLavado_DW,listaTemp) 
		
		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaCargaEnLaTuberiaDeLavadoDW.xlsx",'Resultados',listaEncabezados1,50, listaEntradaTemp1, 15, listaUnidades1, 15,False,[], 50)
			

		#DatosPara2
		
		
	
		coeficienteRugosidadHazenLista = [140, 140, 140, 140, 150, 150, 150, 150]

		rugosidadHazenDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadHazenDic[MaterialTuberiaLista[i]] = coeficienteRugosidadHazenLista[i]

		coeficienteRugosidadHazen= rugosidadHazenDic[listaEU[0]]
		listaEntradaTemp2.append(listaE[0].get())
		listaEntradaTemp2.append(coeficienteRugosidadHazen)

		longitudTuberiaLavado = listaEU[2]
		listaEntradaTemp2.append(round(longitudTuberiaLavado,3))

		diametroNominalTuberiaLavado = listaEU[1]
		listaEntradaTemp2.append(round(diametroNominalTuberiaLavado,3))

		listaEntradaTemp2.append(round(diametroInternoTuberiaLavado,3))

		listaEntradaTemp2.append(round(velocidadFlujoTuberiaLavado,3))

		perdidaCargaUnitariaTuberiaLavado = (velocidadFlujoTuberiaLavado*(1/(0.354597213*coeficienteRugosidadHazen*(diametroInternoTuberiaLavado**0.63))))**(1/0.54)

		listaEntradaTemp2.append(round(perdidaCargaUnitariaTuberiaLavado,3))

		perdidaCargaTuberiaLavadoSinAccesorios = perdidaCargaUnitariaTuberiaLavado*longitudTuberiaLavado

		listaEntradaTemp2.append(round(perdidaCargaTuberiaLavadoSinAccesorios,3))

		listaEncabezados2=[
		"Material de la tuber??a de lavado",
		"Coeficiente de rugosidad de Hazen-Williams",
		"Longitud de la tuber??a de lavado",
		"Di??metro nominal de la tuber??a de lavado",
		"Di??metro interno de la tuber??a de lavado",
		"Velocidad de flujo en la tuber??a de lavado",
		"P??rdida de carga unitaria en la tuber??a\nde lavado",
		"P??rdida de carga en la tuber??a de lavado\n(Sin accersorios)",]
		listaUnidades2=[
		"",
		"-",
		"m",
		unidadesDiametro,
		"m",
		"m/s",
		"m/m",
		"m"
		]
		for i in range(0, len(listaEncabezados2)):
			listaTemp=list()
			listaTemp.append(listaEncabezados2[i])
			listaTemp.append(listaEntradaTemp2[i])
			listaTemp.append(listaUnidades2[i])
			
			newDataTreeview(arbolPerdidaCargaTuberiaLavado_HW,listaTemp)  


		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaCargaEnLaTuberiaDeLavadoHZ.xlsx",'Resultados',listaEncabezados2,50, listaEntradaTemp2, 15, listaUnidades2, 15,False,[], 50)
			
		#DatosPara3
	
		
		tuplasEntradas2=list()
		
		accesoriosLista = ["V??lvula de compuerta\ncompletamente abierta",
		"Codo 90?? radio corto (r/d 1)",
		"Codo 90?? radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Uni??n",
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

		accesoriosListaEntrada= ["V??lvula de compuerta\ncompletamente abierta",
		f"{listaEU[4]}",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Uni??n",
		f"{listaEU[5]}",
		"Salida del tubo"]

		
		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	
		sumaCoeficientesPerdidaMenor= 0
		
		for element in accesoriosListaEntrada:
			sumaCoeficientesPerdidaMenor=sumaCoeficientesPerdidaMenor+ CoeficientePerdidaMenorDic[(element,listaEU[1])]

		col1=list()
		col2=list()
		col3=list()
		col4=list()
		col5=list()
		col6=list()
		peridaCargaTuberiaLavadoAccesorios= sumaCoeficientesPerdidaMenor*cabezaVelocidad
		for elemento in accesoriosListaEntrada:
			listaEntradaTemp3=list()
			listaEntradaTemp3.append(elemento)
			col1.append(elemento)
			listaEntradaTemp3.append(listaEU[1])
			col2.append(listaEU[1])
			listaEntradaTemp3.append(1)
			col3.append(1)
			listaEntradaTemp3.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			col4.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			listaEntradaTemp3.append(round(sumaCoeficientesPerdidaMenor,3))
			col5.append(round(sumaCoeficientesPerdidaMenor,3))
			listaEntradaTemp3.append(round(peridaCargaTuberiaLavadoAccesorios,3))
			col6.append(round(peridaCargaTuberiaLavadoAccesorios,3))
			newDataTreeview(arbolperdidaCargaTuberiaLavado_AC, listaEntradaTemp3)
		colsDatos=[col1,col2,col3,col4,col5,col6]
		pasarTreeViewExcel(colsDatos,arbolperdidaCargaTuberiaLavado_AC,'.\\ResultadosFiltro\\PerdidaEnergiaTuberiaEfluenteAccesorios.xlsx')

		
		perdidaCargaTuberiaLavado_DW_HW2Window.mainloop()


	def valuePerdidaCargaTuberiaLavado_DW_HW2_2(listaE,temperatureValue,listaE1, d60,caudalLista,tasa):
		

		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None

					elif elemento.get() == "Codo 90?? radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90?? radio")
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
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a del efluente debe estar entre 1.5 y 2.5 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None
			
		listaEU.append(temperatureValue)
		


		
		############Insersi??n datos.
		

		listaEntradaTemp1=list()
		
		listaEntradaTemp3=list()
		

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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
		elif tasa == "Tasa m??xima":
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

		accesoriosLista = ["V??lvula de compuerta\ncompletamente abierta",
		"Codo 90?? radio corto (r/d 1)",
		"Codo 90?? radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Uni??n",
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

		accesoriosListaEntrada= ["V??lvula de compuerta\ncompletamente abierta",
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

	def perdidaCargaTuberiaLavado_DW_HW2_2(listaE,temperatureValue,listaE1, d60,caudalLista,tasa,unidadesDiametroNominal):
		
	

		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None

					elif elemento.get() == "Codo 90?? radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90?? radio")
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
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a del efluente debe estar entre 1.5 y 2.5 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None
			
		listaEU.append(temperatureValue)
		


		perdidaCargaTuberiaLavado_DW_HW2Window = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HW2Window.iconbitmap(bitmap=path)
		perdidaCargaTuberiaLavado_DW_HW2Window.geometry("650x470") 
		perdidaCargaTuberiaLavado_DW_HW2Window.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HW2Window.configure(background="#9DC4AA")




		##Panel:
		PanelPerdidaCargaTuberiaLavado = ttk.Notebook(perdidaCargaTuberiaLavado_DW_HW2Window)
		PanelPerdidaCargaTuberiaLavado.pack(fill=BOTH, expand=TRUE)
		###########Frame Principal1
		PerdidaCargaTuberiaLavado_DWFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text=f"Estimaci??n de la p??rdida de energ??a en la tuber??a del efluente a {tasa.lower()} de filtraci??n.", font=("Yu Gothic bold", 10))
		PerdidaCargaTuberiaLavado_DWFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(PerdidaCargaTuberiaLavado_DWFrame,text="Darcy - Weisbach")
		#Frame Treeview
		arbolPerdidaCargaTuberiaLavado_DW_frame = LabelFrame(PerdidaCargaTuberiaLavado_DWFrame, text="Darcy - Weisbach", font=("Yu Gothic bold", 11))
		arbolPerdidaCargaTuberiaLavado_DW_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolPerdidaCargaTuberiaLavado_DW_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolPerdidaCargaTuberiaLavado_DW= ttk.Treeview(arbolPerdidaCargaTuberiaLavado_DW_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set)#,xscrollcommand=sedScrollX.set
		arbolPerdidaCargaTuberiaLavado_DW.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolPerdidaCargaTuberiaLavado_DW.xview)
		sedScrollY.configure(command=arbolPerdidaCargaTuberiaLavado_DW.yview)
		#Define columnas.
		arbolPerdidaCargaTuberiaLavado_DW["columns"]= (
		"Ver f??rmulas","Valores","Unidades"
		)

		#Headings
		arbolPerdidaCargaTuberiaLavado_DW.heading("#0",text="ID", anchor=CENTER)

		for col in arbolPerdidaCargaTuberiaLavado_DW["columns"]:
			arbolPerdidaCargaTuberiaLavado_DW.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg('images\\PerdidaLechoLimpio_PerdidaEnergaEfluenteDW.png',805,465))	

		listaLargoFila1=[0,250,270,100]
		for i in range(1,len(arbolPerdidaCargaTuberiaLavado_DW["columns"])+1):
			arbolPerdidaCargaTuberiaLavado_DW.column(f"#{i}",width=listaLargoFila1[i], stretch=False)		
		arbolPerdidaCargaTuberiaLavado_DW.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("oddrow", background= "#1FCCDB")
		arbolPerdidaCargaTuberiaLavado_DW.tag_configure("evenrow", background= "#9DC4AA")



		##########Frame principal3
		perdidaCargaTuberiaLavado_ACFrame=LabelFrame(PanelPerdidaCargaTuberiaLavado, text="Estimaci??n de la p??rdida de carga en la tuber??a de lavado por accesorios", font=("Yu Gothic bold", 11))
		perdidaCargaTuberiaLavado_ACFrame.pack(side=TOP, fill=BOTH,expand=True)
		PanelPerdidaCargaTuberiaLavado.add(perdidaCargaTuberiaLavado_ACFrame,text="Accesorios")
		#Frame Treeview
		arbolperdidaCargaTuberiaLavado_AC_frame = LabelFrame(perdidaCargaTuberiaLavado_ACFrame, text="Accesorios", font=("Yu Gothic bold", 11))
		arbolperdidaCargaTuberiaLavado_AC_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		sedScrollX=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=HORIZONTAL)
		sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidaCargaTuberiaLavado_AC_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTuberiaLavado_AC= ttk.Treeview(arbolperdidaCargaTuberiaLavado_AC_frame,selectmode=BROWSE, height=11,show="tree headings",xscrollcommand=sedScrollX.set)#,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTuberiaLavado_AC.pack(side=TOP, fill=BOTH, expand=TRUE)

		sedScrollX.configure(command=arbolperdidaCargaTuberiaLavado_AC.xview)
		#sedScrollY.configure(command=arbolperdidaCargaTuberiaLavado_AC.yview)
		#Define columnas.
		arbolperdidaCargaTuberiaLavado_AC["columns"]= (
		"Accesorio",
		"Di??metro nominal",
		"Cantidad",
		"Coeficiente de p??rdida menor",
		"Sumatoria de coeficientes de p??rdida menor",
		"P??rdida de carga en la tuber??a de lavado por accesorios"
		)

		#Headings
		arbolperdidaCargaTuberiaLavado_AC.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTuberiaLavado_AC["columns"]:
			arbolperdidaCargaTuberiaLavado_AC.heading(col, text=col,anchor=CENTER)	

		listaLargoFila=[0,200,200,200,300,450,560]
		for i in range(1,len(arbolperdidaCargaTuberiaLavado_AC["columns"])+1):
			arbolperdidaCargaTuberiaLavado_AC.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidaCargaTuberiaLavado_AC.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("oddrow", background= "#1FCCDB")
		arbolperdidaCargaTuberiaLavado_AC.tag_configure("evenrow", background= "#9DC4AA")



		############Insersi??n datos.
	
		
		contadorFiltro = 0

		listaEntradaTemp1=list()
		listaEntradaTemp2=list()
		listaEntradaTemp3=list()
		datosSalida=list()

		#DatosPara1        
		
	

		#Tablas1
		MaterialTuberiaLista=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
		"Policluro de vinilo (PVC) RDE 26","Policluro de vinilo (PVC) RDE 21"]
		
		rugosidadLista=[0.1500, 0.1500, 0.2500,0.2500,0.0070,0.0070,0.0015,0.0015]


		rugosidadDic=dict()
		
		for i in range(0,len(MaterialTuberiaLista)):
			rugosidadDic[MaterialTuberiaLista[i]] = rugosidadLista[i]
		
		rugosidadAbsoluta= rugosidadDic[listaEU[0]]
		
		listaEntradaTemp1.append(listaEU[0])
		listaEntradaTemp1.append(round(rugosidadAbsoluta,3))
		listaEntradaTemp1.append(listaEU[2])
		listaEntradaTemp1.append(listaEU[1])
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
		listaEntradaTemp1.append(round(diametroInternoTuberiaLavado,3))

		if tasa == "Tasa media":
			caudalLavado = (120.0/86400.0)*ValuepredimensionamientoFiltros(caudalLista)[8]
		elif tasa == "Tasa m??xima":
			caudalLavado = (150.0/86400.0)*ValuepredimensionamientoFiltros(caudalLista)[8]

		listaEntradaTemp1.append(round(caudalLavado,3))

		velocidadFlujoTuberiaLavado = (4.0*caudalLavado)*(1.0/(pi*(diametroInternoTuberiaLavado**2)))
		listaEntradaTemp1.append(round(velocidadFlujoTuberiaLavado,3))
		
		cabezaVelocidad = (velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))
		listaEntradaTemp1.append(round(cabezaVelocidad,3))

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

		listaEntradaTemp1.append(round(viscocidadCinematica,7))

		numeroReynolds= velocidadFlujoTuberiaLavado*diametroInternoTuberiaLavado*(1/viscocidadCinematica)
		listaEntradaTemp1.append(round(numeroReynolds,2))

		factorFriccionI=listaEU[3]
		listaEntradaTemp1.append(round(factorFriccionI,7))
		factorFriccion=listaEU[3]

		for i in range(0,5):
			factorFriccion= (1/(-2*log10(((rugosidadAbsoluta/1000)*(1/(3.7*diametroInternoTuberiaLavado)))+(2.51*(1/(numeroReynolds*sqrt(factorFriccion)))))))**2
		
		listaEntradaTemp1.append(round(factorFriccion,7))

		perdidaCargaTuberiaLavadoDW= factorFriccion*(listaEU[2]/diametroInternoTuberiaLavado)*(velocidadFlujoTuberiaLavado**2)*(1/(2*9.806))

		listaEntradaTemp1.append(round(perdidaCargaTuberiaLavadoDW,3))
		
		listaEncabezados1=[
		"Material de la tuber??a del efluente",
		"Rugosidad absoluta de la tuber??a",
		"Longitud de la tuber??a del efluente",
		"Di??metro nominal de la tuber??a del efluente",
		"Di??metro interno de la tuber??a del efluente",
		"Caudal de filtraci??n",
		"Velocidad de flujo en la tuber??a del efluente",
		"Cabeza de velocidad",
		f"Viscosidad cinem??tica del agua a {temperatureValue} ??C ",
		"N??mero de Reynolds",
		"Factor de fricci??n (Asumido)",
		"Factor de fricci??n (Iteraci??n 4)",
		"P??rdida de carga en la tuber??a de lavado\n(Sin accesorios)"]
		
		listaUnidades1=[
			"",
			"mm",
			"m",
			unidadesDiametroNominal,
			"m",
			"(m^3)/s",
			"m/s",
			"m",
			"(m^2)/s",
			"",
			"",
			"",
			"m"]
		for i in range(0, len(listaEncabezados1)):
			listaTemp=list()
			listaTemp.append(listaEncabezados1[i])
			listaTemp.append(listaEntradaTemp1[i])
			listaTemp.append(listaUnidades1[i])	
			newDataTreeview(arbolPerdidaCargaTuberiaLavado_DW,listaTemp) 
		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaEnergiaEnTuberiaDelEfluente.xlsx",'Resultados',listaEncabezados1,50, listaEntradaTemp1, 15, listaUnidades1, 15,False,[], 50)
			
		#DatosPara3
	
		
		tuplasEntradas2=list()

		accesoriosLista = ["V??lvula de compuerta\ncompletamente abierta",
		"Codo 90?? radio corto (r/d 1)",
		"Codo 90?? radio mediano (r/d 3)",
		"Tee en sentido recto",
		"Tee en sentido lateral",
		"Uni??n",
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


		accesoriosListaEntrada= ["V??lvula de compuerta\ncompletamente abierta",
		"Tee en sentido recto",
		f"{listaEU[5]}",
		"Salida del tubo"]

		
		'''materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada y temperatureValue'''	
		sumaCoeficientesPerdidaMenor= 0
		
		for element in accesoriosListaEntrada:
			sumaCoeficientesPerdidaMenor=sumaCoeficientesPerdidaMenor+ CoeficientePerdidaMenorDic[(element,listaEU[1])]

		
		col1=list()
		col2=list()
		col3=list()
		col4=list()
		col5=list()
		col6=list()
		peridaCargaTuberiaLavadoAccesorios= sumaCoeficientesPerdidaMenor*cabezaVelocidad
		for elemento in accesoriosListaEntrada:
			listaEntradaTemp3=list()
			listaEntradaTemp3.append(elemento)
			col1.append(elemento)
			listaEntradaTemp3.append(listaEU[1])
			col2.append(listaEU[1])
			listaEntradaTemp3.append(1)
			col3.append(1)
			listaEntradaTemp3.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			col4.append(CoeficientePerdidaMenorDic[(elemento,listaEU[1])])
			listaEntradaTemp3.append(round(sumaCoeficientesPerdidaMenor,3))
			col5.append(round(sumaCoeficientesPerdidaMenor,3))
			listaEntradaTemp3.append(round(peridaCargaTuberiaLavadoAccesorios,3))
			col6.append(round(peridaCargaTuberiaLavadoAccesorios,3))
			newDataTreeview(arbolperdidaCargaTuberiaLavado_AC, listaEntradaTemp3)
		colsDatos=[col1,col2,col3,col4,col5,col6]
		pasarTreeViewExcel(colsDatos,arbolperdidaCargaTuberiaLavado_AC,'.\\ResultadosFiltro\\PerdidaCargaTuberiaLavadoAccesorios.xlsx')
		perdidaCargaTuberiaLavado_DW_HW2Window.mainloop()
				

	def perdidaCargaTuberiaLavado_DW_HW(TemperatureValue,listaE, d60,caudalLista,porosidadEntry,profundidadEntry):
		
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None
		

		perdidaCargaTuberiaLavado_DW_HWWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HWWindow.iconbitmap(bitmap=path)
		perdidaCargaTuberiaLavado_DW_HWWindow.geometry("800x600") 
		perdidaCargaTuberiaLavado_DW_HWWindow.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HWWindow.configure(background="#9DC4AA")

		frameperdidaCargaTuberiaLavado_DW_HW= LabelFrame(perdidaCargaTuberiaLavado_DW_HWWindow, text="Estimaci??n de la p??rdida de carga en la tuber??a de lavado",font=("Yu Gothic bold", 11))
		frameperdidaCargaTuberiaLavado_DW_HW.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista, labelExtra):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tuber??a de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
				elif elemento==codoRadio:
					codoRadio.set("Codo 90?? radio")
				elif elemento==tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)
			labelExtra.config(text="Seleccione el diametro nominal de la tuber??a de lavado []:")




		inicialLabel=Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Datos adicionales para c??lculos: ",font=("Yu Gothic bold",15))


		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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
			global indicador
			diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])
			if materialTuberiaLavado.get() == "Acero al carbono API 5L SCH-40" or materialTuberiaLavado.get()== "Acero al carbono API 5L SCH-80" or materialTuberiaLavado.get() == "Policluro de vinilo (PVC) RDE 26" or materialTuberiaLavado.get()=="Policluro de vinilo (PVC) RDE 21":
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [Pulgadas]:")
		
				indicador="Pulgadas"
			else:
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [mm]:")
				indicador="mm"
		
		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tuber??a de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el material de la tuber??a de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="40", state="readonly")
		diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el diametro nominal de la tuber??a de lavado []:",font=("Yu Gothic bold",10))
		


		
		codoRadio = StringVar()
		codoRadio.set("Codo 90?? radio")
		listaValoresTemp3=['Codo 90?? radio corto (r/d 1)', 'Codo 90?? radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, codoRadio, *listaValoresTemp3)
		

		
		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, tipoEntrada, *listaValoresTemp3)
		

	
		
		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Longitud de la tuber??a de lavado [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el factor de fricci??n [0.0001 - 0.1]:", font =("Yu Gothic",9))


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

		botonCalcular = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Calcular la estimaci??n de carga en la tuber??a de lavado.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTuberiaLavado_DW_HW2(listaEntradas,TemperatureValue,listaE, d60,caudalLista,indicador,porosidad,profundidadLechoFijo))
		botonNewEntry = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas,diametroNominalTuberiaLavadoLabel))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		# materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		# diametroNominalTuberiaLavado.set("10")
		# longitudTuberiaLavado.insert(0,"20")
		# factorFriccion.insert(0,"0.0200")
		# codoRadio.set('Codo 90?? radio mediano (r/d 3)')
		# tipoEntrada.set('Entrada con boca acampanada')
		




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
		path=resource_path('icons\\agua.ico')
		perdidaCargaTuberiaLavado_DW_HWWindow.iconbitmap(bitmap=path)
		perdidaCargaTuberiaLavado_DW_HWWindow.geometry("800x600") 
		perdidaCargaTuberiaLavado_DW_HWWindow.resizable(0,0)	
		perdidaCargaTuberiaLavado_DW_HWWindow.configure(background="#9DC4AA")

		frameperdidaCargaTuberiaLavado_DW_HW= LabelFrame(perdidaCargaTuberiaLavado_DW_HWWindow, text=f"Estimaci??n de la p??rdida de carga en la tuber??a de lavado a {tasa.lower()}",font=("Yu Gothic bold", 11))
		frameperdidaCargaTuberiaLavado_DW_HW.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista, extraLabel):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tuber??a de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
				elif elemento == tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)
			extraLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado []:")



		inicialLabel=Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Datos adicionales para c??lculos: ",font=("Yu Gothic bold",15))




		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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
			global indicador
			diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])
			if materialTuberiaLavado.get() == "Acero al carbono API 5L SCH-40" or materialTuberiaLavado.get()== "Acero al carbono API 5L SCH-80" or materialTuberiaLavado.get() == "Policluro de vinilo (PVC) RDE 26" or materialTuberiaLavado.get()=="Policluro de vinilo (PVC) RDE 21":
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [Pulgadas]:")
				indicador="Pulgadas"
			else:
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [mm]:")
				indicador="mm"


		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tuber??a de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el material de la tuber??a de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTuberiaLavado_DW_HW, width="40", state="readonly")
		diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el diametro nominal de la tuber??a de lavado []:",font=("Yu Gothic bold",10))


		
		codoRadio = StringVar()
		codoRadio.set("Codo 90?? radio")
		listaValoresTemp3=['Codo 90?? radio corto (r/d 1)', 'Codo 90?? radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, codoRadio, *listaValoresTemp3)
		

		
		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTuberiaLavado_DW_HW, tipoEntrada, *listaValoresTemp3)
		

	
		
		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Longitud de la tuber??a del efluente [1.5m - 2.5m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTuberiaLavado_DW_HW, text="Seleccione el factor de fricci??n [0.0001 - 0.1]:", font =("Yu Gothic",9))


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

		#Botones.
		
		botonCalcular = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Calcular la estimaci??n de carga en la tuber??a de lavado.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTuberiaLavado_DW_HW2_2(listaEntradas,TemperatureValue,listaE, d60,caudalLista,tasa, indicador))
		botonNewEntry = HoverButton(frameperdidaCargaTuberiaLavado_DW_HW, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas,diametroNominalTuberiaLavadoLabel))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		# materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		# diametroNominalTuberiaLavado.set("10")
		# longitudTuberiaLavado.insert(0,"1.5")
		# factorFriccion.insert(0,"0.0200")
	
		# tipoEntrada.set('Entrada con boca acampanada')
		
		#NOBorrar
		codoRadio.set('Codo 90?? radio mediano (r/d 3)')



		perdidaCargaTuberiaLavado_DW_HWWindow.mainloop()


	def perdidaCargaTotalLavado2(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1,porosidad,profundidad,densidadRelativa):
		
		i=0
		listaEU = list()
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None

					elif elemento.get() == "Codo 90?? radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90?? radio")
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
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None


	
		perdidaCargaTotalLavadoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaTotalLavadoWindow.iconbitmap(bitmap=path)
		perdidaCargaTotalLavadoWindow.geometry("650x400") 
		perdidaCargaTotalLavadoWindow.resizable(0,0)	
		perdidaCargaTotalLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaTotalLavadoFrame=LabelFrame(perdidaCargaTotalLavadoWindow, text="P??rdida de carga total durante el lavado", font=("Yu Gothic bold", 11))
		perdidaCargaTotalLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaTotalLavado_frame = Frame(perdidaCargaTotalLavadoFrame)
		arbolperdidaCargaTotalLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTotalLavado= ttk.Treeview(arbolperdidaCargaTotalLavado_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTotalLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolperdidaCargaTotalLavado.xview)
		# sedScrollY.configure(command=arbolperdidaCargaTotalLavado.yview)
		#Define columnas.
		arbolperdidaCargaTotalLavado["columns"]= (
		"Raz??n","hi","P??rdida de carga","Unidades"
		
		)

		#Headings
		arbolperdidaCargaTotalLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTotalLavado["columns"]:
			arbolperdidaCargaTotalLavado.heading(col, text=col,anchor=CENTER)	

		listaLargoFila=[0,300,50,200,100]
		for i in range(1,len(arbolperdidaCargaTotalLavado["columns"])+1):
			arbolperdidaCargaTotalLavado.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidaCargaTotalLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTotalLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaTotalLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaTotalLavado=list()

		listaValuePerdidaCargaTuberiaLavado = ValuePerdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista,porosidad,profundidad)
		
		perdidaCargaLechoExpandido = valuePerdidaCargaLechoExpandido(porosidad,profundidad,densidadRelativa)[3]
		perdidaCargaLechoGrava = valuePerdidacargaLechoGravaLavado(temperatureValue,d60,porosidad,profundidad)[2]
		perdidaCargaSistemaDrenaje = valuePerdidaCargaSistemaDrenajeLavado(temperatureValue,d60, caudal,listaEntradaDrenaje,porosidad,profundidad)[3]
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


		listaDebidoA= [ 'P??rdida de carga a trav??s del lecho expandido',					
		'P??rdida de carga a trav??s del lecho de grava',					
		'P??rdidad de carga a trav??s del sistema de drenaje',					
		'P??rdida de carga en la tuber??a de lavado\n(Darcy - Weisbach)',	
		'P??rdida de carga en la tuber??a de lavado\n(Hazen - Williams)',				
		'P??rdida de carga  por accesorios en la tuber??a de\nlavado',					
		'P??rdidad de carga total durante el lavado con\nDarcy - Weisbach',
		'P??rdidad de carga total durante el lavado con\nHazen - Williams']
		j=1
		listaUnidades=[
			"m",
			"m",
			"m",
			"m",
			"m",
			"m",
			"m",
			"m",

		]
		for i in range(0,len(perdidaTotalFinal)):
			listaperdidaCargaTotalLavado=list()
			listaperdidaCargaTotalLavado.append(listaDebidoA[i])
			listaperdidaCargaTotalLavado.append(f"h{j}")
			listaperdidaCargaTotalLavado.append(round(perdidaTotalFinal[i],3))
			listaperdidaCargaTotalLavado.append(listaUnidades[i])
			newDataTreeview(arbolperdidaCargaTotalLavado,listaperdidaCargaTotalLavado)
			if i==3 and j==4:
				pass
			elif j==5 or j=="b":
				j="b"
			else:
				j=j+1
		perdidaExcel=list()
		for elemento in perdidaTotalFinal:
			perdidaExcel.append(round(elemento,3))

		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaCargaTotalDuranteLavado.xlsx",'Resultados',listaDebidoA,50, perdidaExcel, 15, listaUnidades, 15,False,[], 50)

		perdidaCargaTotalLavadoWindow.mainloop()

	def perdidaCargaTotalLavado2_2(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1,tasa):
		
		
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None

					elif elemento.get() == "Codo 90?? radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90?? radio")
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
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a del efluente debe estar entre 1.5 y 2.5 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None
		perdidaCargaTotalLavadoWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaTotalLavadoWindow.iconbitmap(bitmap=path)
		perdidaCargaTotalLavadoWindow.geometry("650x400") 
		perdidaCargaTotalLavadoWindow.resizable(0,0)	
		perdidaCargaTotalLavadoWindow.configure(background="#9DC4AA")

		perdidaCargaTotalLavadoFrame=LabelFrame(perdidaCargaTotalLavadoWindow, text=f"P??rdida de energ??a total a {tasa.lower()} de filtraci??n con lecho limpio", font=("Yu Gothic bold", 11))
		perdidaCargaTotalLavadoFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolperdidaCargaTotalLavado_frame = Frame(perdidaCargaTotalLavadoFrame)
		arbolperdidaCargaTotalLavado_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolperdidaCargaTotalLavado_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolperdidaCargaTotalLavado= ttk.Treeview(arbolperdidaCargaTotalLavado_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolperdidaCargaTotalLavado.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolperdidaCargaTotalLavado.xview)
		# sedScrollY.configure(command=arbolperdidaCargaTotalLavado.yview)
		#Define columnas.
		arbolperdidaCargaTotalLavado["columns"]= (
		"Raz??n","hi","P??rdida de carga", "Unidades"
		)

		#Headings
		arbolperdidaCargaTotalLavado.heading("#0",text="ID", anchor=CENTER)

		for col in arbolperdidaCargaTotalLavado["columns"]:
			arbolperdidaCargaTotalLavado.heading(col, text=col,anchor=CENTER)	

		listaLargoFila=[0,300,50,200,100]
		for i in range(1,len(arbolperdidaCargaTotalLavado["columns"])+1):
			arbolperdidaCargaTotalLavado.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolperdidaCargaTotalLavado.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolperdidaCargaTotalLavado.tag_configure("evenrow", background= "#1FCCDB")
		arbolperdidaCargaTotalLavado.tag_configure("oddrow", background= "#9DC4AA")    

		listaperdidaCargaTotalLavado=list()

		
		

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
		'P??rdida de energ??a a trav??s del lecho de grava',					
		'P??rdidad de energ??a a trav??s del sistema de drenaje',					
		'P??rdida de energ??a en la tuber??a del efluente',		
		'P??rdida de energ??a  por accesorios en la tuber??a del\n efluente',					
		f'P??rdidad de energ??a total a {tasa.lower()} de filtraci??n']
		
		listaUnidades=[
		"m",
		"m",
		"m",
		"m",
		"m",
		]

		
		listaSub=["h{}".format(getSub("g")), "h{}".format(getSub("d")),"h{}".format(getSub("tef")),"h{}".format(getSub("acc")),"h{}".format(getSub("f"))]
		
		for i in range(0,len(perdidaTotalLista)):
			listaperdidaCargaTotalLavado=list()
			listaperdidaCargaTotalLavado.append(listaDebidoA[i])
			listaperdidaCargaTotalLavado.append(listaSub[i])
			listaperdidaCargaTotalLavado.append(round(perdidaTotalLista[i],3))
			listaperdidaCargaTotalLavado.append(listaUnidades[i])
			newDataTreeview(arbolperdidaCargaTotalLavado,listaperdidaCargaTotalLavado)
		perdidaTotalListaExcel=list()
		for elemento in perdidaTotalLista:
			perdidaTotalListaExcel.append(round(elemento, 3))

		PasarExcelDatos(".\\ResultadosFiltro\\PerdidaDeEnergiaTotalDuranteFiltradoConLechoLimpio.xlsx",'Resultados',listaDebidoA,50, perdidaTotalListaExcel, 15, listaUnidades, 15,False,[], 50)
		perdidaCargaTotalLavadoWindow.mainloop()


	def perdidaCargaTotalLavadoMain(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,porosidadEntry,profundidadEntry,densidadEntry):
		
		
		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None
		
		if densidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la densidad relativa de arena")
			return None
		try:
			densidadRelativaArena= float(densidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la densidad relativa de arena debe ser un n??mero")
			return None

		if densidadRelativaArena <2.5 or densidadRelativaArena >2.7:
			messagebox.showwarning(title="Error", message="El valor de la densidad relativa de arena debe estar entre 2.5 y 2.7")
			return None


		
		
		
		
		
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		
		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None
		
		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None

		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
	
		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None

		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
	
	
	
		perdidaCargaTotalLavadoMainWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaTotalLavadoMainWindow.iconbitmap(bitmap=path)
		perdidaCargaTotalLavadoMainWindow.geometry("800x600") 
		perdidaCargaTotalLavadoMainWindow.resizable(0,0)	
		perdidaCargaTotalLavadoMainWindow.configure(background="#9DC4AA")

		frameperdidaCargaTotalLavadoMain= LabelFrame(perdidaCargaTotalLavadoMainWindow, text="Datos adicionales para el c??lculo de la p??rdida total durante el lavado.",font=("Yu Gothic bold", 11))
		frameperdidaCargaTotalLavadoMain.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista, labelExtra):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tuber??a de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
				elif elemento==codoRadio:
					codoRadio.set("Codo 90?? radio")
				elif elemento==tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)
			labelExtra.config(text="Seleccione el diametro nominal de la tuber??a de lavado []:")



		inicialLabel=Label(frameperdidaCargaTotalLavadoMain, text="Datos adicionales para c??lculos: ",font=("Yu Gothic bold",15))


		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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
			diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])
			if materialTuberiaLavado.get() == "Acero al carbono API 5L SCH-40" or materialTuberiaLavado.get()== "Acero al carbono API 5L SCH-80" or materialTuberiaLavado.get() == "Policluro de vinilo (PVC) RDE 26" or materialTuberiaLavado.get()=="Policluro de vinilo (PVC) RDE 21":
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [Pulgadas]:")
			else:
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [mm]:")
				




		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tuber??a de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el material de la tuber??a de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="40", state="readonly")
		diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el diametro nominal de la tuber??a de lavado []:",font=("Yu Gothic bold",10))


		

	
		codoRadio = StringVar()
		codoRadio.set("Codo 90?? radio")
		listaValoresTemp3=['Codo 90?? radio corto (r/d 1)', 'Codo 90?? radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTotalLavadoMain, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTotalLavadoMain, tipoEntrada, *listaValoresTemp3)


	

		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTotalLavadoMain, text="Longitud de la tuber??a de lavado [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el factor de fricci??n [0.0001 - 0.1]:", font =("Yu Gothic",9))


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
		botonCalcular = HoverButton(frameperdidaCargaTotalLavadoMain, text="Calcular la p??rdida de carga total durante el lavado", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTotalLavado2(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE,porosidad,profundidadLechoFijo,densidadRelativaArena))
		botonNewEntry = HoverButton(frameperdidaCargaTotalLavadoMain, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas,diametroNominalTuberiaLavadoLabel))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		# materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		# diametroNominalTuberiaLavado.set("10")
		# longitudTuberiaLavado.insert(0,"20")
		# factorFriccion.insert(0,"0.0200")
		# codoRadio.set('Codo 90?? radio mediano (r/d 3)')
		# tipoEntrada.set('Entrada con boca acampanada')





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
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None
		else:
			diametroOrificios=float(listaEntradaDrenaje[0].get()[0])/float(listaEntradaDrenaje[0].get()[2])

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())


		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())


		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()
	
		perdidaCargaTotalLavadoMainWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		perdidaCargaTotalLavadoMainWindow.iconbitmap(bitmap=path)
		perdidaCargaTotalLavadoMainWindow.geometry("800x600") 
		perdidaCargaTotalLavadoMainWindow.resizable(0,0)	
		perdidaCargaTotalLavadoMainWindow.configure(background="#9DC4AA")

		frameperdidaCargaTotalLavadoMain= LabelFrame(perdidaCargaTotalLavadoMainWindow, text= f"Datos adicionales para el c??lculo de la p??rdida total a {tasa.lower()} de filtraci??n con lecho limpio",font=("Yu Gothic bold", 11))
		frameperdidaCargaTotalLavadoMain.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista,extraLab):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tuber??a de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
				elif elemento==tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				elif elemento == codoRadio:
					pass
				else:
					elemento.delete(0, END)
			extraLab.config(text="Seleccione el diametro nominal de la tuber??a de lavado []:")



		inicialLabel=Label(frameperdidaCargaTotalLavadoMain, text="Datos adicionales para c??lculos: ",font=("Yu Gothic bold",15))




		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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
			diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])
			if materialTuberiaLavado.get() == "Acero al carbono API 5L SCH-40" or materialTuberiaLavado.get()== "Acero al carbono API 5L SCH-80" or materialTuberiaLavado.get() == "Policluro de vinilo (PVC) RDE 26" or materialTuberiaLavado.get()=="Policluro de vinilo (PVC) RDE 21":
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [Pulgadas]:")
				indicador="Pulgadas"
			else:
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [mm]:")
				indicador="mm"

		materialTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tuber??a de lavado")

		materialTuberiaLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el material de la tuber??a de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameperdidaCargaTotalLavadoMain, width="40", state="readonly")
		diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el diametro nominal de la tuber??a de lavado []:",font=("Yu Gothic bold",10))

		
		codoRadio = StringVar()
		codoRadio.set("Codo 90?? radio")
		listaValoresTemp3=['Codo 90?? radio corto (r/d 1)', 'Codo 90?? radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameperdidaCargaTotalLavadoMain, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameperdidaCargaTotalLavadoMain, tipoEntrada, *listaValoresTemp3)


	

		longitudTuberiaLavadoLabel = Label(frameperdidaCargaTotalLavadoMain, text="Longitud de la tuber??a del efluente [1.5m - 2.5m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameperdidaCargaTotalLavadoMain, text="Seleccione el factor de fricci??n [0.0001 - 0.1]:", font =("Yu Gothic",9))


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
		botonCalcular = HoverButton(frameperdidaCargaTotalLavadoMain, text="Calcular la p??rdida de carga total durante el lavado", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: perdidaCargaTotalLavado2_2(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE,tasa))
		botonNewEntry = HoverButton(frameperdidaCargaTotalLavadoMain, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas,diametroNominalTuberiaLavadoLabel))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		# materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		# diametroNominalTuberiaLavado.set("10")
		# longitudTuberiaLavado.insert(0,"1.50")
		# factorFriccion.insert(0,"0.0200")	
		# tipoEntrada.set('Entrada con boca acampanada')

		#NOBorrar
		codoRadio.set('Codo 90?? radio mediano (r/d 3)')




		perdidaCargaTotalLavadoMainWindow.mainloop()


	def verificacionVelocidadesDise??oTuberiaMain(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,porosidadEntry,profundidadEntry):
		

		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None
		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None

		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None
	

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		

		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
	

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
	

		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
	

	
		

		verificacionVelocidadesDise??oTuberiaMainWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		verificacionVelocidadesDise??oTuberiaMainWindow.iconbitmap(bitmap=path)
		verificacionVelocidadesDise??oTuberiaMainWindow.geometry("800x600") 
		verificacionVelocidadesDise??oTuberiaMainWindow.resizable(0,0)	
		verificacionVelocidadesDise??oTuberiaMainWindow.configure(background="#9DC4AA")

																												

		frameverificacionVelocidadesDise??oTuberiaMain= LabelFrame(verificacionVelocidadesDise??oTuberiaMainWindow, text="Datos adicionales para el c??lculo de las velocidades de dise??o en las tuber??as del filtro durante el lavado ",font=("Yu Gothic bold", 11))
		frameverificacionVelocidadesDise??oTuberiaMain.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista,labelExtra):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tuber??a de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
				elif elemento == codoRadio:
					codoRadio.set("Codo 90?? radio")
				elif elemento == tipoEntrada:
					tipoEntrada.set("Tipo de entrada")
				else:
					elemento.delete(0, END)
			labelExtra.config(text="Seleccione el diametro nominal de la tuber??a de lavado []:")




		inicialLabel=Label(frameverificacionVelocidadesDise??oTuberiaMain, text="Datos adicionales para c??lculos: ",font=("Yu Gothic bold",15))



		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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
			diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])
			if materialTuberiaLavado.get() == "Acero al carbono API 5L SCH-40" or materialTuberiaLavado.get()== "Acero al carbono API 5L SCH-80" or materialTuberiaLavado.get() == "Policluro de vinilo (PVC) RDE 26" or materialTuberiaLavado.get()=="Policluro de vinilo (PVC) RDE 21":
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [Pulgadas]:")
				indicador="Pulgadas"
			else:
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [mm]:")
				indicador="mm"
		materialTuberiaLavado = ttk.Combobox(frameverificacionVelocidadesDise??oTuberiaMain, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tuber??a de lavado")

		materialTuberiaLabel= Label(frameverificacionVelocidadesDise??oTuberiaMain, text="Seleccione el material de la tuber??a de lavado:",font=("Yu Gothic bold",10))


		diametroNominalTuberiaLavado = ttk.Combobox(frameverificacionVelocidadesDise??oTuberiaMain, width="40", state="readonly")
		diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
		diametroNominalTuberiaLavadoLabel= Label(frameverificacionVelocidadesDise??oTuberiaMain, text="Seleccione el diametro nominal de la tuber??a de lavado []:",font=("Yu Gothic bold",10))

	
		codoRadio = StringVar()
		codoRadio.set("Codo 90?? radio")
		listaValoresTemp3=['Codo 90?? radio corto (r/d 1)', 'Codo 90?? radio mediano (r/d 3)']
		codoRadioName = OptionMenu(frameverificacionVelocidadesDise??oTuberiaMain, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(frameverificacionVelocidadesDise??oTuberiaMain, tipoEntrada, *listaValoresTemp3)




		longitudTuberiaLavadoLabel = Label(frameverificacionVelocidadesDise??oTuberiaMain, text="Longitud de la tuber??a de lavado [5m - 50m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(frameverificacionVelocidadesDise??oTuberiaMain, text="Seleccione el factor de fricci??n [0.0001 - 0.1]:", font =("Yu Gothic",9))

		longitudTuberiaLavado = Entry(frameverificacionVelocidadesDise??oTuberiaMain)
		factorFriccion = Entry(frameverificacionVelocidadesDise??oTuberiaMain)




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
		botonCalcular = HoverButton(frameverificacionVelocidadesDise??oTuberiaMain, text="Calcular las velocidades de dise??o en las tuber??as del filtro", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: verificacionVelocidadesDise??oTuberias(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE,porosidad,profundidadLechoFijo))
		botonNewEntry = HoverButton(frameverificacionVelocidadesDise??oTuberiaMain, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=2, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas,diametroNominalTuberiaLavadoLabel))
		botones=[botonCalcular,botonNewEntry]
		alturaBotones=450
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+50

		#Borrar

		# materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		# diametroNominalTuberiaLavado.set("10")
		# longitudTuberiaLavado.insert(0,"20")
		# factorFriccion.insert(0,"0.0200")

		#NOBORRAR.
		codoRadio.set('Codo 90?? radio mediano (r/d 3)')
		tipoEntrada.set('Entrada con boca acampanada')





		verificacionVelocidadesDise??oTuberiaMainWindow.mainloop()







	def verificacionVelocidadesDise??oTuberias(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1,porosidad,profundidad):
		
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None
					else:  
						if i==0 or i==4 or i==5:
							listaEU.append(elemento.get())
						else:
							listaEU.append(float(elemento.get()))
					
						i=i+1
				else:
					
					if i==2 and (float(elemento.get())>50.0 or float(elemento.get())<5.0):
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a de lavado debe estar entre 5 y 50 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None



		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()
		

		verificacionVelocidadesDise??oTuberiasWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		verificacionVelocidadesDise??oTuberiasWindow.iconbitmap(bitmap=path)
		verificacionVelocidadesDise??oTuberiasWindow.geometry("970x200") 
		verificacionVelocidadesDise??oTuberiasWindow.resizable(0,0)	
		verificacionVelocidadesDise??oTuberiasWindow.configure(background="#9DC4AA")

		verificacionVelocidadesDise??oTuberiasFrame=LabelFrame(verificacionVelocidadesDise??oTuberiasWindow, text="P??rdida de carga total durante el lavado", font=("Yu Gothic bold", 11))
		verificacionVelocidadesDise??oTuberiasFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolverificacionVelocidadesDise??oTuberias_frame = Frame(verificacionVelocidadesDise??oTuberiasFrame)
		arbolverificacionVelocidadesDise??oTuberias_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolverificacionVelocidadesDise??oTuberias_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolverificacionVelocidadesDise??oTuberias_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolverificacionVelocidadesDise??oTuberias= ttk.Treeview(arbolverificacionVelocidadesDise??oTuberias_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolverificacionVelocidadesDise??oTuberias.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolverificacionVelocidadesDise??oTuberias.xview)
		# sedScrollY.configure(command=arbolverificacionVelocidadesDise??oTuberias.yview)
		#Define columnas.
		arbolverificacionVelocidadesDise??oTuberias["columns"]= (
			"Velocidad de dise??o",
			"Rango de dise??o [m/s]",
			"Calculada [m/s]",
			"Adicional"
		
		)

		#Headings
		arbolverificacionVelocidadesDise??oTuberias.heading("#0",text="ID", anchor=CENTER)

		for col in arbolverificacionVelocidadesDise??oTuberias["columns"]:
			arbolverificacionVelocidadesDise??oTuberias.heading(col, text=col,anchor=CENTER)	

		listaLargoFila=[0,250,220,200,300]
		for i in range(1,len(arbolverificacionVelocidadesDise??oTuberias["columns"])+1):
			arbolverificacionVelocidadesDise??oTuberias.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolverificacionVelocidadesDise??oTuberias.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolverificacionVelocidadesDise??oTuberias.tag_configure("evenrow", background= "#1FCCDB")
		arbolverificacionVelocidadesDise??oTuberias.tag_configure("oddrow", background= "#9DC4AA")    
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







		listaverificacionVelocidadesDise??oTuberias=list()

		listaVelocidadDise??o=["Velocidad en la tuber??a de lavado","Velocidad en tuber??a de drenaje en lavado\n(m??ltiple)",
		"Velocidad en tuber??a de drenaje en lavado\n(laterales)"]
		listaRangoDise??o=["1.5 - 3.0","0.9 - 2.4", "0.9 - 2.4"]
		
		velocidadTuberiaLavado= ValuePerdidaCargaTuberiaLavado_DW_HW2(listaE,temperatureValue,listaE1, d60,caudalLista,porosidad,profundidad)[0][2]
		velocidadTuberiaDrenajeMultiple= ValueConsumoAguaLavado(listaE1, temperatureValue, d60, caudalLista,porosidad,profundidad)[5] *(1.0/AreaSeccionDic[seccionTransvMultiple])
		velocidadTuberiaDrenajeLaterales = ValueConsumoAguaLavado(listaE1, temperatureValue, d60, caudalLista,porosidad,profundidad)[5]/(( ValueDrenajeFiltro2(caudal,listaEntradaDrenaje)[2])*areaLateralesDic[diametroLaterales])

		listaCalculada=[velocidadTuberiaLavado, velocidadTuberiaDrenajeMultiple, velocidadTuberiaDrenajeLaterales]
		
	

		

		if velocidadTuberiaLavado<1.5:
			velocidadTuberiaLavadoInfo= "La velocidad en la tuber??a de lavado es baja, seleccione\notro di??metro."
		elif velocidadTuberiaLavado>3.0:
			velocidadTuberiaLavadoInfo= "La velocidad en la tuber??a de lavado es alta, seleccione\notro di??metro."
		else:
			velocidadTuberiaLavadoInfo= "La velocidad en la tuber??a de lavado es adecuada"

		if velocidadTuberiaDrenajeMultiple<0.9:
			velocidadTuberiaDrenajeMultipleInfo ="La velocidad en el m??ltiple es baja, seleccione\notra secci??n"
		elif velocidadTuberiaDrenajeMultiple>2.4:
			velocidadTuberiaDrenajeMultipleInfo = "La velocidad en el m??ltiple es alta, seleccione\notra secci??n"
		else: 
			velocidadTuberiaDrenajeMultipleInfo = "La velocidad en el m??ltiple es adecuada"

		if velocidadTuberiaDrenajeLaterales<0.9:
			velocidadTuberiaDrenajeLateralesInfo ="La velocidad en el lateral es baja, seleccione\notro di??metro o distanciamiento"
		elif velocidadTuberiaDrenajeLaterales>2.4:
			velocidadTuberiaDrenajeLateralesInfo = "La velocidad en el lateral es alta, seleccione\notro di??metro o distanciamiento"
		else:
			velocidadTuberiaDrenajeLateralesInfo = "La velocidad en el lateral es adecuada"
		listaAdicional=[velocidadTuberiaLavadoInfo,velocidadTuberiaDrenajeMultipleInfo, velocidadTuberiaDrenajeLateralesInfo]

		for i in range(0, len(listaVelocidadDise??o)):
			listaverificacionVelocidadesDise??oTuberias=list()
			listaverificacionVelocidadesDise??oTuberias.append(listaVelocidadDise??o[i])
			listaverificacionVelocidadesDise??oTuberias.append(listaRangoDise??o[i])
			listaverificacionVelocidadesDise??oTuberias.append(round(listaCalculada[i],3))
			listaverificacionVelocidadesDise??oTuberias.append(listaAdicional[i])
			newDataTreeview(arbolverificacionVelocidadesDise??oTuberias,listaverificacionVelocidadesDise??oTuberias)
		listaCalculadaExcel=list()
		for elemento in listaCalculada:
			listaCalculadaExcel.append(round(elemento,3))

		PasarExcelDatos(".\\ResultadosFiltro\\VerificacionVelocidadDisenoEnTuberiaFiltroDuranteLavado.xlsx",'Resultados',listaVelocidadDise??o,50, listaRangoDise??o, 15, listaCalculadaExcel, 15,True,listaAdicional, 50)
		verificacionVelocidadesDise??oTuberiasWindow.mainloop()

	

	
	
	
	def hidraulicaSistemaLavado(listaTamiz, listaAR, optnValue, listaCaudal):
		#Hidraulica

		try: 
			caudalMedio=float(listaCaudal[0].get())
			
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero.")
			return None

		if caudalMedio<0.01 or caudalMedio>0.2:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero entre 0.01 y 0.2")
			return None

		listaNTamizTemp=listaTamiz.copy()
		listaARetenidaTemp=listaAR.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de los n??meros de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de la arena retenida.")
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
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores est??ndar para n??mero de tamiz. Pulse el bot??n para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de n??mero de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
	

		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
				
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de n??mero de tamiz no coincide con la cantidad de datos de arena retendia.")
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
		path=resource_path('icons\\agua.ico')
		hidraulicaSistemaLavadoMainWindow.iconbitmap(bitmap=path)
		hidraulicaSistemaLavadoMainWindow.geometry("800x600") 
		hidraulicaSistemaLavadoMainWindow.resizable(0,0)	
		hidraulicaSistemaLavadoMainWindow.configure(background="#9DC4AA")

		hidraulicaSistemaLavadoMainFrame=LabelFrame(hidraulicaSistemaLavadoMainWindow, text="Datos adicionales para la hidr??ulica del sistema de lavado", font=("Yu Gothic bold", 11))
		hidraulicaSistemaLavadoMainFrame.pack(side=TOP, fill=BOTH,expand=True)

		
		
		diametroOrificios = StringVar()
		diametroOrificios.set("Diametro de los orificios")
		listaValoresTempDiametroOrificios=list()
		listaValoresTempDiametroOrificios.append("1/4")
		listaValoresTempDiametroOrificios.append("3/8")
		listaValoresTempDiametroOrificios.append("1/2")
		listaValoresTempDiametroOrificios.append("5/8")
		diametroOrificiosName = OptionMenu(hidraulicaSistemaLavadoMainFrame, diametroOrificios, *listaValoresTempDiametroOrificios)
		diametroOrificiosLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione el di??metro de los orificios [pulgadas]:", font=("Yu Gothic bold", 10))
		

		
		distanciaOrificios = StringVar()
		distanciaOrificios.set("Distancia entre los orificios")
		listaValoresTempDistanciaOrificios=list()
		listaValoresTempDistanciaOrificios.append("0.750")
		listaValoresTempDistanciaOrificios.append("0.100")
		listaValoresTempDistanciaOrificios.append("0.125")
		listaValoresTempDistanciaOrificios.append("0.150")
		distanciaOrificiosName = OptionMenu(hidraulicaSistemaLavadoMainFrame, distanciaOrificios, *listaValoresTempDistanciaOrificios)
		distanciaOrificiosLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione la distancia entre orificios [m]:", font=("Yu Gothic bold", 10))


		seccionTransversal = StringVar()
		seccionTransversal.set("Secci??n transversal")
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
		seccionTransversalLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione la secci??n transversal comercial del m??ltiple [pulgadas^2]:", font=("Yu Gothic bold", 9))


		distanciaLaterales = StringVar()
		distanciaLaterales.set("Distancia entre laterales")
		listaValoresTempDistanciaLaterales=list()
		listaValoresTempDistanciaLaterales.append("0.20")
		listaValoresTempDistanciaLaterales.append("0.25")
		listaValoresTempDistanciaLaterales.append("0.30")
		distanciaLateralesName = OptionMenu(hidraulicaSistemaLavadoMainFrame, distanciaLaterales, *listaValoresTempDistanciaLaterales)
		distanciaLateralesLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione la distancia entre laterales [m]:", font=("Yu Gothic bold", 10))
		

		
		diametroEntreLaterales = StringVar()
		diametroEntreLaterales.set("Di??metro de los laterales")
		listaValoresTempDiametroEntreLaterales=list()
		listaValoresTempDiametroEntreLaterales.append("1 1/2")
		listaValoresTempDiametroEntreLaterales.append("2")
		listaValoresTempDiametroEntreLaterales.append("2 1/2")
		listaValoresTempDiametroEntreLaterales.append("3")
		diametroEntreLateralesName = OptionMenu(hidraulicaSistemaLavadoMainFrame, diametroEntreLaterales, *listaValoresTempDiametroEntreLaterales)
		diametroEntreLateralesLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione el di??metro de los laterales [pulgadas]:", font=("Yu Gothic bold", 10))

		tiempoRetrolavado = StringVar()
		tiempoRetrolavado.set("Tiempo de retrolavado")
		listaValoresTemptiempoRetrolavado=list()
		listaValoresTemptiempoRetrolavado.append("10")
		listaValoresTemptiempoRetrolavado.append("11")
		listaValoresTemptiempoRetrolavado.append("12")
		listaValoresTemptiempoRetrolavado.append("13")
		listaValoresTemptiempoRetrolavado.append("14")
		tiempoRetrolavadoName = OptionMenu(hidraulicaSistemaLavadoMainFrame, tiempoRetrolavado, *listaValoresTemptiempoRetrolavado)
		tiempoRetrolavadoLabel= Label(hidraulicaSistemaLavadoMainWindow, text="Seleccione el tiempo de retrolavado [s]:", font=("Yu Gothic bold", 10))

		porosidadLechoFijoLabel = Label(hidraulicaSistemaLavadoMainFrame, text="Porosidad del lecho fijo [0.4 - 0.48]:", font =("Yu Gothic bold",10))
		porosidadLechoFijo = Entry(hidraulicaSistemaLavadoMainFrame)
		
		profundidadLechoFijoArenaLabel = Label(hidraulicaSistemaLavadoMainFrame, text="Profundidad del lecho fijo de arena [0.6m - 0.75m]:", font =("Yu Gothic bold",10))
		profundidadLechoFijoArena = Entry(hidraulicaSistemaLavadoMainFrame)
		
		densidadRelativaArenaLabel = Label(hidraulicaSistemaLavadoMainFrame, text="Densidad relativa de la arena [2.5 - 2.7]:", font =("Yu Gothic bold",10))
		densidadRelativaArena = Entry(hidraulicaSistemaLavadoMainFrame)

		
		listaEntradaDrenaje2=[diametroOrificiosName,distanciaOrificiosName,seccionTransversalName,distanciaLateralesName, diametroEntreLateralesName,tiempoRetrolavadoName, porosidadLechoFijo,profundidadLechoFijoArena,densidadRelativaArena]
		listaLabel= [diametroOrificiosLabel,distanciaOrificiosLabel, seccionTransversalLabel, distanciaLateralesLabel, diametroEntreLateralesLabel,tiempoRetrolavadoLabel,porosidadLechoFijoLabel,profundidadLechoFijoArenaLabel,densidadRelativaArenaLabel]
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]
		listaEntradaExtra=[tiempoRetrolavado]
		
		#Borrar

		# profundidadLechoFijoArena.insert(0,"0.7")
		# porosidadLechoFijo.insert(0,"0.47")
		# densidadRelativaArena.insert(0,"2.5")
		# diametroOrificios.set("1/2")
		# distanciaOrificios.set("0.150")
		# seccionTransversal.set("8 X 8")
		# distanciaLaterales.set("0.25")
		# diametroEntreLaterales.set("2 1/2")
		# tiempoRetrolavado.set("14")
		

		
	
		altIn= 30
		altIn2=30
		for ind in range(0,len(listaLabel)):
			if ind%2==0:
				# if ind==6:
				# 	listaLabel[ind].place(x=20,y=altIn)
				# 	listaEntradaDrenaje2[ind].place(x=270, y= altIn+20)
				# 	altIn=altIn+80
				# else: 
					listaLabel[ind].place(x=20,y=altIn)
					listaEntradaDrenaje2[ind].place(x=20, y= altIn+20)
					altIn=altIn+69
			else:

				listaLabel[ind].place(x=450,y=altIn2)
				listaEntradaDrenaje2[ind].place(x=450, y= altIn2+20)
				altIn2=altIn2+69
			
		#BotonesHidraulica
		#botonCalculoDrenaje = HoverButton(hidraulicaSistemaLavadoMainFrame, text="C??lculos para el drenaje del filtro", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: calculoDrenaje())

		botonVelocidadLavadoExpansionLechoFiltrante = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Velocidad de lavado\n y expansi??n del lecho filtrante", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: velocidadLavadoExpansionLechoFiltrante(valorTemperatura,d60,porosidadLechoFijo,profundidadLechoFijoArena))

		botonConsumoAguaLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Consumo de agua de\n lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: consumoAguaLavado(listaEntradaExtra,valorTemperatura,d60,listaCaudal,porosidadLechoFijo,profundidadLechoFijoArena))

		botonPerdidaCargaLechoExpandido = HoverButton(hidraulicaSistemaLavadoMainFrame, text="P??rdida de carga a trav??s\n del lecho expandido", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaLechoExpandido(porosidadLechoFijo,profundidadLechoFijoArena,densidadRelativaArena))
 
		botonPerdidacargaLechoGravaLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="P??rdida de carga a trav??s\n del lecho de grava durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidacargaLechoGravaLavado(valorTemperatura,d60,porosidadLechoFijo,profundidadLechoFijoArena) )

		botonPerdidaCargaSistemaDrenajeLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="P??rdida de carga a trav??s\n del sistema de drenaje durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaSistemaDrenajeLavado(valorTemperatura,d60, caudalMedio, listaEntradaDrenaje,porosidadLechoFijo,profundidadLechoFijoArena) )

		botonPerdidaCargaTuberiaLavado_DW = HoverButton(hidraulicaSistemaLavadoMainFrame, text="P??rdida de carga en la tuber??a\n de lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTuberiaLavado_DW_HW(valorTemperatura,listaEntradaExtra,d60,listaCaudal,porosidadLechoFijo,profundidadLechoFijoArena)) 

		botonPerdidaCargaTotalLavado = HoverButton(hidraulicaSistemaLavadoMainFrame, text="P??rdida de carga total durante\n el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTotalLavadoMain(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal,porosidadLechoFijo,profundidadLechoFijoArena,densidadRelativaArena))

		botonVerificacionVelocidadesDise??oTuberias = HoverButton(hidraulicaSistemaLavadoMainFrame, text="Verificaci??n de velocidad de dise??o\n en tuber??as de filtro durante el lavado", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: verificacionVelocidadesDise??oTuberiaMain(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal, porosidadLechoFijo,profundidadLechoFijoArena) )

	

				
		def newEntryFiltroHidraulica(lista,porosidad,profundidad,densidad): 
			
				lista2= [
							"Diametro de los orificios",
							"Distancia entre los orificios",
							"Secci??n transversal",
							"Distancia entre laterales",
							"Di??metro de los laterales",
							"Tiempo de retrolavado"]

				for i in range(0, len(lista)):		
					lista[i].set(lista2[i])
				porosidad.delete(0,END)
				profundidad.delete(0,END)
				densidad.delete(0,END)

		botonLimpiarEntradasHidraulica = HoverButton(hidraulicaSistemaLavadoMainFrame, text="L\ni\nm\np\ni\na\nr\n\ne\nn\nt\nr\na\nd\na\ns", activebackground="#9DC4AA", anchor=CENTER , width=3, height=15, bg= "#09C5CE", font =("Courier",8), command= lambda: newEntryFiltroHidraulica(listaEntradaDrenaje+listaEntradaExtra,porosidadLechoFijo,profundidadLechoFijoArena,densidadRelativaArena))

			

		listaBotones=[botonVelocidadLavadoExpansionLechoFiltrante ,botonConsumoAguaLavado ,
		botonPerdidaCargaLechoExpandido ,botonPerdidacargaLechoGravaLavado ,botonPerdidaCargaSistemaDrenajeLavado 
		,botonPerdidaCargaTuberiaLavado_DW,botonPerdidaCargaTotalLavado ,botonVerificacionVelocidadesDise??oTuberias]
		 
		counter= 0
		
		altIn=altIn-10
		altIn2= altIn

		botonLimpiarEntradasHidraulica.place(x=400, y=altIn-20)


		for elemento in listaBotones:
			if counter < 4:
				elemento.place(x=20,y=altIn)
				altIn=altIn+55
				counter=counter+1
			else: 
				elemento.place(x=500,y=altIn2)
				altIn2=altIn2+55
		#botonCalculoDrenaje.place(x=0, y=altIn)
			
	
		
		listaCU = valorCoeficienteDeUniformidad(listaTamiz,listaAR)
		d10= listaCU[0]
		CU=listaCU[1]
		d60=d10*CU

		##return [d10,CU]
		
		hidraulicaSistemaLavadoMainWindow.mainloop()

	def canaletasDeLavado2(tempValue,d60, listaCaudal, listaExtra, ValorNuevo,valorNuevo2,porosidad,profundidadLechoFijo):
		
		if ValorNuevo.get() == "Ancho":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el ancho de la canaleta")
			return None
		else:
			anchoCanaleta = float(ValorNuevo.get())
		
		if valorNuevo2.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta introducir el espaciamiento entre ejes de canaletas.")
			return None
		else:
			try:
				espaciamientoEntreEjesCanaletas = float(valorNuevo2.get())
			except:
				messagebox.showwarning(title="Error", message="El valor introducido en espaciamiento entre ejes de canaletas no es un n??mero.")
				return None
		
		if espaciamientoEntreEjesCanaletas<1.2 or espaciamientoEntreEjesCanaletas>2.0:
				messagebox.showwarning(title="Error", message="El valor introducido en espaciamiento entre ejes debe estar entre 1.2 y 2")
				return None



		canaletasDeLavado2Window = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		canaletasDeLavado2Window.iconbitmap(bitmap=path)
		canaletasDeLavado2Window.geometry("670x400") 
		canaletasDeLavado2Window.resizable(0,0)	
		canaletasDeLavado2Window.configure(background="#9DC4AA")

		canaletasDeLavado2Frame=LabelFrame(canaletasDeLavado2Window, text="C??lculos para las canaletas de lavado.", font=("Yu Gothic bold", 11))
		canaletasDeLavado2Frame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolcanaletasDeLavado2_frame = Frame(canaletasDeLavado2Frame)
		arbolcanaletasDeLavado2_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolcanaletasDeLavado2_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolcanaletasDeLavado2_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolcanaletasDeLavado2= ttk.Treeview(arbolcanaletasDeLavado2_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set)#,xscrollcommand=sedScrollX.set
		arbolcanaletasDeLavado2.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolcanaletasDeLavado2.xview)
		sedScrollY.configure(command=arbolcanaletasDeLavado2.yview)
		#Define columnas.
		arbolcanaletasDeLavado2["columns"]= (
		"Ver f??rmulas","Valores","Unidades","Adicional"

		)

		#Headings
		arbolcanaletasDeLavado2.heading("#0",text="ID", anchor=CENTER)

		for col in arbolcanaletasDeLavado2["columns"]:
			arbolcanaletasDeLavado2.heading(col, text=col,anchor=CENTER, command=lambda: proyectarImg('images\\PerdidaLechoLimpio_CanaletasLavado.png',1005,451) )	
		listaLargoFila=[0,250,100,100,200]
		
		for i in range(1,len(arbolcanaletasDeLavado2["columns"])+1):
			arbolcanaletasDeLavado2.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arbolcanaletasDeLavado2.column("#0",width=0, stretch=False)

		#Striped row tags
		arbolcanaletasDeLavado2.tag_configure("evenrow", background= "#1FCCDB")
		arbolcanaletasDeLavado2.tag_configure("oddrow", background= "#9DC4AA")    

		listacanaletasDeLavado2=list()
		
		

		listacanaletasDeLavado2.append(round(espaciamientoEntreEjesCanaletas,3))
		
		longitudFiltro= ValuepredimensionamientoFiltros(listaCaudal)[9]
		listacanaletasDeLavado2.append(round(longitudFiltro,3))

		numeroCanaletas= round(longitudFiltro/espaciamientoEntreEjesCanaletas,0)
		listacanaletasDeLavado2.append(numeroCanaletas)

		caudalLavado = ValueConsumoAguaLavado(listaExtra, tempValue, d60, listaCaudal,porosidad,profundidadLechoFijo)[5]
		listacanaletasDeLavado2.append(round(caudalLavado,3))

		caudalLavadoEcuadoCanaleta = caudalLavado/float(numeroCanaletas)
		listacanaletasDeLavado2.append(round(caudalLavadoEcuadoCanaleta,3))

		listacanaletasDeLavado2.append(anchoCanaleta)
		
		profundidadMaximaAguaCanaleta = (caudalLavadoEcuadoCanaleta/(anchoCanaleta*1.38))**(2/3)
		listacanaletasDeLavado2.append(round(profundidadMaximaAguaCanaleta,3))

		if profundidadMaximaAguaCanaleta/2 <0.05:
			bordeLibreCanaleta=0.05
		elif profundidadMaximaAguaCanaleta/2 > 0.1:
			bordeLibreCanaleta=0.1
		else:
			bordeLibreCanaleta= bordeLibreCanaleta*(0.5)

		listacanaletasDeLavado2.append(bordeLibreCanaleta)

		alturaTotalInternaCanaleta= round(profundidadMaximaAguaCanaleta+bordeLibreCanaleta,2)
		listacanaletasDeLavado2.append(alturaTotalInternaCanaleta)


		listacanaletasDeLavado2.append(profundidadLechoFijo)

		profundidadLechoExpandido = ValuevelocidadLavadoExpansionLechoFiltrante(tempValue, d60,porosidad,profundidadLechoFijo)[9]

		listacanaletasDeLavado2.append(round(profundidadLechoExpandido,3))

		alturaCanaletaMedioFiltrante = ((0.75*profundidadLechoFijo)+alturaTotalInternaCanaleta+(alturaTotalInternaCanaleta+profundidadLechoFijo))*(1/2)
		
		listacanaletasDeLavado2.append(round(alturaCanaletaMedioFiltrante,3))

		espaciamientoEjesCorregido= longitudFiltro/float(numeroCanaletas)
		
		listacanaletasDeLavado2.append(round(espaciamientoEjesCorregido,3))

		distanciaSeguridadLechoExpandidoYFondoCanaleta = alturaCanaletaMedioFiltrante -(profundidadLechoExpandido-profundidadLechoFijo)

		listacanaletasDeLavado2.append(round(distanciaSeguridadLechoExpandidoYFondoCanaleta,3))


		listaEncabezados= ['Espaciamiento entre ejes de canaletas\n(asumido)',
			'Longitud del filtro',
			'N??mero de canaletas',					
			'Caudal de lavado',				
			'Caudal de lavado ecuado por cada canaleta',
			"Ancho de la canaleta",
			'Profundidad m??xima del agua en la canaleta',							
			'Borde libre de la canaleta',	
			'Altura total interna de la canaleta',
			'Profundidad del lecho fijo',				
			'Profundidad del lecho expandido',					
			'Altura de la canaleta sobre el medio filtrante',
			'Espaciamiento entre ejes de canaletas\n(corregido)',					
			'Distancia de seguridad entre lecho expandido\ny fondo canaleta']

		listaUnidades=["m",
		"m",
		"",
		"(m^3)/s",
		"(m^3)/s",
		"m",
		"m",
		"m",
		"m",
		"m",
		"m",
		"m",
		"m",
		"m"
		]

		if alturaTotalInternaCanaleta>anchoCanaleta:
			alturaTotalInternaCanaletaInfo= "??Error, aumente ancho de\nla canaleta!"
		elif alturaTotalInternaCanaleta<(0.8*anchoCanaleta):
			alturaTotalInternaCanaletaInfo= "??Error, disminuya ancho de\nla canaleta!"
		else:
			alturaTotalInternaCanaletaInfo= "El valor de la altura total interna\nde la canaleta es adecuado "
		
		listaAdicional=[
		"",
		"",
		"",
		"",
		"",
		"",
		"",
		"",
		alturaTotalInternaCanaletaInfo,
		"",
		"",
		"",
		"",
		""
		]

		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listacanaletasDeLavado2[i])
			listaTemp.append(listaUnidades[i])
			listaTemp.append(listaAdicional[i])	
			newDataTreeview(arbolcanaletasDeLavado2,listaTemp)  

		PasarExcelDatos(".\\ResultadosFiltro\\CanaletasDeLavado.xlsx",'Resultados',listaEncabezados,50, listacanaletasDeLavado2, 15, listaUnidades, 15,True,listaAdicional, 50)

		canaletasDeLavado2Window.mainloop()

	def dimensionesYCotasFiltros(temperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,listaE1,tasa,profundidadLechoFijoArena):

		
		
		listaE
		listaEU=list()
		i=0
		for elemento in listaE:
			try:
				if i==0 or i==1 or i==4 or i==5 or i==6:
					if elemento.get() == "Material de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el material de la tuber??a de lavado")
						return None
					elif elemento.get() == "Di??metro nominal de la tuber??a de lavado":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro nominal de la tuber??a de lavado")
						return None

					elif elemento.get() == "Codo 90?? radio":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el valor del codo 90?? radio")
						return None
					
					
					elif elemento.get() == "Tipo de entrada":
						messagebox.showwarning(title="Error", message="Hace falta seleccionar el tipo de entrada del accesorio")
						return None
					
					elif elemento.get() == "Ancho":
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
						messagebox.showwarning(title="Error", message="El valor de la longitud de la tuber??a del efluente debe estar entre 1.5 y 2.5 metros.")
						return None

					elif i==3 and (float(elemento.get())>0.1 or float(elemento.get())<0.00001):
						messagebox.showwarning(title="Error", message="El valor del factor de fricci??n debe estar entre 0.00001 y 0.1")
						return None   
					
						


					
					elif i==7 and (float(elemento.get())>0.2 or float(elemento.get())<0.15):
						messagebox.showwarning(title="Error", message="El nivel del vertedero sobre el lecho fijo de arena debe estar entre 0.15 y 0.20")
						return None   

					elif i==8 and (float(elemento.get())>2.0 or float(elemento.get())<1.8):
						messagebox.showwarning(title="Error", message="El valor de la energ??a disponible de filtraci??n debe estar entre 1.8 y 2.0")
						return None 


					elif i==9 and (float(elemento.get())>0.50 or float(elemento.get())<0.40):
						messagebox.showwarning(title="Error", message="El valor del borde libre debe estar entre 0.40 y 0.50")
						return None 

					else:
						listaEU.append(float(elemento.get()))
					i=i+1
			except:
				messagebox.showwarning(title="Error", message="El valor ingresado no es un n??mero")
				return None
			
		



		dimensionesYCotasFiltrosWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		dimensionesYCotasFiltrosWindow.iconbitmap(bitmap=path)
		dimensionesYCotasFiltrosWindow.geometry("450x350") 
		dimensionesYCotasFiltrosWindow.resizable(0,0)	
		dimensionesYCotasFiltrosWindow.configure(background="#9DC4AA")

		dimensionesYCotasFiltrosFrame=LabelFrame(dimensionesYCotasFiltrosWindow, text="C??lculo de dimensiones y cotas en los filtros", font=("Yu Gothic bold", 11))
		dimensionesYCotasFiltrosFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arboldimensionesYCotasFiltros_frame = Frame(dimensionesYCotasFiltrosFrame)
		arboldimensionesYCotasFiltros_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arboldimensionesYCotasFiltros_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldimensionesYCotasFiltros_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldimensionesYCotasFiltros= ttk.Treeview(arboldimensionesYCotasFiltros_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set)#,xscrollcommand=sedScrollX.set
		arboldimensionesYCotasFiltros.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arboldimensionesYCotasFiltros.xview)
		sedScrollY.configure(command=arboldimensionesYCotasFiltros.yview)
		#Define columnas.
		arboldimensionesYCotasFiltros["columns"]= (
		"Ver f??rmulas","Valores","Unidades"

		
		)

		#Headings
		arboldimensionesYCotasFiltros.heading("#0",text="ID", anchor=CENTER)

		for col in arboldimensionesYCotasFiltros["columns"]:
			arboldimensionesYCotasFiltros.heading(col, text=col,anchor=CENTER, command= lambda: proyectarImg('images\\PerdidaLechoLimpio_DimensionesCotasFiltros.png',1004,267) ) 	

		listaLargoFila=[0,250,100,100]
		for i in range(1,len(arboldimensionesYCotasFiltros["columns"])+1):
			arboldimensionesYCotasFiltros.column(f"#{i}",width=listaLargoFila[i], stretch=False)		
		arboldimensionesYCotasFiltros.column("#0",width=0, stretch=False)

		#Striped row tags
		arboldimensionesYCotasFiltros.tag_configure("evenrow", background= "#1FCCDB")
		arboldimensionesYCotasFiltros.tag_configure("oddrow", background= "#9DC4AA")    

		#C??lculoP??rdidaTotal
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
		
		#Insersi??n datos. 
		profundidadLechoGrava = 0.450
		listadimensionesYCotasFiltros.append(round(profundidadLechoGrava,3))
		listadimensionesYCotasFiltros.append(round(profundidadLechoFijoArena,3))
		listadimensionesYCotasFiltros.append(listaE[7].get())
		listadimensionesYCotasFiltros.append(listaE[8].get())
		listadimensionesYCotasFiltros.append(round(perdidaCargaTotal,3))
		listadimensionesYCotasFiltros.append(listaE[9].get())
		nivelLaminaAguaLechoLimpio= profundidadLechoGrava+ profundidadLechoFijoArena+listaEU[7]+perdidaCargaTotal
		listadimensionesYCotasFiltros.append(round(nivelLaminaAguaLechoLimpio,3))

		nivelLaminaAguaPerdidaEnergiaMaxima= profundidadLechoGrava+ profundidadLechoFijoArena+listaEU[7]+listaEU[8]
		listadimensionesYCotasFiltros.append(round(nivelLaminaAguaPerdidaEnergiaMaxima,3))

		alturaInternaTotal = nivelLaminaAguaPerdidaEnergiaMaxima+ listaEU[9]
		listadimensionesYCotasFiltros.append(round(alturaInternaTotal,3))
		 
		
		listaEncabezados=['Profundidad del lecho de grava',		
		'Profundidad del lecho fijo de arena',	
		'Altura del vertedero de control sobre el\nlecho fijo',
		'Energ??a disponible de filtraci??n',
		'P??rdida de energ??a total a tasa media de\nfiltraci??n con lecho limpio',
		'Borde libre',
		'Nivel de la l??mina de agua con lecho limpio',
		'Nivel de la l??mina de agua con p??rdida de\nenerg??a m??xima',
		'Altura interna total del filtro']

		listaUnidades=[
		"m",
		"m",
		"m",	
		"m",
		"m",
		"m",
		"m",
		"m",
		"m",
		]
		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listadimensionesYCotasFiltros[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arboldimensionesYCotasFiltros,listaTemp)  

		PasarExcelDatos(".\\ResultadosFiltro\\CotasEnLosFiltros.xlsx",'Resultados',listaEncabezados,50, listadimensionesYCotasFiltros, 15, listaUnidades, 15,False,[], 50)
		
		dimensionesYCotasFiltrosWindow.mainloop()
	


		

	def canaletasDeLavadoYDimensionesFiltros(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaE,caudalLista,tasaE,porosidadEntry,profundidadEntry):
		
		if porosidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la porosidad del lecho fijo.")
			return None
		if profundidadEntry.get() == "":
			messagebox.showwarning(title="Error", message="Hace falta escribir el valor de la profundidad del lecho fijo.")
			return None
		try:
			porosidad= float(porosidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe ser un n??mero.")
			return None

		try:
			profundidadLechoFijo= float(profundidadEntry.get())
		except:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe ser un n??mero.")
			return None

		if porosidad<0.4 or porosidad>0.48:
			messagebox.showwarning(title="Error", message="El valor de la porosidad del lecho fijo debe estar entre 0.4 y 0.48")
			return None

		if profundidadLechoFijo <0.6 or profundidadLechoFijo >0.75:
			messagebox.showwarning(title="Error", message="El valor de la profundidad del lecho fijo debe estar entre 0.6 y 0.75")
			return None

		if tasaE.get() == "Tasa":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la tasa.")
			return None
		else:
			tasa = tasaE.get()

		if listaEntradaDrenaje[0].get() == "Diametro de los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los orificios.")
			return None

		if listaEntradaDrenaje[1].get() == "Distancia entre los orificios":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre los orificios")
			return None
		else:
			distanciaOrificios=float(listaEntradaDrenaje[1].get())


		if listaEntradaDrenaje[2].get() == "Secci??n transversal":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la secci??n transversal")
			return None
		else:
			seccionTransvMultiple=listaEntradaDrenaje[2].get()

		if listaEntradaDrenaje[3].get() == "Distancia entre laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar la distancia entre laterales")
			return None
		else:
			distanciaLaterales=float(listaEntradaDrenaje[3].get())


		if listaEntradaDrenaje[4].get() == "Di??metro de los laterales":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el di??metro de los laterales")
			return None
		else:
			diametroLaterales=listaEntradaDrenaje[4].get()

		if listaE[0].get() == "Tiempo de retrolavado":
			messagebox.showwarning(title="Error", message="Hace falta seleccionar el tiempo de retrolavado")
			return None
		else:
			tiempoRetrolavado = float(listaE[0].get())

		

		canaletasDeLavadoYDimensionesFiltrosWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		canaletasDeLavadoYDimensionesFiltrosWindow.iconbitmap(bitmap=path)
		canaletasDeLavadoYDimensionesFiltrosWindow.geometry("800x650") 
		canaletasDeLavadoYDimensionesFiltrosWindow.resizable(0,0)	
		canaletasDeLavadoYDimensionesFiltrosWindow.configure(background="#9DC4AA")

		framecanaletasDeLavadoYDimensionesFiltros= LabelFrame(canaletasDeLavadoYDimensionesFiltrosWindow, text= f"Datos adicionales para el c??lculo de la p??rdida total a {tasa.lower()} de filtraci??n con lecho limpio",font=("Yu Gothic bold", 11))
		framecanaletasDeLavadoYDimensionesFiltros.pack(side=TOP,fill=BOTH,expand=True)

		def newEntryFiltroP(lista,extraLb):
			for elemento in lista:
				if elemento == materialTuberiaLavado:
					materialTuberiaLavado.set("Material de la tuber??a de lavado")
				elif elemento ==diametroNominalTuberiaLavado:
					diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
				elif elemento==tipoEntrada:
					elemento.set("Tipo de entrada")
				elif elemento == AnchoCanaleta:
					elemento.set("Ancho")
				elif elemento == codoRadio:
					pass
				else:
					elemento.delete(0, END)
			extraLb.config(text="Seleccione el diametro nominal de la tuber??a de lavado []:")




		inicialLabel=Label(framecanaletasDeLavadoYDimensionesFiltros, text="Datos adicionales para c??lculos: ",font=("Yu Gothic bold",15))

		listaValoresTemp=["Acero al carbono API 5L SCH-40","Acero al carbono API 5L SCH-80","Hierro d??ctil C30",
		"Hierro d??ctil C40","Polietileno de alta densidad (PEAD) PE 100 RDE 21","Polietileno de alta densidad (PEAD) PE 100 RDE 17",
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
			diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
			diametroNominalTuberiaLavado.config(values=opcionesDic[materialTuberiaLavado.get()])
			if materialTuberiaLavado.get() == "Acero al carbono API 5L SCH-40" or materialTuberiaLavado.get()== "Acero al carbono API 5L SCH-80" or materialTuberiaLavado.get() == "Policluro de vinilo (PVC) RDE 26" or materialTuberiaLavado.get()=="Policluro de vinilo (PVC) RDE 21":
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [Pulgadas]:")
				indicador="Pulgadas"
			else:
				diametroNominalTuberiaLavadoLabel.config(text="Seleccione el diametro nominal de la tuber??a de lavado [mm]:")
				indicador="mm"

		materialTuberiaLavado = ttk.Combobox(framecanaletasDeLavadoYDimensionesFiltros, width="50", state="readonly", values=tuple(opcionesDic.keys()))
		materialTuberiaLavado.bind("<<ComboboxSelected>>", on_combobox_select)
		materialTuberiaLavado.set("Material de la tuber??a de lavado")

		materialTuberiaLabel= Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione el material de la tuber??a de lavado:",font=("Yu Gothic bold",10))
		

		diametroNominalTuberiaLavado = ttk.Combobox(framecanaletasDeLavadoYDimensionesFiltros, width="40", state="readonly")
		diametroNominalTuberiaLavado.set("Di??metro nominal de la tuber??a de lavado")
		diametroNominalTuberiaLavadoLabel= Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione el diametro nominal de la tuber??a de lavado []:",font=("Yu Gothic bold",10))



		
		
		codoRadio = StringVar()
		codoRadio.set("Codo 90?? radio")
		listaValoresTemp3=['Codo 90?? radio corto (r/d 1)', 'Codo 90?? radio mediano (r/d 3)']
		codoRadioName = OptionMenu(framecanaletasDeLavadoYDimensionesFiltros, codoRadio, *listaValoresTemp3)



		tipoEntrada = StringVar()
		tipoEntrada.set("Tipo de entrada")
		listaValoresTemp3=['Entrada recta a tope', 'Entrada con boca acampanada']
		tipoEntradaName = OptionMenu(framecanaletasDeLavadoYDimensionesFiltros, tipoEntrada, *listaValoresTemp3)

		AnchoCanaleta = StringVar()
		AnchoCanaleta.set("Ancho")
		listaValoresTemp3=['0.10','0.15','0.20','0.25','0.30','0.35']
		AnchoCanaletaName = OptionMenu(framecanaletasDeLavadoYDimensionesFiltros, AnchoCanaleta, *listaValoresTemp3)


		


		longitudTuberiaLavadoLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Longitud de la tuber??a del efluente [1.5m - 2.5m]:", font =("Yu Gothic",9))

		factorFriccionLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione el factor de fricci??n [0.0001 - 0.1]:", font =("Yu Gothic",9))
		
		divisorAccesoriosLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione los tipos de accesorios:", font=("Yu Gothic bold",10))
		
		divisorCanaletasLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione los valores para las canaletas de lavado:", font=("Yu Gothic bold",10))
		
		divisorDimensionesYCotasFiltrosLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Seleccione los valores para las dimensiones y cotas en los filtros:", font=("Yu Gothic bold",10))

		alturaVertederoControlLechoFijoLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Introduzca el nivel de vertedero sobre el lecho fijo de arena [0.15m - 0.20m]:", font=("Yu Gothic",10))

		energiaDisponibleFiltracionLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Introduzca la energ??a disponible de filtraci??n [1.8m - 2.0m]", font=("Yu Gothic",10))

		bordeLibreLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Introduzca el valor del borde libre [0.40m - 0.50m]", font=("Yu Gothic",10))


		longitudTuberiaLavado = Entry(framecanaletasDeLavadoYDimensionesFiltros)
		factorFriccion = Entry(framecanaletasDeLavadoYDimensionesFiltros)	


		alturaVertederoControlLechoFijo = Entry(framecanaletasDeLavadoYDimensionesFiltros)	
		energiaDisponibleFiltracion = Entry(framecanaletasDeLavadoYDimensionesFiltros)	
		bordeLibre = Entry(framecanaletasDeLavadoYDimensionesFiltros)	

		
		espaciamientoEntreEjesAsumidoLabel = Label(framecanaletasDeLavadoYDimensionesFiltros, text="Espaciamiento entre ejes de canaletas(asumido)[1.2m - 2m]:", font=("Yu Gothic",10))
		espaciamientoEntreEjes= Entry(framecanaletasDeLavadoYDimensionesFiltros,width=7)	
		anchoCanaletaLabel= Label(framecanaletasDeLavadoYDimensionesFiltros, text="Ancho de la canaleta [m]:", font=("Yu Gothic",10))
		



		listaEntradas=[materialTuberiaLavado, diametroNominalTuberiaLavado, longitudTuberiaLavado, factorFriccion,codoRadio,tipoEntrada,AnchoCanaleta,
		alturaVertederoControlLechoFijo, energiaDisponibleFiltracion, bordeLibre,espaciamientoEntreEjes]

		listaLabel=[inicialLabel, materialTuberiaLabel , materialTuberiaLavado, diametroNominalTuberiaLavadoLabel, 
		diametroNominalTuberiaLavado,longitudTuberiaLavadoLabel, factorFriccionLabel,divisorAccesoriosLabel,tipoEntradaName,
		divisorCanaletasLabel, AnchoCanaletaName, divisorDimensionesYCotasFiltrosLabel, alturaVertederoControlLechoFijoLabel,
		 energiaDisponibleFiltracionLabel,
		bordeLibreLabel]

		alturaInicialLabel=20
		m=0
		for elemento in listaLabel:
			if elemento==AnchoCanaletaName:
				alturaInicialExtra=alturaInicialLabel
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

		UbicarFinal=[anchoCanaletaLabel, AnchoCanaletaName,espaciamientoEntreEjesAsumidoLabel, espaciamientoEntreEjes]
		xUbicacionFinal=[50,220,320,700]
		for i in range(0,len(UbicarFinal)):
			UbicarFinal[i].place(x=xUbicacionFinal[i],y=alturaInicialExtra)
	

		#BotonesCanaletasDimensiones 
		botonCalcularCanaletas = HoverButton(framecanaletasDeLavadoYDimensionesFiltros, text="C??lculos canaletas de lavado", activebackground="#9DC4AA", width=100, height=1, bg= "#09C5CE", font =("Courier",9),command= lambda: canaletasDeLavado2(TemperatureValue,d60, caudalLista,listaE, listaEntradas[6],listaEntradas[10],porosidad,profundidadLechoFijo))
		botonCalcularDimensionesYCotasFiltros = HoverButton(framecanaletasDeLavadoYDimensionesFiltros, text="C??lculos dimensiones y cotas en los filtros", activebackground="#9DC4AA", width=100, height=1, bg= "#09C5CE", font =("Courier",9),command= lambda: dimensionesYCotasFiltros(TemperatureValue,d60, caudal,listaEntradaDrenaje, listaEntradas,caudalLista,listaE,tasa,profundidadLechoFijo))
		botonNewEntry = HoverButton(framecanaletasDeLavadoYDimensionesFiltros, text="Limpiar entradas.", activebackground="#9DC4AA", width=100, height=1, bg= "#09C5CE", font =("Courier",9),command= lambda: newEntryFiltroP(listaEntradas, diametroNominalTuberiaLavadoLabel))
		botones=[botonCalcularCanaletas, botonCalcularDimensionesYCotasFiltros, botonNewEntry]
		alturaBotones= alturaInicialEntradas2-45
		for elemento in botones:
			elemento.place(x=40, y=alturaBotones)
			alturaBotones= alturaBotones+30

		#Borrar
		# materialTuberiaLavado.set("Acero al carbono API 5L SCH-80")
		# diametroNominalTuberiaLavado.set("10")
		# longitudTuberiaLavado.insert(0,"1.50")
		# factorFriccion.insert(0,"0.0200")	
		# tipoEntrada.set('Entrada con boca acampanada')
		# alturaVertederoControlLechoFijo.insert(0,"0.2")
		# energiaDisponibleFiltracion.insert(0,"1.8")
		# bordeLibre.insert(0,"0.4")
		# AnchoCanaleta.set("0.15")
		# espaciamientoEntreEjes.insert(0,"1.2")
		#NOBorrar
		codoRadio.set('Codo 90?? radio mediano (r/d 3)')
		




		canaletasDeLavadoYDimensionesFiltrosWindow.mainloop()


	def perdidaEnergiaLechoLimpio(listaTamiz, listaAR, optnValue, listaCaudal):
		#PerdidaLechoLimpio
		try: 
			caudalMedio=float(listaCaudal[0].get())
			
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero.")
			return None

		if caudalMedio<0.01 or caudalMedio>0.2:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero entre 0.01 y 0.2")
			return None

		listaNTamizTemp=listaTamiz.copy()
		listaARetenidaTemp=listaAR.copy()
		listaNTamiz=list()
		listaARetenida=list()

		if listaNTamizTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de los n??meros de tamiz.")
			return None
		if listaARetenidaTemp[0].get() == "":
			messagebox.showwarning(title="Error", message="Hace falta alg??n dato de la arena retenida.")
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
							messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no coincide con los valores est??ndar para n??mero de tamiz. Pulse el bot??n para conocerlos.")
							return None
					if  ind%2 != 0:
						guardaValColumna2 = int(listaNTamizTemp[ind].get())	
					
					if ind !=0 and ind%2==0 and int(listaNTamizTemp[ind].get()) != guardaValColumna2:
						messagebox.showwarning(title="Error", message=f"El valor donde finaliza un rango debe ser el valor inicial del siguiente rango.")
						return None
					if ind != 0 and int(listaNTamizTemp[ind].get()) < variableControlCreciente:
						messagebox.showwarning(title="Error", message=f"Los valores de los rangos de n??mero de tamiz deben ir en orden creciente.")
						return None
					variableControlCreciente=int(listaNTamizTemp[ind].get())

					
					listaNTamiz.append(int(listaNTamizTemp[ind].get()))

				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None


		for ind in range(0, len(listaARetenidaTemp)):
			if listaARetenidaTemp[ind].get() == "" and ind != 0:
				break
			else:
				try:
					listaARetenida.append(float(listaARetenidaTemp[ind].get()))
				except:
					messagebox.showwarning(title="Error", message="Alguno de los valores ingresados no es un n??mero")
					return None
		if len(listaARetenida) != len(listaNTamiz)/2:
			messagebox.showwarning(title="Error", message="La cantidad de datos ingresados en los rangos de n??mero de tamiz no coincide con la cantidad de datos de arena retendia.")
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
		path=resource_path('icons\\agua.ico')
		perdidaEnergiaLechoLimpioMainWindow.iconbitmap(bitmap=path)
		perdidaEnergiaLechoLimpioMainWindow.geometry("800x600") 
		perdidaEnergiaLechoLimpioMainWindow.resizable(0,0)	
		perdidaEnergiaLechoLimpioMainWindow.configure(background="#9DC4AA")

		perdidaEnergiaLechoLimpioMainFrame=LabelFrame(perdidaEnergiaLechoLimpioMainWindow, text="Datos adicionales para calcular la p??rdida de energ??a durante filtrado con lecho limpio", font=("Yu Gothic bold", 11))
		perdidaEnergiaLechoLimpioMainFrame.pack(side=TOP, fill=BOTH,expand=True)

		
		
		diametroOrificios = StringVar()
		diametroOrificios.set("Diametro de los orificios")
		listaValoresTempDiametroOrificios=list()
		listaValoresTempDiametroOrificios.append("1/4")
		listaValoresTempDiametroOrificios.append("3/8")
		listaValoresTempDiametroOrificios.append("1/2")
		listaValoresTempDiametroOrificios.append("5/8")
		diametroOrificiosName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, diametroOrificios, *listaValoresTempDiametroOrificios)
		diametroOrificiosLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione el di??metro de los orificios [pulgadas]:", font=("Yu Gothic bold", 10))
		

		
		distanciaOrificios = StringVar()
		distanciaOrificios.set("Distancia entre los orificios")
		listaValoresTempDistanciaOrificios=list()
		listaValoresTempDistanciaOrificios.append("0.750")
		listaValoresTempDistanciaOrificios.append("0.100")
		listaValoresTempDistanciaOrificios.append("0.125")
		listaValoresTempDistanciaOrificios.append("0.150")
		distanciaOrificiosName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, distanciaOrificios, *listaValoresTempDistanciaOrificios)
		distanciaOrificiosLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la distancia entre orificios [m]:", font=("Yu Gothic bold", 10))


		seccionTransversal = StringVar()
		seccionTransversal.set("Secci??n transversal")
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
		seccionTransversalLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la secci??n transversal comercial del m??ltiple [pulgadas^2]:", font=("Yu Gothic bold", 9))


		distanciaLaterales = StringVar()
		distanciaLaterales.set("Distancia entre laterales")
		listaValoresTempDistanciaLaterales=list()
		listaValoresTempDistanciaLaterales.append("0.20")
		listaValoresTempDistanciaLaterales.append("0.25")
		listaValoresTempDistanciaLaterales.append("0.30")
		distanciaLateralesName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, distanciaLaterales, *listaValoresTempDistanciaLaterales)
		distanciaLateralesLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la distancia entre laterales [m]:", font=("Yu Gothic bold", 10))
		

		
		diametroEntreLaterales = StringVar()
		diametroEntreLaterales.set("Di??metro de los laterales")
		listaValoresTempDiametroEntreLaterales=list()
		listaValoresTempDiametroEntreLaterales.append("1 1/2")
		listaValoresTempDiametroEntreLaterales.append("2")
		listaValoresTempDiametroEntreLaterales.append("2 1/2")
		listaValoresTempDiametroEntreLaterales.append("3")
		diametroEntreLateralesName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, diametroEntreLaterales, *listaValoresTempDiametroEntreLaterales)
		diametroEntreLateralesLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione el di??metro de los laterales [pulgadas]:", font=("Yu Gothic bold", 10))

		tiempoRetrolavado = StringVar()
		tiempoRetrolavado.set("Tiempo de retrolavado")
		listaValoresTemptiempoRetrolavado=list()
		listaValoresTemptiempoRetrolavado.append("10")
		listaValoresTemptiempoRetrolavado.append("11")
		listaValoresTemptiempoRetrolavado.append("12")
		listaValoresTemptiempoRetrolavado.append("13")
		listaValoresTemptiempoRetrolavado.append("14")
		tiempoRetrolavadoName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, tiempoRetrolavado, *listaValoresTemptiempoRetrolavado)
		tiempoRetrolavadoLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione el tiempo de retrolavado [s]:", font=("Yu Gothic bold", 10))

		
		TasaElegir = StringVar()
		TasaElegir.set("Tasa")
		listaValoresTempTasaElegir=list()
		listaValoresTempTasaElegir.append("Tasa media")
		listaValoresTempTasaElegir.append("Tasa m??xima")
		TasaElegirName = OptionMenu(perdidaEnergiaLechoLimpioMainFrame, TasaElegir, *listaValoresTempTasaElegir)
		TasaElegirLabel= Label(perdidaEnergiaLechoLimpioMainWindow, text="Seleccione la tasa.", font=("Yu Gothic bold", 10))

		
		porosidadLechoFijoLabel = Label(perdidaEnergiaLechoLimpioMainFrame, text="Porosidad del lecho fijo [0.4 - 0.48]:", font =("Yu Gothic bold",10))
		porosidadLechoFijo = Entry(perdidaEnergiaLechoLimpioMainFrame)

		profundidadLechoFijoArenaLabel = Label(perdidaEnergiaLechoLimpioMainFrame, text="Profundidad del lecho fijo de arena [0.6m - 0.75m]:", font =("Yu Gothic bold",10))
		profundidadLechoFijoArena = Entry(perdidaEnergiaLechoLimpioMainFrame)




		listaEntradaDrenaje2=[diametroOrificiosName,distanciaOrificiosName,seccionTransversalName,distanciaLateralesName, diametroEntreLateralesName,tiempoRetrolavadoName,TasaElegirName,porosidadLechoFijo,profundidadLechoFijoArena]
		listaLabel= [diametroOrificiosLabel,distanciaOrificiosLabel, seccionTransversalLabel, distanciaLateralesLabel, diametroEntreLateralesLabel,tiempoRetrolavadoLabel,TasaElegirLabel,porosidadLechoFijoLabel,profundidadLechoFijoArenaLabel]
		listaEntradaDrenaje=[diametroOrificios,distanciaOrificios,seccionTransversal,distanciaLaterales, diametroEntreLaterales]
		listaEntradaExtra=[tiempoRetrolavado]
		
		#Borrar
		# profundidadLechoFijoArena.insert(0,"0.7")
		# porosidadLechoFijo.insert(0,"0.47")
		# diametroOrificios.set("1/2")
		# distanciaOrificios.set("0.150")
		# seccionTransversal.set("8 X 8")
		# distanciaLaterales.set("0.25")
		# diametroEntreLaterales.set("2 1/2")
		# tiempoRetrolavado.set("14")
		# TasaElegir.set('Tasa media')
		
		

		altIn= 30
		altIn2=30
		for ind in range(0,len(listaLabel)):
			if ind%2==0:
				listaLabel[ind].place(x=20,y=altIn)
				listaEntradaDrenaje2[ind].place(x=20, y= altIn+20)
				altIn=altIn+70
			else:
				listaLabel[ind].place(x=500,y=altIn2)
				listaEntradaDrenaje2[ind].place(x=500, y= altIn2+20)
				altIn2=altIn2+70
			
		#BotonesPerdidaEnergiaLechoLimpio
		

		#TasaElegir
		

		
	
		botonPerdidacargaLechoGravaLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="P??rdida de energ??a en el lecho de grava\ndurante filtrado con lecho limpio", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidacargaLechoGravaLavado_2(TasaElegir) ) 
		botonPerdidaCargaSistemaDrenajeLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="P??rdida de energ??a en el sistema de\ndrenaje durante filtrado con lecho limpio", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaSistemaDrenajeLavado_2(caudalMedio, listaEntradaDrenaje, TasaElegir) )
		botonPerdidaCargaTuberiaLavado_DW = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="P??rdida de energ??a en la tuber??a\n del efluente", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTuberiaLavado_DW_HW_2(valorTemperatura,listaEntradaExtra,d60,listaCaudal,TasaElegir)) 
		botonPerdidaCargaTotalLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="P??rdida de energ??a total durante\n filtrado con lecho limpio", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: perdidaCargaTotalLavadoMain_2(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal,TasaElegir))
		botonCanaletasLavado = HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Canaletas de lavado &\n dimensiones y cotas en los filtros", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: canaletasDeLavadoYDimensionesFiltros(valorTemperatura,d60,caudalMedio, listaEntradaDrenaje,listaEntradaExtra,listaCaudal,TasaElegir,porosidadLechoFijo,profundidadLechoFijoArena) )
		

		def newEntryPerdidaTotal(lista,porosidad,profundidad): 
			lista2= [
						"Diametro de los orificios",
						"Distancia entre los orificios",
						"Secci??n transversal",
						"Distancia entre laterales",
						"Di??metro de los laterales",
						"Tiempo de retrolavado",
						"Tasa"]

			for i in range(0, len(lista)):
					lista[i].set(lista2[i])
			porosidad.delete(0,END)
			profundidad.delete(0,END)

		listaTasa= [TasaElegir]
		botonLimpiarEntradasPerdidaTotal =  HoverButton(perdidaEnergiaLechoLimpioMainFrame, text="Limpiar Entradas", activebackground="#9DC4AA", anchor=CENTER , width=40, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: newEntryPerdidaTotal(listaEntradaDrenaje+listaEntradaExtra+listaTasa,porosidadLechoFijo,profundidadLechoFijoArena))


		 

		

		listaBotones=[botonPerdidacargaLechoGravaLavado ,botonPerdidaCargaSistemaDrenajeLavado 
		,botonPerdidaCargaTuberiaLavado_DW,botonPerdidaCargaTotalLavado, botonCanaletasLavado, botonLimpiarEntradasPerdidaTotal]
			
		counter= 0
		altIn=altIn-20
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

	def caudalDise??o(caudalMedioEntry):
		
		
		if caudalMedioEntry[0].get()== "": 
			messagebox.showwarning(title="Error", message="Hace falta introducir el valor del caudal medio")
			return None
		try: 
			caudalMedio=float(caudalMedioEntry[0].get())
		except:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero.")
			return None
		
		if caudalMedio<0.01 or caudalMedio>0.2:
			messagebox.showwarning(title="Error", message="El caudal medio diario debe ser un n??mero entre 0.01 y 0.2")
			return None



		CaudalesDise??oWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		CaudalesDise??oWindow.iconbitmap(bitmap=path)
		CaudalesDise??oWindow.geometry("500x280") 
		CaudalesDise??oWindow.resizable(0,0)	
		CaudalesDise??oWindow.configure(background="#9DC4AA")

		CaudalesDise??oFrame=LabelFrame(CaudalesDise??oWindow, text="Caudales de dise??o", font=("Yu Gothic bold", 11))
		CaudalesDise??oFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolCaudalesDise??o_frame = Frame(CaudalesDise??oFrame)
		arbolCaudalesDise??o_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolCaudalesDise??o_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolCaudalesDise??o_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCaudalesDise??o= ttk.Treeview(arbolCaudalesDise??o_frame,selectmode=BROWSE, height=11,show="tree headings")#,yscrollcommand=sedScrollY.set, xscrollcommand=sedScrollX.set)
		arbolCaudalesDise??o.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolCaudalesDise??o.xview)
		# sedScrollY.configure(command=arbolCaudalesDise??o.yview)
		#Define columnas.
		arbolCaudalesDise??o["columns"]= (
		"1","Valores","Unidades")

		

		#Headings
		arbolCaudalesDise??o.heading("#0",text="ID", anchor=CENTER)



		for col in arbolCaudalesDise??o["columns"]:
			arbolCaudalesDise??o.heading(col, text=col,anchor=CENTER)	

		arbolCaudalesDise??o.column("#1",width=300, stretch=False)
		arbolCaudalesDise??o.column("#2",width=100, stretch=False)
		arbolCaudalesDise??o.column("#3",width=100, stretch=False)
		


		arbolCaudalesDise??o.column("#0",width=0, stretch=False)
		
		

		#Striped row tags
		arbolCaudalesDise??o.tag_configure("evenrow", background= "#1FCCDB")
		arbolCaudalesDise??o.tag_configure("oddrow", background= "#9DC4AA")


		listaCaudalesDise??o=list()


		encabezadosLista=[
		"Factor de mayoraci??n del caudal m??ximo diario",
		"Factor de mayoraci??n del caudal m??ximo horario",
		"Caudal medio diario",			
		"Caudal m??ximo diario",			
		"Caudal m??ximo horario",			
		]
		unidadesLista=["",
		"",
		"(m^3)/s",
		"(m^3)/s",
		"(m^3)/s",
						]
		
		factorMayoracionMD = 1.3
		factorMayoracionMH = 1.6
		listaCaudalesDise??o.append(round(factorMayoracionMD,3))
		listaCaudalesDise??o.append(round(factorMayoracionMH,3))
		listaCaudalesDise??o.append(round(caudalMedio,5))
		caudalMaximoDiario=caudalMedio*factorMayoracionMD
		listaCaudalesDise??o.append(round(caudalMaximoDiario,5))
		caudalMaximoHorario=caudalMedio*factorMayoracionMH
		listaCaudalesDise??o.append(round(caudalMaximoHorario,5))
		
		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listaCaudalesDise??o[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolCaudalesDise??o,listaTemp)

		PasarExcelDatos(".\\ResultadosFiltro\\CaudalesDeDise??o.xlsx",'Resultados',encabezadosLista,50, listaCaudalesDise??o, 15, unidadesLista, 15,False,[], 50)
		CaudalesDise??oWindow.mainloop()


	def propiedadesFisicasAgua(temperaturaEntry):
		if temperaturaEntry.get()[0:10] == "Seleccione":
			messagebox.showwarning(title="Error", message=f"Hace falta seleccionar la temperatura del agua a tratar")
			return None	
		else:
			temperatura=float(temperaturaEntry.get())

		propiedadesFisicasAguaFWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		propiedadesFisicasAguaFWindow.iconbitmap(bitmap=path)
		propiedadesFisicasAguaFWindow.geometry("500x250") 
		propiedadesFisicasAguaFWindow.resizable(0,0)	
		propiedadesFisicasAguaFWindow.configure(background="#9DC4AA")

		propiedadesFisicasAguaFFrame=LabelFrame(propiedadesFisicasAguaFWindow, text="Propiedades f??sicas de agua a tratar", font=("Yu Gothic bold", 11))
		propiedadesFisicasAguaFFrame.pack(side=TOP, fill=BOTH,expand=True)

		#Frame Treeview
		arbolpropiedadesFisicasAguaF_frame = Frame(propiedadesFisicasAguaFFrame)
		arbolpropiedadesFisicasAguaF_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolpropiedadesFisicasAguaF_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolpropiedadesFisicasAguaF_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolpropiedadesFisicasAguaF= ttk.Treeview(arbolpropiedadesFisicasAguaF_frame,selectmode=BROWSE, height=11,show="tree headings")#,yscrollcommand=sedScrollY.set, xscrollcommand=sedScrollX.set)
		arbolpropiedadesFisicasAguaF.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolpropiedadesFisicasAguaF.xview)
		# sedScrollY.configure(command=arbolpropiedadesFisicasAguaF.yview)
		#Define columnas.
		arbolpropiedadesFisicasAguaF["columns"]= (
		"1","Valores","Unidades")



		#Headings
		arbolpropiedadesFisicasAguaF.heading("#0",text="ID", anchor=CENTER)




		for col in arbolpropiedadesFisicasAguaF["columns"]:
			arbolpropiedadesFisicasAguaF.heading(col, text=col,anchor=CENTER)	

		arbolpropiedadesFisicasAguaF.column("#1",width=300, stretch=False)
		arbolpropiedadesFisicasAguaF.column("#2",width=100, stretch=False)
		arbolpropiedadesFisicasAguaF.column("#3",width=100, stretch=False)



		arbolpropiedadesFisicasAguaF.column("#0",width=0, stretch=False)



		#Striped row tags
		arbolpropiedadesFisicasAguaF.tag_configure("evenrow", background= "#1FCCDB")
		arbolpropiedadesFisicasAguaF.tag_configure("oddrow", background= "#9DC4AA")


		listapropiedadesFisicasAguaF=list()


		encabezadosLista=[
		"Temperatura del agua a tratar",
		f"Densidad del agua a {temperatura} ??C",
		f"Viscocidad din??mica del agua a {temperatura} ??C",
		f"Viscocidad cinem??tica del agua a {temperatura} ??C",

		]
		unidadesLista=[
		"??C",
		"kg/(m^3)",
		"(N.s)/(m^2)",
		"(m^2)/s",
						]

		valorTemperaturas=list()

		tablaTemperaturaViscocidadCinematica=dict()
		viscosidadDinamicaDic=dict()
		tablaTemperaturaDensidad=dict()

		for i in range(0,36):    
			valorTemperaturas.append(i)
					
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		viscosidadDinamicaValor = [0.001792, 0.001731, 
		0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 
		0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 
		0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 
		0.001083, 0.001056, 0.00103, 0.001005, 0.000981, 
		0.000958, 0.000936, 0.000914, 0.000894, 0.000874,
		0.000855, 0.000836, 0.000818, 0.000801, 0.000784,
		0.000768, 0.000752, 0.000737, 0.000723]


		valorDensidad= [999.82, 999.89, 999.94, 999.98, 1000.0, 1000.0, 999.99, 999.96, 999.91, 999.85, 999.77, 999.68, 999.58, 999.46, 999.33, 999.19, 999.03, 998.86, 998.68, 998.49, 998.29, 998.08, 997.86, 997.62, 997.38, 997.13, 
			996.86, 996.59, 996.31, 996.02, 995.71, 995.41, 995.09, 994.76, 994.43, 994.08]

		for ind in range(0,len(valorTemperaturas)):
			tablaTemperaturaDensidad[valorTemperaturas[ind]]= valorDensidad[ind]
			tablaTemperaturaViscocidadCinematica[valorTemperaturas[ind]]=valorViscocidad[ind]
			viscosidadDinamicaDic[valorTemperaturas[ind]]=viscosidadDinamicaValor[ind]

		valorDensidadAgua = tablaTemperaturaDensidad[temperatura]
		viscosidadDinamica = viscosidadDinamicaDic[temperatura]
		viscosidadCinematica = tablaTemperaturaViscocidadCinematica[temperatura]


		listapropiedadesFisicasAguaF.append(round(temperatura))
		listapropiedadesFisicasAguaF.append(round(valorDensidadAgua,2))
		listapropiedadesFisicasAguaF.append(round(viscosidadDinamica,9))
		listapropiedadesFisicasAguaF.append(round(viscosidadCinematica,9))


		for i in range(0, len(encabezadosLista)):
			listaTemp=list()
			listaTemp.append(encabezadosLista[i])
			listaTemp.append(listapropiedadesFisicasAguaF[i])
			listaTemp.append(unidadesLista[i])
			newDataTreeview(arbolpropiedadesFisicasAguaF,listaTemp)

		PasarExcelDatos(".\\ResultadosFiltro\\propiedadesFisicasAgua.xlsx",'Resultados',encabezadosLista,50, listapropiedadesFisicasAguaF, 15, unidadesLista, 15,False,[], 50)
		propiedadesFisicasAguaFWindow.mainloop()

        


	mainWindow.withdraw()
	filtroWindow = tk.Toplevel()
	filtroWindow.protocol("WM_DELETE_WINDOW", on_closing)
	path=resource_path('icons\\agua.ico')
	filtroWindow.iconbitmap(bitmap=path)
	filtroWindow.geometry("1000x650") 
	filtroWindow.resizable(0,0)	
	filtroWindow.configure(background="#9DC4AA")

	#panelF = ttk.Notebook(filtroWindow)
	#panelF.pack(fill=BOTH, expand=TRUE)
	frameFiltro= LabelFrame(filtroWindow, text="Filtro r??pido", font=("Yu Gothic bold", 11))
	frameFiltro.pack(side=LEFT,fill=BOTH,expand=TRUE)
	#panelF.add(frameFiltro, text="Filtro r??pido")
	pathAtras= resource_path('images\\atras.png')
	imageAtras= PhotoImage(file=pathAtras)
	pathRestringido = resource_path("images\\restringido.png")
	imageRestringido=PhotoImage(file=pathRestringido)
	#BotonesFiltro 


	botonAtras= HoverButton(frameFiltro, image=imageAtras , width=100, height=40, bg= None, command=lambda: returnMainWindow(filtroWindow))
	botonAtras.place(x=0,y=10)
	botonRestriccionNumTamiz=  HoverButton(frameFiltro, image=imageRestringido, bg=None, width=20, height=20,command= lambda: messagebox.showinfo(title="Valores est??ndar tama??o de tamiz",message=f"Los tama??os est??ndar son: 4,6,8,12,14,18,20,25,30,35,40,45,50,60,70,80,100,140") )
	botonRestriccionNumTamiz.place(x=150,y=65)


	botonNewEntryFiltro = HoverButton(frameFiltro, text="Limpiar entradas", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: newEntryFiltro(lista_entradas, tempAgua, entradasCaudal))

	botonPrincipalesCaracteristicasDelFiltro = HoverButton(frameFiltro, text="Ver principales caracter??sticas del filtro", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=principalesCaracFiltro)

	botonGranulometria = HoverButton(frameFiltro, text="Granulometr??a del medio filtrante de arena", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: granulometria(listaNumTamiz,listaAR))

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
	tipoCaudalLabel = Label(frameFiltro, text="Caudal de dise??o:",font=("Yu Gothic bold",10))
	#tipoCaudalLabel.place(x=250, y=157)
	caudalMedioLabel= Label(frameFiltro, text="Caudal medio diario [(m^3)/s]: ",font=("Yu Gothic bold",8))	
	caudalMedio = Entry(frameFiltro, width=7)

	altIninicial=157
	listaTipoCaudal = [tipoCaudalLabel, caudalMedioLabel]
	for elem in listaTipoCaudal:
		elem.place(x=330, y=altIninicial)
		altIninicial=altIninicial+35
	caudalMedio.place(x=500, y=altIninicial-35)
	entradasCaudal= [caudalMedio]

	#####FIN TEMP AGUA
	
	#BotonesFiltro2

	botonEstimacionPerdidaEnergiaLechoFiltranteArenaLimpio = HoverButton(frameFiltro, text="P??rdida de energ??a en el lecho filtrante de arena limpio", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: estimacionPerdidaEnergiaArena(listaNumTamiz,listaAR,tempAgua))

	#botonEstimacionPerdidaLechoGrava = HoverButton(frameFiltro, text="Estimaci??n de la p??rdida de energ??a en el lecho de grava, y\n ??Carga?", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command= lambda: estPerdidaLechoGravaYPredimensionamientoFiltros(listaNumTamiz, listaAR,tempAgua))

	#botonPerdidaCargaLechoExpandido = HoverButton(frameFiltro, text="P??rdida de carga a trav??s del lecho expandido", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command= perdidaCargaLechoExpandido)

	botonPredimensionamientoFiltros = HoverButton(frameFiltro, text="Predimensionamiento de los filtros", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: predimensionamientoFiltros(entradasCaudal))

	botonDrenajeFiltro = HoverButton(frameFiltro, text="Drenaje del filtro - Tuber??as perforadas", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: drenajeFiltro(entradasCaudal))
	

	botonHidraulicaSistemaLavado = HoverButton(frameFiltro, text="Hidr??ulica del sistema de lavado", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: hidraulicaSistemaLavado(listaNumTamiz,listaAR,tempAgua, entradasCaudal))

	botonPerdidaEnergiaLechoLimpio = HoverButton(frameFiltro, text="P??rdidas de energ??a durante el filtrado con lecho limpio", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: perdidaEnergiaLechoLimpio(listaNumTamiz,listaAR,tempAgua, entradasCaudal))
 
	botonCaudalDise??o = HoverButton(frameFiltro, text="Caudales de dise??o", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: caudalDise??o(entradasCaudal))

	botonPropiedadesFisicasAguaTratar = HoverButton(frameFiltro, text="Propiedades f??sicas del agua a tratar", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9), command=lambda: propiedadesFisicasAgua(tempAgua))
	
	botonAyudaVisual = HoverButton(frameFiltro, text="Ayuda visual-\nGeometr??a del filtro r??pido", activebackground="#9DC4AA", anchor=CENTER , width=40, height=4, bg= "#09C5CE", font =("Courier",9), command=lambda: proyectarImg('images\\VistaFiltro.png',712,561))

	listaBotonesOrg=[botonNewEntryFiltro,botonCaudalDise??o,botonPrincipalesCaracteristicasDelFiltro, 
	botonPropiedadesFisicasAguaTratar,botonGranulometria,botonCoefUniformidad,botonEstimacionPerdidaEnergiaLechoFiltranteArenaLimpio,botonPredimensionamientoFiltros
	,botonDrenajeFiltro,botonHidraulicaSistemaLavado,botonPerdidaEnergiaLechoLimpio,
	]#,botonEstimacionPerdidaLechoGrava,botonPerdidaCargaLechoExpandido]

	alturaInicialBotones=70
	for boton in listaBotonesOrg:
		boton.place(x=560, y=alturaInicialBotones)
		alturaInicialBotones=alturaInicialBotones+50
	
	botonAyudaVisual.place(x=100,y=alturaInicialBotones-100)

	Label(frameFiltro, text="Dise??o de filtro",font=("Yu Gothic bold",10)).place(x=170, y=30)

	numTamizLabel = Label(frameFiltro, text="N??mero de tamiz",font=("Yu Gothic bold",10))
	numTamizLabel.place(x=30, y=70)
	arenaRetenidaLabel = Label(frameFiltro, text="Arena retenida [%]",font=("Yu Gothic bold",10))
	arenaRetenidaLabel.place(x=200, y=70)
	tempAguaLabel = Label(frameFiltro, text="Temperatura del agua a tratar[??C]:",font=("Yu Gothic bold",9))
	tempAguaLabel.place(x=340, y=70)
	
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
	
	#BorrarFiltro
	
	
	# tempAgua.set("8")
	# caudalMedio.insert(0,"0.0432")
	listaNTamiz=[14, 20, 20, 25, 25, 30, 30, 35, 35, 40, 40, 50, 50, 60, 60, 70, 70, 100]
	listaARetenida= [16 , 33.70, 33.90, 6.20, 3.00, 3.00, 2.25, 1.25, 0.7]
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

	def newEntryFloculador(lista):
		
		i=0
		for elemento in lista:
			try:
				elemento.set("Seleccione")
				
				i=i+1
			except:
				elemento.delete(0, END)

		lista[5].insert(0,9.81)
		

	def newDataTreeview(tree,listaS):
		global contadorFloculador

		if contadorFloculador%2 ==0:
			tree.insert("",END,text= f"{contadorFloculador+1}", values=tuple(listaS),
			iid=contadorFloculador, tags=("evenrow",))	
		else:	
			tree.insert("",END,text= f"{contadorFloculador+1}", values=tuple(listaS),
				iid=contadorFloculador, tags=("oddrow",))
		contadorFloculador=contadorFloculador+1
	def datosIniciales(listaEntry, numCamaras):
		listaE2=list()

		labels=["caudal de dise??o", "ancho",
		"longitud", "altura", "gravedad"]
		labelsComboBox= ["tiempo de floculaci??n", "temperatura"]
		
		listaSinComboBox=[listaEntry[0],listaEntry[2],listaEntry[3],
		listaEntry[4],listaEntry[5]]
		
		listaComboBox=[listaEntry[1],listaEntry[6]]

		# listaEntryNueva= [0= caudalDise??o,1=tiempoFloculacion,
		# 		2=ancho,3=longitud,4=altura,5=gravedad,6=temperatura,]
		
		# listaEntry= [0= caudalDise??o,1=tiempoFloculacion,2=diametroInterno,
		# 3=diametroExterno,
		# 4=ancho,5=longitud,6=altura,7=gravedad,8=temperatura,
		# 9=coeficienteDescarga,10=coeficienteDescargaOrificios]
		
		for i in range(0, len(listaComboBox)):
			if listaComboBox[i].get() == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labelsComboBox[i]} ")	
				return None
		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None
		j=0
		for elemento in listaSinComboBox:
			try:
				listaE2.append(float(elemento.get()))
				j=j+1
			except:	
				messagebox.showwarning(title="Error", message=f"El/la {labels[j]} debe ser un n??mero")
				return None
		
			# listaEntryNueva= [0= caudalDise??o,1=tiempoFloculacion,
		# 		2=ancho,3=longitud,4=altura,5=gravedad,6=temperatura,]
		
		#[caudal, ancho,longitud, altura, gravedad]
		caudalDise??o= listaE2[0]
	
		ancho = listaE2[1]
		longitud = listaE2[2]
		altura = listaE2[3]
		gravedad = listaE2[4]
		coeficienteDescarga = 0.76
		coeficienteDescargaOrificios = 0.80
		tiempoFloculacion= float(listaComboBox[0].get())
		temperatura= float(listaComboBox[1].get())


		if caudalDise??o<10 or caudalDise??o>100:
			messagebox.showwarning(title="Error", message=f"El valor del caudal de Dise??o debe estar entre 10 y 100")
			return None	
		numeroCamaras= float(numCamaras.get())

		if caudalDise??o<15:
			diametroInterconexion=0.15
		elif caudalDise??o<25:
			diametroInterconexion=0.25
		elif caudalDise??o<35:
			diametroInterconexion=0.30
		elif caudalDise??o<55:
			diametroInterconexion=0.35
		elif caudalDise??o<65:
			diametroInterconexion=0.40
		elif caudalDise??o<85:
			diametroInterconexion=0.45
		elif caudalDise??o<101:
			diametroInterconexion=0.50
		
		diametroInteriorLista=[
		0.05458,
		0.06607,
		0.08042,
		0.10342,
		0.15222,
		0.19821,
		0.24709,
		0.29307,
		0.32176,
		0.36770,
		0.41366,
		0.45964,
		0.55154,
		]
		diametroPulgadaLista=[
		2.0,
		2.5,
		3.0,
		4.0,
		6.0,
		8.0,
		10.0,
		12.0,
		14.0,
		16.0,
		18.0,
		20.0,
		24.0,
		]
		diametroExteriorLista=[
		0.06032,
		0.07303,
		0.08890,
		0.11430,
		0.16828,
		0.21908,
		0.27305,
		0.32305,
		0.35560,
		0.40640,
		0.45720,
		0.50800,
		0.60960,

		]
		ListaTuplasDiametroExteriorDiametroPulgada=list()

		for i in range(0,len(diametroExteriorLista)):
			ListaTuplasDiametroExteriorDiametroPulgada.append((diametroExteriorLista[i],diametroPulgadaLista[i]))

		diametroInteriorListaExteriorPulgadaDic=dict()
		for i in range(0, len(diametroInteriorLista)):
			diametroInteriorListaExteriorPulgadaDic[diametroInteriorLista[i]]=ListaTuplasDiametroExteriorDiametroPulgada[i]

		

		mayor=0.55154
		for elemento in diametroInteriorLista:
			if elemento>diametroInterconexion and elemento<mayor:
				mayor=elemento


		diametroInterno = mayor
		diametroExterno = diametroInteriorListaExteriorPulgadaDic[mayor][0]
		
		datosInicialesWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		datosInicialesWindow.iconbitmap(bitmap=path)
		datosInicialesWindow.geometry("470x590") 
		datosInicialesWindow.resizable(0,0)	
		datosInicialesWindow.configure(background="#9DC4AA")

		#Frame Treeview
		arboldatosIniciales_frame = LabelFrame(datosInicialesWindow, text="Visualizaci??n de los c??lculos para floculador alabama", font=("Yu Gothic bold", 11))
		arboldatosIniciales_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arboldatosIniciales_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arboldatosIniciales_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arboldatosIniciales= ttk.Treeview(arboldatosIniciales_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set)#,xscrollcommand=sedScrollX.set
		arboldatosIniciales.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arboldatosIniciales.xview)
		sedScrollY.configure(command=arboldatosIniciales.yview)
		#Define columnas.
		arboldatosIniciales["columns"]= (
		"1","Valores","Unidades"
		)

		#Headings
		arboldatosIniciales.heading("#0",text="ID", anchor=CENTER)

		for col in arboldatosIniciales["columns"]:
			arboldatosIniciales.heading(col, text=col,anchor=CENTER)



		arboldatosIniciales.column("#0",width=0, stretch=False)
		arboldatosIniciales.column("#1",width=250, stretch=False)
		arboldatosIniciales.column("#2",width=100, stretch=False)
		arboldatosIniciales.column("#3",width=100, stretch=False)
		#Striped row tags
		arboldatosIniciales.tag_configure("evenrow", background= "#1FCCDB")
		arboldatosIniciales.tag_configure("oddrow", background= "#9DC4AA")
		contadorFloculador=0

		listaEntrada= list()



		valorTemperaturas=list()
		viscosidadCinematicaDic=dict()
		for i in range(0,36):    
			valorTemperaturas.append(i)
						
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		for ind in range(0,len(valorTemperaturas)):
			viscosidadCinematicaDic[valorTemperaturas[ind]]=valorViscocidad[ind]
		densidadDic=dict()

		valorDensidad=[999.82, 999.89, 999.94, 999.98, 1000.0, 1000.0, 999.99, 
		999.96, 999.91, 999.85, 999.77, 999.68, 999.58, 999.46, 
		999.33, 999.19, 999.03, 998.86, 998.68, 998.49, 998.29, 
		998.08, 997.86, 997.62, 997.38, 997.13, 996.86, 996.59,
		996.31, 996.02, 995.71, 995.41, 995.09, 994.76, 994.43, 
		994.08]

		for ind in range(0,len(valorTemperaturas)):
			densidadDic[valorTemperaturas[ind]]=valorDensidad[ind]

		viscosidadDinamicaDic=dict()
		viscosidadDinamicaValor = [0.001792, 0.001731, 
		0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 
		0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 
		0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 
		0.001083, 0.001056, 0.00103, 0.001005, 0.000981, 
		0.000958, 0.000936, 0.000914, 0.000894, 0.000874,
		0.000855, 0.000836, 0.000818, 0.000801, 0.000784,
		0.000768, 0.000752, 0.000737, 0.000723]

		for ind in range(0,len(valorTemperaturas)):
			viscosidadDinamicaDic[valorTemperaturas[ind]]=viscosidadDinamicaValor[ind]


		caudalDise??oEnM = caudalDise??o/1000.0
		areaTuberia = pi*(diametroInterno**2)*(1/4.0)
		areaOrificio = pi*(diametroExterno**2)*(1/4.0)
		tiempoFloculacionS= tiempoFloculacion*60.0
		tiempoDetencionCamara= tiempoFloculacionS/numeroCamaras
		viscosidadCinematica = viscosidadCinematicaDic[temperatura]
		densidad=densidadDic[temperatura]
		viscosidadDinamica = viscosidadDinamicaDic[temperatura]

		

		volumenCamara= tiempoDetencionCamara*caudalDise??oEnM


		listaValores=[caudalDise??o,caudalDise??oEnM,tiempoFloculacion,tiempoFloculacionS,
		tiempoDetencionCamara,volumenCamara,diametroInterconexion,
		diametroInterno,areaTuberia,diametroExterno,areaOrificio,
		ancho,longitud,altura,densidad,viscosidadDinamica,viscosidadCinematica,
		gravedad,temperatura, coeficienteDescarga, coeficienteDescargaOrificios]
		for valor in listaValores:
			if valor== viscosidadDinamica or valor == viscosidadCinematica:
				listaEntrada.append(round(valor,9))
			else:
				listaEntrada.append(round(valor,3))

		listaEncabezados = ["Caudal de Dise??o (QMD)",
		"Caudal de Dise??o (QMD)",
		"Tiempo de floculaci??n (T)",
		"Tiempo de floculaci??n (T)",
		"Tiempo de detencion de la camara (Tr)",
		"Volumen de cada camara (???c)",
		"Diametro interconexi??n (D)",
		f"Diametro de interno {diametroInteriorListaExteriorPulgadaDic[mayor][1]}\" (Di)",
		f"Area de la tuberia {diametroInteriorListaExteriorPulgadaDic[mayor][1]}\" (N)",
		f"Diametro de externo {diametroInteriorListaExteriorPulgadaDic[mayor][1]}\" (De)",
		f"Area del orificio {diametroInteriorListaExteriorPulgadaDic[mayor][1]}\" (A)",
		"Ancho (W)",
		"Longitud (L)",
		"Altura (a)",
		"Densidad del agua (p)",
		"Viscocidad Dinamica del agua (??)",
		"Viscocidad Cinematica del agua (v)",
		"Gravedad (g)",
		"Temperatura (??c) ",
		"Coeficiente de descarga (Cd)",
		"Coeficiente de descarga Orificios (Cd)",
				]
		listaUnidades = [
			"L/s",
			"m??/s",
			"min",
			"s",
			"s",
			"m??",
			"m",
			"m",
			"m??",
			"m",
			"m??",
			"m",
			"m",
			"m",
			"Kg/m??",
			"N.s/m2",
			"m??/s",
			"m/s2",
			"??C",
			"K",
			"K",

		]



		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaEntrada[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arboldatosIniciales,listaTemp)

		PasarExcelDatos(".\\ResultadosFloculador\\VerDatosIniciales.xlsx",'Resultados',listaEncabezados,50, listaEntrada, 15, listaUnidades, 15,False,[], 50)


		datosInicialesWindow.mainloop()





	def calculosFloculador(listaEntry,numCamaras):
		listaE2=list()

		labels=["caudal de dise??o", "ancho",
		"longitud", "altura", "gravedad"]
		labelsComboBox= ["tiempo de floculaci??n", "temperatura"]
		
		listaSinComboBox=[listaEntry[0],listaEntry[2],listaEntry[3],
		listaEntry[4],listaEntry[5]]
		
		listaComboBox=[listaEntry[1],listaEntry[6]]

		# listaEntryNueva= [0= caudalDise??o,1=tiempoFloculacion,
		# 		2=ancho,3=longitud,4=altura,5=gravedad,6=temperatura,]
		
		# listaEntry= [0= caudalDise??o,1=tiempoFloculacion,2=diametroInterno,
		# 3=diametroExterno,
		# 4=ancho,5=longitud,6=altura,7=gravedad,8=temperatura,
		# 9=coeficienteDescarga,10=coeficienteDescargaOrificios]
		
		for i in range(0, len(listaComboBox)):
			if listaComboBox[i].get() == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labelsComboBox[i]} ")	
				return None
		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None
		j=0
		for elemento in listaSinComboBox:
			try:
				listaE2.append(float(elemento.get()))
				j=j+1
			except:	
				messagebox.showwarning(title="Error", message=f"El/la {labels[j]} debe ser un n??mero")
				return None
		
			# listaEntryNueva= [0= caudalDise??o,1=tiempoFloculacion,
		# 		2=ancho,3=longitud,4=altura,5=gravedad,6=temperatura,]
		
		#[caudal, ancho,longitud, altura, gravedad]
		caudalDise??o= listaE2[0]
	
		ancho = listaE2[1]
		longitud = listaE2[2]
		altura = listaE2[3]
		gravedad = listaE2[4]
		coeficienteDescarga = 0.76
		coeficienteDescargaOrificios = 0.80
		tiempoFloculacion= float(listaComboBox[0].get())
		temperatura= float(listaComboBox[1].get())


		if caudalDise??o<10 or caudalDise??o>100:
			messagebox.showwarning(title="Error", message=f"El valor del caudal de Dise??o debe estar entre 10 y 100")
			return None	
		numeroCamaras= float(numCamaras.get())

		if caudalDise??o<15:
			diametroInterconexion=0.15
		elif caudalDise??o<25:
			diametroInterconexion=0.25
		elif caudalDise??o<35:
			diametroInterconexion=0.30
		elif caudalDise??o<55:
			diametroInterconexion=0.35
		elif caudalDise??o<65:
			diametroInterconexion=0.40
		elif caudalDise??o<85:
			diametroInterconexion=0.45
		elif caudalDise??o<101:
			diametroInterconexion=0.50

		diametroInteriorLista=[
		0.05458,
		0.06607,
		0.08042,
		0.10342,
		0.15222,
		0.19821,
		0.24709,
		0.29307,
		0.32176,
		0.36770,
		0.41366,
		0.45964,
		0.55154,
		]
		diametroPulgadaLista=[
		2.0,
		2.5,
		3.0,
		4.0,
		6.0,
		8.0,
		10.0,
		12.0,
		14.0,
		16.0,
		18.0,
		20.0,
		24.0,
		]
		diametroExteriorLista=[
		0.06032,
		0.07303,
		0.08890,
		0.11430,
		0.16828,
		0.21908,
		0.27305,
		0.32305,
		0.35560,
		0.40640,
		0.45720,
		0.50800,
		0.60960,

		]
		ListaTuplasDiametroExteriorDiametroPulgada=list()

		for i in range(0,len(diametroExteriorLista)):
			ListaTuplasDiametroExteriorDiametroPulgada.append((diametroExteriorLista[i],diametroPulgadaLista[i]))

		diametroInteriorListaExteriorPulgadaDic=dict()
		for i in range(0, len(diametroInteriorLista)):
			diametroInteriorListaExteriorPulgadaDic[diametroInteriorLista[i]]=ListaTuplasDiametroExteriorDiametroPulgada[i]

		

		mayor=0.55154
		for elemento in diametroInteriorLista:
			if elemento>diametroInterconexion and elemento<mayor:
				mayor=elemento


		diametroInterno = mayor
		diametroExterno = diametroInteriorListaExteriorPulgadaDic[mayor][0]

	
		CFloculadorWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		CFloculadorWindow.iconbitmap(bitmap=path)
		CFloculadorWindow.geometry("600x590") 
		CFloculadorWindow.resizable(0,0)	
		CFloculadorWindow.configure(background="#9DC4AA")

		#Frame Treeview
		arbolCFloculador_frame = LabelFrame(CFloculadorWindow, text="Visualizaci??n de los c??lculos para floculador alabama", font=("Yu Gothic bold", 11))
		arbolCFloculador_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolCFloculador_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		# sedScrollY=Scrollbar(arbolCFloculador_frame,orient=VERTICAL)
		# sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolCFloculador= ttk.Treeview(arbolCFloculador_frame,selectmode=BROWSE, height=11,show="tree headings")#,xscrollcommand=sedScrollX.set,yscrollcommand=sedScrollY.set)
		arbolCFloculador.pack(side=TOP, fill=BOTH, expand=TRUE)

		# sedScrollX.configure(command=arbolCFloculador.xview)
		# sedScrollY.configure(command=arbolCFloculador.yview)
		#Define columnas.
		arbolCFloculador["columns"]= (
		"1","Valores","Unidades","Adicional"
		)

		#Headings
		arbolCFloculador.heading("#0",text="ID", anchor=CENTER)

		for col in arbolCFloculador["columns"]:
			arbolCFloculador.heading(col, text=col,anchor=CENTER)

		
		
		arbolCFloculador.column("#0",width=0, stretch=False)
		arbolCFloculador.column("#1",width=200, stretch=False)
		arbolCFloculador.column("#2",width=100, stretch=False)
		arbolCFloculador.column("#3",width=100, stretch=False)
		arbolCFloculador.column("#4",width=200, stretch=False)
		#Striped row tags
		arbolCFloculador.tag_configure("evenrow", background= "#1FCCDB")
		arbolCFloculador.tag_configure("oddrow", background= "#9DC4AA")
		contadorFloculador=0
		
		listaEntrada= list()
		
		

		valorTemperaturas=list()
		viscosidadCinematicaDic=dict()
		for i in range(0,36):    
			valorTemperaturas.append(i)
						
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		for ind in range(0,len(valorTemperaturas)):
			viscosidadCinematicaDic[valorTemperaturas[ind]]=valorViscocidad[ind]
		densidadDic=dict()

		valorDensidad=[999.82, 999.89, 999.94, 999.98, 1000.0, 1000.0, 999.99, 
		999.96, 999.91, 999.85, 999.77, 999.68, 999.58, 999.46, 
		999.33, 999.19, 999.03, 998.86, 998.68, 998.49, 998.29, 
		998.08, 997.86, 997.62, 997.38, 997.13, 996.86, 996.59,
		996.31, 996.02, 995.71, 995.41, 995.09, 994.76, 994.43, 
		994.08]

		for ind in range(0,len(valorTemperaturas)):
			densidadDic[valorTemperaturas[ind]]=valorDensidad[ind]

		viscosidadDinamicaDic=dict()
		viscosidadDinamicaValor = [0.001792, 0.001731, 
		0.001673, 0.001619, 0.001567, 0.001519, 0.001473, 
		0.001428, 0.001386, 0.001346, 0.001308, 0.001271, 
		0.001236, 0.001203, 0.001171, 0.00114, 0.001111, 
		0.001083, 0.001056, 0.00103, 0.001005, 0.000981, 
		0.000958, 0.000936, 0.000914, 0.000894, 0.000874,
		0.000855, 0.000836, 0.000818, 0.000801, 0.000784,
		0.000768, 0.000752, 0.000737, 0.000723]

		for ind in range(0,len(valorTemperaturas)):
			viscosidadDinamicaDic[valorTemperaturas[ind]]=viscosidadDinamicaValor[ind]
		

		caudalDise??oEnM = caudalDise??o/1000.0
		areaTuberia = pi*(diametroInterno**2)*(1/4.0)
		areaOrificio = pi*(diametroExterno**2)*(1/4.0)
		tiempoFloculacionS= tiempoFloculacion*60.0
		tiempoDetencionCamara= tiempoFloculacionS/numeroCamaras
		viscosidadCinematica = viscosidadCinematicaDic[temperatura]
		densidad=densidadDic[temperatura]
		viscosidadDinamica = viscosidadDinamicaDic[temperatura]



		volFloculador = ancho*longitud*altura*numeroCamaras		
		velFlujoCodos= caudalDise??oEnM/areaTuberia
		perdidadPasamuro = ((caudalDise??oEnM**2))/((2*gravedad)*(coeficienteDescarga**2)*(areaTuberia**2))
		perdidaCodo = 0.4*((velFlujoCodos**2)/(2*gravedad))
		perdidaOrificio= (caudalDise??oEnM**2)/((2*gravedad)*(coeficienteDescargaOrificios**2)*(areaOrificio**2))
		perdidaTotalFloculador= perdidadPasamuro+perdidaCodo+ perdidaOrificio

		perdidadCargaenCamaras= perdidaTotalFloculador*numeroCamaras
		gradienteMezcla= sqrt((gravedad*perdidaTotalFloculador)/(tiempoDetencionCamara*viscosidadCinematica))
		numeroCamp= gradienteMezcla*tiempoDetencionCamara
		pendiente= perdidaTotalFloculador/longitud
		numeroReynolds= densidad*diametroInterno*velFlujoCodos*(1/viscosidadDinamica)
		estabilidadFloculo = (gradienteMezcla/(sqrt(numeroReynolds)))
		
		
		listaValores=[volFloculador,numeroCamaras,velFlujoCodos,perdidadPasamuro,perdidaCodo,perdidaOrificio,
		perdidaTotalFloculador,perdidadCargaenCamaras,gradienteMezcla,numeroCamp,pendiente, numeroReynolds,estabilidadFloculo]
		for valor in listaValores:
			listaEntrada.append(round(valor,3))

		listaEncabezados = [
		"V = Volumen floculador",
		"#c = N??mero de c??maras",
		"{} = Velocidad de flujo entre codos".format(getSub("v")),
		"H\' = P??rdida Pasamuro",
		"H\'\' = Perdida Codo",
		"H\'\'\' = Perdidas Orificio",
		"H = Perdida total floculador",
		f"Pc = Perdidas de carga en las\n {numeroCamaras} c??maras",
		"G = Gradiente de mezcla",
		"Gt = Numero de camp",
		"P = Pendiente",
		"N??mero de Reynolds",
		"S = Estabilidad del floculo"
		]
		listaUnidades = ["m^3",
				"unid",
				"m/s",
				"m",
				"m",
				"m",
				"m",
				"m",
				"s^(-1)",
				"",
				"%",
				"",
				""
				]

		if velFlujoCodos>=0.25 and velFlujoCodos<=0.65:
			cumpleVelocidadFlujoCodos="El valor de la velocidad de flujo\nentre codos cumple."
		else:
			cumpleVelocidadFlujoCodos = "El valor de la velocidad de flujo\nentre codos NO cumple.."
		if gradienteMezcla>=35 and gradienteMezcla<=55:
			cumpleGradienteMezcla= "El valor del gradiente\nde mezcla cumple."
		else:
			cumpleGradienteMezcla="Cuidado, el valor del gradiente\nde mezcla NO cumple."
		if  estabilidadFloculo<0.3:
			cumpleEstabilidadFloculo= "Cumple"
		else:
			cumpleEstabilidadFloculo= "No cumple"
		listaAdicional =[
		"",
		"",
		f"{cumpleVelocidadFlujoCodos}",
		"",
		"",
		"",
		"",
		"", 
		f"{cumpleGradienteMezcla}",
		"",
		"",
		"",
		f"{cumpleEstabilidadFloculo}"
		]



		for i in range(0, len(listaEncabezados)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaEntrada[i])
			listaTemp.append(listaUnidades[i])
			listaTemp.append(listaAdicional[i])
			newDataTreeview(arbolCFloculador,listaTemp)

		PasarExcelDatos(".\\ResultadosFloculador\\CalculosAdicionalesParaDise??oFloculador.xlsx",'Resultados',listaEncabezados,50, listaEntrada, 15, listaUnidades, 15,True,listaAdicional, 50)
			
		CFloculadorWindow.mainloop()


	def salidaCamara(listaEntry, numCamaras, valorParImpar):
		
		listaE2=list()

		labels=["caudal de dise??o", "ancho",
		"longitud", "altura", "gravedad"]
		labelsComboBox= ["tiempo de floculaci??n", "temperatura"]
		
		listaSinComboBox=[listaEntry[0],listaEntry[2],listaEntry[3],
		listaEntry[4],listaEntry[5]]
		
		listaComboBox=[listaEntry[1],listaEntry[6]]

		# listaEntryNueva= [0= caudalDise??o,1=tiempoFloculacion,
		# 		2=ancho,3=longitud,4=altura,5=gravedad,6=temperatura,]
		
		# listaEntry= [0= caudalDise??o,1=tiempoFloculacion,2=diametroInterno,
		# 3=diametroExterno,
		# 4=ancho,5=longitud,6=altura,7=gravedad,8=temperatura,
		# 9=coeficienteDescarga,10=coeficienteDescargaOrificios]
		
		for i in range(0, len(listaComboBox)):
			if listaComboBox[i].get() == "Seleccione":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labelsComboBox[i]} ")	
				return None
		for i in range(0, len(listaSinComboBox)):
			if listaSinComboBox[i].get() == "":
				messagebox.showwarning(title="Error", message=f"Hace falta ingresar el valor del/de la {labels[i]} ")	
				return None
		j=0
		for elemento in listaSinComboBox:
			try:
				listaE2.append(float(elemento.get()))
				j=j+1
			except:	
				messagebox.showwarning(title="Error", message=f"El/la {labels[j]} debe ser un n??mero")
				return None
		
			# listaEntryNueva= [0= caudalDise??o,1=tiempoFloculacion,
		# 		2=ancho,3=longitud,4=altura,5=gravedad,6=temperatura,]
		
		#[caudal, ancho,longitud, altura, gravedad]
		caudalDise??o= listaE2[0]
	
		ancho = listaE2[1]
		longitud = listaE2[2]
		altura = listaE2[3]
		gravedad = listaE2[4]
		coeficienteDescarga = 0.76
		coeficienteDescargaOrificios = 0.80
		tiempoFloculacion= float(listaComboBox[0].get())
		temperatura= float(listaComboBox[1].get())


		if caudalDise??o<10 or caudalDise??o>100:
			messagebox.showwarning(title="Error", message=f"El valor del caudal de Dise??o debe estar entre 10 y 100")
			return None	
		numeroCamaras= float(numCamaras.get())

		if caudalDise??o<15:
			diametroInterconexion=0.15
		elif caudalDise??o<25:
			diametroInterconexion=0.25
		elif caudalDise??o<35:
			diametroInterconexion=0.30
		elif caudalDise??o<55:
			diametroInterconexion=0.35
		elif caudalDise??o<65:
			diametroInterconexion=0.40
		elif caudalDise??o<85:
			diametroInterconexion=0.45
		elif caudalDise??o<101:
			diametroInterconexion=0.50

		diametroInteriorLista=[
		0.05458,
		0.06607,
		0.08042,
		0.10342,
		0.15222,
		0.19821,
		0.24709,
		0.29307,
		0.32176,
		0.36770,
		0.41366,
		0.45964,
		0.55154,
		]
		diametroPulgadaLista=[
		2.0,
		2.5,
		3.0,
		4.0,
		6.0,
		8.0,
		10.0,
		12.0,
		14.0,
		16.0,
		18.0,
		20.0,
		24.0,
		]
		diametroExteriorLista=[
		0.06032,
		0.07303,
		0.08890,
		0.11430,
		0.16828,
		0.21908,
		0.27305,
		0.32305,
		0.35560,
		0.40640,
		0.45720,
		0.50800,
		0.60960,

		]
		ListaTuplasDiametroExteriorDiametroPulgada=list()

		for i in range(0,len(diametroExteriorLista)):
			ListaTuplasDiametroExteriorDiametroPulgada.append((diametroExteriorLista[i],diametroPulgadaLista[i]))

		diametroInteriorListaExteriorPulgadaDic=dict()
		for i in range(0, len(diametroInteriorLista)):
			diametroInteriorListaExteriorPulgadaDic[diametroInteriorLista[i]]=ListaTuplasDiametroExteriorDiametroPulgada[i]

		

		mayor=0.55154
		for elemento in diametroInteriorLista:
			if elemento>diametroInterconexion and elemento<mayor:
				mayor=elemento

		if valorParImpar=="par":
			diametroInternoOrificio = mayor
		else:
			if mayor != 0.55154: 
				diametroInternoOrificio = diametroInteriorLista[(diametroInteriorLista.index(mayor))+1]
			else:
				diametroInternoOrificio = mayor
		



		
		salidaCamaraWindow = tk.Toplevel()
		path=resource_path('icons\\agua.ico')
		salidaCamaraWindow.iconbitmap(bitmap=path)
		salidaCamaraWindow.geometry("520x450") 
		salidaCamaraWindow.resizable(0,0)	
		salidaCamaraWindow.configure(background="#9DC4AA")

		#Frame Treeview
		arbolSalidaCamara_frame = LabelFrame(salidaCamaraWindow, text=f"Datos de salida para c??mara {valorParImpar}", font=("Yu Gothic bold", 11))
		arbolSalidaCamara_frame.pack(side=LEFT,fill=BOTH,expand=TRUE)

		#Scrollbar
		# sedScrollX=Scrollbar(arbolSalidaCamara_frame,orient=HORIZONTAL)
		# sedScrollX.pack(side=BOTTOM, fill=X)
		sedScrollY=Scrollbar(arbolSalidaCamara_frame,orient=VERTICAL)
		sedScrollY.pack(side=LEFT, fill=Y)

		#Treeview
		arbolSalidaCamara= ttk.Treeview(arbolSalidaCamara_frame,selectmode=BROWSE, height=11,show="tree headings",yscrollcommand=sedScrollY.set) #xscrollcommand=sedScrollX.set
		arbolSalidaCamara.pack(side=TOP, fill=BOTH, expand=TRUE)

		#sedScrollX.configure(command=arbolSalidaCamara.xview)
		sedScrollY.configure(command=arbolSalidaCamara.yview)
		#Define columnas.
		arbolSalidaCamara["columns"]= (
		"1","Valores","Unidades")

	

		#Headings
		arbolSalidaCamara.heading("#0",text="ID", anchor=CENTER)

		for col in arbolSalidaCamara["columns"]:
			arbolSalidaCamara.heading(col, text=col,anchor=CENTER)

		arbolSalidaCamara.column("#0",width=0, stretch=False)
		arbolSalidaCamara.column("#1",width=300, stretch=False)
		arbolSalidaCamara.column("#2",width=100, stretch=False)
		arbolSalidaCamara.column("#3",width=100, stretch=False)

		#Striped row tags
		arbolSalidaCamara.tag_configure("oddrow", background= "#1FCCDB")
		arbolSalidaCamara.tag_configure("evenrow", background= "#9DC4AA")
		contadorFloculador=0
		listaEntrada=list()
		valorTemperaturas=list()
		viscosidadCinematicaDic=dict()
		for i in range(0,36):    
			valorTemperaturas.append(i)
						
		valorViscocidad=[1.792e-06, 1.731e-06, 1.673e-06, 1.619e-06, 1.567e-06, 1.519e-06, 1.473e-06, 0.000001428
		,1.386e-06, 1.346e-06, 1.308e-06, 1.271e-06, 1.237e-06, 1.204e-06, 
		1.172e-06, 1.141e-06, 1.112e-06, 1.084e-06, 1.057e-06, 1.032e-06, 1.007e-06, 9.83e-07, 9.6e-07, 9.38e-07, 9.17e-07, 8.96e-07, 8.76e-07, 8.57e-07, 8.39e-07, 8.21e-07, 8.04e-07, 7.88e-07, 7.72e-07, 7.56e-07, 7.41e-07, 7.27e-07]

		for ind in range(0,len(valorTemperaturas)):
			viscosidadCinematicaDic[valorTemperaturas[ind]]=valorViscocidad[ind]
		

		
		


		diametroInternoOrificioC = diametroInternoOrificio

		if valorParImpar=="impar":
			diametroInternoOrificio = mayor

		caudalDise??oEnM = caudalDise??o/1000.0
		areaTuberia = pi*(diametroInternoOrificio**2)*(1/4.0)
		tiempoFloculacionS= tiempoFloculacion*60.0
		tiempoDetencionCamara= tiempoFloculacionS/numeroCamaras
		viscosidadCinematica = viscosidadCinematicaDic[temperatura]
		velocidadFlujoEntreCodos = caudalDise??oEnM/areaTuberia


		areaOrificio= pi*(diametroInternoOrificioC**2)*(1/4.0)
		coeficienteDescarga = coeficienteDescargaOrificios
		
		perdidaPasamuros= (caudalDise??oEnM**2)/((2*gravedad)*(coeficienteDescarga**2)*(areaTuberia**2))
		perdidaCodo = (0.4)*((velocidadFlujoEntreCodos**2)/(2*gravedad))
		perdidaOrificio= (caudalDise??oEnM**2)/((2*gravedad)*(coeficienteDescargaOrificios**2)*(areaOrificio**2))
	
		
		perdidaTotalFloculador = perdidaPasamuros + perdidaCodo+ perdidaOrificio
		
		
		gradienteMezcla = sqrt((gravedad*perdidaTotalFloculador)/(viscosidadCinematica*tiempoDetencionCamara))
		
		numeroCamp= gradienteMezcla*tiempoDetencionCamara
		pendiente=perdidaTotalFloculador/longitud
		
		
		listaValores=[diametroInternoOrificioC, areaOrificio, coeficienteDescarga,
		perdidaPasamuros,perdidaCodo, perdidaOrificio, perdidaTotalFloculador,
		gradienteMezcla,numeroCamp,pendiente]

		for valores in listaValores:
			listaEntrada.append(round(valores,3))

		listaEncabezados=[
		"Di = Diametro de interno Orificio",
		"A= ??rea del orificio",
		"Cd = Coeficiente de descarga",
		"H\' = P??rdida Pasamuro",
		"H\'\' = Perdida Codo",
		"H\'\'\' = Perdidas Orificio",
		"H = Perdida total floculador",
		"G = Gradiente de mezcla",
		"Gt = Numero de camp",
		"P = Pendiente"			
		]
		listaUnidades=["m",
		"m^2",
		"",
		"m",
		"m",
		"m",
		"m",
		"s^(-1)",
		"",
		"%"			]

		for i in range(0, len(listaEntrada)):
			listaTemp=list()
			listaTemp.append(listaEncabezados[i])
			listaTemp.append(listaEntrada[i])
			listaTemp.append(listaUnidades[i])
			newDataTreeview(arbolSalidaCamara,listaTemp)
		
		if gradienteMezcla>=35 and gradienteMezcla<=55:
			messagebox.showinfo(title="Informaci??n", message="El valor del gradiente de mezcla cumple. Se encuentra entre 35 y 55.")
		else:
			messagebox.showwarning(title="??Cuidado!", message="El valor del gradiente de mezcla NO cumple. No se encuentra entre 35 y 55.")
		
		PasarExcelDatos(f".\\ResultadosFloculador\\datosSalidaCamara{valorParImpar}.xlsx",'Resultados',listaEncabezados,50, listaEntrada, 15, listaUnidades, 15,False,[], 50)

		salidaCamaraWindow.mainloop()
	

	mainWindow.withdraw()
	floculadorWindow = tk.Toplevel()
	floculadorWindow.protocol("WM_DELETE_WINDOW", on_closing)
	path=resource_path('icons\\agua.ico')
	floculadorWindow.iconbitmap(bitmap=path)
	floculadorWindow.geometry("1000x600") 
	floculadorWindow.resizable(0,0)	
	floculadorWindow.configure(background="#9DC4AA")


	frameFloculador= LabelFrame(floculadorWindow, text="Dise??o Floculador Alabama", font=("Yu Gothic bold", 11))
	frameFloculador.pack(side=LEFT,fill=BOTH,expand=TRUE)

	
	pathAtras= resource_path('images\\atras.png')
	imageAtras= PhotoImage(file=pathAtras)
	
	



	#BotonesFloculador

	botonAtrasFlo= HoverButton(frameFloculador, image=imageAtras , width=100, height=40, bg= None, command=lambda: returnMainWindow(floculadorWindow))
	botonAtrasFlo.place(x=0,y=10)

	botonNewEntryFloculador = HoverButton(frameFloculador, text="Limpiar entradas", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: newEntryFloculador(listaEntry))
	botonVerCalculos = HoverButton(frameFloculador, text="C??lculos adicionales para dise??o del floculador", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT, command= lambda: calculosFloculador(listaEntry, numeroCamaras))
	botonDatosSalidaCamaraPar = HoverButton(frameFloculador, text="Datos de salida C??mara No. (par)", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: salidaCamara(listaEntry,numeroCamaras,"par"))
	botonDatosSalidaCamaraImpar = HoverButton(frameFloculador, text="Datos de salida C??mara No. (impar)", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: salidaCamara(listaEntry,numeroCamaras, "impar"))
	botonDatosIniciales= HoverButton(frameFloculador, text="Ver datos iniciales", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: datosIniciales(listaEntry, numeroCamaras))
	botonAyudaVisual= HoverButton(frameFloculador, text="Ayuda visual - geometr??a Floculador Alabama", activebackground="#9DC4AA", anchor=CENTER , width=60, height=2, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: proyectarImg('images\\VistaFloculador.png',708,622))
	
	botonGuiaDise??oCaudalDiametroInterconexion = HoverButton(frameFloculador, text="Gu??a de dise??o para\nfloculadores tipo Alabama", activebackground="#9DC4AA", anchor=CENTER , width=35, height=4, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: proyectarImg('images\\Floc_GuiaDiseno.png',455,332))
	botonEspecificacionesTecnicasTuberiasPVC= HoverButton(frameFloculador, text="Especificaciones t??cnicas\ntuber??as PVC tipo 1 RDE21", activebackground="#9DC4AA", anchor=CENTER , width=35, height=4, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: proyectarImg('images\\Floc_GuiaPVC.png',546,315))
	botonCriteriosFloculadorTipoAlabama= HoverButton(frameFloculador, text="Criterios de dise??o de\nfloculador tipo Alabama", activebackground="#9DC4AA", anchor=CENTER , width=35, height=4, bg= "#09C5CE", font =("Courier",9),justify=LEFT,command= lambda: proyectarImg('images\\Floc_Criterios.png',559,307))
	
	listaBotones2 = [botonGuiaDise??oCaudalDiametroInterconexion,
	botonEspecificacionesTecnicasTuberiasPVC,
	botonCriteriosFloculadorTipoAlabama]
	listaBotones=[botonNewEntryFloculador, botonDatosIniciales,botonVerCalculos,botonDatosSalidaCamaraPar,botonDatosSalidaCamaraImpar, botonAyudaVisual]


	datosEntradaLabel = Label(frameFloculador, text="Datos iniciales: ",font=("Yu Gothic bold",10))
	caudalDise??oLabel = Label(frameFloculador, text="QMD = Caudal de dise??o [10 (L/s) - 100(L/s)]:",font=("Yu Gothic bold",10))
	tiempoFloculacionLabel = Label(frameFloculador, text="T = Tiempo de floculaci??n [min]:",font=("Yu Gothic bold",10))
	anchoLabel = Label(frameFloculador, text="W = Ancho [m]:",font=("Yu Gothic bold",10))
	longitudLabel = Label(frameFloculador, text="L = Longitud [m]:",font=("Yu Gothic bold",10))
	alturaLabel = Label(frameFloculador, text="a = Altura [m]:",font=("Yu Gothic bold",10))
	gravedadLabel = Label(frameFloculador, text="g = Gravedad [m/(s^2)]",font=("Yu Gothic bold",10))
	temperaturaLabel = Label(frameFloculador, text="??C = Temperatura [??C]:",font=("Yu Gothic bold",10))
	
	
	
	listaLabel = [datosEntradaLabel,caudalDise??oLabel,tiempoFloculacionLabel,
				anchoLabel , longitudLabel,alturaLabel,gravedadLabel,temperaturaLabel,]

	caudalDise??o = Entry(frameFloculador)
	caudalDise??o.focus()
	
	listaValoresTemperaturaFloculacion=list()
	for i in range(20,41):
		listaValoresTemperaturaFloculacion.append(f"{i}")
	tiempoFloculacion = ttk.Combobox(frameFloculador, width="18", state="readonly",values=listaValoresTemperaturaFloculacion)
	tiempoFloculacion.set("Seleccione")

	ancho = Entry(frameFloculador)
	longitud = Entry(frameFloculador)
	altura = Entry(frameFloculador)
	gravedad = Entry(frameFloculador)
	gravedad.insert(0,9.81)

	listaValoresTemperatura=list()
	for i in range(0,36):
		listaValoresTemperatura.append(f"{i}")
	temperatura = ttk.Combobox(frameFloculador, width="18", state="readonly",values=listaValoresTemperatura)
	temperatura.set("Seleccione")


	

	listaEntry= [caudalDise??o,tiempoFloculacion,
				ancho,longitud,altura,gravedad,temperatura,]
	
	entryDiametroInternoAdicional= Entry(frameFloculador)
	entryDiametroInternoAdicional.insert(0,"0.46")
	numeroCamaras= Entry(frameFloculador)
	numeroCamaras.insert(0,"12")

	
	# listaLabel = [datosEntradaLabel,caudalDise??oLabel,tiempoFloculacionLabel,
	# 			anchoLabel , longitudLabel,alturaLabel,gravedadLabel,temperaturaLabel,]
	# listaEntry= [caudalDise??o,tiempoFloculacion,
	# 			ancho,longitud,altura,gravedad,temperatura,]
	
	control=0
	alturaInicial=70
	alturaInicial2=113
	for elemento in listaLabel:
		if control<5:
			elemento.place(x=20,y=alturaInicial)
			alturaInicial+=43
		else:
			elemento.place(x=550,y=alturaInicial2)
			alturaInicial2+=43
		control=control+1
	control=0
	alturaInicial=113
	alturaInicial2=113
	for elemento in listaEntry:
		if control<4:
			elemento.place(x=330,y=alturaInicial)
			alturaInicial+=43
		else:
			elemento.place(x=770,y=alturaInicial2)
			alturaInicial2+=43
		control=control+1
	xInicial=20
	xInicial2=20
	control=0
	alturaInicial2+=43
	alturaInicial3=alturaInicial2

	for elemento in listaBotones:
		if control<3:
			elemento.place(x=xInicial ,y=alturaInicial2+43)
			alturaInicial2+=43
		else:
			elemento.place(x=xInicial2+500 ,y=alturaInicial3+43)
			alturaInicial3+=43
		control+=1
	alturaInicial3+=55
	for elemento in listaBotones2:
		elemento.place(x=xInicial,y=alturaInicial3)
		xInicial+=350
		


	#BorrarFLoc

	# listaEntry= [caudalDise??o,tiempoFloculacion,
	# 			ancho,longitud,altura,gravedad,temperatura,]
	# listaValores=[30.00,27.00,1.30,1.60,2.75,9.81,20.00]
	# for i in range(0, len(listaValores)):	
	# 	if i == 5:
	# 		pass
	# 	elif i == 1:
	# 		listaEntry[i].set(27)
	# 	elif i==6:
	# 		listaEntry[i].set(20)
	# 	else:
	# 		listaEntry[i].insert(0, listaValores[i])

	floculadorWindow.mainloop()



mainWindow = Tk()
mainWindow.title("FlocSedFil")
path=resource_path('icons\\agua.ico')
mainWindow.iconbitmap(bitmap= path)
path=resource_path('icons\\agua.ico')
#mainWindow.iconbitmap(bitmap=path)
mainWindow.geometry("370x350")
#Anchoxalto
mainWindow.resizable(0,0)


frame = LabelFrame(mainWindow, text="P??gina principal")
frame.grid(row=0, column=0)

pathFondo= resource_path("images\\fondo31.png")
bg= PhotoImage(file=pathFondo)


my_canvas = Canvas(frame, width=370, height=350)
my_canvas.grid(row=0,column=0)
my_canvas.create_image(0,0, image=bg, anchor="nw")


#Label
my_canvas.create_text(175,20, text= "Seleccione una de las siguientes opciones:", font=("Courier",10), fill="white")

#Buttons

boton_sed= HoverButton(frame, text="Sedimentador alta tasa", activebackground="#9DC4AA", justify=CENTER, width=50, height=2, bg= "#09C5CE", font =("Courier",9), command= openSedWindow)
boton_sed_window = my_canvas.create_window(5,160, anchor= "nw", window=boton_sed)

boton_filtro= HoverButton(frame, text="Filtro r??pido", activebackground="#9DC4AA", justify=CENTER, width=50, height=2, bg= "#09C5CE", font =("Courier",9), command=openFiltroWindow)
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




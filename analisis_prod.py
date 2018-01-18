# -*- coding: utf-8 -*-
#comentario
import sys
import pandas as pd
import numpy as np
from PyQt5 import QtCore, QtWidgets
import datetime

class Ui_FormFecha(object):
    #Funcion para desarrollar la interfaz de usuario
    
    def __init__(self):
        widgetfecha = QtWidgets.QWidget()
        widgetfecha.setObjectName("widgetfecha")
        widgetfecha.resize(650, 345)

    def setupUi(self, widgetfecha):
        #Calendario1
        self.calWidg1 = QtWidgets.QCalendarWidget(widgetfecha)
        self.calWidg1.setGeometry(QtCore.QRect(10, 10, 310, 183))
        self.calWidg1.showToday()
        self.calWidg1.setObjectName("calWidg1")
            
        #Calendario2
        self.calWidg2 = QtWidgets.QCalendarWidget(widgetfecha)
        self.calWidg2.setGeometry(QtCore.QRect(350, 10, 310, 183))
        self.calWidg2.showToday()
        self.calWidg2.setObjectName("calWidg2")
        
        self.pBtnAceptar = QtWidgets.QPushButton(widgetfecha)
        self.pBtnAceptar.setGeometry(QtCore.QRect(350, 258, 151, 21))
        self.pBtnAceptar.setEnabled(False)
        self.pBtnAceptar.setAutoDefault(True)
        self.pBtnAceptar.setObjectName("pBtnAceptar")
            
        self.gBoxFecha = QtWidgets.QGroupBox(widgetfecha)
        self.gBoxFecha.setGeometry(QtCore.QRect(10, 200, 700, 30))
        self.gBoxFecha.setObjectName("gBoxFecha")
        self.label_fecha_inicial = QtWidgets.QLabel(self.gBoxFecha)
        self.label_fecha_inicial.setObjectName("label_fecha_inicial")
        self.label_fecha_inicial.setGeometry(QtCore.QRect(10,0,70,32))
            
        self.label_fecha_final = QtWidgets.QLabel(self.gBoxFecha)
        self.label_fecha_final.setObjectName("label_fecha_final")
        self.label_fecha_final.setGeometry(QtCore.QRect(350,0,70,32))

        self.retranslateUi(widgetfecha)
        self.calWidg1.selectionChanged.connect(self.fecha_inicial)
        self.calWidg2.selectionChanged.connect(self.fecha_final)
        self.pBtnAceptar.clicked.connect(self.rango_fechas)
     
        #Funcion para traducir los textos
    def retranslateUi(self, widgetfecha):       
        _translate = QtCore.QCoreApplication.translate
        self.label_fecha_inicial.setText(_translate("widgetfecha", "fecha Inicio"))
        self.label_fecha_final.setText(_translate("widgetfecha", "fecha Fin"))
        self.pBtnAceptar.setText(_translate("widgetfecha", "Aceptar"))
    
    
        # Guarda el dia, mes y año en diferentes variables            
    def fecha_inicial(self):
        dia = self.calWidg1.selectedDate().day()
        mes = self.calWidg1.selectedDate().month()
        año = self.calWidg1.selectedDate().year()
        self.fecha1 = datetime.date(año,mes,dia)
        fecha_str = str(dia)+'/'+str(mes)+'/'+str(año)
        self.label_fecha_inicial.setText(fecha_str)
        return self.fecha1

    def fecha_final(self):
        dia = self.calWidg2.selectedDate().day()
        mes = self.calWidg2.selectedDate().month()
        año = self.calWidg2.selectedDate().year()
        self.fecha2 = datetime.date(año,mes,dia)
            
        fecha2_str = str(dia)+'/'+str(mes)+'/'+str(año)
        self.label_fecha_final.setText(fecha2_str)
        self.pBtnAceptar.setEnabled(True)

    def rango_fechas (self):
        widgetfecha.close()
        print(self.fecha1)
        print(self.fecha2)
        data = datos(self.fecha1,self.fecha2)
        datos_prod = datos.read_data_prod(self.fecha1, self.fecha2)
        return datos_prod
        

class datos():
    def __init__(self,fecha1,fecha2):
        print(fecha1, fecha2)
        datos_prod = self.datos.read_data_prod()
        print(datos_prod)
    
    def read_data_prod(self):# función donde se lee el archivo principal CSV

        prod = pd.read_csv('datos_produccion.csv', index_col = 0, encoding = 'utf-8')
        prod.apply(lambda x: pd.api.types.infer_dtype(x.values))
        print('DataFrame Completo')
        print(prod)
        
        return prod
        

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    widgetfecha = QtWidgets.QWidget()
    ui = Ui_FormFecha()
    ui.setupUi(widgetfecha)
    widgetfecha.show()
    sys.exit(app.exec_())
    
    
    

    
    
    
    
    

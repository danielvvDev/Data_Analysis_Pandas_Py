# -*- coding: utf-8 -*-

import sys
import pandas as pd
import numpy as np

def read_data_prod():
    prod = pd.read_csv('datos_produccion.csv', index_col = 0, encoding = 'utf-8')
    prod.apply(lambda x: pd.api.types.infer_dtype(x.values))
    return prod

if __name__ == "__main__":
    leer = read_data_prod() # Lee los datos del archivo datos_produccion.csv y los guarda en la variable leer
    
    #crea el DataFrame con los campos seleccionados del archivo CSV
    lista1 = leer[['indice_planta', 'fecha','linea','turno', 'producto1', 'cajas_prod1', 'lbs_prod1', 'resto1', 'vel_producto1', 'tprod1']]
    
    #Cambia el nombre a las columnas para hacer mÃ¡s entendible el DataFrame
    lista1 = lista1.rename(columns = {'indice_planta':'planta','producto1':'producto', 'cajas_prod1': 'cajas','lbs_prod1': 'lbs', 'vel_producto1': 'velocidad', 'tprod1': 'tipo', 'resto1':'resto' })
    lista1[['cajas','velocidad','lbs']] = lista1[['cajas','velocidad','lbs']].apply(pd.to_numeric)
    
    #imprime el dataFrame para verificar que se importo correctamente
    print('lista 1',lista1)
    print('datos concatenados')
    input()
    lista2 = leer[['indice_planta', 'fecha','linea','turno', 'producto2', 'cajas_prod2', 'lbs_prod2', 'resto2', 'vel_producto2', 'tprod2']]
    lista2 = lista2.rename(columns = {'indice_planta':'planta','producto2':'producto', 'cajas_prod2': 'cajas','lbs_prod2': 'lbs', 'vel_producto2': 'velocidad', 'tprod2': 'tipo', 'resto2':'resto' })
    lista3 = leer[['indice_planta', 'fecha','linea','turno', 'producto3', 'cajas_prod3', 'lbs_prod3', 'resto3', 'vel_producto3', 'tprod3']]
    lista3 = lista3.rename(columns = {'indice_planta':'planta','producto3':'producto', 'cajas_prod3': 'cajas','lbs_prod3': 'lbs', 'vel_producto3': 'velocidad', 'tprod3': 'tipo', 'resto3':'resto' })
    lista4 = leer[['indice_planta', 'fecha','linea','turno', 'producto4', 'cajas_prod4', 'lbs_prod4', 'resto4', 'vel_producto4', 'tprod4']]
    lista4 = lista4.rename(columns = {'indice_planta':'planta','producto4':'producto', 'cajas_prod4': 'cajas','lbs_prod4': 'lbs', 'vel_producto4': 'velocidad', 'tprod4': 'tipo', 'resto4':'resto' })
    lista5 = leer[['indice_planta', 'fecha','linea','turno', 'producto5', 'cajas_prod5', 'lbs_prod5', 'resto5', 'vel_producto5', 'tprod5']]
    lista5 = lista5.rename(columns = {'indice_planta':'planta','producto5':'producto', 'cajas_prod5': 'cajas','lbs_prod5': 'lbs', 'vel_producto5': 'velocidad', 'tprod5': 'tipo', 'resto5':'resto' })
    lista6 = leer[['indice_planta', 'fecha','linea','turno', 'producto6', 'cajas_prod6', 'lbs_prod6', 'resto6', 'vel_producto6', 'tprod6']]
    lista6 = lista6.rename(columns = {'indice_planta':'planta','producto6':'producto', 'cajas_prod6': 'cajas','lbs_prod6': 'lbs', 'vel_producto6': 'velocidad', 'tprod6': 'tipo', 'resto6':'resto' })
    lista7 = leer[['indice_planta', 'fecha','linea','turno', 'producto7', 'cajas_prod7', 'lbs_prod7', 'resto7', 'vel_producto7', 'tprod7']]
    lista7 = lista7.rename(columns = {'indice_planta':'planta','producto7':'producto', 'cajas_prod7': 'cajas','lbs_prod7': 'lbs', 'vel_producto7': 'velocidad', 'tprod7': 'tipo', 'resto7':'resto' })
    lista8 = leer[['indice_planta', 'fecha','linea','turno', 'producto8', 'cajas_prod8', 'lbs_prod8', 'resto8', 'vel_producto8', 'tprod8']]
    lista8 = lista8.rename(columns = {'indice_planta':'planta','producto8':'producto', 'cajas_prod8': 'cajas','lbs_prod8': 'lbs', 'vel_producto8': 'velocidad', 'tprod8': 'tipo', 'resto8':'resto' })
    lista_nueva = pd.concat([lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8])
    lista_nueva = lista_nueva[(lista_nueva['producto']!='SELECCIONE UN PRODUCTO')] # se eliminan los renglones que no tienen datos
    lista_produccion_procesos = lista_nueva[(lista_nueva['tipo']=='PROCESO')] # se genera una lista con los datos de productos en proceso
    lista_produccion_terminado = lista_nueva[(lista_nueva['tipo']=='TERMINADO')] # se genera una lista con los datos de producto terminado
    #lista_produccion_terminado['velocidad'].astype(np.float64) # Se cambia el tipo de datos a float64 en la columna velocidad de la tabla de producto terminado
    print('se mostrara la lista de prod terminado filtrando la velocidad')
    input()
    print( lista_produccion_terminado)
    print('se muestra la tabla de producto terminado')
    input()
    


    groups_means = lista_produccion_terminado.reset_index().groupby(["planta","linea","producto"])['velocidad'].transform('mean')
    print('se muestran las medias')
    input()
    print(groups_means)
    print('se genera las medias de la velocidad de los diferentes productos')
    input()
    
    
    lista_produccion_terminado.loc[(lista_produccion_terminado['velocidad'].isnull()),'velocidad']= groups_means
    print('se mostrara la lista de terminados con las medias en la velocidad')
    print(lista_produccion_terminado)
    lista_produccion_terminado.lbs.astype(np.float64)
    lista_produccion_terminado.velocidad.astype(np.float64)
    
    prod_planta = lista_produccion_terminado.reset_index().groupby(['planta'])['lbs'].sum()
    print('produccion planta\n', prod_planta)
    input()
    prod_linea = lista_produccion_terminado.reset_index().groupby(['planta','linea'])['lbs'].sum()
    print('produccion producto \n',prod_linea )
    input()
    prod_producto = lista_produccion_terminado.reset_index().groupby(['planta','linea','producto'])['lbs'].sum()
    print('produccion producto \n',prod_producto )
    input()
    
    
    
    

    lista_nueva.to_csv('listra_produccion.csv', encoding = 'utf-8')
    lista_produccion_procesos.to_csv('listra_produccion_procesos.csv', encoding = 'utf-8')
    lista_produccion_terminado.to_csv('listra_produccion_terminados.csv', encoding = 'utf-8')
    groups_means.to_csv('medias.csv', encoding = 'utf-8')
    

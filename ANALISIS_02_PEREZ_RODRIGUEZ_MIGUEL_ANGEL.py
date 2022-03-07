from audioop import reverse
from funciones_auxiliares import promedio_ingresos, value_per_rute, value_per_transport, prozent_per_country
import pandas as pd
import numpy as np


df = pd.read_csv('synergy_logistics_database.csv') #leectura de archivo csv

just_exports = df[df['direction'] == 'Exports'] #Frame solo con exportaciones
just_imports = df[df['direction'] == 'Imports'] #Frame solo con importaciones

# Diccionarios de {ruta: #_viajes} de importacion y exportacion
import_demand = dict(just_imports[['origin', 'destination']].value_counts()) 
export_demand = dict(just_exports[['origin', 'destination']].value_counts()) 

##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- Para la opcion 1 -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Obtencion de lista con ruta e ingresos de ruta y total de la ruta 
nth_import, imp_income = value_per_rute(just_imports,import_demand,10)
nth_export, exp_income = value_per_rute(just_exports,export_demand,10)

# Se obtiene un ingreso y el promedio resultante de cada direccion de la base
imp_income, imp_prozent = promedio_ingresos(just_imports, imp_income)
exp_income, exp_prozent = promedio_ingresos(just_exports, exp_income)

print('\n\n Para la opcion 1 \n\n')
print('Operaciones de importacion: \n')
for a in nth_import:
    print('La ruta: {} - {} genera {} USD'.format(a[0][0],a[0][1],format(a[1], ',')))
print('Las 10 rutas mas demandadas generan {} USD, que es el {}%  de del total de operaciones'.format(imp_income, imp_prozent))
print('\n\n')

print('Operaciones de exportacion: \n')
for a in nth_export:
    print('La ruta: {} - {} genera {} USD'.format(a[0][0],a[0][1],format(a[1], ',')))
print('Las 10 rutas mas demandadas generan {} USD, que es el {}%  de del total de operaciones'.format(exp_income, exp_prozent))


##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- Para la opcion 2 -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
print('\n\n Para la opcion 2 \n\n')
#diccionarios del valor de transporte para un analisis totalitario, de importaciones y exportaciones
medios = dict(df['transport_mode'].value_counts())
imp_t_m = dict(just_imports['transport_mode'].value_counts())
exp_t_m = dict(just_exports['transport_mode'].value_counts())

TM_imports = value_per_rute(just_imports, imp_t_m)
TM_exports = value_per_rute(just_exports, exp_t_m)
TM_all = value_per_rute(df, medios)

value_per_transport(just_imports,TM_imports,'importaciones')
print('\n\n')
value_per_transport(just_exports,TM_exports,'exportaciones')
print('\n\n')
value_per_transport(df, TM_all,'operaciones totales')

##-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#- Para la opcion 3 -#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

medios1 = dict(df['origin'].value_counts())
orden = prozent_per_country(df, medios1)
control = 0
a = 0
print('\n\n Para la opcion 3 \n\n')
while control <= 80:
    
    print('{}, con {} operaciones, genera {} USD y representa el {}% del total de ingresos'.format(orden[a][1],orden[a][2], orden[a][3],orden[a][0]))
    control += orden[a][0]
    a += 1
    

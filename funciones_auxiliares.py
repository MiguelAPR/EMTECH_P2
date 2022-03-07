
def value_per_rute(frame, dic1, num = 0):
    ''' Crea una lista de coordenadas (ingresos, ruta)
    que dan el ingreso de la exisente ruta '''
    llave = list(dic1.keys())
    if num == 0:
        medio = [[a, frame[frame['transport_mode'] == a]['total_value'].sum()] for a in llave]
        return medio
    else:
        list_return = [[llave[a],frame[(frame['origin'] == llave[a][0]) & (frame['destination'] == llave[a][1])]['total_value'].sum()] for a in range(num)]
        ingresos = [a[1] for a in list_return]
        return list_return, ingresos

    

def value_per_transport(frame, list, string):
    medio, porciento = promedio_ingresos(frame, [a[1] for a in list])
    print('Para {}: \n\n'.format(string))
    for i in list:
        a, b = promedio_ingresos(frame, [i[1]])
        print('El medio {} genera {} USD, que es el {}% de las {}'.format(i[0], a, b, string))



def prozent_per_country(frame, dict):
    'Genera lista de [porciento_de_aporte, pais, operaciones, ingresos]'
    list_return = []
    for a,b in dict.items():

        country = frame[frame['origin'] == a]['total_value'].sum()

        money, prozent = promedio_ingresos(frame,[country])
        list_return.append([float(prozent), a, b, money]) #se agrega lista[porcentaje_total, pais, operaciones, ingresos ]
        
    return sorted(list_return, reverse= True)


def promedio_ingresos(frame,list1):
    
    total = frame['total_value'].sum()
    dinero = sum(list1)
    porciento = (100*dinero)/total
    return format(dinero,','), format(porciento, '0.2f')

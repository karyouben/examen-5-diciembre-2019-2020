# -*- coding: utf-8 -*-
'''
Created on 25 ene 2022

@author: willi
'''
import csv
from collections import namedtuple
from collections import Counter
from parsers import *
import statistics

Ventas = namedtuple('Ventas', 'año,comunidad,contratos,llamadas,publicidad')

def lee_datos_ventas(fichero):
    with open (fichero, encoding= 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        res=[]
        for año,comunidad,contratos,llamadas,publicidad in lector:
            tupla_ventas = Ventas(int(año),comunidad,int(contratos),int(llamadas),int(publicidad))
            res.append(tupla_ventas)
    return res

def total_contratos(registros,comunidad=None):
    res = sum(t.contratos for t in registros if t.comunidad == comunidad or comunidad is None)
    return res

def año_mas_contratos_por_llamadas_comunidad(registros,comunidad):
    return max(((t.año,(t.contratos/t.llamadas)*100) for t in registros if t.comunidad == comunidad), key = lambda x:x[1])

def variaciones_anuales_contratos(registros, comunidad):
    registros = [t for t in registros if t.comunidad == comunidad]
    return [(r1.año,r2.año,r2.contratos-r1.contratos) for r1,r2 in zip(registros,registros[1:])]

def año_mas_contratos(registros):
    dicc = agrupa_por_años(registros)
    maximo = max(dicc.items(), key = lambda x:x[1])
    return maximo
    
def agrupa_por_años(registros):
    dicc= {}
    for t in registros:
        clave=t.año
        if clave in dicc:
            dicc[clave]+=t.contratos
        else:
            dicc[clave]= t.contratos
    return dicc

def agrupa_datos_por_años(registros):
    dicc={}
    for t in registros:
        clave=t.año
        if clave not in dicc:
            dicc[clave] = [0,0,0]
        dicc[clave][0]+=t.contratos
        dicc[clave][1]+=t.llamadas
        dicc[clave][2]+=t.publicidad
    return[Ventas(año,'Todas',n1,n2,n3) for año, (n1,n2,n3) in dicc.items()]

def correlaciones_datos_anuales(registros):
    dicc = agrupa_datos_por_años(registros)
    contratos = [t[2] for t in dicc]
    return pearson(contratos,[t[3] for t in dicc]), pearson(contratos, [t[4] for t in dicc])
            
        
            
    
    
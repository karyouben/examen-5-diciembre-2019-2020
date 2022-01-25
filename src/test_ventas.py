# -*- coding: utf-8 -*-
'''
Created on 25 ene 2022

@author: willi
'''
from ventas import *



def test_lee_datos_ventas(fichero):
    res = lee_datos_ventas(fichero)
    print("="*20+ "test_lee_datos_ventas"+"="*20)
    print(f"Leidos {len(res)} registros")
    print("")
    print(f"Los tres primeros registros son: ")
    mostrar_registros(res[:3])
    print("")
    print(f"Los tres últimos registros son: ")
    mostrar_registros(res[-3:])
    print("")

def mostrar_registros(registros):
    for indx, registro in enumerate(registros):
        print(f"{indx+1}-> {registro}")
def mostrar_diccionarios(dicc):
    for clave,valor in dicc.items:
        print(f"{clave}-> {valor}")

def test_total_contratos(registros,comunidad):
    res = total_contratos(registros,comunidad)
    print("="*20+ "test_total_contratos"+"="*20)
    if comunidad != None:
        print(f"El total de contratos de {comunidad} es: {res} ")
    else:
        print(f"El total de contratos en todo el pais es: {res}")
    print("")

def test_año_mas_contratos_por_llamadas_comunidad(registros,comunidad):
    res = año_mas_contratos_por_llamadas_comunidad(registros,comunidad)
    print("="*20+ "test_año_mas_contratos_por_llamadas_comunidad"+"="*20)
    print(f"El año con mayor porcentaje de contratos por llamadas en {comunidad} es: {res}")
    print("")
    
def test_variaciones_anuales_contratos(registros, comunidad):
    res = variaciones_anuales_contratos(registros, comunidad)
    print("="*20+ "test_variaciones_anuales_contratos"+"="*20)
    print(f"las variaciones de contratos en {comunidad} es: ")
    mostrar_registros(res)
    print("")
    
def test_año_mas_contratos(registros):
    res = año_mas_contratos(registros)
    print("="*20+ "test_año_mas_contratos"+"="*20)
    print(f"El año con mayor número de contratos fue el {res[0]} con un total de {res[1]} contratos")
    print("")

def test_agrupa_datos_por_años(registros):
    res = agrupa_datos_por_años(registros)
    print("="*20+ "test_agrupa_datos_por_años"+"="*20)
    print(f"Los datos por años son: ")
    mostrar_registros(res)
    print("")
    
def test_correlaciones_datos_anuales(registros):
    res = correlaciones_datos_anuales(registros)
    print("="*20+ "test_correlaciones_datos_anuales"+"="*20)
    print(f"Las correlaciones de Pearson son: ")
    mostrar_registros(res)
    print("")
       

def main():
    
    fichero = ('../data/ventas.csv')
    test_lee_datos_ventas(fichero)
    REGISTROS = lee_datos_ventas(fichero)
    test_total_contratos(REGISTROS,'Andalucía')
    test_total_contratos(REGISTROS,None)
    test_año_mas_contratos_por_llamadas_comunidad(REGISTROS,'Extremadura')
    test_variaciones_anuales_contratos(REGISTROS, 'Andalucía')
    test_año_mas_contratos(REGISTROS)
    test_agrupa_datos_por_años(REGISTROS)
    test_correlaciones_datos_anuales(REGISTROS)
if __name__=="__main__":
    main()
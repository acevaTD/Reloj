"""
Ej_EDA_Reloj.py

Dada la siguiente especificación de tipo se debe implementar en Python la clase correspondiente:
Especificación de datos de tiempo con precisión de segundos. La información se proporciona en términos de horas, minutos, segundos y milisegundos.

Operaciones:
• Constructor: Crea un objeto con el tiempo 00:00:00:000
• SetTiempo: Modifica los 4 datos temporales del objeto.
• IncrMinuto: Incrementa el tiempo en 1 minuto.
• DecrMinuto: Decrementa el tiempo en 1 minuto.
• GetHora: Devuelve el valor hora.
• GetMinutos: Devuelve el valor minutos.
• GetSegundos: Devuelve el valor segundos.
• ToMilisegundos: Devuelve el valor convertido a ms
• Str: devuelve una cadena de caracteres con los datos temporales del objeto en un formato interpretable por un humano.

Version 1.0

Autor: Aleix Cebrián Valero

Fecha: 21/02/2026

"""

class Tiempo:
    
    
    def __init__(self):
        self.__hora = int()
        self.__minuto = int()
        self.__segundo = int()
        self.__milisegundo = int()
    
        return
    
    
    def SetTiempo(self, h: int, m: int, s: int, ms: int):
        
        self.__hora = h
        self.__minuto = m
        self.__segundo = s
        self.__milisegundo = ms
        
        return
    

    def IncrMinuto(self):
        
        if self.__milisegundo != 999:    
            self.__milisegundo += 1
        
        else:
            
            self.__milisegundo = 0
            
            if self.__segundo != 59:                
                self.__segundo += 1
                
            else:
                self.__segundo = 0
                
                if self.__hora != 23:
                    self.__hora += 1
                    
                else:
                    self.__hora = 0
                    

print("hello world")
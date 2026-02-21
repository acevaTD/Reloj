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
    
    
    def __TiempoValido(h: int, m: int, s: int, ms: int) -> bool:

        valido = bool()

        if h >= 0 and h < 24:
            if m >= 0 and m < 60 and s >= 0 and s < 60:
                if ms >= 0 and ms < 1000:
                    valido = True
                else:
                    valido = False
            else:
                valido = False
        else:
            valido = False

        return valido
    
    
    def SetTiempo(self, h: int, m: int, s: int, ms: int):

        if Tiempo.__TiempoValido(h,m,s,ms):

            self.__hora = h
            self.__minuto = m
            self.__segundo = s
            self.__milisegundo = ms
        
        return
    

    def IncrMinuto(self):
        
        if self.__minuto != 59:
            self.__minuto += 1

        else:
            self.__minuto = 0
            if self.__hora == 23:
                self.__hora = 0
            else:
                self.__hora += 1
                

        return

    
    def DecrMinuto(self):

        if self.__minuto != 0:
            self.__minuto -= 1

        else:
            self.__minuto = 59
            if self.__hora == 0:
                self.__hora = 23
            else:
                self.__hora -= 1

        return
    

    def GetHora(self):

        return self.__hora
    
    def GetMinutos(self):

        return self.__minuto
    
    def GetSegundos(self):

        return self.__segundo
    
    def ToMilisegundos(self):

        milisegundos = self.__hora * 60 * 60 * 1000 + self.__minuto * 60 * 1000 + self.__segundo * 1000 + self.__milisegundo
    
        return milisegundos

    def Str(self): # EL zfill permite poner ceros a la izquierda para que hayan dos dígitos.

        cad = "La hora es: " + str(self.__hora).zfill(2) + ":" + str(self.__minuto).zfill(2) + ":" + str(self.__segundo).zfill(2) + ":" + str(self.__milisegundo).zfill(3)

        return cad                  



def main():

    
    lista_r = []
    for i in range(3):

        tiempo = Tiempo()
        lista_r.append(tiempo)

    lista_r[0].SetTiempo(12,0, 56, 820)
    lista_r[1].SetTiempo(3,45,12,0)
    lista_r[2].SetTiempo(23,59,59,125)

    elem_0 = lista_r[0].Str()
    print(elem_0)

    for i in range(5):
        lista_r[1].DecrMinuto()


if __name__ == "__main__":
    main()
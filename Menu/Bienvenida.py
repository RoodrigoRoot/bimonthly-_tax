from  mensual.Mensual import *
from semanal.Week import Week
class Bienvenido ():
    MENU = """ Escoge una opción
            1-Semanal
            2.-Mensual
            3.-Total  
"""
    option = 0
    def __init__(self):
        pass
    
    @classmethod
    def Menu(cls):
        cls.option=int(input(cls.MENU))
        if cls.option==1:
            Week.count_Week(weeks=int(input("Semanas pagadas")))
        
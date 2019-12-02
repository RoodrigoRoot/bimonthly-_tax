#from Menu.Bienvenida import Bienvenido
from semanal.Week import Weeks

class Main():
    def __init__(self):
        pass
    def semana(self):
        week=Weeks(int(input("Semanas pagadas: ")))
        #print(week.count_Week())
        print(week.sum_weeks())
main=Main()
main.semana()
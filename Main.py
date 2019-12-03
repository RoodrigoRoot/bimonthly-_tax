#from Weekly.Week import Weeks
#from Monthly.Monthly import Months
from Reports.Report import Reports

class Main:
    
    def __init__(self):
        
        pass
    @classmethod
    def semana(cls):
        #week1 = Weeks(int(input("Semanas pagadas del primer mes: ")))
        #week2 = Weeks(int(input("Semanas pagadas del segundo mes: ")))
        #month=Months(week1.sum_weeks(), week2.sum_weeks_2())
        Reports.generate_Report()

if __name__=="__main__":
    Main.semana()
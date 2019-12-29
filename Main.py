from weekly.Week import Weeks
from monthly.Monthly import Months
from Reports.Report import Reports

class Main:

    
    @classmethod
    def semana(cls):
        while True:
                
            try:
                    
                week1 = Weeks(int(input("Semanas pagadas del primer mes: ")))
                week2 = Weeks(int(input("Semanas pagadas del segundo mes: ")))
                month=Months(week1.sum_weeks(), week2.sum_weeks_2())
                if month:
                    Reports.generate_Report()
                    break
                
            except ValueError:
                print("Solo aceptamos numeros")
            except KeyboardInterrupt:
                print("No puedes terminar la App")
            except Exception as e:
                print(e.__class__)

if __name__=="__main__":
    Main.semana()